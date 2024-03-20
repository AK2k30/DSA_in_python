class ListNode:
  def __init__(self, x):
      self.val = x
      self.next = None

class Solution:
  def hasCycle(self, head: ListNode) -> bool:
      # Initialize both pointers at the head of the list
      slow = head
      fast = head

      # Loop until fast pointer reaches the end of the list
      while fast and fast.next:
          slow = slow.next           # Move slow pointer by 1
          fast = fast.next.next      # Move fast pointer by 2

          # Check if the pointers have met
          if slow == fast:
              return True

      # If we reach here, there's no cycle
      return False
