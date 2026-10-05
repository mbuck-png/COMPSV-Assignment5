# 🔍 Problem 1: Find Most Frequent Element

# Given a list of integers, return the value that appears most frequently.
# If there's a tie, return any of the most frequent.

def most_frequent(numbers):
    counts = {}

    for number in numbers:
        if number in counts:
            counts[number] += 1
        else:
            counts[number] = 1

    if not counts:
        return None

    most_common = None
    highest_count = 0

    for number in counts:
        if counts[number] > highest_count:
            most_common = number
            highest_count = counts[number]

    return most_common


"""
Time and Space Analysis for problem 1:

- Best-case: O(n)
- Worst-case: O(n)
- Average-case: O(n)
- Space complexity: O(n)

- Why this approach?

I used a dictionary to count how many times each number appears.
The function goes through the list and then checks the dictionary
to find the number with the highest count.

- Could it be optimized?

It could be shortened by using collections.Counter, but the
dictionary approach is easy to understand and still has O(n)
time complexity.

The trade-off is that the dictionary uses extra memory, but it
makes counting much faster than repeatedly searching the list.
"""


# 🔍 Problem 2: Remove Duplicates While Preserving Order

# Write a function that returns a list with duplicates removed
# but preserves order.

def remove_duplicates(nums):
    seen = set()
    result = []

    for number in nums:
        if number not in seen:
            seen.add(number)
            result.append(number)

    return result


"""
Time and Space Analysis for problem 2:

- Best-case: O(n)
- Worst-case: O(n)
- Average-case: O(n)
- Space complexity: O(n)

- Why this approach?

I used a set to keep track of numbers that have already appeared.
This makes checking for duplicates quick while the result list
keeps the original order.

- Could it be optimized?

The solution is already efficient. A set gives average O(1)
lookup time.

The trade-off is that the set uses extra memory, but it makes
the solution faster than checking the result list every time.
"""


# 🔍 Problem 3: Return All Pairs That Sum to Target

# Write a function that returns all unique pairs of numbers
# in the list that sum to a target.
# Order of output does not matter. Assume input list has no duplicates.

def find_pairs(nums, target):
    seen = set()
    pairs = []

    for number in nums:
        needed = target - number

        if needed in seen:
            pairs.append((needed, number))

        seen.add(number)

    return pairs


"""
Time and Space Analysis for problem 3:

- Best-case: O(n)
- Worst-case: O(n)
- Average-case: O(n)
- Space complexity: O(n)

- Why this approach?

I used a set to quickly check whether the number needed to reach
the target has already been seen.

- Could it be optimized?

Yes. A nested-loop solution would take O(n²) because it compares
every number with every other number.

I optimized the solution by using a set. This reduces the lookup
to O(1) on average and makes the overall solution O(n).

Trade-off:

The optimized version uses O(n) extra memory, but it is much
faster than the original O(n²) approach for large lists.

Original approach:
O(n²) time and O(1) extra space.

Optimized approach:
O(n) average time and O(n) space.
"""


# 🔍 Problem 4: Simulate List Resizing (Amortized Cost)

# Create a function that adds n elements to a list that has a fixed
# initial capacity.
# When the list reaches capacity, simulate doubling its size by
# creating a new list and copying all values over.

def add_n_items(n):
    capacity = 2
    items = []

    for i in range(n):
        if len(items) == capacity:
            print("Resizing from", capacity, "to", capacity * 2)

            new_items = []

            for item in items:
                new_items.append(item)

            items = new_items
            capacity *= 2

        items.append(i)

    return items


"""
Time and Space Analysis for problem 4:

- When do resizes happen?

Resizing happens when the number of items reaches the current
capacity. The capacity is then doubled.

- What is the worst-case for a single append?

A single append can take O(n) when the list needs to resize
because all existing items have to be copied.

- What is the amortized time per append overall?

The amortized time per append is O(1). Resizing is expensive,
but it only happens occasionally.

- Space complexity:

O(n), because the list stores n items. During resizing, another
list is temporarily created to copy the values.

- Why does doubling reduce the cost overall?

Doubling the capacity means the list does not need to resize
after every append. This makes most append operations very fast.

The trade-off is that some extra memory is used during resizing,
but the overall performance is better.
"""


# 🔍 Problem 5: Compute Running Totals

# Write a function that takes a list of numbers and returns a new list
# where each element is the sum of all elements up to that index.

def running_total(nums):
    result = []
    total = 0

    for number in nums:
        total += number
        result.append(total)

    return result


"""
Time and Space Analysis for problem 5:

- Best-case: O(n)
- Worst-case: O(n)
- Average-case: O(n)
- Space complexity: O(n)

- Why this approach?

The function goes through the list once and keeps a running total.
This avoids repeatedly adding the same numbers.

- Could it be optimized?

The time complexity is already O(n), so there is not much to
improve. The space could be reduced by changing the original
list instead of creating a new one, but that would modify the
input.

The trade-off is using extra memory for the result while keeping
the original list unchanged.
"""


# --------------------------------------------------
# Test Cases
# --------------------------------------------------

print("Problem 1:")
print(most_frequent([1, 3, 2, 3, 4, 1, 3]))
print(most_frequent([5]))
print(most_frequent([]))

print("\nProblem 2:")
print(remove_duplicates([4, 5, 4, 6, 5, 7]))
print(remove_duplicates([1, 1, 1, 1]))
print(remove_duplicates([]))

print("\nProblem 3:")
print(find_pairs([1, 2, 3, 4], 5))
print(find_pairs([1, 5, 7, 3], 8))
print(find_pairs([], 10))

print("\nProblem 4:")
print(add_n_items(6))
print(add_n_items(0))

print("\nProblem 5:")
print(running_total([1, 2, 3, 4]))
print(running_total([5]))
print(running_total([]))
