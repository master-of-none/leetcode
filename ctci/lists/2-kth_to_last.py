from LinkedList import LinkedList

def kth_to_last(l1, k):
    left = l1.head
    right = l1.head

    while k > 0:
        if right == None:
            return None
        right = right.next
        k -= 1
    
    while right:
        left = left.next
        right = right.next

    return left

if __name__ == "__main__":
    l1 = LinkedList()
    l1.generate(10, 0, 99)
    print(l1)
    print(kth_to_last(l1, 5))
