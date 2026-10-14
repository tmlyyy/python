"""Route mixed data to registered processors using their common interface."""

from typing import Any

from data_processor import (DataProcessor, LogProcessor, NumericProcessor,
                            TextProcessor)


class DataStream:
    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for element in stream:
            for processor in self.processors:
                if processor.validate(element):
                    processor.ingest(element)
                    break
            else:
                print(f"DataStream error - Can't process element in stream: "
                      f"{element}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self.processors:
            print("No processor found, no data")
        for processor in self.processors:
            name = (type(processor).__name__
                    .replace("Processor", " Processor"))
            total = processor.total_processed
            remaining = processor.remaining
            print(f"{name}: total {total} items processed, "
                  f"remaining {remaining} on processor")


if __name__ == "__main__":
    print("=== Code Nexus - Data Stream ===")
    print("\nInitialize Data Stream...")
    stream = DataStream()
    stream.print_processors_stats()
    numeric = NumericProcessor()
    print("\nRegistering Numeric Processor")
    stream.register_processor(numeric)
    batch: list[Any] = [
        "Hello world", [3.14, -1, 2.71],
        [{"log_level": "WARNING", "log_message": "Telnet access! "
          "Use ssh instead"},
         {"log_level": "INFO", "log_message": "User wil is connected"}],
        42, ["Hi", "five"],
    ]
    print(f"\nSend first batch of data on stream: {batch}")
    stream.process_stream(batch)
    stream.print_processors_stats()
    text = TextProcessor()
    logs = LogProcessor()
    print("\nRegistering other data processors")
    stream.register_processor(text)
    stream.register_processor(logs)
    print("Send the same batch again")
    stream.process_stream(batch)
    stream.print_processors_stats()
    print("\nConsume some elements from the data processors: "
          "Numeric 3, Text 2, Log 1")
    for processor, count in [(numeric, 3), (text, 2), (logs, 1)]:
        for _ in range(count):
            processor.output()
    stream.print_processors_stats()
