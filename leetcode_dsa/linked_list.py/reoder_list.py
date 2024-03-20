class ListNode:
  def __init__(self, val=0, next=None):
      self.val = val
      self.next = next

class Solution:
  def reorderList(self, head: 'Optional[ListNode]') -> None:
      if not head or not head.next:
          return

      # Step 1: Find the middle of the list
      slow, fast = head, head
      while fast.next and fast.next.next:
          slow = slow.next
          fast = fast.next.next

      # Step 2: Reverse the second half of the list
      prev, curr = None, slow.next
      while curr:
          nxt = curr.next
          curr.next = prev
          prev = curr
          curr = nxt
      # Disconnect the first half and the second half
      slow.next = None

      # Step 3: Merge the two halves
      first, second = head, prev
      while second:
          tmp1, tmp2 = first.next, second.next
          first.next = second
          second.next = tmp1
          first, second = tmp1, tmp2
