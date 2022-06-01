# 008 Snowflake Tutorial - How to Load Data in Snowflake
![image](https://user-images.githubusercontent.com/102650331/171132415-a6bec2db-08ac-42aa-94c6-23e3352eaaaf.png)

![image](https://user-images.githubusercontent.com/102650331/171132457-a7fcdf64-00e2-4c6e-9e26-2a337753922e.png)

![image](https://user-images.githubusercontent.com/102650331/171132616-3d7f78ff-436f-4e9d-b678-bf63380f7e97.png)

![image](https://user-images.githubusercontent.com/102650331/171135623-cd85b8b9-b600-4d73-80d0-ca65c30a051d.png)

![image](https://user-images.githubusercontent.com/102650331/171135681-ccbf9739-20fa-4571-a14a-d7433293e124.png)

![image](https://user-images.githubusercontent.com/102650331/171135736-72cbeded-aba1-4db6-b327-344aa7f22711.png)


![image](https://user-images.githubusercontent.com/102650331/171309472-dcb2de32-d75a-4662-be80-c36656a95dd3.png)


![image](https://user-images.githubusercontent.com/102650331/171310866-f9b8b1be-aaca-4bd3-ae2d-b466b9851124.png)

```sql
copy into trips from @citibike_trips 
file_format=CSV
on_error = 'skip_file';

```

```python
copy into trips from @citibike_trips 
pattern='.*trips_2013.*[^0-9].*.csv.gz' 
FORCE = TRUE 
file_format=CSV;

```

![image](https://user-images.githubusercontent.com/102650331/171311246-b4e68d44-455f-47b3-bcc6-e4630f0f0fb4.png)

```sql
select * from trips;

```

![image](https://user-images.githubusercontent.com/102650331/171318118-051e457e-d3a3-43fa-bde8-54971fe2cf19.png)

![image](https://user-images.githubusercontent.com/102650331/171322346-b0dcfb99-e97a-4644-9a34-96cfdc13912b.png)

