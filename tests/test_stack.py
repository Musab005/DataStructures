from src.stacks.stack import Stack


class TestStack:

    def test_push_1(self):
        stack1 = Stack()
        stack1.push(1)
        stack1.push(10)
        stack1.push(5)
        assert str(stack1) == "5 -> 10 -> 1 -> None"

    def test_pop_1(self):
        stack1 = Stack()
        stack1.push(1)
        stack1.push(10)
        stack1.push(5)
        stack1.pop()
        stack1.pop()
        assert str(stack1) == "1 -> None"

    def test_peek_1(self):
        stack1 = Stack()
        stack1.push(1)
        stack1.push(10)
        stack1.push(5)
        assert stack1.peek() == 5

    def test_isempty_1(self):
        stack1 = Stack()
        stack1.push(1)
        stack1.push(10)
        stack1.push(5)
        assert not stack1.is_empty()

    def test_isempty_2(self):
        stack2 = Stack()
        stack2.push(1)
        stack2.push(10)
        stack2.push(5)
        stack2.pop()
        stack2.pop()
        stack2.pop()
        assert stack2.is_empty()

    def test_isempty_3(self):
        stack3 = Stack()
        assert stack3.is_empty()

    def test_len_1(self):
        stack1 = Stack()
        assert len(stack1) == 0

    def test_len_2(self):
        stack2 = Stack()
        stack2.push(1)
        stack2.push(2)
        stack2.push(3)
        assert len(stack2) == 3

    def test_len_3(self):
        stack2 = Stack()
        stack2.push(1)
        stack2.push(2)
        stack2.pop()
        assert len(stack2) == 1
