class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        num_coins = [amount + 1] * (amount + 1)
        num_coins[0] = 0
        for i in range(1, amount+1):
            for coin in coins:
                if i - coin >= 0:
                    num_coins[i] = min(num_coins[i], 1 + num_coins[i - coin])
        if num_coins[amount] != amount + 1:
            return num_coins[amount]
        else:
            return -1