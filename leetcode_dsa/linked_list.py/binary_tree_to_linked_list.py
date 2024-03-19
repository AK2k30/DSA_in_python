class TreeNode:
  def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

class Solution:
  def flatten(self, root: TreeNode) -> None:
      def flattenTree(node):
          # Handle the null scenario
          if not node:
              return None

          # For a leaf node, we simply return the node as is.
          if not node.left and not node.right:
              return node

          # Recursively flatten the left subtree
          leftTail = flattenTree(node.left)

          # Recursively flatten the right subtree
          rightTail = flattenTree(node.right)

          # If there was a left subtree, we shuffle the connections
          # around so that there is nothing on the left side anymore.
          if leftTail:
              leftTail.right = node.right
              node.right = node.left
              node.left = None

          # We need to return the "rightmost" node after we are
          # done wiring the new connections. 
          return rightTail if rightTail else leftTail

      flattenTree(root)
