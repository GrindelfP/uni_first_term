def eratosthenes_sieve(top_edge):
    primes = [0] * top_edge
    probably_prime = 1
    while probably_prime < top_edge - 1:
        probably_prime += 1
        if primes[probably_prime] == 0:
            mult_prime = 2 * probably_prime
            while mult_prime < top_edge:
                primes[mult_prime] = 1
                mult_prime += probably_prime
    real_primes = []
    for index in range(0, top_edge):
        if primes[index] == 0:
            real_primes.append(index)
    return real_primes


top_edge_of_search = int(input("Enter the biggest integer of your search massive -> "))
print(eratosthenes_sieve(top_edge_of_search))
