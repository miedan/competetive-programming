class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:

        players.sort()
        trainers.sort()

        i, j = 0, 0
        n, m = len(players), len(trainers)
        team = 0
        while i < n and j < m:

            if players[i] <= trainers[j]:
                team += 1
                i += 1
                j += 1
            else:
                j += 1
        return team