# Here is my HackerRank Solutions

> The repository contains the solutions to various HackerRank problems.Organize the solutions so they are easy to navigate and understand. Each solution includes a reference to the problem statement and is well-documented to explain the logic and approach.

---

You can find the problem statements and descriptions for these solutions by following the provided commands within the Python programs or by visiting the Hackerrank website [here](https://www.hackerrank.com/challenges). Simply search for the program name to access the detailed problem statement.

---

### birthdayCakeCandles

- [Solution](./python/Birthday%20Cake%20Candles.py)

### - Explanation:

        The function birthdayCakeCandles takes a list of integers called candles as input, representing the heights of candles.
        It initializes two variables: max_height to keep track of the maximum height and count to store the count of candles with
        the maximum height. Both are initially set to 0.
        The max function is used to find the maximum height among all the candles in the candles list.
        This is done by iterating through the list and updating max_height if a taller candle is found.
        After finding the maximum height, the function uses the count method on the candles list to count how many times the maximum
        height appears in the list. This count represents the number of candles with the tallest height.
        Finally, the count is returned as the result of the function.
        For example, let's say the input list candles is [4, 4, 1, 3, 2, 4]. The function will identify
        that the tallest candles have a height of 4 and count how many times 4 appears in the list, which is 3.
        Therefore, the function will return 3 as the output.

---

### Sherlock and the Valid String

- [Solution](./python/Sherlock%20and%20the%20Valid%20String.py)

### - Explanation:

        Create a dictionary to count the frequency of each character in the string.
        Create another dictionary to count the frequency of each character frequency. For example, if the original string has the following character frequencies: {'a': 2, 'b': 2, 'c': 1}, then the frequency count of character frequencies would be: {2: 2, 1: 1}.
        Check if there are more than two different character frequencies. If there are more than two, it's not possible to make the string valid.
        If there are only one or two different character frequencies, check if one of the following conditions is met:
        a. If there is only one character with a frequency of 1, it's possible to remove that character to make the string valid.
        b. If the difference between the two character frequencies is 1 and one of them occurs only once, you can remove that character to make the string valid.
        c. If one of the character frequencies is 1 and the character occurs at the maximum frequency, you can remove one instance of that character to make the string valid.

---

### Sherlock and Anagrams

- [Solution](./python/Sherlock%20and%20Anagrams.py)

### - Explanation:

        The sherlockAndAnagrams function calculates anagrammatic pairs by iterating through all possible substrings of the input string and storing the frequency of each substring's characters in the substr_freq dictionary.
        It uses a sorted version of the characters in the substring as a key to identify anagrams. If two substrings have the same sorted character frequency, they are anagrams.
        It keeps track of the count of anagrammatic pairs and increments it when it encounters the same character frequency pattern.
        Finally, the function returns the count of anagrammatic pairs.

---

### Common Child

- [Solution](./python/Common%20Child.py)

### - Explanation:

        The code defines a function, commonChild, to find the length of the longest common child between two input strings, s1 and s2. It uses dynamic programming to build a 2D table (dp) and iterates through the strings, incrementing dp values for matching characters. The final value in dp represents the answer, which is the length of the longest common child.

---

### Count Strings

- [Solution](./python/Count%20Strings.py)

### - Explanation:

        This Python code counts the number of valid strings of a given length that match a regular expression. It uses NFA and DFA representations, translates the regular expression, and efficiently calculates the count of matching strings. Input is read from and results are written to external files.

---

### String Function Calculation

- [Solution](./python/String%20Function%20Calculation.py)

### - Explanation:

        The Python code defines a function maxValue that computes the maximum score for a given string t. It employs various string processing techniques, including suffix arrays and longest common prefixes, to find repeating patterns in the input string. The corrected code ensures proper execution and accurate result computation for the specified task.

---

### Build a String

- [Solution](./python/Build%20a%20String.py)

### - Explanation:

        The Python code defines a function buildString that calculates the minimum cost of constructing a target string 's' with two operations: appending a character at a cost 'a' or copying a substring at a cost 'b'. The function uses dynamic programming to determine the optimal way to construct 's'. The code reads input values for the number of test cases, the costs 'a' and 'b', and the target string 's', and then calculates and prints the minimum cost for each test case. It does this by maintaining an array 'costs' where each element represents the minimum cost to construct the string up to that position. The code then iterates through the characters in 's', trying to find repeated substrings and comparing the cost of appending a character with the cost of copying a substring. The final result is the minimum cost to construct 's'. The code is designed to read input from standard input and write output to standard output.

---

### Cards Permutation

- [Solution](./python/Cards%20Permutation.py)

### - Explanation:

        The Python code defines a function called solve, which takes a list of integers 'x' as input. It implements a solution to a mathematical problem involving permutations and missing elements. The code uses a Fenwick tree data structure to efficiently calculate the total cost of rearranging the elements in 'x' to form a specific sequence. The result is then written to an output file.

---