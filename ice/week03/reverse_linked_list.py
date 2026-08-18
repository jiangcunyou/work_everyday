from ice.week03.ListNode import ListNode

class Solution:
    def reverseList(self, head):
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev

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

print("Before:")
print_linked_list(head)

solution = Solution()
reversed_head = solution.reverseList(head)

print("After:")
print_linked_list(reversed_head)

#TC: O(n)
#SC: O(1)