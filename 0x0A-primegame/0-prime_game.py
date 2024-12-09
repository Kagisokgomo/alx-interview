#!/usr/bin/python3

def isWinner(x, nums):
    def sieve_of_eratosthenes(n):
        """Generates a list of primes up to n using the Sieve of Eratosthenes."""
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False  # 0 and 1 are not primes
        for i in range(2, int(n**0.5) + 1):
            if sieve[i]:
                for j in range(i * i, n + 1, i):
                    sieve[j] = False
        return [i for i in range(2, n + 1) if sieve[i]]

    def play_round(n):
        """Simulate the game for one round and return the winner ('Maria' or 'Ben')."""
        primes = sieve_of_eratosthenes(n)
        if len(primes) % 2 == 0:  # Even number of primes
            return 'Ben'
        else:  # Odd number of primes
            return 'Maria'

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = play_round(n)
        if winner == 'Maria':
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None
