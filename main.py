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
            self.cache.remove(address)
            self.cache.append(address)
        else:
            print(f"Address {address} → MISS")
            self.misses += 1

            if len(self.cache) >= self.cache_size:
                lru = self.cache.pop(0)
                print(f"Evicting {lru} (LRU)")

            self.cache.append(address)

        self.display_cache()

    def display_cache(self):
        print(f"Cache: {self.cache}\n")

    def show_statistics(self):
        total = self.hits + self.misses
        hit_rate = (self.hits / total) * 100 if total > 0 else 0

        print("=== CACHE STATISTICS ===")
        print(f"Total accesses : {total}")
        print(f"Cache hits     : {self.hits}")
        print(f"Cache misses   : {self.misses}")
        print(f"Hit rate       : {hit_rate:.2f}%")


def main():
    cache = CacheSimulator(cache_size=4)

    addresses = [
        "0x12", "0x2f", "0x12", "0x8a", "0x2f",
        "0x44", "0x12", "0x8a", "0x90", "0x44",
        "0x2f", "0x90", "0x12", "0x33", "0x12"
    ]

    print("=== MEMORY ACCESS SIMULATION ===\n")

    for address in addresses:
        cache.access_memory(address)

    cache.show_statistics()


if __name__ == "__main__":
    main()