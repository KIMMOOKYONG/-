# 5 Features Of Snowflake That Data Engineers Must Know
- https://www.analyticsvidhya.com/blog/2021/10/5-features-of-snowflake-that-data-engineers-must-know/

# The 5 features
- Stages
- Zero copy cloning
- Time Travel
- Streams
- Tasks

## Stages in Snowflake
- 데이터 저장 위치 정보
- 데이터 로딩 또는 데이터 언로딩(내려받기)하는 위치 정보

## Stages 분류
- Internal Stage
```
Snowflake 내부 데이터 저장 공간

```
- External Stage
```
Snowflake 외부 데이터 저장 공간

```

### Internal Stages
- https://www.analyticsvidhya.com/blog/2021/07/demystifying-stages-in-snowflake/
- User Stages
- Tables Stages
- Named Stages

## Time Travel in Snowflake
- 기간: 기본은 1일, 엔터프라이즈 버전 이상은 90일

```sql
-- TIME TRAVEL EXAMPLE
use role sysadmin;
create database demo_db;
use demo_db;
use schema public;

create or replace table t_emp_detls 
(
    empid number,
    empname varchar
)
data_retention_time_in_days = 4;

insert into t_emp_detls values(1,'Micheal');
insert into t_emp_detls values(2,'Nick');
insert into t_emp_detls values(3,'George');
insert into t_emp_detls values(4,'Donald');
insert into t_emp_detls values(5,'Vincent');
insert into t_emp_detls values(6,'Leo');

select * from t_emp_detls;

-- 5분 후 아래 데이터 입력
insert into t_emp_detls values(7,'William');

-- 5분 뒤로 돌아가고 싶다.
select * from t_emp_detls at(offset => -60 * 5) as t;
select * from t_emp_detls_cln;

```

## Zero Copy Cloning in Snowflake
- 운영환경의 특정 테이블을 개발환경으로 cloning 
- 개발환경에서 변경한 데이터가 마이크로 파티션의 복사본을 생성하고
- 생성한 복사본에 대해서만 과금을 한다.

```sql
-- cloning 원본 테이블에 time travel 설정은 복제되지 않는다.
create or replace table t_emp_detls_cln clone t_emp_detls ;

--
use role accountadmin;
-- 오브젝트명은 대소문자 구분이 없으나 데이터 값에 대해서는 대소문자 구분 있음.
select * from demo_db.information_schema.table_storage_metrics where table_name like '%T_EMP_DETLS%';

```
## Streams in Snowflake
### 스트림 처리를 위해서 추가되는 칼럼 정보
- METADATA$ACTION
- METADATA$ISUPDATE
- METADATA$ROW_ID 

### Snowflake supports 3 types of streams
- Standard
- Append only
- Insert Only – external table만 지원

```sql
create stream st_emp_dtls on table t_emp_detls;
insert into t_emp_detls values(8,'Arnold');
select * from st_emp_dtls;

```

## Tasks in Snowflake
- You need to resume the task to start it.

```sql
create or replace table test_emp_table
(
    empid number,
    empname varchar
);

-- task 정의
create task t_task1
warehouse = compute_wh
schedule = '5 minute'
when
system$stream_has_data('st_emp_dtls')
as
insert into test_emp_table(empid,empname) select empid,empname from st_emp_dtls where metadata$action = 'INSERT';

-- task 활성화
alter task t_task1 resume;

select * from test_emp_table;

alter task t_task1 suspend;

```

# Getting Started With Snowflake Data Platform
- https://www.analyticsvidhya.com/blog/2021/07/getting-started-with-snowflake-data-platform/

## Introduction
- Data Engineering
- Data Lake
- Datawarehouse
- DataScience
- DataApplications
- DataExchange

## The Architecture of Snowflake
- Database Storage Layer
- Query Processing Layer
- Cloud Services Layer

## Hands-on
```sql
--Creating a warehouse 
create warehouse if not exists test_warehouse warehouse_size ='SMALL' auto_suspend=300 initially_suspended=true;
use warehouse test_warehouse;

--Create a test database 
create database testdb;

--Check if the database is created successfully
show databases like 'test%';
USE DATABASE testdb 

--Create a test schema 
create schema testschema;

--Check if the schema is created successfully
show schemas;
use schema testschema

--Creating a sample employee table with two columns empname,empid
create or replace table test_emptable (empid number,empname varchar);

--Inserting  sample data into an employee table
insert into test_emptable values(1,'Micheal');
insert into test_emptable values(2,'Nick');
insert into test_emptable values(3,'George');

--Check if the table is created successfully
show tables like 'test_emptable';

--Display the content of the table
select * from test_emptable

```
