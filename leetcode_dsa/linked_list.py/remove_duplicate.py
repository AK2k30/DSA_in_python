class ListNode:
  def __init__(self, val=0, next=None):
      self.val = val
      self.next = next

class Solution:
  def deleteDuplicates(self, head: ListNode) -> ListNode:
      current = head
      # Loop through the list until the end
      while current and current.next:
          # If the current value is the same as the next value, skip the next node
          if current.val == current.next.val:
              current.next = current.next.next
          else:
              # Move to the next node if no duplicate
              current = current.next
      return head
