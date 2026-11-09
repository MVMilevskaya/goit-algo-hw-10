import time

def find_coins_greedy(amount: int) -> dict[int, int]:

    coins = [50, 25, 10, 5, 2, 1]
    result = {}

    for coin in coins:
      if amount == 0:
        break
      count = amount // coin
      if count > 0:
        result[coin] = count
        amount -= coin * count

    return result


def find_min_coins(amount: int) -> dict[int, int]:

    coins = [50, 25, 10, 5, 2, 1]

    dp = [float("inf")] * (amount + 1)
    dp[0] = 0

    coin_used = [0] * (amount + 1)

    for i in range(1, amount + 1):
      for coin in coins:
        if i >= coin and dp[i - coin] + 1 < dp[i]:
          dp[i] = dp[i - coin] + 1
          coin_used[i] = coin

    result = {}
    curr = amount
    while curr > 0:
      coin = coin_used[curr]
      result[coin] = result.get(coin, 0) + 1
      curr -= coin

    return result

if __name__ == "__main__":
    test_amount = 113
    print(f"Сума: {test_amount}")
    print(f"Greedy result:   {find_coins_greedy(test_amount)}")
    print(f"DP result:       {find_min_coins(test_amount)}")

    print("\n--- Порівняння продуктивності на великій сумі (10000) ---")
    big_amount = 10000

    t0 = time.perf_counter()
    find_coins_greedy(big_amount)
    t_greedy = time.perf_counter() - t0

    t0 = time.perf_counter()
    find_min_coins(big_amount)
    t_dp = time.perf_counter() - t0

    print(f"Greedy time for {big_amount}: {t_greedy:.6f} сек")
    print(f"DP time for {big_amount}:     {t_dp:.6f} сек")