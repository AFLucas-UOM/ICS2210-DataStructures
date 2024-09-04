import random
import statistics
import sys
import time
import math

class SkipListNode:
    """Node class for Skip List."""
    def __init__(self, key, level):
        self.key = key
        self.forward = [None] * (level + 1)

class SkipList:
    """Skip List implementation."""
    def __init__(self, max_levels, p):
        self.max_levels = max_levels
        self.p = p
        self.header = self.create_node(float('-inf'), max_levels)
        self.level = 0
        self.steps = []  # List to track steps taken during insertion
        self.promotions = []  # List to track promotions during insertion

    def create_node(self, key, level):
        """Create a new node with the given key and level."""
        return SkipListNode(key, level)

    def random_level(self):
        """Generate a random level for a new node."""
        level = 0
        while random.random() < self.p and level < self.max_levels:
            level += 1
        return level

    def insert(self, key):
        """Insert a key into the skip list."""
        update = [None] * (self.max_levels + 1)
        x = self.header
        for i in range(self.level, -1, -1):
            while x.forward[i] and x.forward[i].key < key:
                x = x.forward[i]
            update[i] = x
        x = x.forward[0]
        if not x or x.key != key:
            new_level = self.random_level()
            if new_level > self.level:
                for i in range(self.level + 1, new_level + 1):
                    update[i] = self.header
                self.level = new_level
            x = self.create_node(key, new_level)
            for i in range(new_level + 1):
                x.forward[i] = update[i].forward[i]
                update[i].forward[i] = x
            self.steps.append(sum(1 for _ in update))
            self.promotions.append(new_level)
        else:
            self.steps.append(sum(1 for _ in update))

    def get_statistics(self):
        """Compute statistics of the skip list."""
        if not self.steps or not self.promotions:
            return None
        min_steps = min(self.steps)
        max_steps = max(self.steps)
        mean_steps = round(statistics.mean(self.steps), 3)
        std_steps = round(statistics.stdev(self.steps), 3) if len(self.steps) > 1 else 0
        median_steps = round(statistics.median(self.steps), 3)

        min_promotions = min(self.promotions)
        max_promotions = max(self.promotions)
        mean_promotions = round(statistics.mean(self.promotions), 3)
        std_promotions = round(statistics.stdev(self.promotions), 3) if len(self.promotions) > 1 else 0
        median_promotions = round(statistics.median(self.promotions), 3)

        levels = self.level + 1

        return {
            "Steps": {
                "Min": min_steps,
                "Max": max_steps,
                "Mean": mean_steps,
                "Standard Deviation (std)": std_steps,
                "Median": median_steps
            },
            "Promotions": {
                "Min": min_promotions,
                "Max": max_promotions,
                "Mean": mean_promotions,
                "Standard Deviation (std)": std_promotions,
                "Median": median_promotions
            },
            "Levels": levels
        }

def knuth_shuffle(array):
    """Implement Knuth shuffle algorithm to randomize the order of elements in the array."""
    n = len(array)
    for i in range(n - 1, 0, -1):
        j = random.randint(0, i)
        array[i], array[j] = array[j], array[i]
    return array

def construct_skip_list(array, part_name):
    """Construct the skip list from an array."""
    max_levels = int(math.log(len(array), 2))  # Calculate maximum levels based on array size
    p = 0.5  # Probability parameter for skip list
    skip_list = SkipList(max_levels, p)
    print(f"\033[1;32mConstructing Skip List ({part_name}):\033[0m")
    for i, num in enumerate(array):
        skip_list.insert(num)
        progress = (i + 1) / len(array)
        sys.stdout.write("\r\033[1;32m[{:<50}] {:.2f}%\033[0m".format("=" * int(progress * 50), progress * 100))
        sys.stdout.flush()
        time.sleep(0.0001) #delay to show the process of inserting nodes
    print("\n")
    return skip_list

def clear_terminal():
    """Clear the terminal."""
    print("\033[2J\033[H")

def print_box(title, content):
    """Print content inside a box."""
    print(f"+{'-' * (len(title) + 2)}+")
    print(f"| {title} |")
    print(f"+{'-' * (len(title) + 2)}+")
    print(content)
    print(f"+{'-' * (len(title) + 2)}+")

if __name__ == "__main__":
    clear_terminal()
    array1 = list(range(1, 5001))
    array1 = knuth_shuffle(array1)

    skip_list = construct_skip_list(array1, "Part 1")
    time.sleep(1)

    clear_terminal()

    array2 = [random.randint(0, 100000) for _ in range(1000)]
    skip_list.steps = []
    skip_list.promotions = []

    skip_list = construct_skip_list(array2, "Part 2")
    time.sleep(1)

    clear_terminal()

    print("\033[1;32mSkip List Construction Complete\033[0m\n")

    statistics = skip_list.get_statistics()
    if statistics:
        print_box("Steps", "\n".join([f"{key}: {value}" for key, value in statistics["Steps"].items()]))
        print("\n")
        time.sleep(1)
        print_box("Promotions", "\n".join([f"{key}: {value}" for key, value in statistics["Promotions"].items()]))
        print("\n")
        time.sleep(1)
        print(f"\033[1;32mLevels: {statistics['Levels']}\033[0m")
