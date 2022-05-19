# 코랩 스파크 설치
```
!apt-get install openjdk-8-jdk-headless -qq > /dev/null
!wget -q https://archive.apache.org/dist/spark/spark-3.1.2/spark-3.1.2-bin-hadoop3.2.tgz
!tar -xvf spark-3.1.2-bin-hadoop3.2.tgz
!pip install -q findspark
```
# 데이터 프레임 생성
```python
import os
import pyspark
from pyspark.sql import SparkSession
import findspark

os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-8-openjdk-amd64"
os.environ["SPARK_HOME"] = "/content/spark-3.1.2-bin-hadoop3.2"

findspark.init()

spark = SparkSession.builder.master("local[*]").getOrCreate()

df = spark.createDataFrame([{"hello": "world"} for x in range(1000)])
df.show(3)

a = [{
            "plantcd" : "공장",
            "eventdtm" : "20210518154548",
            "tagGroup" : {
                "b" : "2",
                "a" : 1,
            }
        },
        {
            "plantcd" : "공장",
            "eventdtm" : "20210518154550",
            "tagGroup" : {
                "b" : 10,
                "a" : '9',
                "c" : '11',
            }
}]

df_schema = pyspark.sql.types.StructType([
    pyspark.sql.types.StructField("plantcd", pyspark.sql.types.StringType(), True),
    pyspark.sql.types.StructField("eventdtm", pyspark.sql.types.StringType(), True),
    pyspark.sql.types.StructField("tagGroup", pyspark.sql.types.MapType(
        pyspark.sql.types.StringType(), pyspark.sql.types.StringType()), True)
])

data_test = spark.createDataFrame(data = a , schema = df_schema)

# 테이블 생성
data_test.createOrReplaceTempView("table_name")

table_name= spark.sql("""
SELECT  eventdtm,
        plantcd,
        explode( tagGroup )
FROM table_name
""")

```

# 테스트 코드
```python
%%writefile app.py
import findspark
findspark.init()

import pyspark
from pyspark.sql import SparkSession

spark = SparkSession.builder.master("local[*]").getOrCreate()

df = spark.createDataFrame([{"hello": "world"} for x in range(1000)])
df.show(3)

a = [{
            "plantcd" : "공장",
            "eventdtm" : "20210518154548",
            "tagGroup" : {
                "b" : "2",
                "a" : 1,
            }
        },
        {
            "plantcd" : "공장",
            "eventdtm" : "20210518154550",
            "tagGroup" : {
                "b" : 10,
                "a" : '9',
                "c" : '11',
            }
}]


df_schema = pyspark.sql.types.StructType([
    pyspark.sql.types.StructField("plantcd", pyspark.sql.types.StringType(), True),
    pyspark.sql.types.StructField("eventdtm", pyspark.sql.types.StringType(), True),
    pyspark.sql.types.StructField("tagGroup", pyspark.sql.types.MapType(
        pyspark.sql.types.StringType(), pyspark.sql.types.StringType()), True)
])

data_test = spark.createDataFrame(data = a , schema = df_schema)
data_test.show()

data_test.createOrReplaceTempView("table_name")
table_name= spark.sql("""
SELECT  eventdtm,
        plantcd,
        explode( tagGroup )
FROM table_name
""")

table_name.show()

```
# 테스트 실행
```
!python app.py

```

# 참조 사이트
https://urame.tistory.com/entry/무료-개발-spark-서버-환경-구축-구글-colab-활용

