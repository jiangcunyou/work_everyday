from ice.week03.ListNode import ListNode


class Solution:
    def hasCycle(self, head) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False

def build_cycle_list(values, pos):
    if not values:
        return None

    nodes = [ListNode(value) for value in values]

    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    if pos != -1:
        nodes[-1].next = nodes[pos]

    return nodes[0]


# Test 1: 有环
head1 = build_cycle_list([3, 2, 0, -4], 1)
print(Solution().hasCycle(head1))
# Expected: True


# Test 2: 有环
head2 = build_cycle_list([1, 2], 0)
print(Solution().hasCycle(head2))
# Expected: True


# Test 3: 无环
head3 = build_cycle_list([1, 2, 3, 4], -1)
print(Solution().hasCycle(head3))
# Expected: False


# Test 4: 单节点无环
head4 = build_cycle_list([1], -1)
print(Solution().hasCycle(head4))
# Expected: False

#TC: O(n)
#SC: O(1)