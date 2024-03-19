class ListNode:
  def __init__(self, val=0, next=None):
      self.val = val
      self.next = next

class Solution:
  def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
      # Initialize the dummy head of the resulting list
      dummy = ListNode(0)
      # Initialize the current node to dummy
      current = dummy
      # Initialize carry to 0
      carry = 0

      # Loop through lists l1 and l2 until you reach both ends
      while l1 or l2:
          # Get the value of the current nodes, or 0 if we've reached the end of the list
          x = l1.val if l1 else 0
          y = l2.val if l2 else 0

          # Calculate the sum and update the carry
          total = x + y + carry
          carry = total // 10
          total = total % 10

          # Create a new node with the total and attach it to the current node
          current.next = ListNode(total)

          # Move the current node forward
          current = current.next

          # Move l1 and l2 forward
          if l1:
              l1 = l1.next
          if l2:
              l2 = l2.next

      # If there's a carry left, create a new node with the carry
      if carry > 0:
          current.next = ListNode(carry)

      # The dummy node's next node is the head of the resulting list
      return dummy.next
