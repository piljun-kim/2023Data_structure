class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None  # 큐의 전단을 가리키는 포인터
        self.rear = None   # 큐의 후단을 가리키는 포인터

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = self.rear = new_node  # 큐가 비어있을 경우 새 노드를 전단과 후단으로 설정
        else:
            self.rear.next = new_node  # 기존 후단의 다음 노드로 새 노드를 설정
            self.rear = new_node       # 후단을 새 노드로 업데이트

    def dequeue(self):
        if self.is_empty():
            return None
        data = self.front.data
        if self.front == self.rear:    # 큐에 하나의 요소만 남아있을 경우
            self.front = self.rear = None  # 전단과 후단을 모두 None으로 설정하여 큐를 비움
        else:
            self.front = self.front.next  # 전단을 다음 노드로 업데이트
        return data

    def peek(self):
        if self.is_empty():
            return None
        return self.front.data  # 전단의 데이터 반환

# 큐 테스트
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("큐의 전단:", queue.peek())

print("큐에서 삭제된 값:", queue.dequeue())
print("큐에서 삭제된 값:", queue.dequeue())

print("큐의 전단:", queue.peek())

queue.enqueue(4)
print("큐의 전단:", queue.peek())