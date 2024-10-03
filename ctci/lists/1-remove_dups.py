from LinkedList import LinkedList

def remove_dups(l1):
    if not l1.head:
        return
    
    cur = l1.head
    hashset = set([cur.value])

    while cur.next:
        if cur.next.value in hashset:
            cur.next = cur.next.next
        else:
            hashset.add(cur.next.value)
            cur = cur.next

    return l1

l1 = LinkedList()
l1.generate(100, 0, 9)
print(l1)
remove_dups(l1)
print(l1)
