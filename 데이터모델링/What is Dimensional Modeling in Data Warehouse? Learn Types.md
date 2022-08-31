# What is Dimensional Modeling in Data Warehouse? Learn Types
# 참조
[원문](https://www.guru99.com/dimensional-model-data-warehouse.html)

# Dimensional Modeling
```
Dimensional Modeling (DM) is a data structure technique optimized for data storage in a Data warehouse.
The purpose of dimensional modeling is to optimize the database for faster retrieval of data.
The concept of Dimensional Modelling was developed by Ralph Kimball and consists of fact and dimension tables.

```

```
A dimensional model in data warehouse is designed to read, summarize, analyze numeric information like values,
balances, counts, weights, etc. in a data warehouse.
In contrast, relation models are optimized for addition, updating and deletion of data
in a real-time Online Transaction System.

These dimensional and relational models have their unique way of data storage that has specific advantages.
For instance, in the relational mode, normalization and ER models reduce redundancy in data.
On the contrary, dimensional model in data warehouse arranges data in such a way
that it is easier to retrieve information and generate reports.
Hence, Dimensional models are used in data warehouse systems and not a good fit for relational systems.
In this tutorial, you will learn

```

- Elements of Dimensional Data Model
    - Fact
    - Dimension
    - Attributes
    - Fact Table
    - Dimension Table
- Types of Dimensions in Data Warehouse
- Steps of Dimensional Modelling
    - Step 1) Identify the Business Process
    - Step 2) Identify the Grain
    - Step 3) Identify the Dimensions
    - Step 4) Identify the Fact
    - Step 5) Build Schema
- Rules for Dimensional Modelling
- Benefits of Dimensional Modeling

# Elements of Dimensional Data Model
## Fact
```
Facts are the measurements/metrics or facts from your business process.
For a Sales business process, a measurement would be quarterly sales number

```
## Dimension
```
Dimension provides the context surrounding a business process event.
In simple terms, they give who, what, where of a fact.
In the Sales business process, for the fact quarterly sales number, dimensions would be

◎ Who – Customer Names
◎ Where – Location
◎ What – Product Name

In other words, a dimension is a window to view information in the facts.

```

## Attributes
```
The Attributes are the various characteristics of the dimension in dimensional data modeling.
In the Location dimension, the attributes can be
◎ State
◎ Country
◎ Zipcode etc.
Attributes are used to search, filter, or classify facts. Dimension Tables contain Attributes

```
## Fact Table
```
A fact table is a primary table in dimension modelling.
◎ A Fact Table contains
◎ Measurements/facts
Foreign key to dimension table

```
## Dimension Table
```
◎ A dimension table contains dimensions of a fact.
◎ They are joined to fact table via a foreign key.
◎ Dimension tables are de-normalized tables.
◎ The Dimension Attributes are the various columns in a dimension table
◎ Dimensions offers descriptive characteristics of the facts with the help of their attributes
◎ No set limit set for given for number of dimensions
◎ The dimension can also contain one or more hierarchical relationships

```

# Types of Dimensions in Data Warehouse
```
Following are the Types of Dimensions in Data Warehouse:

◎ Conformed Dimension
◎ Outrigger Dimension
◎ Shrunken Dimension
◎ Role-playing Dimension
◎ Dimension to Dimension Table
◎ Junk Dimension
◎ Degenerate Dimension
◎ Swappable Dimension
◎ Step Dimension

```

# Steps of Dimensional Modelling
```
The accuracy in creating your Dimensional modeling determines the success of your data warehouse implementation.
Here are the steps to create Dimension Model

◎ Identify Business Process
◎ Identify Grain (level of detail)
◎ Identify Dimensions
◎ Identify Facts
◎ Build Star

```

```
The model should describe the Why, How much, When/Where/Who and What of your business process

```
![image](https://user-images.githubusercontent.com/102650331/187611515-ac172314-b76f-4f57-b55b-ba6e38ea8825.png)

