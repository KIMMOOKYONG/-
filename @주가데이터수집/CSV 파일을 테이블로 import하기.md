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
