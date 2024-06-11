'''
Given an array of integers `a`, your task is to find how many of its contiguous subarrays of length `m` contain a pair of integers with a sum equal to `k`.

More formally, given the array `a`, your task is to count the number of indices `0 <= i <= a.length - m` such that a subarray `[a[i], a[i+1], ..., a[i + m - 1]]` contains at least one pair `(a[s], a[t])` where:

* `a != t`
* `a[a] + a[t] = k`

Example

For `a = [2, 4, 7, 5, 3, 5, 8, 5, 1, 7]`, `m=4`, and `k=10`, the output should be `solution(a, m, k) = 5`:

* Subarray a[1...4] = [4, 7, 5, 3] contains a[2] + a[4] = 7 + 3 = 10
* Subarray a[2..5] = [7, 5, 3, 5] contains two pairs, let's take one, a[2] + a[4] = 7 + 3 + 10
* Subarray a[3...6] = [5, 3, 5, 8] contains a[3] + a[5] = 5 + 5 = 10
* Subarray a[4...7] = [3, 5, 8, 5] contains a[5] + a[7] = 5 + 5 = 10
* Subarray a[5...8] = [5, 8, 5, 1] contains a[5] + a[7] = 5 + 5 = 10
'''
