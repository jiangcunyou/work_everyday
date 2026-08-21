from ice.week03.ListNode import ListNode

class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        curr = dummy

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next

            curr = curr.next

        if list1:
            curr.next = list1

        if list2:
            curr.next = list2

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

#
# list1 = build_linked_list([1, 2, 4])
# list2 = build_linked_list([1, 3, 4])
#
# result = Solution().mergeTwoLists(list1, list2)
#
# print_linked_list(result)

#TC: O(m+n)
#SC: O(1)