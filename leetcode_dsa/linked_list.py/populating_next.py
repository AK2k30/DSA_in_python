class Node:
  def __init__(self, val=0, left=None, right=None, next=None):
      self.val = val
      self.left = left
      self.right = right
      self.next = next

class Solution:
  def connect(self, root: 'Node') -> 'Node':
      # Start with the root node
      head = root
      # Use a dummy node to help in linking the next level's nodes
      dummy = Node(0)
      while head:
          # Use 'current' to traverse the current level, 'tail' to build connections for the next level
          current, tail = head, dummy
          # Reset head to None, it will be set for the next level
          head = None
          while current:
              # Check the left child
              if current.left:
                  # If head is not set, set it to current's left child
                  if not head:
                      head = current.left
                  tail.next = current.left
                  tail = tail.next
              # Check the right child
              if current.right:
                  # If head is not set, set it to current's right child
                  if not head:
                      head = current.right
                  tail.next = current.right
                  tail = tail.next
              # Move to the next node in the current level
              current = current.next
          # Clear the next pointer of the dummy node
          tail.next = None
      return root
