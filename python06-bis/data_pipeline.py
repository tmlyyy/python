"""Export processor output through structural, Protocol-based plugins."""

from typing import Any, Protocol

from data_processor import LogProcessor, NumericProcessor, TextProcessor
from data_stream import DataStream as BaseDataStream


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        """Export ranked values."""


class DataStream(BaseDataStream):
    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        if nb < 0:
            raise ValueError("nb must be non-negative")
        for processor in self.processors:
            data = [processor.output()
                    for _ in range(min(nb, processor.remaining))]
            try:
                plugin.process_output(data.copy())
            except Exception:
                processor._restore_output(data)
                raise


def _csv_field(value: str) -> str:
    if not value or any(char in value for char in ',"\r\n'):
        return '"' + value.replace('"', '""') + '"'
    return value


class CSVExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("CSV Output:")
        print(",".join(_csv_field(value) for _, value in data))


def _json_string(value: str) -> str:
    pieces: list[str] = ['"']
    for char in value:
        if char == '"':
            pieces.append('\\"')
        elif char == "\\":
            pieces.append("\\\\")
        elif char == "\b":
            pieces.append("\\b")
        elif char == "\f":
            pieces.append("\\f")
        elif char == "\n":
            pieces.append("\\n")
        elif char == "\r":
            pieces.append("\\r")
        elif char == "\t":
            pieces.append("\\t")
        elif ord(char) < 32:
            pieces.append("\\u" + format(ord(char), "04x"))
        else:
            pieces.append(char)
    return "".join(pieces) + '"'


class JSONExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        fields = [f'{_json_string("item_" + str(rank))}: '
                  f'{_json_string(value)}' for rank, value in data]
        print("JSON Output:")
        print("{" + ", ".join(fields) + "}")


if __name__ == "__main__":
    print("=== Code Nexus - Data Pipeline ===")
    print("\nInitialize Data Stream...\n")
    stream = DataStream()
    stream.print_processors_stats()
    print("\nRegistering Processors")
    stream.register_processor(NumericProcessor())
    stream.register_processor(TextProcessor())
    stream.register_processor(LogProcessor())
    first: list[Any] = [
        "Hello world", [3.14, -1, 2.71],
        [{"log_level": "WARNING", "log_message": "Telnet access! "
          "Use ssh instead"},
         {"log_level": "INFO", "log_message": "User wil is connected"}],
        42, ["Hi", "five"],
    ]
    print(f"\nSend first batch of data on stream: {first}\n")
    stream.process_stream(first)
    stream.print_processors_stats()
    print("\nSend 3 processed data from each processor to a CSV plugin:")
    stream.output_pipeline(3, CSVExportPlugin())
    print()
    stream.print_processors_stats()
    second: list[Any] = [
        21, ["I love AI", "LLMs are wonderful", "Stay healthy"],
        [{"log_level": "ERROR", "log_message": "500 server crash"},
         {"log_level": "NOTICE", "log_message":
          "Certificate expires in 10 days"}],
        [32, 42, 64, 84, 128, 168], "World hello",
    ]
    print(f"\nSend another batch of data: {second}\n")
    stream.process_stream(second)
    stream.print_processors_stats()
    print("\nSend 5 processed data from each processor to a JSON plugin:")
    stream.output_pipeline(5, JSONExportPlugin())
    print()
    stream.print_processors_stats()
