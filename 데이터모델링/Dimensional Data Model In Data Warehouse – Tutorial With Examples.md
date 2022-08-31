# Dimensional Data Model In Data Warehouse – Tutorial With Examples
# Dimensional Data Models
```
Dimensional data models are the data structures that are available to the end-users in ETL flow,
to query and analyze the data.
The ETL process ends up with loading data into the target Dimensional Data Models.
Every dimensional data model is built with a fact table surrounded by multiple dimension tables.

```

# Steps to be followed while designing a Dimensional Data Model:
![image](https://user-images.githubusercontent.com/102650331/187673030-273e643b-4e6e-4772-b393-c75c5e95b772.png)

# Benefits Of Dimensional Data Modeling
```
Enlisted below are the various benefits of Dimensional Data Modeling.

● They are secured to use the continuously changing DW environments.
● Huge data can be easily built with the help of dimensional data models.
● The data from the dimensional data models are easy to understand and analyze.
● They are quickly accessible by the end-users for querying with high performance.
● Dimensional data models allow us to drill down (or) roll up the data hierarchically.

```

# ER Modeling Vs Dimensional Data Modeling
```
● ER modeling is suitable for operational systems whereas dimensional modeling is suitable
for the data warehouse.
● ER modeling maintains detailed current transactional data whereas dimensional modeling
maintains the summary of both current and historical transactional data.
● ER modeling has normalized data whereas dimensional modeling has de-normalized data.
● ER modeling uses more joins during query retrieval whereas dimensional modeling uses 
a lesser number of joins hence query performance is faster in dimensional modeling.

```

# Dimensional Data Modeling Myths
```
Given below are some of the existing dimensional data modeling myths.

● Dimensional data models are used only to represent the summary of the data.
● They are department-specific in an organization.
● They do not support scalability.
● They are designed to serve the purpose of end-user reports and queries.
● We can't integrate the dimensional data models.

```
# Dimension Tables
```
Dimension tables play a key role in the DW system by storing all the analyzed metric values.
These values are stored under easily selectable dimensional attributes (columns) in the table.
The quality of a DW system mostly depends on the depth of dimension attributes.
Hence we should try to provide many attributes along with their respective values in the dimension tables.
Let’s explore the structure of dimension tables!!

```

## 1) Dimension Table Key:
```
Every Dimension table will have any one of its dimension attributes as a primary key 
to uniquely identify each row.
Hence the distinct numeric values of that attribute can act as primary keys.

If the attribute values are not unique in any case,
then you can consider sequentially generated system numbers as the primary keys.
These are also called as Surrogate keys.

Dimensional data models must have the referential integrity constraint
for each key between dimensions and facts.
Thus Fact tables will have a foreign key reference for each primary/surrogate key
in the dimension table to maintain referential integrity.

If it is failed, then the respective fact table data cannot be retrieved for that dimension key.

```

## 2) Table Is Wide:
```
We can say that dimension tables are wide as we can add any number of attributes
to a dimension table at any point in the DW cycle.
DW architect will request the ETL team to add respective new attributes to the schema.

In real-time scenarios, you can see dimension tables with 50 (or) more attributes.

```

## 3) Textual Attributes:
```
Dimensional attributes can be of any type as preferably text (or) numeric.
Textual attributes will have real business words rather than codes.
Dimension tables are not meant for calculations hence numeric values are rarely used
for dimensional attributes.

```

## 4) Attributes May Not Be Directly Related:
```
All the attributes in a dimension table may not be related to one another.

```

## 5) Not Normalized:
```
Normalizing a dimension table brings more intermediary tables into the picture
which is not efficient. Thus dimension tables are not normalized.

Dimensional attributes can act as the source for constraints in queries and can also be displayed
as labels in the reports.
The queries will perform efficiently
if you directly pick an attribute from the dimension table and refer directly
to the respective fact table without touching any other intermediary tables.

```

## 6) Drilling Down and Rolling Up:
```
Dimension attributes have the capability to drill down (or) roll up the data whenever needed.

```

## 7) Multiple Hierarchies:
```
A single dimension table having multiple hierarchies is very common.
A dimension table will have a simple hierarchy if only one path exists from the bottom level to the top.
Similarly, it will have multiple hierarchies
if there are multiple paths present to reach from the bottom level to the top.

```

## 8) Few Records:
```
Dimension tables will have less number of records (in hundreds) than the fact tables (in millions).
Though they are smaller than the facts, they provide all the inputs to the fact tables.

```
