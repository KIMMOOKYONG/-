# How to Calculate Continuous Data Ingestion Costs Using Snowpipe in Snowflake
# Continuous Data Ingestion Workload & Key Metrics
![image](https://user-images.githubusercontent.com/102650331/176987806-513026cb-ca51-4f7a-b388-2272b4189450.png)

# Snowpipe Auto Ingest Flow for Continuous Data Load
![image](https://user-images.githubusercontent.com/102650331/176987857-92e69263-a009-4e95-a26f-fa31d0790950.png)

# Code Set
## Integration object with cloud storage (Azure Blob)
```sql
create storage integration azure_int
    type = external_stage
storage_provider = azure
    enabled = true
 	azure_tenant_id = '<tenant_id>'
 	storage_allowed_locations = ('azure://myaccount.blob.core.windows.net/mycontainer/path1/')

```

## Create external stage object
```sql
create stage my_blob_stage
url = 'azure://blob_loccation/delta/'
    storage_integration = azure_int

```

## Create pipe object
```sql
create pipe stage.raw.mypipe
    auto_ingest=true as
    copy into stage.raw.my_table
    from
@my_blob_stage/csv_files
    file_format = (type = 'CSV' compression='GZIP');

```

# Snowpipe Credit Trend & Load Latency Simulation Result
## Copy History Query
```sql
select
    pipe_name,
    file_name,
    status,
    row_count,
    file_size,
    pipe_received_time ,
    first_commit_time,
    hour(pipe_received_time) as "nth hr",
    minute(pipe_received_time) as "nth min",
    round((file_size/(1000*1024)),2) as "size(mb)",
    timediff(second,pipe_received_time,first_commit_time ) as "latency(s)"
from snowflake.account_usage.copy_history

```

## Pipe Usage History Query
```sql
select
    pipe_id,
    pipe_name,
    start_time,
    end_time,
    hour(start_time) as "nth hr",
    minute(start_time) as "nth min" ,
    credits_used,
    bytes_inserted,
    (bytes_inserted/(1000*1024)) as "size(mb)",
    files_inserted
from
    snowflake.account_usage.pipe_usage_history

```
