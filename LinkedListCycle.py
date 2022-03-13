class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

llist = ListNode(3)
second = ListNode(2)
third = ListNode(0)
forth = ListNode(-4)

llist.next = second
second.next = third
third.next = forth
forth.next = second

def hasCycle(list):
    try:
        location = {}
        trail = list
        while True:
            if trail in location:
                return True
            elif trail.next == None:
                return False
            else:
                location[trail] = ""
                trail = trail.next
    except:
        return False

x = hasCycle(llist)
print(x)

