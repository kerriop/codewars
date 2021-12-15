from typing import List, Optional


# 3
def findDisappearedNumbers(nums: List[int]) -> List[int]:
    i = 0
    while i < len(nums):
        pos = nums[i] - 1
        if nums[i] != nums[pos]:
            nums[i], pos[i] = nums[pos], nums[i]
        else:
            i += 1
    miss = []
    for i in range(len(nums)):
        if nums[i] != i + 1:
            miss.append(i + 1)
    return miss


# 4
def singleNumber(nums: List[int]) -> int:
    mask = 0

    for num in nums:
        mask ^= num
    return mask


# 5
def climbStairs(n: int) -> int:
    if n == 1:
        return 1
    n1 = 1
    n2 = 2
    for i in range(3, n + 1):
        n1, n2 = n2, n1 + n2
    return n2


# 6
def maxProfit(prices: List[int]) -> int:
    max_profit = 0
    current_min = prices[0]

    for i in range(1, len(prices)):
        price = prices[i]

        max_profit = max(max_profit, price - current_min)
        current_min = min(current_min, price)

    return max_profit


# 7
def maxSubArray(nums: List[int]) -> int:
    max_sum = nums[0]
    current_sum = nums[0]

    for i in range(1, len(nums)):
        num = nums[i]

        current_sum = max(current_sum + num, num)
        max_sum = max(current_sum, max_sum)

    return max_sum


# 8
# class NumArray:
#     def __init__(self, nums: List[int]):
#
#
#     def sumRange(self, left: int, right: int) -> int:

# 9
def countBits(n: int) -> List[int]:
    memo = [0] * (n + 1)
    for i in range(1, n + 1):
        memo[i] = memo[i >> 1] + i % 2
    return memo[:n + 1]


# 10
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def hasCycle(head: ListNode) -> bool:
    if not head:
        return False

    slow = fast = head
    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True
    return False


# 11
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def middleNode(head: ListNode) -> ListNode:
    slow = fast = head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    return slow


# 12
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head: ListNode) -> ListNode:
    prev = None
    current = head

    while current:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
    return prev


# 13
def isPalindrome(head: ListNode) -> bool:
    if not head:
        return None
    middle = middleNode(head)
    reverse = reverseList(middle)

    while reverse:
        if reverse.val != head.val:
            return False
        reverse = reverse.next
        head = head.next
    return True


# 14
def removeElements(head: ListNode, val: int) -> ListNode:
    result = ListNode(0)
    result.next = head

    current = result
    while current.next:
        if current.next.val == val:
            current.next = current.next.next
        else:
            current = current.next

    return result.next


# 15
def deleteDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    current = head

    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    return head


# 16
def mergeTwoLists(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    merged = ListNode(0)
    result = merged

    while l1 and l2:
        if l1.val < l2.val:
            merged.next = ListNode(l1.val)
            l1 = l1.next
        else:
            merged.next = ListNode(l2.val)
            l2 = l2.next

        merged = merged.next

    while l1:
        merged.next = ListNode(l1.val)
        l1 = l1.next
        merged = merged.next
    while l2:
        merged.next = ListNode(l2.val)
        l2 = l2.next
        merged = merged.next

    return result.next


# 17
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


def canAttendMeetings(intervals):
    intervals = sorted(intervals, key=lambda x: x.start)

    for i in range(len(intervals) - 1):
        if intervals[i].end > intervals[i + 1].start:
            return False

    return True


# 18
def search(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right:
        middle = left + (right - left) // 2

        if nums[middle] == target:
            return middle
        if nums[middle] > target:
            right = middle - 1
        else:
            left = middle + 1
    return - 1


# print(search([-1, 0, 3, 5, 9, 12], 9))

# 19
def nextGreatestLetter(letters: List[str], target: str) -> str:
    left = 0
    right = len(letters) - 1

    while left <= right:
        middle = left + (right - left) // 2

        if letters[middle] > target:
            right = middle - 1
        else:
            left = middle + 1
    return letters[left % len(letters)]


# 20
def peakIndexInMountainArray(arr: List[int]) -> int:
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            right = mid - 1
    return left
