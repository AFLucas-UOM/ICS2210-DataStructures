# Comparison of Datastructures - ICS2210 Course Project
 This repository compares AVL Trees, Red-Black Trees, and Skip Lists through custom implementations and performance testing. It evaluates these data structures based on insertion statistics like steps, rotations, and tree height.

## Introduction
Introduction
In computer science, the choice of data structure can significantly impact the efficiency and performance of algorithms. This project focuses on comparing three fundamental data structures: AVL Trees, Red-Black Trees, and Skip Lists.

AVL Trees are a type of self-balancing binary search tree where the heights of the two child subtrees of any node differ by no more than one. Red-Black Trees are another form of self-balancing binary search tree with additional constraints to ensure balanced height and provide efficient insertion and deletion operations. Skip Lists, on the other hand, are a probabilistic alternative that use multiple levels of linked lists to achieve balanced search times.

This repository provides custom implementations of these data structures and evaluates their performance through various metrics, including insertion statistics, the number of rotations, and the overall tree height. By analyzing these factors, the project aims to shed light on the practical differences and efficiencies of each data structure.

## Motivation
The primary motivation behind this project is to understand and compare the practical implications of using different self-balancing data structures. While theoretical analysis of AVL Trees, Red-Black Trees, and Skip Lists provides insights into their expected performance, real-world performance can vary based on implementation details and specific usage scenarios.

By implementing and testing these data structures, this project seeks to:

- Offer a hands-on comparison of their operational characteristics.
- Measure how each data structure handles insertions and maintains balance.
- Provide empirical data on the performance trade-offs between these data structures in terms of steps required, rotations performed, and height adjustments.

This project serves as both an educational exercise and a practical guide for developers and researchers who need to make informed decisions about data structure choices in their work.

## Getting Started

### Prerequisites

- Python 3.x
- Python libraries: `random`, `statistics`, `sys`, `time`, and `math`

### Installation

Clone the repository:
   ```
   git clone https://github.com/AFLucas-UOM/ICS2210-DataStructures.git
   ```

## Acknowledgments

This project was developed as part of an academic assignment. Unit: `ICS2210` at the `University of Malta`.

## Contact

For any inquiries or feedback, please contact [Andrea Filiberto Lucas](mailto:andrea.f.lucas.22@um.edu.mt)
