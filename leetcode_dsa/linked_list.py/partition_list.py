class ListNode:
  def __init__(self, val=0, next=None):
      self.val = val
      self.next = next

class Solution:
  def partition(self, head: ListNode, x: int) -> ListNode:
      # Create two dummy nodes for the two partitions
      before_head = ListNode(0)
      after_head = ListNode(0)
      # Pointers to the current node in each partition
      before = before_head
      after = after_head

      while head:
          # If the current node's value is less than x, place it in the 'before' list
          if head.val < x:
              before.next = head
              before = before.next
          else:
              # Otherwise, place it in the 'after' list
              after.next = head
              after = after.next
          # Move to the next node
          head = head.next

      # Connect the two partitions
      before.next = after_head.next
      # Make sure to end the list to prevent a cycle
      after.next = None

      # Return the start of the 'before' list, skipping the dummy node
      return before_head.next
