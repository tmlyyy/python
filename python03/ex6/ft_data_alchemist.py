#!/usr/bin/env python3
import random


def main() -> None:
    print("=== Game Data Alchemist ===")

    players: list[str] = [
        "Alice",
        "bob",
        "Charlie",
        "dylan",
        "Emma",
        "Gregory",
        "john",
        "kevin",
        "Liam",
    ]

    print(f"Initial list of players: {players}")

    # 1. Capitaliza todos os nomes da lista original
    capitalized_players: list[str] = [p.capitalize() for p in players]
    print(f"New list with all names capitalized: {capitalized_players}")

    # 2. Filtra os nomes que já estavam capitalizados no início
    initially_capitalized: list[str] = [
        p for p in players if p == p.capitalize()
    ]
    print(f"New list of capitalized names only: {initially_capitalized}")

    # 3. Gera pontuação aleatória de 1 a 1000 para cada jogador
    score_dict: dict[str, int] = {
        p: random.randint(1, 1000) for p in capitalized_players
    }
    print(f"Score dict: {score_dict}")

    # 4. Cálculos estatísticos da média
    total_scores = sum(score_dict.values())
    total_len = len(score_dict)
    avg_score = (
        float(total_scores) / total_len if total_len > 0 else 0.0
    )
    print(f"Score average is {avg_score:.2f}")

    # 5. Filtra apenas os jogadores com pontuação acima da média
    high_scores: dict[str, int] = {
        name: score
        for name, score in score_dict.items()
        if score > avg_score
    }
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
