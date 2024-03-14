import time


def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    for coin in coins:
        if amount == 0:
            break
        count = amount // coin
        if count != 0:
            result[coin] = count
        amount %= coin
    return result


def find_min_coins(amount):
    coins = [50, 25, 10, 5, 2, 1]
    dp = [0] + [float('inf')] * amount
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    if dp[amount] == float('inf'):
        return None
    result = {}
    while amount:
        for coin in coins:
            if amount >= coin and dp[amount] == dp[amount - coin] + 1:
                result[coin] = result.get(coin, 0) + 1
                amount -= coin
                break
    return result


def compare_algorithms(amount):
    start_time = time.time()
    greedy_result = find_coins_greedy(amount)
    greedy_time = time.time() - start_time

    start_time = time.time()
    dp_result = find_min_coins(amount)
    dp_time = time.time() - start_time

    print(f"Жадібний алгоритм: {greedy_result}, час виконання: {greedy_time} секунд")
    print(f"Алгоритм динамічного програмування: {dp_result}, час виконання: {dp_time} секунд")


compare_algorithms(10127124)
