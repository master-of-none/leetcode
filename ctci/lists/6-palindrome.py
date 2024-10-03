from LinkedList import LinkedList
from LinkedList import LinkedListNode
def is_palindrome(l1):
    reversedList = reverseList(l1)

    return isEqual(l1.head, reversedList)

def reverseList(l1):
    prev = None
    cur = l1.head

   
    while cur:
        new_node = LinkedListNode(cur.value)  
        new_node.next = prev  
        prev = new_node  
        cur = cur.next


    return prev

def isEqual(l1, l2):
    while l1 and l2:
        if l1.value != l2.value:
            return False

        l1 = l1.next
        l2 = l2.next

    return l1 == None and l2 == None

l1_true = LinkedList([1, 2, 3, 4, 5, 4, 3, 2, 1])
print(is_palindrome(l1_true))
l2_false = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(is_palindrome(l2_false))

