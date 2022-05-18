# 4 Apache Airflow components
- Metadata Database: stores information regarding the state of tasks
- Scheduler: decide which tasks need to be executed and execution priority
- Executor: processes that execute the logic of tasks
- Web Server: erver which supports the Graphical User Interface (GUI) that displays information to the user
- 

# Task status
- running, success, failed, skipped, or up for retry, etc.

# Task type
- Operator(태스크를 실행해주는 엔진)
    - PythonOperator, BashOperator, EmailOperator, SimpleHttpOperator

- Sensor(특정 조건을 충족할 때까지 작업 대기)
- 태스크는 일반적으로 sensor > operator 순서로 실행된다.
- 태스크는 Directed Acyclic Graph (DAG)로 연결되어 워크플로우를 구성한다.

# Installing Airflow
```
!pip install tpot
```
