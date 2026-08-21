from ice.week03.merge_two_sorted_lists import build_linked_list, print_linked_list

class Solution:
    def reorderList(self, head) -> None:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None

        prev = None
        curr = second

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        second = prev

        first = head

        while second:
            first_next = first.next
            second_next = second.next

            first.next = second
            second.next = first_next

            first = first_next
            second = second_next

head = build_linked_list([1, 2, 3, 4, 5])
Solution().reorderList(head)
print_linked_list(head)

#TC: O(n)
#SC: O(1)