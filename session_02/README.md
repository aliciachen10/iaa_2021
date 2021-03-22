# [Institute for Advanced Analytics](https://analytics.ncsu.edu/)
Distributed Data Processing - Dan Zaratsian

[**Slides**](https://docs.google.com/presentation/d/1zB7K2ud91WOKuCENic4WNLz6lSqJ0yUbijYQJ3HbFU0/edit#slide=id.g714c40836b_0_347)

---

## IAA Module - Session 2 - SQL and NoSQL Services
* Hadoop 101
* Intro to Apache Hive
* Apache Hive Syntax and Schema Design
* Intro to Apache HBase and Apache Phoenix (NoSQL)
* Apache HBase Schema Design & Best Practices
* Apache Phoenix Syntax
* Intro to Apache SparkSQL
* Apache SparkSQL 
* BigQuery (Serverless SQL)
* Google Cloud Firestore (NoSQL)
* [Google Colab Notebook Environment](https://colab.sandbox.google.com/)
* [Google BigQuery Sandbox](https://console.cloud.google.com/bigquery)

**Assignment**
- [Assignment 1 SQL](Assignment_1_SQL.md) - Solution
- [Assignment 2 NoSQL](Assignment_2_NoSQL.ipynb) - Solution

--- 

**Docker Containers**
NOTE: In order to run Docker containers, make sure that you have [Docker installed](https://docs.docker.com/get-docker/). 

To pull and execute a PySpark container, run the following:
```
# Pull Docker container
docker pull jupyter/pyspark-notebook

# Execute Container
# You can use the -d parameter to detach the container and run in the background
docker run -p 8888:8888 jupyter/pyspark-notebook

# Alternatively, you could also run this command to get a Jupyter Hub environment
# docker run -p 8888:8888 -e JUPYTER_ENABLE_LAB=yes -v "$PWD":/home/jovyan/work jupyter/pyspark-notebook 

# Open Jupyter in your browser
# Go to the link that is provided in the terminal (ie. http://a0f0ce0e598e:8888/?token=abcdefg)

# You can also login directly to the container: 
docker exec -it name_of_running_container bash
```

Google Cloud provided [Deep Learning Containers](https://cloud.google.com/ai-platform/deep-learning-containers/docs/choosing-container)

---

## References
* [Apache Spark Docs](https://spark.apache.org/docs/latest/)
* [Google Cloud BigQuery](https://cloud.google.com/bigquery/what-is-bigquery)
* [Google Cloud PubSub](https://cloud.google.com/pubsub/docs/concepts)
* [Google Cloud Firestore](https://cloud.google.com/firestore/docs)
* [Apache Kafka Docs](https://kafka.apache.org/20/documentation.html)
* [Apache NiFi Docs](https://nifi.apache.org/docs.html)
* [Apache Hive Docs](https://cwiki.apache.org/confluence/display/Hive/GettingStarted)
* [Apache HBase Docs](https://hbase.apache.org/book.html)
* [Apache Phoenix Docs](https://phoenix.apache.org/)
* [Docker Docs](https://docs.docker.com/)
