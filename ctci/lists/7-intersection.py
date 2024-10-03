from LinkedList import LinkedList

def intersection(l1, l2):
    if l1.tail is not l2.tail:
        return False

    short = l1 if len(l1) < l2 else l2
    long = l2 if len(l1) < l2 else l1

    diff = len(long) - len(short)

    short_node = short.head
    long_node = long.head

    for _ in range(diff):
        long_node = long_node.next

    while long_node is not short_node:
        short_node = short_node.next
        long_node = long_node.next

    return long_node
