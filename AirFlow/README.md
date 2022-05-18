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

# Using Airflow with Python
- Defining the DAG(default_args)
    - owner: owner of the DAG
    - start_date: start date to run DAG, this must be a historical date
    - schedule_interval: interval to run DAG, can be defined with datetime.timedelta, or a string following CRON schedule format
    - email: email addresses to send emails upon failure or retry
    - retries: number of retry attempts
    - retry_delay: delay between each retry

- Defining the tasks
```python
import datetime

from airflow.models import DAG
from airflow.operators.python import PythonOperator
from airflow.sensors.python import PythonSensor


# Define functions
def job_1():
    print("Perform job 1")


def job_2():
    print("Perform job 2")


def sensor_job():
    print("Sensor Job")


# Parameters
WORFKLOW_DAG_ID = "my_example_dag"
WORFKFLOW_START_DATE = datetime.datetime(2022, 1, 1)
WORKFLOW_SCHEDULE_INTERVAL = "* * * * *"
WORKFLOW_EMAIL = ["dbkorea@bplace.kr"]

WORKFLOW_DEFAULT_ARGS = {
    "owner": "kayjan",
    "start_date": WORFKFLOW_START_DATE,
    "email": WORKFLOW_EMAIL,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 0,
}

# Initialize DAG
dag = DAG(
    dag_id=WORFKLOW_DAG_ID,
    schedule_interval=WORKFLOW_SCHEDULE_INTERVAL,
    default_args=WORKFLOW_DEFAULT_ARGS,
)

# Define jobs
job_1_operator = PythonOperator(
    task_id="task_job_1",
    python_callable=job_1,
    dag=dag,
)

job_2_sensor = PythonSensor(
    task_id="task_job_2_sensor",
    python_callable=sensor_job,
    dag=dag,
    poke_interval=180,
)

job_2_operator = PythonOperator(
    task_id="task_job_2",
    python_callable=job_2,
    dag=dag,
)


# Set dependency
job_1_operator >> job_2_sensor >> job_2_operator

```

- 실행코드 검증
```
# 오류 검증
!python dag.py

# 작업 등록
cp dags_folder/dag.py /home/kayjan/airflow/dags/

```

# Launching Web Server
```
# 사용자 등록
airflow users create -r Admin -u <username> -p <password> -f <first_name> -l <last_name> -e <email>

# 사용자 삭제
airflow users delete -u <username>

# 스케줄러 실행
airflow scheduler

# 웹서버 실행
airflow webserver

```

