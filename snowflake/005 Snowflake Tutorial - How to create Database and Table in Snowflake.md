# 005 Snowflake Tutorial - How to create Database and Table in Snowflake
![image](https://user-images.githubusercontent.com/102650331/170955464-22a62130-1775-4083-9569-b1c1319453f3.png)

## 데이터베이스 생성
![image](https://user-images.githubusercontent.com/102650331/170956067-19dce6e4-f434-4aec-9e13-168836129a2f.png)

```sql
CREATE DATABASE CITYBIKE COMMENT = 'Sample database';

```

## 테이블 생성
![image](https://user-images.githubusercontent.com/102650331/170956547-ba74e09f-01b9-4aa7-a02c-b22a6b55048a.png)

![image](https://user-images.githubusercontent.com/102650331/170956999-75b4c23b-368f-4380-a69e-dc60a97c222f.png)

![image](https://user-images.githubusercontent.com/102650331/170957236-8f6c8a98-e9b2-4a69-b72e-b6bb568e2c16.png)

![image](https://user-images.githubusercontent.com/102650331/170957473-a7a4f2b9-6819-4ea2-be23-75648ad0ad41.png)

![image](https://user-images.githubusercontent.com/102650331/170958434-f4fc69c7-02c3-4f63-bbc7-f0a95864b165.png)

```sql
create or replace table trips (
	tripduration integer,
	starttime timestamp,
	stoptime timestamp,
	start_station_id integer,
	start_station_name string,
	start_station_latitude float,
	start_station_longitude float,
	end_station_id integer,
	end_station_name string,
	end_station_latitude float,
	end_station_longitude float,
	bikeid integer,
	membership_type string,
	usertype string,
	birth_year integer,
	gender integer
);

```

![image](https://user-images.githubusercontent.com/102650331/170958585-bffd8a64-81ef-4452-a773-0ceecec1865b.png)

![image](https://user-images.githubusercontent.com/102650331/170962536-039b959f-78c8-4481-acfe-b1103b27c375.png)


