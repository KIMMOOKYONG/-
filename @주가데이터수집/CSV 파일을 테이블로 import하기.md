# CSV 파일을 테이블로 import하기
```sql
# 문법
LOAD DATA LOCAL INFILE '/경로/파일명.csv'
REPLACE
INTO TABLE `mydb`.`target_table`
COLUMNS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES;

# REPLACE : PK가 동일할 경우 덮어쓴다.
# IGNORE 1 LINES : header column을 무시한다.

```
# test.csv
```
1000,"hana"
1001,"hanajava"

```

![image](https://user-images.githubusercontent.com/102650331/190417290-e0663f07-7b66-448c-a75b-494c1e174d09.png)

