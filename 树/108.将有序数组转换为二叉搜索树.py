"""
将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

示例:

给定有序数组: [-10,-3,0,5,9],

一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：

      0
     / \
   -3   9
   /   /
 -10  5
"""

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def helper(nums,left,right):
            if left > right:
                return None
            p = (left+right)//2 # 找出中间位置

            root = TreeNode(nums[p])
            root.left = helper(nums,left,p-1)
            root.right = helper(nums,p+1,right)
            return root
        return helper(nums,0, len(nums)-1)
