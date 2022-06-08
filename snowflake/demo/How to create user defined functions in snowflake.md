# 참고
- https://dwgeek.com/snowflake-user-defined-functions-syntax-and-examples.html/

# How to create user defined functions in snowflake
```sql
create or replace function calculate_mul(oneval float, secondval float)
returns float
as
    $$
        case
            when secondval is null then 0
            else
                oneval * secondval
        end
    $$
    ;

```

![image](https://user-images.githubusercontent.com/102650331/172561685-fd5b740a-6adc-4675-a714-a594f525c65a.png)


```sql
select calculate_mul(3,2)

```
![image](https://user-images.githubusercontent.com/102650331/172561910-41264734-e1fe-4313-8f5e-f1d5f5c6c026.png)

```sql
select calculate_mul(3, null);

```
![image](https://user-images.githubusercontent.com/102650331/172562199-3a870de9-4865-460e-8445-accdd6c3009f.png)

# creation of javascript user defined function with try catch block
```javascript
# 입력 값에 대해서 자바스크립트 내부에서 참조할때 반드시 대문자로 참조해야한다.
# 아니면 오류가 발생한다.
create or replace function validate_id(id float)
returns varchar
language javascript
as 
    $$
    try {
        if (ID < 0) {
            throw "id cannot be negative!";
        } else {
            return "id validated."
        }
    } catch (err) {
        return "Error: " + err
    }
    $$;


```

![image](https://user-images.githubusercontent.com/102650331/172563434-58fcd888-dea3-4dff-be6b-0b965af3cee5.png)

![image](https://user-images.githubusercontent.com/102650331/172567983-cce8cf7e-8f86-4010-9800-853c1071cae1.png)


# create a table with valid and invalid values
```sql
create or replace table students(id integer);
insert into students (id) values (44), (-44);

```

# calling the function in sql query
```sql
select id, validate_id(id) from students order by id;

```
![image](https://user-images.githubusercontent.com/102650331/172568239-5e8ce429-1701-4687-a2d1-582709c4645f.png)

