# ETL Pipeline 만들기
# Prefect(https://docs-v1.prefect.io/):
- 파이썬 기반 워크플로우 관리 시스템

# 제공 기능:
- logging
- retries
- dynamic mapping
- caching
- failure notifications

# 학습 목표:
- tasks, flows, parameters, failures, schedules
- Prefect 설치
- 파이썬으로 단순 ETL pipeline 구성
- tasks, flows, parameters, schedules, handle failures 선언하는 방법
- Prefect 실행

# How to Install Prefect Locally
## 가상환경 생성
```
conda create — name prefect_env python=3.8
conda activate prefect_env

```

## prefect
```
!pip install prefect

```

# Writing an ETL Pipeline With Python
- download the data from a dummy API
- transform it
- save it as a CSV
- 파일명 01_etl_pipeline.py
- data 폴더는 프로그램 실행전에 생성해두어야 한다.

# 주요 모듈
```
extract(url: str) -> dict
transform(data: dict) -> pd.DataFrame
load(data: pd.DataFrame, path: str) -> None

```

```python
# 코드 실행전에 data라는 폴더를 만들어 두어야 한다.
import json
import requests
import pandas as pd
from datetime import datetime

def extract(url: str) -> dict:
    res = requests.get(url)
    if not res:
        raise Exception("No data fetched!")
    return json.loads(res.content)


def transform(data: dict) -> pd.DataFrame:
    transformed = []
    for user in data:
        transformed.append({
            "ID": user["id"],
            "Name": user["name"],
            "Username": user["username"],
            "Email": user["email"],
            "Address": f"{user["address"]["street"]}, {user["address"]["suite"]}, {user["address"]["city"]}",
            "PhoneNumber": user["phone"],
            "Company": user["company"]["name"]
        })
    return pd.DataFrame(transformed)


def load(data: pd.DataFrame, path: str) -> None:
    data.to_csv(path_or_buf=path, index=False)


if __name__ == "__main__":
    users = extract(url="https://jsonplaceholder.typicode.com/users")
    df_users = transform(users)
    load(data=df_users, path=f"data/users_{int(datetime.now().timestamp())}.csv")

```
