# 011 Snowflake Tutorial - How does Snowflake Caching work - Part I
![image](https://user-images.githubusercontent.com/102650331/171390314-9c13944c-e31a-4700-98c9-a413bf1a9555.png)

![image](https://user-images.githubusercontent.com/102650331/171390426-0d8673a4-ad41-42be-a25c-58bf14ca7d8a.png)

![image](https://user-images.githubusercontent.com/102650331/171390572-92c25833-d7a9-4e63-8c06-2f7a02a0a4ba.png)

![image](https://user-images.githubusercontent.com/102650331/171390928-b33253bd-192a-429f-ad12-b849324efc74.png)

![image](https://user-images.githubusercontent.com/102650331/171391066-4656b77e-eea0-483f-b127-fbbdc7b2b834.png)

```sql
create or replace WAREHOUSE WM_EAMPLE_1
    with
        WAREHOUSE_SIZE='X-SMALL'
        AUTO_SUSPEND=120 -- 초단위 설정. 120초, 2분
        AUTO_RESUME=TRUE
        INITIALLY_SUSPENDED=TRUE

```
![image](https://user-images.githubusercontent.com/102650331/171392785-112ca2fa-3ff6-4728-9ac1-0cbcba9ac77e.png)

```sql
select * from customer;

```
![image](https://user-images.githubusercontent.com/102650331/171392969-26cdd961-a9c1-4e6a-ac16-554699e0ac6d.png)

![image](https://user-images.githubusercontent.com/102650331/171393266-add35a7c-8d9f-4efe-b6f6-402bbbebb18a.png)

![image](https://user-images.githubusercontent.com/102650331/171393304-e5f0231c-97e3-4d87-8f6f-571ba8d7f3df.png)

![image](https://user-images.githubusercontent.com/102650331/171393960-7a247cb6-fb51-4cdb-b78f-5beca37a41a0.png)

## 캐싱 적용 결과
![image](https://user-images.githubusercontent.com/102650331/171395119-99e4845e-fe4c-4251-bf4d-c51f6c236413.png)

![image](https://user-images.githubusercontent.com/102650331/171395235-82d652e2-b93f-40aa-956d-3431405e2f6f.png)

