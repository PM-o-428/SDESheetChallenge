# Solution - 26
# Problem Link - https://www.codingninjas.com/codestudio/problems/reverse-the-singly-linked-list_799897?topList=striver-sde-sheet-problems
# Challege Start Date - 04.06.2022
# Date - 05.07.2022
# Day 29
def reverseLinkedList(self):
    # Write your code here.
    prev = None
    current = head
    while(current is not None):
        next = current.next
        current.next = prev
        prev = current
        current = next
        head = prev
    return head