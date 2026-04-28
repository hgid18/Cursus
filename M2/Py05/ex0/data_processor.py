from abc import ABC, abstractmethod
from typing import Any, Union


class DataProcessor(ABC):
    """Abstract base class for all data processors."""

    def __init__(self) -> None:
        self._storage: list[str] = []
        self._total_processed: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Check whether input data is appropriate for this processor."""
        ...

    @abstractmethod
    def ingest(self, data: Any) -> None:
        """Process and store input data."""
        ...

    def output(self) -> tuple[int, str]:
        """Extract the oldest stored item and its processing rank."""
        if not self._storage:
            raise IndexError("No data available in processor.")
        rank = self._total_processed - len(self._storage)
        value = self._storage.pop(0)
        return (rank, value)

    def remaining(self) -> int:
        """Return number of items still stored."""
        return len(self._storage)

    def total_processed(self) -> int:
        """Return total number of items ever ingested."""
        return self._total_processed


class NumericProcessor(DataProcessor):
    """Processes int, float, and lists of both types."""

    def validate(self, data: Any) -> bool:
        """Return True if data is int, float, or a list of int/float."""
        if isinstance(data, bool):
            return False
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            return all(
                isinstance(item, (int, float)) and not isinstance(item, bool)
                for item in data
            )
        return False

    def ingest(
        self,
        data: Union[int, float, list[Union[int, float]]]
    ) -> None:
        """Convert numeric data to strings and store internally."""
        if not self.validate(data):
            raise TypeError("Improper numeric data")
        if isinstance(data, list):
            for item in data:
                self._storage.append(str(item))
                self._total_processed += 1
        else:
            self._storage.append(str(data))
            self._total_processed += 1


class TextProcessor(DataProcessor):
    """Processes str and lists of strings."""

    def validate(self, data: Any) -> bool:
        """Return True if data is a str or a list of str."""
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(item, str) for item in data)
        return False

    def ingest(self, data: Union[str, list[str]]) -> None:
        """Store text data internally."""
        if not self.validate(data):
            raise TypeError("Improper text data")
        if isinstance(data, list):
            for item in data:
                self._storage.append(item)
                self._total_processed += 1
        else:
            self._storage.append(data)
            self._total_processed += 1


class LogProcessor(DataProcessor):
    """Processes dict[str, str] and lists of that type."""

    def validate(self, data: Any) -> bool:
        """Return True if data is a dict[str,str] or a list thereof."""
        if isinstance(data, dict):
            return all(
                isinstance(k, str) and isinstance(v, str)
                for k, v in data.items()
            )
        if isinstance(data, list):
            return all(
                isinstance(item, dict) and all(
                    isinstance(k, str) and isinstance(v, str)
                    for k, v in item.items()
                )
                for item in data
            )
        return False

    def ingest(
        self,
        data: Union[dict[str, str], list[dict[str, str]]]
    ) -> None:
        """Convert log dicts to 'LEVEL: message' strings and store."""
        if not self.validate(data):
            raise TypeError("Improper log data")
        if isinstance(data, list):
            for item in data:
                log_level = item.get("log_level", "")
                log_message = item.get("log_message", "")
                self._storage.append(f"{log_level}: {log_message}")
                self._total_processed += 1
        else:
            log_level = data.get("log_level", "")
            log_message = data.get("log_message", "")
            self._storage.append(f"{log_level}: {log_message}")
            self._total_processed += 1


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===")

    # --- NumericProcessor ---
    print("\nTesting Numeric Processor...")
    num_proc = NumericProcessor()

    print(f" Trying to validate input '42': {num_proc.validate(42)}")
    print(f" Trying to validate input 'Hello': {num_proc.validate('Hello')}")

    print(" Test invalid ingestion of string 'foo' without prior validation:")
    try:
        num_proc.ingest("foo")  # type: ignore[arg-type]
    except TypeError as e:
        print(f" Got exception: {e}")

    data_num = [1, 2, 3, 4, 5]
    print(f" Processing data: {data_num}")
    num_proc.ingest(data_num)

    print(" Extracting 3 values...")
    for _ in range(3):
        rank, value = num_proc.output()
        print(f" Numeric value {rank}: {value}")

    # --- TextProcessor ---
    print("\nTesting Text Processor...")
    txt_proc = TextProcessor()

    print(f" Trying to validate input '42': {txt_proc.validate(42)}")

    data_txt = ["Hello", "Nexus", "World"]
    print(f" Processing data: {data_txt}")
    txt_proc.ingest(data_txt)

    print(" Extracting 1 value...")
    rank, value = txt_proc.output()
    print(f" Text value {rank}: {value}")

    # --- LogProcessor ---
    print("\nTesting Log Processor...")
    log_proc = LogProcessor()

    print(f" Trying to validate input 'Hello': {log_proc.validate('Hello')}")

    data_log = [
        {"log_level": "NOTICE", "log_message": "Connection to server"},
        {"log_level": "ERROR", "log_message": "Unauthorized access!!"},
    ]
    print(f" Processing data: {data_log}")
    log_proc.ingest(data_log)

    print(" Extracting 2 values...")
    for _ in range(2):
        rank, value = log_proc.output()
        print(f" Log entry {rank}: {value}")
