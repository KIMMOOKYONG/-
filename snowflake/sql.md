```sql
# warehouse 인스턴스 생성
use role sysadmin;

create or replace warehouse ETL_WH
warehouse_size = xsmall
max_cluster_count = 3
min_cluster_count = 1
scaling_policy = economy
auto_suspend = 300
auto_resume = true
initially_suspended = true
comment = 'virtual warehouse for ETL workloads. auto scales between 1 and 3 clusters depending on the workload';

# 신규 계정 관리자 생성
use role securityadmin;

create user secondary_account_admin
password = 'password1234'
default_role = "accountadmin"
must_change_password = true;

grant role "ACCOUNTADMIN" to user secondary_account_admin;

# 데이터베이스 관리하기
create database our_first_database
comment = 'our first database';

show databases like 'our_first_database';

create database production_database
data_retention_time_in_days = 15
comment = 'Critical production database';

show databases like 'production_database'

create transient database temporary_database
data_retention_time_in_days = 0
comment = 'Temporary database for ETL processing';

show databases like 'temporary_database';

alter database temporary_database
set data_retention_time_in_days = 1;

show databases like 'temporary_database';

# 데이터 스키마 관리
create database testing_schema_creation;
show databases like 'testing_schema_creation';
show schemas in database testing_schema_creation;

create schema a_custom_schema
comment = 'a new custom schema';
show schemas in database testing_schema_creation;


create transient schema temporary_data
data_retention_time_in_days = 0
comment = 'Schema containing temporary data used by ETL processes';

# 테이블 관리
create table customers (
    id int not null,
    last_name varchar(100),
    first_name varchar(100),
    email varchar(100),
    company varchar(100),
    phone varchar(100),
    address1 varchar(150),
    address2 varchar(150),
    city varchar(100),
    state varchar(100),
    postal_code varchar(15),
    country varchar(50)
);

describe table customers;

create or replace table customers (
    id int not null,
    last_name varchar(100),
    first_name varchar(100),
    email varchar(100),
    company varchar(100),
    phone varchar(100),
    address1 string,
    address2 string,
    city varchar(100),
    state varchar(100),
    postal_code varchar(15),
    country varchar(50)
);

describe table customers;

copy into customers
from s3://snowflake-cookbook/ch2/r3/customer.csv
file_format = (type=csv skip_header=1 field_optionally_enclosed_by='"');

create or replace table
customers_deep_copy
as 
select * from customers;

create or replace table 
customers_shallow_copy
like customers;

select count(*) shallow_count from customers_shallow_copy;

create temporary table customers_temp
as 
select * from customers
where try_to_number(postal_code) is not null;

create transient table customers_trans
as
select * from customers
where try_to_number(postal_code) is not null;

# 외부 테이블과 스테이지 관리
create or replace stage sfuser_ext_stage
url = 's3://snowflak-cookbook/ch2/r4';

alter stage sfuser_ext_stage
set url = 's3://snowflake-cookbook/ch2/r4';

list @sfuser_ext_stage;

create or replace external table ext_table_userdata1
with location = @sfuser_ext_stage
file_format = (type=parquet);

show tables

select * from ext_table_userdata1;

create or replace external table ext_card_data
with location = @sfuser_ext_stage/csv
file_format = (type=csv)
pattern = '.*headless[.]csv';

select * from ext_card_data;

select top 5 value:c3::float as card_sum,
value:c2::string as period
from ext_card_data;

drop table ext_card_data;
drop table ext_table_userdata1;

# 데이터 뷰 관리
create database test_view_creation;

create view test_view_creation.public.data_wise_orders
as
select l_commitdate as order_date,
sum(l_quantity) as tot_qty,
sum(l_extendedprice) as tot_price 
from snowflake_sample_data.tpch_sf1000.lineitem
group by l_commitdate;


select * from test_view_creation.public.data_wise_orders;


create materialized view test_view_creation.public.date_wise_orders_fast
as
select l_commitdate as order_date,
sum(l_quantity) as tot_qty,
sum(l_extendedprice) as tot_price 
from snowflake_sample_data.tpch_sf1000.lineitem
group by l_commitdate;

select * from test_view_creation.public.date_wise_orders_fast;

```
