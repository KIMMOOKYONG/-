# How to load CSV file into Snowflake by using CLI
![image](https://user-images.githubusercontent.com/102650331/172334596-09322bf6-e417-45b0-a945-7990e1220a16.png)

![image](https://user-images.githubusercontent.com/102650331/172335401-4b0b2d15-003a-4f5d-a445-d4f58bc97b32.png)

- acount-name

![image](https://user-images.githubusercontent.com/102650331/172337880-5280b3e0-9340-465c-bb99-fe48578511b0.png)

![image](https://user-images.githubusercontent.com/102650331/172336666-88d90c8b-1098-4c64-9813-fe6a6602883d.png)

![image](https://user-images.githubusercontent.com/102650331/172337401-3f3f77b9-82aa-4d96-9545-6b4042e18e82.png)

- 연결 성공

![image](https://user-images.githubusercontent.com/102650331/172338852-83ee5ed3-8f3d-40d2-b81b-2af6b84aecfe.png)

- 연결 종료 방법은 ctrl + d

![image](https://user-images.githubusercontent.com/102650331/172338960-abf9f135-e0f9-4d72-ba51-fb5cae82845c.png)


- 환경 설정

![image](https://user-images.githubusercontent.com/102650331/172339920-10ff75dd-9422-4a2f-b388-071a614f7900.png)

![image](https://user-images.githubusercontent.com/102650331/172340467-be6422b3-ba9f-4987-994c-3b40491bd542.png)

![image](https://user-images.githubusercontent.com/102650331/172342383-6bad5109-bf22-4e14-80da-5c7d5dc307ac.png)

# 테스트
- 테이블 생성

![image](https://user-images.githubusercontent.com/102650331/172343259-e9119cb3-bae4-4652-a8e9-1027f347db47.png)

- 데이터 로딩

![image](https://user-images.githubusercontent.com/102650331/172353621-381dfd06-5d82-494e-9ca4-4690e7f02644.png)

![image](https://user-images.githubusercontent.com/102650331/172354536-87b0c92e-8b39-428b-8c58-d9957c00e423.png)

```
# 스테이징 영역에 데이터 로딩하기
put file://C:\Users\dbkorea\Downloads\departments.csv @EMPLOYEES.PUBLIC.%departments;

```

- 스테이징 영역 확인

![image](https://user-images.githubusercontent.com/102650331/172354959-05d02afd-ec0f-4bdf-bb84-a30d3e92bb5a.png)

- 테이블 데이터 로딩

```
copy into departments
    from @%departments
    file_format = (type = csv field_optionally_enclosed_by='"')
    pattern = 'departments.csv.gz'
    on_error = 'skip_file';

```

![image](https://user-images.githubusercontent.com/102650331/172355875-b303057a-3010-49e7-aa0f-21b7a26e4426.png)

![image](https://user-images.githubusercontent.com/102650331/172356056-3b6e9034-ff2f-4713-b9d2-77e275946bbd.png)

