# 🚀 Algorithmic Problem Solving & Logic Foundations

## Comprehensive Python Solutions for 5 Core Challenges

This repository contains clean, optimized, and mathematically sound Python solutions for a series of core algorithmic and logic-based programming challenges. 

We went beyond merely finding the correct answers; the focus of this repository is on writing readable, efficient code that handles edge cases perfectly. The solutions are designed to be robust enough for automated judging systems (such as Quera) while maintaining high structural quality.

## ✨ Key Highlights

- 🛡️ **Zero External Dependencies:** Built entirely using Python's standard library (`sys`, math operations), ensuring maximum portability and rapid execution time.
- 🧠 **Optimized Time Complexity:** Applied advanced mathematical shortcuts—such as iterating only up to `i * i <= n` for prime factorization—to effortlessly handle massive input constraints (up to 10^8).
- 🤖 **Robust Text Processing:** Implemented a state-machine-like approach for typo detection, carefully filtering out punctuation, handling edge cases, and ignoring valid abbreviations (e.g., HTTPS).
- 🎛️ **Dynamic Pattern Generation:** Utilized dynamic string manipulation and index mapping to generate complex, overlapping 2D geometric patterns (Twin Diamonds) in the terminal.
- 🎯 **Standardized I/O Pipelines:** All scripts are built with standard `stdin` and `stdout` handling, making them fully compatible with server-side algorithmic test environments.

## 📈 Algorithmic Breakdown & Performance

By eliminating brute-force methods and focusing on optimized logic, the solutions address different computer science fundamentals:

| Problem Name | Evaluation Concept | Mathematical / Algorithmic Implication |
|--------------------------|----------------|------------------------------------------------------------------------------------------------------------------|
| **1. Twin Diamonds** | 2D Geometry & Nested Loops | Calculates precise spaces and active characters to merge two distinct shapes with a shared center axis. |
| **2. Digit Repeater** | String/Int Casting | Demonstrates dynamic string multiplication driven by on-the-fly character value parsing. |
| **3. Next Power of 2** | Loop Logic | Efficiently scales a base multiplier in a `while` loop until the dynamic upper bound is surpassed. |
| **4. Prime Factorization**| Number Theory | Reduces brute-force factorization time significantly by stopping the primary loop at the square root of `n`. |
| **5. Typo Finder** | Text Parsing & Conditionals | Tracks consecutive consonant states while dynamically ignoring vowels, symbols, and fully capitalized words. |

## 🛠️ Repository Structure

```text
📦 PYTHON-ALGORITHMS
┣ 📂 src                                       # Core source code containing all solutions
┃ ┣ 📜 question1.py                            # Solution: Twin Star Diamonds
┃ ┣ 📜 question2.py                            # Solution: Digit Repeater
┃ ┣ 📜 question3.py                            # Solution: Next Power of 2
┃ ┣ 📜 question4.py                            # Solution: Prime Factorization
┃ ┗ 📜 question5.py                            # Solution: Simple Typo Finder
┣ 📜 .gitignore
┗ 📜 README.md
```

📦 Requirements
Core Language
Python >= 3.6
Note: No external packages (like NumPy or Pandas) are required. The entire pipeline relies purely on Python's built-in capabilities.

🚀 How to Run
Pipeline Execution
The project is modular. You can run and test each algorithmic challenge independently via the terminal.

Phase 1: Mathematical & Logic Problems
Bash
# 1. Run the Twin Diamonds generator
python src/question1.py
# Input: Single odd integer (e.g., 5)

# 2. Run the Digit Repeater
python src/question2.py
# Input: A string of numbers (e.g., 50943)

# 3. Find the Next Power of 2
python src/question3.py
# Input: Single integer (e.g., 95)

# 4. Execute Prime Factorization
python src/question4.py
# Input: Large integer to factorize (e.g., 100)
Phase 2: Text Processing
Bash
# 5. Run the Typo Finder
python src/question5.py
# Input: Multi-line text. To submit the input, press Enter twice to trigger EOF.
💡 Logic Layer: X-Ray into Prime Factorization (Q4)
Algorithmic efficiency is critical when dealing with large inputs. For Question 4 (Prime Factorization), a naive approach would iterate from 2 to n.

Our engine optimizes this by using the i * i <= n mathematical rule. This drastically cuts down execution time.

Real Output Example from the System:

🔢 Input Value: 98
⚙️ Execution Engine Processing...
🔍 Factorization Steps:
    - Divisible by 2 (Count: 1) -> n becomes 49
    - Divisible by 7 (Count: 2) -> n becomes 1
💡 System Output:
    2*7^2