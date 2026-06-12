# Learning
Python - Hamrah Academy Final Project
Markdown
# Python Programming Practice

This repository contains my solutions to 5 algorithmic and logic problems written in Python. These exercises focus on standard programming concepts like loops, string manipulation, prime factorization, and basic text processing.

## 1. Twin Star Diamonds
**Description:** A program that takes an odd integer `n` and prints two side-by-side star diamonds of size `n`. The two diamonds share a single star in the middle row.
* **Input:** A single odd integer `n` (1 <= n <= 19).
* **Output:** The twin diamond pattern.
* **Example Input:** `3`
* **Example Output:** 

   * *
  *****
   * *


2. Digit Repeater
Description: A program that reads a number of unknown length and prints each digit repeated a number of times equal to its value.

Input: A single string of numbers (length < 100).

Output: Each digit printed in the format digit: repeated_string.

Example Input: 50943

Example Output:

Plaintext
  5: 55555
  0: 
  9: 999999999
  4: 4444
  3: 333


3. Next Power of 2
Description: A program that finds the first power of 2 that is strictly greater than the given input number n.

Input: A single integer n (1 <= n <= 10^9).

Output: The next power of 2 greater than n.

Example Input: 95

Example Output: 128


4. Prime Factorization
Description: A math algorithm that decomposes a number into its prime factors and prints them in ascending order.

Input: A single integer n (1 <= n <= 10^8).

Output: Prime factors in the format p1^k1*p2^k2.... If a prime factor has a power of 1, the power is omitted.

Example Input: 100

Example Output: 2^2*5^2


5. Simple Typo Finder
Description: A text processing tool designed to find typing errors. In normal English, 5 consonants rarely appear in a row. This program finds and reports any word containing 5 consecutive consonants. It ignores punctuation and skips fully uppercase words (like HTTPS) which might be abbreviations.

Input: A multi-line string of text containing normal sentences and punctuation.

Output: A space-separated list of misspelled words (words with 5+ consecutive consonants).

Example Input:

Plaintext
  HTTPS is short form of Hyper text transfrd protocol secure.
Example Output:

Plaintext
  transfrd
How to Run
To test any of the solutions, simply run the Python file in your terminal. For example:

Bash
python question1.py