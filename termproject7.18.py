class ArraySet:
    def __init__(self, capacity=100):
        # ArraySet 클래스 초기화
        self.capacity = capacity  # 용량 설정
        self.array = [None] * capacity  # capacity만큼의 None으로 초기화된 배열 생성
        self.size = 0  # 현재 요소 개수 초기화

    def isEmpty(self):
        # 집합이 비어있는지 확인
        return self.size == 0

    def isFull(self):
        # 집합이 가득 찼는지 확인
        return self.size == self.capacity

    def __str__(self):
        # 배열 형태의 문자열로 변환하여 반환
        return str(self.array[0:self.size])

    def contains(self, e):
        # 이진 탐색을 사용하여 요소 e가 집합에 있는지 확인
        return self.binary_search(0, self.size - 1, e)

    def binary_search(self, left, right, e):
        # 이진 탐색 알고리즘
        if (left > right):
            return False  # 왼쪽 인덱스가 오른쪽을 넘어서면 False 반환

        mid = (left + right) // 2  # 중간 인덱스 계산
        if self.array[mid] == e:  # 중간 값이 e와 같으면 True 반환
            return True
        elif self.array[mid] < e:  # 중간 값이 e보다 작으면 오른쪽 부분 탐색
            return self.binary_search(mid + 1, right, e)
        else:  # 중간 값이 e보다 크면 왼쪽 부분 탐색
            return self.binary_search(left, mid - 1, e)

    def insert(self, e):
        # e가 집합에 없고, 집합이 가득 차지 않은 경우 e를 삽입
        if not self.contains(e) and not self.isFull():
            self.array[self.size] = e  # 배열에 e를 추가
            self.size += 1  # 요소 개수 증가
            self.array[:self.size] = sorted(self.array[:self.size])  # 배열을 정렬하여 유지
        else:
            pass

    def delete(self, e):
        # e를 찾아 삭제
        for i in range(self.size):
            if self.array[i] == e:  # e를 찾으면 삭제 수행
                self.array[i] = self.array[self.size - 1]  # 삭제할 위치에 마지막 요소를 복사
                self.size -= 1  # 요소 개수 감소
                self.array[:self.size] = sorted(self.array[:self.size])  # 배열을 정렬하여 유지
                break

    def union(self, setB):
        # 다른 집합(setB)과의 합집합을 반환
        setC = ArraySet()  # 새로운 집합 생성
        for i in range(self.size):
            setC.insert(self.array[i])  # 현재 집합의 요소를 새로운 집합에 추가
        for i in range(setB.size):
            setC.insert(setB.array[i])  # 다른 집합의 요소를 새로운 집합에 추가
        return setC

    def intersect(self, setB):
        # 다른 집합(setB)과의 교집합을 반환
        setC = ArraySet()  # 새로운 집합 생성
        for i in range(setB.size):
            if self.contains(setB.array[i]):  # 다른 집합의 요소가 현재 집합에 있으면 추가
                setC.insert(setB.array[i])
        return setC

    def difference(self, setB):
        # 다른 집합(setB)과의 차집합을 반환
        setC = ArraySet()  # 새로운 집합 생성
        for i in range(self.size):
            if not setB.contains(self.array[i]):  # 다른 집합에 없는 요소만 추가
                setC.insert(self.array[i])
        return setC


my_set = ArraySet()
my_set.insert(10)
my_set.insert(20)
my_set.insert(30)

# contains() 연산 사용 예제
element_to_check = 20
if my_set.contains(element_to_check):
    print(f"The set contains {element_to_check}")
else:
    print(f"The set does not contain {element_to_check}")

element_to_check = 40
if my_set.contains(element_to_check):
    print(f"The set contains {element_to_check}")
else:
    print(f"The set does not contain {element_to_check}")