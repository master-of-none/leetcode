from LinkedList import LinkedList

def loop_detection(l1):
    fast = l1.head
    slow = l1.head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            break

    if not fast or not fast.next:
        return None

    slow = l1.head
    while fast != slow:
        slow = slow.next
        fast = fast.next

    
    return slow
