class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(self.min_stack[-1], val))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
#push: O(1)
#pop: O(1)
#top: O(1)
#getMin: O(1)
#SC: O(n)