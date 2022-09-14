# Prefect: How to Write and Schedule Your First ETL Pipeline with Python
```
Prefect is a Python-based workflow management system based on a simple premise
- Your code probably works, but sometimes it doesn't (source).
No one thinks about workflow systems when everything works as expected.
But when things go south, Prefect will guarantee your code fails successfully.

```

```
As a workflow management system, Prefect makes it easy to add logging,
retries, dynamic mapping, caching, failure notifications,
and more to your data pipelines.
It is invisible when you don't need it — when everything works as expected,
and visible when you do. Something like insurance.

```

```
While Prefect isn't the only available workflow management system for Python users,
it is undoubtedly the most proficient one.
Alternatives such as Apache Airflow usually work well,
but introduce a lot of headaches when working on big projects.
You can read a detailed comparison between Prefect and Airflow here.

```

```
This article covers the basics of the library, such as tasks,
flows, parameters, failures, and schedules, 
and also explains how to set up the environment both locally and in the cloud.
We'll use Saturn Cloud for that part, as it makes the configuration effortless.
It is a cloud platform made by data scientists,
so most of the heavy lifting is done for you.

```

```
Saturn Cloud can handle Prefect workflows without breaking a sweat.
It is also a cutting-edge solution for anything from dashboards
to distributed machine learning, deep learning, and GPU training.

Today you'll learn how to:
- Install Prefect locally
- Write a simple ETL pipeline with Python
- Use Prefect to declare tasks, flows, parameters, schedules and handle failures
- Run Prefect in Saturn Cloud

```

# How to Install Prefect Locally
```
We'll install the Prefect library inside a virtual environment.
The following commands will create and activate the environment named prefect_env
through Anaconda, based on Python 3.8:

conda create — name prefect_env python=3.8
conda activate prefect_env

You'll have to enter y a couple of times to instruct Anaconda to proceed,
but that's the case with every installation.
Library-wise, we'll need Pandas for data manipulation, Requests for downloading the data,
and of course, Prefect for workflow management:

conda install requests pandas
conda install -c conda-forge prefect

We now have everything needed to start writing Python code. Let's do that next.

```

# Writing an ETL Pipeline With Python
```
We'll use Prefect to complete a relatively simple task today
— run an ETL pipeline.
This pipeline will download the data from a dummy API, transform it,
and save it as a CSV.
The JSON Placeholder website will serve as our dummy API.
Among other things, it contains fake data for ten users:

```

![image](https://user-images.githubusercontent.com/102650331/190069327-5b0622ab-2103-47b2-833b-bc787f73e4c0.png)

