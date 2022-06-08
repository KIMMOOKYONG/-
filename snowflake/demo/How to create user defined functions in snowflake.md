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

# 자바스크립트 활용 함수 정의
```javascript
create or replace function validate_id(id float)
returns varchar
language javascript
as 
    $$
    try {
        if (id < 0) {
            throw "id cannot be negative!";
        } else {
            return "id validated."
        }
    } catch (err) {
        return "Error: " + err
    }
    $$;


```
