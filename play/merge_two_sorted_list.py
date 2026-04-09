from play.merge_k_sorted_list import ListNode


def merge_two_sorted_list(self, l1, l2):
    dummy = ListNode(0)

    curr = dummy

    while l1 and l2:
        if l1.val < l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next

        curr = curr.next

    curr.next = l1 if l1 is not None else l2

    return dummy.next