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

## 2.1 Customer 클래스
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

## 2.2 customer_generate 함수
```python
def customer_generate(self):
    for i in range(self.number):
        name = "Customer-%s" % i
        arrive = self.env.now
        print(name, "%8.3f" % arrive, "카페도착")
        
        # 도착한 고객은 주문하러 이동
        self.env.process(self.order_coffee(name, staff))

        # 고객은 10초마다 카페에 도착
        interval_time = 10
        yield self.env.timeout(interval_time)

```

self.number 값만큼의 인원이 스타벅스에 온다.  
카페에 도착하면 고객 ID가 부여되며, 도착한 그 순간에 고객 ID, 도착한 시간, "카페도착" 값이 함께 출력된다.  
카페에 들어온 고객은 주문하러 이동하고 order_coffee 함수가 수행된다.  
또 다른 고객은 10초 후에 도착하는데,  
이는 env 객체에 timeout 10초를 두어, 시간 값을 지연시켜 표현한다.  
고객 도착 시간에 상수 값이 아닌 분포를 적용하고 싶다면  
interval_time 변수에 random.expovaiate(1.0/3) 이런 식으로 분포를 넣어주면 된다.  

## 2.3 order_coffee 함수
```python
def order_coffee(self, name, staff):
    # 직원 요청
    with staff.request() as req:
        yield req

        # 직원에게 30초동안 주문
        ordering_duration = 30
        yield self.env.timeout(ordering_duration)
        print(name, "%8.3f" % self.env.now, "주문완료")

    # 주문한 고객은 커피 수령을 위해 대기
    yield self.env.process(self.wait_for_coffee(name))

```
staff변수는 주문을 받는 직원 수를 의미한다.  
고객은 커피 주문을 위해 직원을 요청하는데, 이는 with staff.request() as req: yield req로 표현한다.  
위처럼 with 구문을 쓰면, 직원은 자동적으로 점유 상태에서 해제된다.  
즉, 앞 고객의 주문이 끝나서, 커피 주문을 받을 수 있는 직원이 생기면, 바로 다음 고객의 주문을 받을 수 있게 된다는 의미이다.  
만약 request()를 with 없이 쓰는 경우는, release()를 사용하여 직접 자원(여기서는 직원)을 해제해야 한다.  

고객에게 직원이 할당되면, 고객은 30초 동안 커피 주문을 하고,  
주문이 완료되면 고객 ID, 완료된 시간, "주문완료" 값을 함께 출력한다.  
주문 후 wait_for_coffee 함수가 실행되도록 해서, 주문이 끝난 고객이 음료가 제조되기를 기다리는 상황을 표현하면 된다.  

