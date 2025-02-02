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

![image](https://user-images.githubusercontent.com/102650331/187675522-c7a45d6c-fb6b-4c96-b550-786ff4f5b722.png)

```
By understanding the above concepts,
you can decide if a data field can act as a dimension attribute (or) not while extracting the data
from the source itself.

```

# The Basic Load Plan For A Dimension
```
Dimensions can be created in two ways i.e.
By extracting the dimension data from external source systems (or)
The ETL system can build the dimensions from staging without involving any external sources.
However, an ETL system without any external processing is more suitable to create dimension tables.

```

# The Basic Load Plan For A Dimension
```
Dimensions can be created in two ways i.e.
By extracting the dimension data from external source systems (or)
The ETL system can build the dimensions from staging without involving any external sources.
However, an ETL system without any external processing is more suitable to create dimension tables.

```

## Below are the steps involved in this process:
```
● Data Cleaning:
Data is cleaned, validated and business rules are applied before loading into the dimension table
to maintain consistency.
● Data Conforming:
Data from other parts of the data warehouse should be properly aggregated as a single value,
with respect to each field of the dimension table.
● Share the same Domains:
Once the data is confirmed it is stored again in staging tables.
● Data Delivery:
Finally all the dimensional attribute values get loaded with primary / surrogate keys assigned.

```

# Types Of Dimensions
```
The various types of Dimensions are listed below for your reference.

```

## 1) Small Dimensions
```
Small dimensions in data warehouse act as lookup tables with less number of rows and columns.
Data into small dimensions can be easily loaded from spreadsheets.
If required small dimensions can be combined as a super dimension.

```

## 2) Conformed Dimension
```
A conformed dimension is a dimension that can be referred
in the same way with every fact table it is related.
Date dimension is the best example of a conformed dimension 
as the attributes of date dimension such as year, month, week, days etc.
communicate the same data in the same way across any number of facts.

```

![image](https://user-images.githubusercontent.com/102650331/187677059-69b9f27a-b55c-4c22-8135-cd9a10f5a6b8.png)


## 3) Junk Dimension
```
Few attributes in a fact table such as flags and indicators can be moved to a separate junk dimension table.
These attributes do not belong to any other existing dimension tables as well.
In general, the values of these attributes are simply a "yes/no" (or) "true/false".

Creating a new dimension for every individual flag attribute makes it complex
by creating more number of foreign keys to the fact table.

At the same time, keeping all these flags and indicator information in fact tables 
also increases the amount of data stored in facts which thereby degrades the performance.

Hence the best solution for this is creating a single junk dimension as a junk dimension
is capable of holding any number of "yes/no" or "true/false" indicators.
However, junk dimensions store descriptive values for these indicators (yes/no (or) true/false)
such as active & pending, etc.

Based on the complexity of a fact table and it's indicators,
a fact table can have one or more junk dimensions.

```

![image](https://user-images.githubusercontent.com/102650331/187677772-98c1d356-b334-4ae7-b2a7-e284a00c84f1.png)


## 4) Role-Playing Dimension
```
A single dimension that can be referred for multiple purposes in a fact table
is known as Role-playing dimension.

The best example for a role-playing dimension is again a Date dimension table
as the same date attribute in a dimension can be used for different purposes in a fact
such as date of order, date of delivery, date of transaction, date of cancellation, etc.

If necessary you can create four different views on the date dimension table
with respect to four different date attributes of a fact table.

```

![image](https://user-images.githubusercontent.com/102650331/187677967-ebe3be0c-53be-4c08-807a-4bc4732bb955.png)


## 5) Degenerate Dimensions
```
There may be few attributes that can be neither dimensions (metrics) nor facts (measures)
but they need for analysis.
All such attributes can be moved into degenerate dimensions.

For example,
you can consider the order number, invoice number etc as degenerate dimension attributes.

```

![image](https://user-images.githubusercontent.com/102650331/187678221-e6554b4d-64b6-43a2-a5ed-3dcf25646c79.png)


## 6) Slowly Changing Dimensions
```
A slowly changing dimension is a kind where data can change slowly at any time rather than in periodic regular intervals.
Modified data in dimension tables can be handled in different ways as explained below.

You can select the SCD type to respond to a change individually for every attribute in a dimensional table.

```

### (i) Type 1 SCD
```
In type 1 when there is a change in the values of the dimensional attributes,
the existing values are overwritten with the newly modified values which is nothing but an update.
Old data is not maintained for historical reference.
Past reports can’t be regenerated because of the non-existence of old data.
Easy to maintain.
The impact on fact tables is more.

```

![image](https://user-images.githubusercontent.com/102650331/187678642-fb9e34c6-c88e-415a-a6ce-394a72f1b117.png)


### (ii) Type 2 SCD
```
In type 2, when there is a change in the values of the dimensional attributes,
a new row will be inserted with the modified values without changing the old row data.
If there is any foreign key reference that exists to the old record in any of the fact tables,
then the old surrogate key gets updated everywhere with a new surrogate key automatically.
The impact on the fact table changes is very less with the above step.
Old data is not considered anywhere after the changes.
In type 2, we can track all the changes that are happening to the dimensional attributes.
There is no limit on the storage of historical data.
In type 2, adding few attributes to each row such as changed date, effective date-time, end date-time,
the reason for the change and the current flag is optional.
But this is significant if the business wants to know the number of changes made during a certain time period.

```

![image](https://user-images.githubusercontent.com/102650331/187678856-9604dc59-e9af-4787-9c4c-a33caf41fa01.png)

### (iii) Type 3 SCD
```
In type 3 when there is a change in the values of the dimensional attributes,
new values are updated but the old values still remain valid as the second option.
Instead of adding a new row for every change, a new column will be added if it is not existing previously.
Old values are placed in the above-added attributes and the primary attribute's data is
overwritten with the changed value as in type 1.
There is a limit on the storage of historical data.
The impact on fact tables is more.

```
![image](https://user-images.githubusercontent.com/102650331/187679126-d9929670-1cdd-4e74-8988-ae4236b38f6d.png)

### (iv) Type 4 SCD
```
In type 4, the current data is stored in one table.
All historical data is maintained in another table.

```

![image](https://user-images.githubusercontent.com/102650331/187679206-bdaaa14a-612a-44c7-b797-cfaa2b6d814f.png)


### (v) Type 6 SCD
```
A dimensional table can also have a combination of all three SCD types 1, 2 
and 3 which is known as a Type 6 (or) Hybrid slowly changing dimension.

```

# Fact Tables
```
Fact tables store a set of quantitatively measured values that are used for calculations.
The fact table’s values get displayed in the business reports.
In contrast to the dimension tables textual data type, fact tables data type is significantly Numeric.

Fact tables are deep whereas dimension tables are wide as fact tables will have a higher number of rows 
and a lesser number of columns.
A primary key defined in the fact table is primarily to identify each row separately.
The primary key is also called a Composite key in fact table.

If the composite key is missing in a fact table and if any two records have the same data,
it is very tough to differentiate between the data and to refer the data in dimension tables.

Hence, if a proper unique key exists as the composite key,
then it is good to generate a sequence number for each fact table record.
Another alternative is to form a concatenated primary key.
This will be generated by concatenating all the referred primary keys of dimension tables row-wise.

A single fact table can be surrounded by multiple dimension tables.
With the help of the foreign keys that exist in fact tables,
the respective context (verbose data) of the measured values can be referred to in the dimension tables.
With the help of queries, the users will perform drill down and roll up efficiently.

The lowest level of data that can be stored in a fact table is known as Granularity.
The number of dimension tables associated with a fact table is 
inversely proportional to the granularity of that fact table data. i.e.
The smallest measurement value needs more dimension tables to be referred.

In a dimensional model, the fact tables maintain many-to-many relation with dimension tables.

```
![image](https://user-images.githubusercontent.com/102650331/187679690-58a975ce-a8aa-41e2-aff3-4e2033aa0dc2.png)


# Load Plan For Fact Tables
```
You can load a fact table data efficiently by considering the following pointers:

```

## 1) Drop And Restore Indexes
```
Indexes in fact tables are good performance boosters while querying the data,
but they demolish the performance while loading the data.
Hence, before loading any huge data into fact tables primarily drop all the indexes on that table,
load the data and restore the indexes.

```

## 2) Separate Inserts From Updates
```
Do not merge insert and update records while loading into a fact table.
If the number of updates is less, then process inserts, and updates separately.
If the number of updates is more then it is advisable to truncate and reload the fact table for quick results.

```
## 3) Partitioning
```
Do the partitioning physically on a fact table into mini tables for better query performance 
on bulk fact table’s data.
Except for the DBAs and the ETL team no one will be aware of the partitions on facts.

As an example,
you can partition a table month-wise, quarter wise, year-wise, etc.
While querying, only the partitioned data is considered instead of scanning the entire table.

```

## 4) Load In Parallel
```
We have now got an idea about partitions on fact tables.
Partitions on facts are also beneficial while loading huge data into facts.
To do this, first, break the data logically into different data files and run the ETL jobs
to load all these logical portions of data in parallel.

```
##5) Bulk Load Utility
```
Unlike other RDBMS systems,
ETL system does not need to maintain rollback logs explicitly for mid-transaction failures.
Here "bulk loads" happen into facts instead of "SQL inserts" to load huge data.
If in case a single load fails, then the entire data can be easily reloaded (or)
it can get continued from where it is left off with the bulk load.

```

## 6) Deleting A Fact Record
```
Deleting a fact table record happens only if the business wants explicitly.
If there is any fact table data that no longer exists in the source systems 
then that respective data can be deleted either physically (or) logically.

Physical delete: Unwanted records are removed from the fact table permanently.
Logical delete: A new column will be added to the fact table such as "deleted" of Bit (or) Boolean type.
This acts as a flag to represent the deleted records.
You must ensure that you are not selecting the deleted records while querying the fact table data.

```

## 7) Sequence For Updates And Deletes In A Fact Table
```
When there is any data to be updated,
the dimension tables should get updated first followed by updating the surrogate keys
in the lookup table if necessary and after that the respective fact table updates.
Deletion happens in reverse because deleting all unwanted data from fact tables makes easy
to delete the linked unwanted data from the dimension tables.

We should follow the above sequence in both cases because dimension tables
and fact tables maintain referential integrity all the time.

```

# Types Of Facts
```
Based on the behavior of fact tables data they are categorized as transaction fact tables,
snapshot fact tables, and accumulated snapshot fact tables.
All these three types follow different features with different data load strategies.

```

## 1) Transaction Fact Tables
```
As the name indicates transaction fact tables store transaction-level data for each event that happens.
Such kind of data is easy to analyze at the fact table level itself. But for further analysis,
you can also refer to the associated dimensions.

For example,
every sale (or) purchase happening from a marketing website should be loaded into a transaction fact table.

```

![image](https://user-images.githubusercontent.com/102650331/187681086-6163070c-8bc7-4531-9fe6-865b87c5b1fd.png)


## 2) Periodic Snapshot Fact Tables
```
As the name indicates data in periodic snapshot fact table is
stored in the form of snapshots (pictures) at periodic intervals
such as for every day, week, month, quarter etc depending on the business needs.

So it is clear that this is an aggregation of data all the time.
Hence snapshot facts are more complex compared to transaction fact tables.
For example, any performance revenue reports data can be stored in snapshot fact tables for easy reference.

```

![image](https://user-images.githubusercontent.com/102650331/187681397-4f8992cd-b075-4385-9e2c-a086b3a8c1f2.png)

## 3) Accumulating Snapshot Fact Tables
```
Accumulating snapshot fact tables allow you to store data into tables for the entire lifetime of a product.
This acts as a combination of the above two types where data can be inserted
by any event at any time as a snapshot.

In this type, 
additional date columns and data for each row gets updated with every milestone of that product.

```

![image](https://user-images.githubusercontent.com/102650331/187681546-1427dd96-0a95-402b-b931-a61934ae4a80.png)


```
In addition to the above three types, here are a few other types of fact tables:

```

## 4) Factless Fact Tables:
```
A fact is a collection of measures whereas fact less captures only events (or) conditions
that do not contain any measures. A fact-less fact table is mainly used to track a system.
The data in these tables can be analyzed and used for reporting.

For example,
you can look for details of an employee who has taken leave and the type of leave in a year, etc.
Including all these non-clear fact details in a fact, the table will definitely increase the size of facts.

```

![image](https://user-images.githubusercontent.com/102650331/187681793-a10ecc63-e2b4-439f-9d26-36e55fd3b89d.png)

## 5) Conformed Fact Tables:
```
A conformed fact is a fact which can be referred in the same way with every data mart it is related to.

```

# Specifications Of A Fact Table
```
Given below are the specifications of a Fact Table.

● Fact name: This is a string that describes the functionality of the fact table in brief.
● Business process: Talks about the business need to be fulfilled by that fact table.
● Questions: Mentions a list of business questions that will be answered by that fact table.
● Grain: Indicates the lowest level of detail associated with that fact table data.
● Dimensions: List out all the dimension tables associated with that fact table.
● Measures: The calculated values stored in the fact table.
● Load frequency Represents the time intervals to load data into the fact table.
● Initial rows: Refer to the initial data populated in the fact table for the first time.

```

# Example Of Dimensional Data Modeling
```
You can get an idea of how dimension tables and fact tables can be designed for a system
by looking at the below dimensional data modeling diagram for sales and orders.

```

![image](https://user-images.githubusercontent.com/102650331/187682695-2cf51b52-7058-4a09-a94a-54c1d5af58f4.png)


