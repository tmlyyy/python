#!/usr/bin/env python3
import random

ACHIEVEMENTS = [
    "First Steps",
    "Survivor",
    "Treasure Hunter",
    "Boss Slayer",
    "Master Explorer",
    "Crafting Genius",
    "Collector Supreme",
    "Untouchable",
    "Unstoppable",
    "Strategist",
    "Speed Runner",
    "World Savior",
    "Sharp Mind",
    "Hidden Path Finder",
]


def gen_player_achievements() -> set[str]:
    # Seleciona de 5 a 10 conquistas aleatÃ³rias do pool
    k = random.randint(5, 10)
    sampled = random.sample(ACHIEVEMENTS, k)
    return set(sampled)


def main() -> None:
    print("=== Achievement Tracker System ===")

    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()

    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")

    # Encontra todas as conquistas distintas presentes entre os jogadores
    all_distinct = set.union(alice, bob, charlie, dylan)
    print(f"All distinct achievements: {all_distinct}")

    # Encontra as conquistas comuns a todos os jogadores
    common = set.intersection(alice, bob, charlie, dylan)
    print(f"Common achievements: {common}")

    # Identifica as conquistas exclusivas de cada jogador
    only_alice = set.difference(alice, set.union(bob, charlie, dylan))
    only_bob = set.difference(bob, set.union(alice, charlie, dylan))
    only_charlie = set.difference(charlie, set.union(alice, bob, dylan))
    only_dylan = set.difference(dylan, set.union(alice, bob, charlie))

    print(f"Only Alice has: {only_alice}")
    print(f"Only Bob has: {only_bob}")
    print(f"Only Charlie has: {only_charlie}")
    print(f"Only Dylan has: {only_dylan}")

    # Identifica as conquistas que faltam para cada jogador ter todas do grupo
    print(f"Alice is missing: {set.difference(all_distinct, alice)}")
    print(f"Bob is missing: {set.difference(all_distinct, bob)}")
    print(f"Charlie is missing: {set.difference(all_distinct, charlie)}")
    print(f"Dylan is missing: {set.difference(all_distinct, dylan)}")


if __name__ == "__main__":
    main()
