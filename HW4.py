from collections import Counter


def determine_winner(candidates, votes):
    vote_counts = Counter(votes)
    max_votes = max(vote_counts.values())

    winners = [candidate for candidate, count in vote_counts.items() if count == max_votes]
    if len(winners) == 1:
        return winners[0]
    else:
        winners = sorted(winners, key=len)
        return winners[0]

candidates = [
    "Аскаров", "Бекмуханов", "Ернур", "Пешая",
    "Карим", "Шаримазданов"  # и т.д.
]
votes = [
    "Аскаров", "Аскаров", "Шаримазданов", "Ернур", "Пешая",
    "Карим", "Шаримазданов", "Ернур"  # и т.д.
]

winner = determine_winner(candidates, votes)
winner_vote_count = votes.count(winner)

print("Победитель выборов:", winner)
print("Количество голосов победителя:", winner_vote_count)
input("press any key to close window")
