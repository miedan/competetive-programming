class Solution:
    def mincostTickets(self, days: List[int], cost: List[int]) -> int:

        @cache

        def dp(idx):

            if idx >= len(days):
                return 0

            prices = min(dp(bisect.bisect_left(days, days[idx] + 1 )) + cost[0],
            dp(bisect.bisect_left(days, days[idx] + 7 )) + cost[1], dp(bisect.bisect_left(days, days[idx] + 30 )) + cost[2])

            return prices
        return dp(0)