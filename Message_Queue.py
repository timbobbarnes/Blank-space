import queue


class Message_Queue(queue.Queue):
    def put(self, item, block=True, timeout=None):
        queue.Queue.put(self, str(item), block, timeout)


if __name__ == "__main__":
    q = Message_Queue(10)
    q.put("Hello there")
    q.put("a second string")
    q.put("...and a third")
    while not q.empty():
        print(q.get())
