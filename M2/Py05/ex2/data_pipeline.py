from abc import ABC, abstractmethod
from typing import Any, Union
import typing


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


class ExportPlugin(typing.Protocol):
    """Protocol that all export plugins must satisfy."""

    def process_output(self, data: list[tuple[int, str]]) -> None:
        """Export a list of (rank, value) tuples."""
        ...


class CSVExportPlugin:
    """Exports data as a CSV row (values only, comma-separated)."""

    def process_output(self, data: list[tuple[int, str]]) -> None:
        """Print data as a single CSV line."""
        values = [value for _, value in data]
        csv_line = ",".join(values)
        print("CSV Output:")
        print(csv_line)


class JSONExportPlugin:
    """Exports data as a JSON object keyed by item index."""

    def process_output(self, data: list[tuple[int, str]]) -> None:
        """Print data as a JSON object."""
        pairs = [f'"item_{rank}": "{value}"' for rank, value in data]
        json_str = "{" + ", ".join(pairs) + "}"
        print("JSON Output:")
        print(json_str)


class DataStream:
    """Routes a mixed data stream to the appropriate data processors."""

    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        """Register a data processor for use in the stream."""
        self._processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        """Route each element to the first processor that accepts it."""
        for element in stream:
            handled = False
            for proc in self._processors:
                if proc.validate(element):
                    proc.ingest(element)
                    handled = True
                    break
            if not handled:
                print(
                    f"DataStream error - Can't process element "
                    f"in stream: {element}"
                )

    def print_processors_stats(self) -> None:
        """Print statistics for all registered data processors."""
        print("== DataStream statistics ==")
        if not self._processors:
            print("No processor found, no data")
            return
        for proc in self._processors:
            name = type(proc).__name__
            total = proc.total_processed()
            remaining = proc.remaining()
            print(
                f"{name}: total {total} items processed, "
                f"remaining {remaining} on processor"
            )

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        """Consume nb elements from each processor and export via plugin."""
        for proc in self._processors:
            collected: list[tuple[int, str]] = []
            for _ in range(nb):
                if proc.remaining() == 0:
                    break
                collected.append(proc.output())
            if collected:
                plugin.process_output(collected)


if __name__ == "__main__":
    print("=== Code Nexus - Data Pipeline ===")

    stream = DataStream()

    print("\nInitialize Data Stream...")
    stream.print_processors_stats()

    print("\nRegistering Processors")
    num_proc = NumericProcessor()
    txt_proc = TextProcessor()
    log_proc = LogProcessor()
    stream.register_processor(num_proc)
    stream.register_processor(txt_proc)
    stream.register_processor(log_proc)

    batch1: list[Any] = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {"log_level": "WARNING",
             "log_message": "Telnet access! Use ssh instead"},
            {"log_level": "INFO",
             "log_message": "User wil is connected"},
        ],
        42,
        ["Hi", "five"],
    ]

    print(f"\nSend first batch of data on stream: {batch1}")
    stream.process_stream(batch1)
    stream.print_processors_stats()

    csv_plugin = CSVExportPlugin()
    print("\nSend 3 processed data from each processor to a CSV plugin:")
    stream.output_pipeline(3, csv_plugin)
    stream.print_processors_stats()

    batch2: list[Any] = [
        21,
        ["I love AI", "LLMs are wonderful", "Stay healthy"],
        [
            {"log_level": "ERROR", "log_message": "500 server crash"},
            {"log_level": "NOTICE",
             "log_message": "Certificate expires in 10 days"},
        ],
        [32, 42, 64, 84, 128, 168],
        "World hello",
    ]

    print(f"\nSend another batch of data: {batch2}")
    stream.process_stream(batch2)
    stream.print_processors_stats()

    json_plugin = JSONExportPlugin()
    print("\nSend 5 processed data from each processor to a JSON plugin:")
    stream.output_pipeline(5, json_plugin)
    stream.print_processors_stats()
