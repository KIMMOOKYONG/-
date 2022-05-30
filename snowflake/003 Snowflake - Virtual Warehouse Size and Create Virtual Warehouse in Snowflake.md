![image](https://user-images.githubusercontent.com/102650331/170950100-0911278e-b721-499e-babf-ca2aeb7eaf90.png)

![image](https://user-images.githubusercontent.com/102650331/170950339-87da14fd-fcca-4d72-b8a5-c1d49389e61f.png)

![image](https://user-images.githubusercontent.com/102650331/170952362-863bc4a6-2270-4fe8-8951-f6e7e9bbb38f.png)

# 명령을 통한 WAREHOUSE 생성
![image](https://user-images.githubusercontent.com/102650331/170952396-41699971-aa82-407e-ab83-c45a6ff168c9.png)

![image](https://user-images.githubusercontent.com/102650331/170952438-d91fff3a-df92-4fe9-80fe-8de719365577.png)

```sql
CREATE OR REPLACE WAREHOUSE VM_EXAMPLE_1
	WITH
		WAREHOUSE_SIZE = 'X-SMALL'
		AUTO_SUSPEND = 120
		AUTO_RESUME = TRUE
		INITIALLY_SUSPENDED = TRUE;

```

![image](https://user-images.githubusercontent.com/102650331/170953461-b4a1c3fc-b395-4765-9f7b-5064e12681ec.png)


# UI를 통한 WAREHOUSE 생성
