class ListNode:
  def __init__(self, val=0, next=None):
      self.val = val
      self.next = next

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

class Solution:
  def sortedListToBST(self, head: ListNode) -> TreeNode:
      # Function to count the nodes in the linked list
      def countNodes(node):
          count = 0
          while node:
              node = node.next
              count += 1
          return count

      # Function to construct BST in in-order
      def convertListToBST(left, right):
          nonlocal head
          # Base case
          if left > right:
              return None

          mid = (left + right) // 2

          # First step of simulated in-order traversal. Recursively form
          # the left half
          left_child = convertListToBST(left, mid - 1)

          # Once left half is traversed, process the current node
          root = TreeNode(head.val)
          root.left = left_child

          # Maintain the invariance mentioned in the algorithm
          head = head.next

          # Recurse on the right hand side and form BST out of them
          root.right = convertListToBST(mid + 1, right)
          return root

      n = countNodes(head)
      return convertListToBST(0, n - 1)
