# Automating Snowpipe Using Cloud Messaging
- 클라우드 저장소에 새로운 파일일 도착했다는 메시지를 snowpipe로 전달

# 참고
- https://www.phdata.io/blog/how-to-optimize-snowpipe-data-load/


# What is Snowpipe?
- Snowpipe는 데이터 공급도구
- 외부의 어플리케이션이 준 실시간으로 데이터를 생성해서 외부 저장소에 데이터 저장
- 외부 저장소에 저장된 데이터를 Snowpipe를 통해서 Snowflake 테이블로 저장
- 내부, 외부 데이터 저장소에 모두 사용 가능

# How The Snowpipe Process Flow Works
![image](https://user-images.githubusercontent.com/102650331/176987075-00bc34f7-7f5a-4746-b85e-a4ac404bda5c.png)


## Configure authentication to the storage system (S3 example is given below)
```sql
create storage integration s3_int
type = external_stage
storage_provider = s3
storage_aws_role_arn = 'arn:aws:iam::001234567890:role/myrole'
enabled = true
storage_allowed_locations = ('s3://mybucket1/path1/', 's3://mybucket2/path2/');

```

## Create stage object
```sql
create stage mystage
url = 's3://mybucket/load/files'
storage_integration = my_storage_int

```
## Create pipe object
```sql
create pipe snowpipe_db.public.mypipe auto_ingest=true as
copy into snowpipe_db.public.mytable
from @snowpipe_db.public.mystage
file_format = (type = 'JSON');

```

## Auto Ingest using Event Notification approach 
![image](https://user-images.githubusercontent.com/102650331/176987223-c5b73640-f772-4490-bb5b-fd5d67d402d7.png)

## REST API approach


