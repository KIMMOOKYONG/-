# 012 Snowflake Tutorial - Snowflake Caching work - Part II - Compute Layer cache
![image](https://user-images.githubusercontent.com/102650331/171395639-eee9625a-470b-4a0b-bd2d-56903a365725.png)

```sql
create or replace WAREHOUSE WM_EAMPLE_1
    with
        WAREHOUSE_SIZE='X-SMALL'
        AUTO_SUSPEND=3000
        AUTO_RESUME=TRUE
        INITIALLY_SUSPENDED=TRUE

```

![image](https://user-images.githubusercontent.com/102650331/171395893-17af9c71-0fca-4dee-b004-379919c52784.png)

## 세션 레벨에서 캐시 사용하지 않도록 설정
```sql
alter session set use_cached_result=false

```
![image](https://user-images.githubusercontent.com/102650331/171396441-07b8ea66-d183-4f5f-9c4b-53c6ddfa5847.png)

```sql
select * from customer;

```
![image](https://user-images.githubusercontent.com/102650331/171396807-c9937bf2-549d-4ffd-8ef7-be7c40330e0f.png)
- VM에 초록불이 들어온것을 알수 있다. 캐시 사용 안함.

![image](https://user-images.githubusercontent.com/102650331/171396983-f085002c-7bb3-48e9-8b0a-cd68c56fa7a8.png)

![image](https://user-images.githubusercontent.com/102650331/171397119-6d2cbc5e-1a1b-41fe-a00a-3ca24ed9cab5.png)

![image](https://user-images.githubusercontent.com/102650331/171397479-c25bf2c9-2811-4507-b6a2-b921488a9933.png)

![image](https://user-images.githubusercontent.com/102650331/171397506-5f380803-4f9c-447b-851e-a19e9ea4c83e.png)

![image](https://user-images.githubusercontent.com/102650331/171397572-4ca44849-5e4f-4293-b119-ed8af16c0970.png)

![image](https://user-images.githubusercontent.com/102650331/171397911-c11683a6-a02a-4994-8f70-16717500d5a4.png)

![image](https://user-images.githubusercontent.com/102650331/171398143-8d7e4e5d-8a66-4913-90db-c52b9da1e6c7.png)

![image](https://user-images.githubusercontent.com/102650331/171398225-ba8aeeb9-b82d-4afd-bcd5-1f8111bbb7d2.png)

