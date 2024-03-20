class Node:
  def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
      self.val = int(x)
      self.next = next
      self.random = random

class Solution:
  def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
      if not head:
          return None

      # Step 1: Clone nodes and insert them next to their originals
      current = head
      while current:
          cloned = Node(current.val, current.next, None)
          current.next = cloned
          current = cloned.next

      # Step 2: Update random pointers for the cloned nodes
      current = head
      while current:
          if current.random:
              current.next.random = current.random.next
          current = current.next.next

      # Step 3: Separate the original and cloned lists
      original = head
      clone = head.next
      clone_head = head.next
      while original:
          original.next = original.next.next
          clone.next = clone.next.next if clone.next else None
          original = original.next
          clone = clone.next

      return clone_head
