"""
https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem
"""
import bisect


def climbingLeaderboard(ranked, player):
    set_ranked = set(ranked)
    ranked = sorted(set_ranked, reverse = False)
    len_ranked = len(ranked)
    answer = list()

    for game in player:
        answer.append(len_ranked - (bisect.bisect(ranked, game)) + 1)

    return answer


print(climbingLeaderboard([100, 90, 90, 80], [70, 80, 105]))
print(climbingLeaderboard([100, 100, 50, 40, 40, 20, 10], [5, 25, 50, 120]))
