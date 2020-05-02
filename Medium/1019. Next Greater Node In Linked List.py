"""
https://leetcode.com/problems/next-greater-node-in-linked-list/

We are given a linked list with head as the first node.  Let's number the nodes in the list: node_1, node_2, node_3, ... etc.

Each node may have a next larger value: for node_i, next_larger(node_i) is the node_j.val such that j > i, node_j.val > node_i.val, and j is the smallest possible choice.  If such a j does not exist, the next larger value is 0.

Return an array of integers answer, where answer[i] = next_larger(node_{i+1}).

Note that in the example inputs (not outputs) below, arrays such as [2,1,5] represent the serialization of a linked list with a head node value of 2, second node value of 1, and third node value of 5.

Example:
    Input: [2,1,5]
    Output: [5,5,0]
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        
        if not head:
            return head
        
        arr = []
        
        while head:
            arr.append(head.val)
            head = head.next
        result = [0 for i in range(len(arr))]
        
        stack = []
        for index, a in enumerate(arr):
            while stack and arr[stack[-1]] < a:
                j = stack.pop()
                result[j] = a
                
            stack.append(index)
        
        return result