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

# Installing Airflow# Installing Airflow
```
# 필요 패키지 설치
!pip install tpot
!pip install apache-airflow

# DB 초기화, sqlite
!airflow db init

# 사용자 등록
!airflow users  create --role Admin --username admin --email admin --firstname admin --lastname admin --password admin

# 스케줄러 백그라운드 실행
!airflow scheduler &>/dev/null&

# 웹 UI 실행
!airflow webserver -p 9090 &>/dev/null&

# 터널링 서비스 실행
!npx localtunnel --port 9090

```

