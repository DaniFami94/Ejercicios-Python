```python
# Algorithm is a set of steps or instructions for completing a task

- Clearly defined problem statement,input and output. Input is a list of values and output is the target value.

- The steps in the algorithm need to be in a very specific order.

- The steps also need to be distinct.

- The algorithm should produce a result.

- The algorithm should complete in a finite amount of time.

# Understanding Big O Notation

- Linear search O(n).

- binary search O(log n): you need first to sort the given list and then apply the binary search.

- Big O is a notation used to describe complexity.

- "O" means: Order of magnitud of complexity.

- Big O measures how the algorithm performs in the worst case scenario.

- Reading a value in a list is a constant time operation.

`O(1) Constant time complexity`: where the algorithm's runtime remains constant regardless of the input size.

- Description: Algorithms with constant time complexity execute in a constant amount of time regardless of the input size.

- Example: Accessing an element in an array by index.

- Comparison: Regardless of the input size, the time is the same.

`O(n) Linear Time Complexity`: When a problem involves reading every item in a list.

- Description: Algorithms with linear time complexity have their runtime grow linearly with the input size.

- Example: Linear search through an unsorted array.

- Comparison: The runtime increases proportionally to the input size.

`O(log n) Logarithmic Time Complexity`: As n grow really large, the number of operations to find the result grows very slowly and flattens out.

- Description: Algorithms with logarithmic time complexity have their runtime grow logarithmically with the input size.

- Example: Binary search in a sorted array.

- Comparison: As the input size increases, the runtime grows slowly, making it more efficient than linear time complexities.


`O(n²) Quadratic time Complexity`: for any given value of n, we carry out n squared number of operation, for example:
 n = 4
 n^2 = 16

- Description: Algorithms with quadratic time complexity have their runtime grow quadratically with the input size.

- Example: Nested loops iterating over the input.

- Comparison: As the input size increases, the runtime grows quadratically, making it less efficient for large inputs.

`O(n log n) Quasilinear Runtimes Complexity`: for every value of n were are going to execute a log n number of operations, hence the run time of n times log n

- Description: Algorithms with quadratic time complexity have their runtime grow quadratically with the input size.

- Example: Nested loops iterating over the input.

- Comparison: As the input size increases, the runtime grows quadratically, making it less efficient for large inputs.

`O(2^n) Exponential Time Complexity`:Brute force algorithms have exponential run times making them very slow, and too expensive computationally to be used because the numbers of operations grow exponentially, for example trying to guess a password of 20 character lenght with a possible combination of 69 characters: this includes letters, numbers from 0 to 9, and special characters.

- Description: Algorithms with exponential time complexity have their runtime grow exponentially with the input size.

- Example: Brute-force algorithms that try all possible combinations.

- Comparison: Extremely inefficient for large inputs, as the runtime increases rapidly with even small increases in input size.

`O(n!) Factorial Time Complexity`: traveling salesman problem, see this example in the web for more explanation.

- Description: Algorithms with factorial time complexity have their runtime grow factorially with the input size.

- Example: Algorithms generating all permutations of a set.

- Comparison: Highly inefficient, with the runtime growing extremely fast with the input size.

# Space complexity is a measure of how much working storage or extra storage is needed as a particular algorithm grows
```
