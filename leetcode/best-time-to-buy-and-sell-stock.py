"""
LC: https://leetcode.com/problems/best-time-to-buy-and-sell-stock

Approach 1
==========

* two-pointer approach.
* left points to the buy day, and right points to the sell day.
* each day in the prices array is checked for (potential) sell day.
* additionally, the lowest stock price seen so far is maintained.
  and as soon as a lower price is seen, lowest so far is updated to that price.

* so for each day:
- what's the profit if sold on this day (i.e., r = 1 ... n-1)
- after considering this day as the sell day, check if should be the buy day
  (i.e., current price < lowest_so_far)


* time complexity: O(n)
* where n = length of prices array

* space complexity: O(1)
* no aux space required; just two pointers


Approach 2
==========

(this approach is similar but more intiuitive to me, and I came up with first, by myself)

* for each stock price, we check the profit if we sold it on that day
* compared with the lowest price seen so far; which is considered as the buy day
* which means, lowest so far is maintained
* and whenever a lower price is seen, lowest so far is updated to that

* this is similar to approach 1
* where each day is evaluated as the potential sell day
* while lowest price is tracked as the potential buy day

* time complexity: O(n) and space complexity: O(1)
"""


# Approach 1
# def maxProfit(prices: List[int]) -> int:
#     # l = buy day and r = sell day
#     l, r = 0, 1
#     # maximum profit so far
#     max_profit = 0
#     # consider each day as a sell day
#     while r < len(prices):
#         # buy first (l) and then sell (r)
#         buy, sell = prices[l], prices[r]
#         # check if the new profit is higher than max profit seen so far
#         max_profit = max(max_profit, sell - buy)
#         # new mimum seen for buy day, so update the buy day pointer
#         if sell < buy:
#             l = r
#         # check next day as sell day
#         r += 1
    
#     return max_profit

# Approach 2
def maxProfit(prices: List[int]) -> int:
    # tracks lowest price of stock seen so far
    lowest_price = prices[0]
    # tracks maximum profit seen so far
    max_profit = 0

    # for each day starting 2 day
    for i in range(1, len(prices)):
        current_price = prices[i]
        # what's the profit if sold on this day, and bought on lowest seen so far?
        current_profit = current_price - lowest_price
        # is this profit bigger than maximum profit seen so far?
        max_profit = max(max_profit, current_profit)
        # is this new price the lowest price seen so far?
        lowest_price = min(lowest_price, current_price)
    
    return max_profit
