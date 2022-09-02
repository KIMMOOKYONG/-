# SimPy 패키지로 스타벅스 예제 만들기
# Starbucks-01 시뮬레이션 예제 구현
- 고객의 프로세스
    - 고객은 10초에 1명씩 총 10명이 도착한다.
    - 도착한 고객은 주문받는 직원이 있는 경우, 30초 동안 커피를 주문한다.
    - 고객이 주문을 완료하면, 음료를 제조하는 직원은 30초 동안 커피를 준비한다.
    - 커피가 완성되면 고객은 커피를 들고 카페를 나간다.

- 카페 상황
    - 주문을 받는 직원은 2명 뿐이며, 음료를 제조하는 직원은 충분히 많다.
    - 주문 받는 직원이 없는 경우 고객은 주문을 하지 못한다.

```python
class Customer(object):
    def __init__(self, env, number):
        self.env = env
        self.number = number
        # 분포에 따라 고객 도착
        self.action = env.process(self.customer_generate())

    def customer_generate(self):
        pass

    def order_coffee(self, name, staff):
        pass

    def wait_for_coffee(self, name):
        pass

```
Customer 라는 클래스를 만들고, 고객의 프로세스대로 함수를 생성했다.

customer_generate 함수는 고객의 도착과 관련되어 있으며,
order_coffee 함수는 커피 주문,
wait_for_coffee 함수는 커피를 수령을 위해 대기하는 행동과 관련되어 있다.

