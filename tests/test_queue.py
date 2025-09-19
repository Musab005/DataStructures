from src.queues.queue import Queue


class TestQueue:
    def test_enqueue_1(self):
        queue1 = Queue()
        queue1.enqueue(1)
        queue1.enqueue(2)
        queue1.enqueue(3)
        assert str(queue1) == "1 -> 2 -> 3 -> None"

    def test_dequeue_1(self):
        queue1 = Queue()
        queue1.enqueue(1)
        queue1.enqueue(2)
        queue1.dequeue()
        queue1.dequeue()
        assert str(queue1) == "None"

    def test_dequeue_2(self):
        queue1 = Queue()
        queue1.enqueue(1)
        queue1.enqueue(2)
        queue1.enqueue(3)
        queue1.dequeue()
        assert str(queue1) == "2 -> 3 -> None"

    def test_dequeue_3(self):
        queue1 = Queue()
        assert queue1.dequeue() is None

    def test_front_1(self):
        queue1 = Queue()
        queue1.enqueue(1)
        queue1.enqueue(2)
        queue1.enqueue(3)
        assert queue1.front() == 1
        assert str(queue1) == "1 -> 2 -> 3 -> None"

    def test_front_2(self):
        queue1 = Queue()
        assert queue1.front() is None
        assert str(queue1) == "None"

    def test_is_empty_1(self):
        queue1 = Queue()
        assert queue1.is_empty()

    def test_is_empty_2(self):
        queue1 = Queue()
        queue1.enqueue(1)
        assert not queue1.is_empty()

    def test_len_1(self):
        queue1 = Queue()
        queue1.enqueue(1)
        queue1.enqueue(2)
        queue1.enqueue(3)
        assert len(queue1) == 3

    def test_len_2(self):
        queue1 = Queue()
        queue1.enqueue(1)
        queue1.enqueue(2)
        queue1.enqueue(3)
        queue1.dequeue()
        queue1.front()
        assert len(queue1) == 2
