def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if temp < 0:
        msg = f"{temp}°C is too cold for plants (min 0°C)"
        raise ValueError(msg)
    if temp > 40:
        msg = f"{temp}°C is too hot for plants (max 40°C)"
        raise ValueError(msg)
    return temp


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===")

    test_cases = ["25", "abc", "100", "-50"]

    for test_input in test_cases:
        print(f"Input data is '{test_input}'")
        try:
            temp = input_temperature(test_input)
            print(f"Temperature is now {temp}°C")
        except Exception as e:
            msg = f"Caught input_temperature error: {e}"
            print(msg)

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
