# Setting up a data pipeline using Snowflake’s Snowpipes in 10 Easy Steps
- https://calogica.com/sql/snowflake/2019/04/04/snowpipes.html
- https://blog.vishnuvp.in/blog/automatic-data-ingestion-in-snowflake-using-snowpipe/
- https://hevodata.com/learn/loading-data-to-snowflake/#2
- 

# Set up a separate database
```sql
create database etl;
use database etl;

```
# Set up a schema to hold our source data
```sql
create schema src;

```

# Create a TablePermalink
```sql
create table src.my_source_table
(
    col_1 varchar,
    col_2 varchar
);

```

# Create the File FormatPermalink
```sql
create or replace file format my_csv_format
    type = csv field_delimiter = ',' skip_header = 1
    field_optionally_enclosed_by = '"'
    null_if = ('NULL', 'null') 
    empty_field_as_null = true;

show file formats;

```

# Create an external stage pointing to your s3 locationPermalink
```sql
create or replace stage my_stage url='s3://my_bucket/key/key/'
    credentials=(aws_key_id='KEY' aws_secret_key='SECRET')
    file_format = my_csv_format;

--또는
create or replace stage my_stage url='s3://my_bucket/key/key/'
    credentials=(aws_role='aws_iam_role=arn:aws:iam::XXXXXXX:role/XXXX')
    file_format = my_csv_format;

show stages;

```

# Review staged files and select data from the files
```sql
list @my_stage;

select t.$1, t.$2
from @my_stage (file_format => my_csv_format) t;

```

# Test loading data into the table
```sql
copy into src.my_source_table
    from @my_stage
    file_format = my_csv_format
    pattern='.*sales.*.csv';

copy into src.my_source_table
    from @my_stage
    file_format = my_csv_format
    on_error='continue';

```

# Create the SnowpipePermalink
```sql
create pipe if not exists my_pipe as
copy into src.my_source_table from @my_stage;

show pipes;

```

# Force a pipe refresh
```sql
alter pipe my_pipe refresh;

```

# Monitor data loads
```sql
select system$pipe_status('my_pipe');

select count(*) from src.my_source_table;

select *
from table(information_schema.copy_history(table_name=>'MY_SOURCE_TABLE', 
    start_time=> dateadd(hours, -24, current_timestamp())));

```

```sql
use role accountadmin;
use snowflake;

select
    convert_timezone('America/Los_Angeles', h.last_load_time)::timestamp_ntz::date as load_date,
    max(convert_timezone('America/Los_Angeles', h.last_load_time)::timestamp_ntz) as max_load_time,
    sum(h.row_count) as rows_loaded,
    sum(h.error_count) as errors
from account_usage.copy_history h
where table_name = 'MY_SOURCE_TABLE'
group by 1
order by 1;

```
