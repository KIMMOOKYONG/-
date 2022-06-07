# How to load data from aws s3 to snowflake 

## create file format objects
```sql
create or replace file format mycsvformat
    type = 'CSV'
    field_delimiter = ','
    skip_header = 1;

```

## create a named stage objects
```sql
create or replace stage my_csv_stage
    file_format = mycsvformat
    url = 's3://data';

```

## create table
```sql
create or replace table departments (
    dept_no     char(4)         not null,
    dept_name   varchar(40)     not null,
    primary key (dept_no);
);

```
## copy data into target table
```sql
copy into departments
    from @my_csv_stage/departments.csv
    on_error = 'skip_file';

```
