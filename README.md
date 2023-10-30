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
        Create another dictionary to count the frequency of each character frequency.
        For example, if the original string has the following character frequencies: {'a': 2, 'b': 2, 'c': 1},
        then the frequency count of character frequencies would be: {2: 2, 1: 1}.
        Check if there are more than two different character frequencies. If there are more than two, it's not possible to make the string valid.
        If there are only one or two different character frequencies, check if one of the following conditions is met:
        a. If there is only one character with a frequency of 1, it's possible to remove that character to make the string valid.
        b. If the difference between the two character frequencies is 1 and one of them occurs only once, you can remove that character to make the string valid.
        c. If one of the character frequencies is 1 and the character occurs at the maximum frequency, you can remove one instance of that character to make the string valid.

---

### Sherlock and Anagrams

- [Solution](./python/Sherlock%20and%20Anagrams.py)

### - Explanation:

        The sherlockAndAnagrams function calculates anagrammatic pairs by iterating through all possible substrings of
        the input string and storing the frequency of each substring's characters in the substr_freq dictionary.
        It uses a sorted version of the characters in the substring as a key to identify anagrams.
        If two substrings have the same sorted character frequency, they are anagrams.
        It keeps track of the count of anagrammatic pairs and increments it when it encounters
        the same character frequency pattern.
        Finally, the function returns the count of anagrammatic pairs.

---

### Common Child

- [Solution](./python/Common%20Child.py)

### - Explanation:

        The code defines a function, commonChild, to find the length of the longest common child between two input strings, s1 and s2.
        It uses dynamic programming to build a 2D table (dp) and iterates through the strings,
        incrementing dp values for matching characters.
        The final value in dp represents the answer, which is the length of the longest common child.

---

### Count Strings

- [Solution](./python/Count%20Strings.py)

### - Explanation:

        This Python code counts the number of valid strings of a given length that match a regular expression.
        It uses NFA and DFA representations, translates the regular expression, and efficiently calculates the count of matching strings.
        Input is read from and results are written to external files.

---

### String Function Calculation

- [Solution](./python/String%20Function%20Calculation.py)

### - Explanation:

        The Python code defines a function maxValue that computes the maximum score for a given string t.
        It employs various string processing techniques, including suffix arrays and longest common prefixes, to find repeating patterns in the input string.
        The corrected code ensures proper execution and accurate result computation for the specified task.

---

### Build a String

- [Problem statement](https://www.hackerrank.com/challenges/build-a-string/problem)
- [Solution](./python/Build%20a%20String.py)

### - Explanation:

        The Python code defines a function buildString that calculates the minimum cost of constructing a target string 's' with two operations: appending a character at a cost 'a' or copying a substring at a cost 'b'.
        The function uses dynamic programming to determine the optimal way to construct 's'.
        The code reads input values for the number of test cases, the costs 'a' and 'b', and the target string 's',
        and then calculates and prints the minimum cost for each test case.
        It does this by maintaining an array 'costs' where each element represents the minimum cost to construct the string up to that position.
        The code then iterates through the characters in 's', trying to find repeated substrings and comparing the cost of appending a character with the cost of copying a substring.
        The final result is the minimum cost to construct 's'.
        The code is designed to read input from standard input and write output to standard output.

---

### Cards Permutation

- [Problem statement](https://www.hackerrank.com/challenges/cards-permutation/problem)
- [Solution](./python/Cards%20Permutation.py)

### - Explanation:

        The Python code defines a function called solve, which takes a list of integers 'x' as input.
        It implements a solution to a mathematical problem involving permutations and missing elements.
        The code uses a Fenwick tree data structure to efficiently calculate the total cost of rearranging the elements in 'x' to form a specific sequence.
        The result is then written to an output file.

---

### Super Reduced String

- [Solution](./python/Super%20Reduced%20String.py)

### - Explanation:

        The code defines a function superReducedString that takes a string s as input and repeatedly removes adjacent matching characters
        until no more matches are found or the string becomes empty.
        If the final string is empty, it returns "Empty String"; otherwise, it returns the reduced string.
        The code uses a while loop to iterate through the string, checking for adjacent matching characters, and removes them until no more matches are found.

---

### Staircase

- [Solution](./python/Staircase.py)

### - Explanation:

        The code defines a function staircase that takes an integer n as input.
        It prints a staircase pattern of height n using spaces and '#' symbols.
        It does this by iterating from 1 to n, printing spaces (n - i) times followed by '#' i times on each line.
        The main block reads the input integer n and calls the staircase function.

---

### Gridland Provinces

- [Solution](./python/Gridland%20Provinces.py)

### - Explanation:

        The provided Python script defines a function gridlandProvinces that calculates the number of unique provinces formed by
        two strings s1 and s2 by concatenating and overlapping them in various ways.
        It utilizes custom hashing techniques to efficiently count the provinces.
        The script reads input data and writes the results to an output file.

---

### Ashton and String

- [Solution](./python/Ashton%20and%20String.py)

### - Explanation:

        The Python code defines a function ashtonString that calculates the k-th character of a modified version of a given string.
        It uses a data structure called a Suffix Array and Longest Common Prefix array to efficiently compute the result.
        The function takes an input string 's' and an integer 'k' and returns the k-th character of the modified string.
        The code reads the number of test cases, input strings, and 'k' values from standard input and writes the results to an output file.

---

### String Similarity

- [Solution](./python/String%20Similarity.py)

### - Explanation:

        The code defines a function, string_similarity, which calculates the similarity of a string s to itself using the Z-algorithm.
        It iterates through the string, computing the length of the longest common prefix between the string and its substrings.
        The total similarity score is the sum of these lengths.

---

### Super Functional Strings

- [Solution](./python/Super%20Functional%20Strings.py)

### - Explanation:

        The code computes super functional strings. It uses various functions to calculate values for given substrings in a string.
        It employs suffix arrays and longest common prefix to determine the common substrings in the input string and efficiently computes the desired results
        while considering character occurrences and powers modulo a given value.

---

### Save Humanity

- [Solution](./python/Save%20Humanity.py)

### - Explanation:

        The Python script defines a function virusIndices that takes two input strings, 'text' and 'pattern'.
        It searches for occurrences of 'pattern' within 'text' and returns the starting indices of matches.
        The function uses a helper function 'match' to compare partial strings for potential matches.
        If there are no matches, it returns "No Match!" Otherwise, it returns the indices as a space-separated string.
        The code reads input test cases, calls the 'virusIndices' function, and prints the results.

---

### Find Strings

- [Solution](./python/Find%20Strings.py)

### - Explanation:

        The Python code defines a program for finding common prefixes of words and returning them based on user queries.
        It uses a suffix array data structure to efficiently find these prefixes.
        The code reads input words, processes them, and then handles user queries to extract and print the desired common prefixes.

---

### Two Two

- [Solution](./python/Two%20Two.py)

### - Explanation:

        The Python code defines a function 'twoTwo' that counts the number of times a specific pattern ('2's) appears in a binary representation of numbers generated up to 2^800.
        It uses a trie data structure to efficiently count the occurrences.
        The code reads input strings, performs pattern counting, and writes the results to an output file.

---

### Palindromic Border

- [Solution](./python/Two%20Two.py)

### - Explanation:

        The provided code defines a Python function palindromicBorder that calculates the number of palindromic substrings within a given input string 's'.
        It first checks if 's' is a monosubstring (consisting of only one character) and computes the count of such substrings.
        Then, it calculates the count of palindromic substrings with even and odd lengths using dynamic programming.
        The code returns the total count of palindromic substrings.

---
