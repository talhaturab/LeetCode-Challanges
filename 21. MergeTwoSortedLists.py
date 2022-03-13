class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

llist1 = ListNode(1)
second1 = ListNode(2)
third1 = ListNode(4)

llist1.next = second1
second1.next = third1

llist2 = ListNode(1)
second2 = ListNode(3)
third2 = ListNode(4)


llist2.next = second2
second2.next = third2

def MergeList(list1, list2):
    sortedList = ListNode
    trail = sortedList
    while list1 and list2:
        if list1.val < list2.val:
            trail.next = list1
            trail = list1
            list1 = list1.next
        else:
            trail.next = list2
            trail = list2
            list2 = list2.next

    if list1:
        trail.next = list1
    else:
        trail.next = list2
    return sortedList.next

x = MergeList(llist1, llist2)

while True:
    print(x.val)
    if x.next == None:
        break
    else:
        x = x.next
