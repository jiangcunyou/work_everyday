from ice.week03.ListNode import ListNode

class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy

        for _ in range(n + 1):
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dummy.next

def build_linked_list(values):
    dummy = ListNode()
    curr = dummy

    for value in values:
        curr.next = ListNode(value)
        curr = curr.next

    return dummy.next


def print_linked_list(head):
    values = []

    while head:
        values.append(str(head.val))
        head = head.next

    print(" -> ".join(values))


head = build_linked_list([1, 2, 3, 4, 5])

result = Solution().removeNthFromEnd(head, 2)

print_linked_list(result)
# Expected:
# 1 -> 2 -> 3 -> 5

#TC: O(n)
#SC: O(1)