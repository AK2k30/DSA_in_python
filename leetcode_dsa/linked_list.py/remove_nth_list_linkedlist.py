class ListNode:
  def __init__(self, val=0, next=None):
      self.val = val
      self.next = next

class Solution:
  def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
      # Initialize a dummy node to simplify edge cases
      dummy = ListNode(0, head)
      fast = slow = dummy

      # Move fast pointer n steps ahead
      for _ in range(n):
          fast = fast.next

      # Move both pointers until fast reaches the end
      while fast.next:
          fast = fast.next
          slow = slow.next

      # Remove the nth node from the end
      slow.next = slow.next.next

      # Return the head of the modified list
      return dummy.next
