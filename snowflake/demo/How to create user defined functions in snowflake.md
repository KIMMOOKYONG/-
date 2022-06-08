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

![image](https://user-images.githubusercontent.com/102650331/172563434-58fcd888-dea3-4dff-be6b-0b965af3cee5.png)

# create a table with valid and invalid values
```sql
create or replace table students(id integer);
insert into students (id) values (44), (-44);

```

# calling the function in sql query
```sql
select id, validate_id(id) from students order by id;

```
