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
