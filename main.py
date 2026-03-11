import random


class CacheSimulator:

    def __init__(self, cache_size):
        self.cache_size = cache_size
        self.cache = []
        self.hits = 0
        self.misses = 0

    def access_memory(self, address):

        if address in self.cache:
            print(f"Address {address} → HIT")
            self.hits += 1

        else:
            print(f"Address {address} → MISS")
            self.misses += 1

            if len(self.cache) >= self.cache_size:
                self.cache.pop(0)

            self.cache.append(address)

    def show_statistics(self):

        total = self.hits + self.misses
        hit_rate = (self.hits / total) * 100 if total > 0 else 0

        print("\n=== CACHE STATISTICS ===")
        print(f"Total accesses : {total}")
        print(f"Cache hits     : {self.hits}")
        print(f"Cache misses   : {self.misses}")
        print(f"Hit rate       : {hit_rate:.2f}%")


def generate_addresses(count):

    addresses = []

    for _ in range(count):
        addr = hex(random.randint(0, 255))
        addresses.append(addr)

    return addresses


def main():

    cache = CacheSimulator(cache_size=4)

    addresses = generate_addresses(15)

    print("=== MEMORY ACCESS SIMULATION ===\n")

    for address in addresses:
        cache.access_memory(address)

    cache.show_statistics()


if __name__ == "__main__":
    main()