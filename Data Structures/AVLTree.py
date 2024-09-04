import random
import statistics
import sys
import time

class AVLNode:
    """Node class for AVL Tree."""
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    """AVL Tree implementation."""
    def __init__(self):
        self.root = None
        self.steps = []  # List to track steps taken during insertion
        self.rotations = []  # List to track rotations during insertion
        self.height = 0  # Initialize height attribute
        self.leaves = 0  # Initialize leaves attribute

    def calculate_height(self, node):
        """Calculate height of a node."""
        return node.height if node else 0

    def rightRotate(self, y):
        """Right rotation operation."""
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = max(self.calculate_height(y.left), self.calculate_height(y.right)) + 1
        x.height = max(self.calculate_height(x.left), self.calculate_height(x.right)) + 1
        return x

    def leftRotate(self, x):
        """Left rotation operation."""
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = max(self.calculate_height(x.left), self.calculate_height(x.right)) + 1
        y.height = max(self.calculate_height(y.left), self.calculate_height(y.right)) + 1
        return y

    def getBalance(self, node):
        """Get balance factor of a node."""
        return self.calculate_height(node.left) - self.calculate_height(node.right)

    def insert(self, node, key):
        """Recursive function to insert a key into the tree."""
        if not node:
            return AVLNode(key)
        elif key < node.key:
            self.steps[-1] += 1
            node.left = self.insert(node.left, key)
        else:
            self.steps[-1] += 1
            node.right = self.insert(node.right, key)
        node.height = 1 + max(self.calculate_height(node.left), self.calculate_height(node.right))
        balance = self.getBalance(node)
        if balance > 1 and key < node.left.key:
            self.rotations[-1] += 1
            return self.rightRotate(node)
        if balance < -1 and key > node.right.key:
            self.rotations[-1] += 1
            return self.leftRotate(node)
        if balance > 1 and key > node.left.key:
            node.left = self.leftRotate(node.left)
            self.rotations[-1] += 1
            return self.rightRotate(node)
        if balance < -1 and key < node.right.key:
            node.right = self.rightRotate(node.right)
            self.rotations[-1] += 1
            return self.leftRotate(node)
        return node

    def insertKey(self, key):
        """Function to insert a key into the tree."""
        self.steps.append(0)  
        self.rotations.append(0) 
        self.root = self.insert(self.root, key)
        self.calculate_height_and_leaves()  

    def calculate_height_and_leaves(self):
        """Calculate height and number of leaves in the tree."""
        if self.root is None:
            self.height = 0
            self.leaves = 0
        else:
            self.height = self.calculate_tree_height(self.root)
            self.leaves = self.calculate_tree_leaves(self.root)

    def calculate_tree_height(self, node):
        """Recursive function to calculate height of the tree."""
        if node is None:
            return 0
        left_height = self.calculate_tree_height(node.left)
        right_height = self.calculate_tree_height(node.right)
        return max(left_height, right_height) + 1

    def calculate_tree_leaves(self, node):
        """Recursive function to calculate number of leaves in the tree."""
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1
        return self.calculate_tree_leaves(node.left) + self.calculate_tree_leaves(node.right)

    def get_statistics(self):
        """Compute statistics of the tree."""
        if not self.steps or not self.rotations:
            return None
        min_steps = min(self.steps)
        max_steps = max(self.steps)
        mean_steps = round(statistics.mean(self.steps), 3)
        std_steps = round(statistics.stdev(self.steps), 3) if len(self.steps) > 1 else 0
        median_steps = round(statistics.median(self.steps), 3)
        min_rotations = min(self.rotations)
        max_rotations = max(self.rotations)
        mean_rotations = round(statistics.mean(self.rotations), 3)
        std_rotations = round(statistics.stdev(self.rotations), 3) if len(self.rotations) > 1 else 0
        median_rotations = round(statistics.median(self.rotations), 3)
        height = self.height
        leaves = self.leaves
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

def knuth_shuffle(array):
    """Implement Knuth shuffle algorithm to randomize the order of elements in the array."""
    n = len(array)
    for i in range(n - 1, 0, -1):
        j = random.randint(0, i)
        array[i], array[j] = array[j], array[i]
    return array

def construct_avl_tree(array, part_name):
    """Construct the AVL tree from an array."""
    print(f"\033[1;32mConstructing AVL Tree ({part_name}):\033[0m")
    for i, num in enumerate(array):
        avl_tree.insertKey(num)
        progress = (i + 1) / len(array)
        sys.stdout.write("\r\033[1;32m[{:<50}] {:.2f}%\033[0m".format("=" * int(progress * 50), progress * 100))
        sys.stdout.flush()
    print("\n")

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

    avl_tree = AVLTree()
    construct_avl_tree(array1, "Part 1")
    time.sleep(1)

    clear_terminal()
    
    array2 = [random.randint(0, 100000) for _ in range(1000)]
    avl_tree.steps = []  
    avl_tree.rotations = []  
    construct_avl_tree(array2, "Part 2")
    time.sleep(1)

    clear_terminal()

    print("\033[1;32mAVL Tree Construction Complete\033[0m\n")
    time.sleep(1)

    statistics = avl_tree.get_statistics()
    if statistics:
        print_box("Steps", "\n".join([f"{key}: {value}" for key, value in statistics["Steps"].items()]))
        print("\n")
        time.sleep(1)
        print_box("Rotations", "\n".join([f"{key}: {value}" for key, value in statistics["Rotations"].items()]))
        print("\n")
        time.sleep(1)
        print(f"\033[1;32mHeight: {statistics['Height']}\033[0m")
        print(f"\033[1;32mLeaves: {statistics['Leaves']}\033[0m")