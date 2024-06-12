'''
https://leetcode.com/problems/hand-of-straights

    Alice has some number of cards and she wants to rearrange the cards into groups so that each group 
    is of size groupSize, and consists of groupSize consecutive cards.

    Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, 
    return true if she can rearrange the cards, or false otherwise.

    Example 1:

        Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
        Output: true
        Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]
  
     Example 2:

        Input: hand = [1,2,3,4,5], groupSize = 4
        Output: false
        Explanation: Alice's hand can not be rearranged into groups of 4.

    Constraints:

        1 <= hand.length <= 104
        0 <= hand[i] <= 109
        1 <= groupSize <= hand.length
'''


from typing import List
from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0: return False

        hand_counter = Counter(hand)
        hand_ordered = sorted(hand_counter.keys())

        for card in hand_ordered:
            card_qty = hand_counter[card]

            if card_qty == 0: continue
            
            for i in range(1, groupSize):
                next_card = card + i
                if (
                    (next_card not in hand_counter)
                    or (hand_counter[next_card] == 0)
                ):
                    return False

                hand_counter[next_card] -= card_qty

        return True


if __name__ == '__main__':
    print(Solution().isNStraightHand([1,2,3,6,2,3,4,7,8], 3))
    print(Solution().isNStraightHand([1,2,3,4,5], 4))
    print(Solution().isNStraightHand([8,8,9,7,7,7,6,7,10,6], 2))
    print(Solution().isNStraightHand([2,3,4,5,6,7,8,9], 8))
    print(Solution().isNStraightHand(
        [66,75,4,37,92,87,68,65,58,100,97,42,19,66,73,1,5,44,30,29,76,31,12,35,26,93,
         9,36,90,16,86,15,4,9,13,98,10,14,18,90,89,3,10,65,24,31,43,25,54,55,54,81,10,
         80,31,12,15,14,59,27,64,93,32,26,69,79,13,32,29,24,27,91,92,82,37,101,100,61,74,
         30,91,62,36,92,28,23,4,63,55,3,11,11,101,22,34,25,2,75,43,72], 2))
    print(Solution().isNStraightHand([1,1,2,2,3,3], 2))