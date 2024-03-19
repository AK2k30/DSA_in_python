class Node:
  def __init__(self, val=0, left=None, right=None, next=None):
      self.val = val
      self.left = left
      self.right = right
      self.next = next

class Solution:
  def connect(self, root: 'Node') -> 'Node':
      if not root:
          return None

      current = root
      # As long as there is a left child, there are more levels to process
      while current.left:
          # Start of the current level
          start = current
          while current:
              # Connect the current node's left child to its right child
              current.left.next = current.right
              # Connect the current node's right child to the next node's left child, if it exists
              if current.next:
                  current.right.next = current.next.left
              # Move to the next node in the current level
              current = current.next
          # Move to the next level
          current = start.left

      return root
