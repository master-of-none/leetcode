from LinkedList import LinkedList

def delete_middle(l):
    if not l or not l.next:
        return

    l.value = l.next.value
    l.next = l.next.next

l1 = LinkedList()
l1.add_multiple([1,2,3,4])
middle = l1.add(5)
l1.add_multiple([6,7,8,9])

print(l1)
delete_middle(middle)
print(l1)
