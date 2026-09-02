#!/usr/bin/env python3
import random
import typing

PLAYERS = ["alice", "bob", "charlie", "dylan"]
ACTIONS = [
    "run",
    "eat",
    "sleep",
    "grab",
    "move",
    "climb",
    "swim",
    "release",
    "use",
]


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    while True:
        player = random.choice(PLAYERS)
        action = random.choice(ACTIONS)
        yield (player, action)


def consume_event(
    event_list: list[tuple[str, str]]
) -> typing.Generator[tuple[str, str], None, None]:
    while event_list:
        item = random.choice(event_list)
        event_list.remove(item)
        yield item


def main() -> None:
    print("=== Game Data Stream Processor ===")

    # 1. Inicializa o nosso fluxo infinito de dados
    event_gen = gen_event()

    # 2. Executa o loop de 1000 eventos usando Tuple Unpacking (sem colchetes)
    for i in range(1000):
        event = next(event_gen)
        player_name, action_name = event
        print(f"Event {i}: Player {player_name} did action {action_name}")

    # 3. Cria a lista de 10 eventos
    ten_events = [next(event_gen) for _ in range(10)]
    print(f"Built list of 10 events: {ten_events}")

    # 4. Consome os itens
    for event in consume_event(ten_events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {ten_events}")


if __name__ == "__main__":
    main()
