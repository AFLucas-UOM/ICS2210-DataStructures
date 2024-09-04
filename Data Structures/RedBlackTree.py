import random
import statistics
import sys
import time

class RBNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.color = "RED"

class RedBlackTree:
    def __init__(self):
        self.root = None
        self.steps = []
        self.rotations = []
        self.height = 0
        self.leaves = 0

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left is not None:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y
        self.rotations[-1] += 1  # Increment rotation count


    def right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right is not None:
            x.right.parent = y
        x.parent = y.parent
        if y.parent is None:
            self.root = x
        elif y == y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x
        x.right = y
        y.parent = x
        self.rotations[-1] += 1  # Increment rotation count


    def insert_fixup(self, z):
        while z.parent is not None and z.parent.color == "RED":
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y is not None and y.color == "RED":
                    z.parent.color = "BLACK"
                    y.color = "BLACK"
                    z.parent.parent.color = "RED"
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self.left_rotate(z)
                    z.parent.color = "BLACK"
                    z.parent.parent.color = "RED"
                    self.right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y is not None and y.color == "RED":
                    z.parent.color = "BLACK"
                    y.color = "BLACK"
                    z.parent.parent.color = "RED"
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.right_rotate(z)
                    z.parent.color = "BLACK"
                    z.parent.parent.color = "RED"
                    self.left_rotate(z.parent.parent)
        self.root.color = "BLACK"

    def insert_key(self, key):
        self.steps.append(0)
        self.rotations.append(0)
        new_node = RBNode(key)
        y = None
        x = self.root
        while x is not None:
            y = x
            self.steps[-1] += 1
            if new_node.key < x.key:
                x = x.left
            else:
                x = x.right
        new_node.parent = y
        if y is None:
            self.root = new_node
        elif new_node.key < y.key:
            y.left = new_node
        else:
            y.right = new_node
        self.insert_fixup(new_node)

    def tree_height(self, node):
        if node is None:
            return 0
        left_height = self.tree_height(node.left)
        right_height = self.tree_height(node.right)
        return max(left_height, right_height) + 1

    def count_leaves(self, node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1
        return self.count_leaves(node.left) + self.count_leaves(node.right)

def knuth_shuffle(array):
    n = len(array)
    for i in range(n - 1, 0, -1):
        j = random.randint(0, i)
        array[i], array[j] = array[j], array[i]
    return array

def construct_red_black_tree(array, part_name):
    print(f"\033[1;32mConstructing Red-Black Tree ({part_name}):\033[0m")
    rb_tree = RedBlackTree()
    for i, num in enumerate(array):
        rb_tree.insert_key(num)
        progress = (i + 1) / len(array)
        sys.stdout.write("\r\033[1;32m[{:<50}] {:.2f}%\033[0m".format("=" * int(progress * 50), progress * 100))
        sys.stdout.flush()
        time.sleep(0.0001) #delay to show the process of inserting nodes
    print("\n")
    return rb_tree

def clear_terminal():
    print("\033[2J\033[H")

def print_box(title, content):
    print(f"+{'-' * (len(title) + 2)}+")
    print(f"| {title} |")
    print(f"+{'-' * (len(title) + 2)}+")
    print(content)
    print(f"+{'-' * (len(title) + 2)}+")

def print_statistics(statistics):
    print_box("Steps", "\n".join([f"{key}: {value}" for key, value in statistics["Steps"].items()]))
    print("\n")
    time.sleep(1)
    print_box("Rotations", "\n".join([f"{key}: {value}" for key, value in statistics["Rotations"].items()]))
    print("\n")
    time.sleep(1)
    print(f"\033[1;32mHeight: {statistics['Height']}\033[0m")
    print(f"\033[1;32mLeaves: {statistics['Leaves']}\033[0m")

def calculate_statistics(tree):
    min_steps = min(tree.steps)
    max_steps = max(tree.steps)
    mean_steps = round(statistics.mean(tree.steps), 3)
    std_steps = round(statistics.stdev(tree.steps), 3) if len(tree.steps) > 1 else 0
    median_steps = round(statistics.median(tree.steps), 3)

    min_rotations = min(tree.rotations)
    max_rotations = max(tree.rotations)
    mean_rotations = round(statistics.mean(tree.rotations), 3)
    std_rotations = round(statistics.stdev(tree.rotations), 3) if len(tree.rotations) > 1 else 0
    median_rotations = round(statistics.median(tree.rotations), 3)

    height = tree.tree_height(tree.root)
    leaves = tree.count_leaves(tree.root)

    return {
        "Steps": {
            "Min": min_steps,
            "Max": max_steps,
            "Mean": mean_steps,
            "Standard Deviation (std)": std_steps,
            "Median": median_steps
        },
        "Rotations": {
            "Min": min_rotations,
            "Max": max_rotations,
            "Mean": mean_rotations,
            "Standard Deviation (std)": std_rotations,
            "Median": median_rotations
        },
        "Height": height,
        "Leaves": leaves
    }

if __name__ == "__main__":
    clear_terminal()
    array1 = list(range(1, 5001))
    array1 = knuth_shuffle(array1)

    rb_tree = construct_red_black_tree(array1, "Part 1")
    time.sleep(1)

    clear_terminal()

    array2 = [random.randint(0, 100000) for _ in range(1000)]
    rb_tree.steps = []
    rb_tree.rotations = []

    rb_tree = construct_red_black_tree(array2, "Part 2")
    time.sleep(1)

    clear_terminal()

    print("\033[1;32mRed-Black Tree Construction Complete\033[0m\n")

    statistics = calculate_statistics(rb_tree)
    print_statistics(statistics)