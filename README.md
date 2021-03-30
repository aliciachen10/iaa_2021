# [Institute for Advanced Analytics](https://analytics.ncsu.edu/)
Distruted Analytics & Machine Learning - Dan Zaratsian, March 2021


---
## IAA Module - Session 1 - Distributed Services and Platform Overview
[**Slides**](https://docs.google.com/presentation/d/1CC03MXct8pW9DblZ4i7sICcYlbXg81xgyB1DLtDh_ig/edit?usp=sharing)
* Introduction and Module Agenda
* Distributed Computing
* Walk-through of Tools and Services for Big Data
* Distributed Architectures and Use Cases
* [Google Colab Notebook Environment](https://colab.sandbox.google.com/)
* [Google BigQuery Sandbox](https://console.cloud.google.com/bigquery)

---
## IAA Module - Session 2 - SQL and NoSQL Services
[**Slides**](https://docs.google.com/presentation/d/1zB7K2ud91WOKuCENic4WNLz6lSqJ0yUbijYQJ3HbFU0/edit)

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

**Assignment**
* [Assignment 1 SQL](https://github.com/zaratsian/iaa_2021/blob/main/session_02/Assignment_1_SQL.md) - Solution 
  - Due on Friday, March 26
  - Please complete as an individual assignment
  - Email your code and answers to d.zaratsian@gmail.com

* [Assignment 2 NoSQL](https://github.com/zaratsian/iaa_2021/blob/main/session_02/Assignment_2_NoSQL.ipynb) - Solution (Due on Friday, March 26)
  - Due on Friday, March 26
  - Please complete as an individual assignment
  - Email your code and answers to d.zaratsian@gmail.com

---
## IAA Module - Session 3 - Spark Data Processing & Machine Learning
[**Slides**](https://docs.google.com/presentation/d/1JG4nMPv1ryovSpZG62XGS0frzpb0c82EEincZZ7acMU/edit#slide=id.g7167105720_0_348)

* Apache Spark Overview
* Spark Machine Learning (MLlib)
* ML Pipelines
* Building and deploying Spark machine learning models
* Considerations for ML in distributed environments
* Spark Best Practices and Tuning
* Spark Code Walk-through (within Google Colab)

**Assignment** 
* [Assignment 3](https://github.com/zaratsian/iaa_2021/blob/main/session_03/Spark_ML_Assignment_(template).ipynb) - Solution 
  - Due on Friday, April 2
  - Please complete as an individual assignment
  - Email your code to d.zaratsian@gmail.com

---
## IAA Module - Session 4 - SparkML & Scikit-learn Model Deployment

NOTE: Slides from this week were a continuation from Session 3

* [Spark Pipeline Components](https://spark.apache.org/docs/latest/ml-pipeline.html#main-concepts-in-pipelines)
* Spark Best Practices
* Deploying / [Submitting Spark Applications](https://spark.apache.org/docs/latest/submitting-applications.html)
* Scikit-learn Model Training (with [NFL Notebook](https://github.com/zaratsian/iaa_2021/blob/main/session_03/NFL_Predictions_Jupyter.ipynb))
* [Scikit-learn Model Deployment Process](https://github.com/zaratsian/ML-Model-Deployment/tree/master/sklearn_nfl)

---
## IAA Module - Session 5 - Realtime, Streaming Systems
[**Slides**](https://docs.google.com/presentation/d/1yyc1PyXpt-suETXmQJr2FF19lhANVRAQMdo5pujVSw0/edit#slide=id.g71681dc956_0_348)

* Apache Kafka
* Google PubSub
* Demo of PubSub
* Spark Streaming
* Demo of Spark Streaming
* Apache Beam (Google Dataflow)

**Assignment** Due on Friday, April 9. 

NOTE: In order to complete the lab, please sign-up on [Qwiklabs.com](https://www.qwiklabs.com/). Then go this this [spreadsheet]() and grab a token from the doc in order to use as part of your Qwiklab assignment.

When you complete the assignment, plase email me to let me know what lab you completed. 

Please choose **one** lab from the list below:

  - [Building an IoT Analytics Pipeline on Google Cloud](https://run.qwiklabs.com/focuses/605?catalog_rank=%7B%22rank%22%3A2%2C%22num_filters%22%3A2%2C%22has_search%22%3Atrue%7D&parent=catalog&search_id=9480640)
  - [Building Realtime Pipelines in Cloud Data Fusion](https://run.qwiklabs.com/focuses/12365?catalog_rank=%7B%22rank%22%3A1%2C%22num_filters%22%3A2%2C%22has_search%22%3Atrue%7D&parent=catalog&search_id=9480847)
  - [Machine Learning with Spark on Google Cloud Dataproc](https://www.qwiklabs.com/focuses/3383?catalog_rank=%7B%22rank%22%3A1%2C%22num_filters%22%3A2%2C%22has_search%22%3Atrue%7D&parent=catalog&search_id=9480871)
  - [Scikit-learn Model Serving with Online Prediction Using AI Platform](https://www.qwiklabs.com/focuses/1788?catalog_rank=%7B%22rank%22%3A4%2C%22num_filters%22%3A2%2C%22has_search%22%3Atrue%7D&parent=catalog&search_id=9480887)
  - [Predict Baby Weight with TensorFlow on AI Platform](https://www.qwiklabs.com/focuses/137?catalog_rank=%7B%22rank%22%3A9%2C%22num_filters%22%3A2%2C%22has_search%22%3Atrue%7D&parent=catalog&search_id=9480887)

---
## IAA Module - Session 6 - CloudML & Serveless Deployments
**Slides**

* Overview of Google Cloud and general cloud services for ML Deployment
* Overview of Serverless
* Google Cloud Functions
* BigQueryML
* AutoML
* App Engine / Container Based Deployments

---

## References:
* [Apache Spark Docs](https://spark.apache.org/docs/latest/)
* [Google BigQuery](https://cloud.google.com/bigquery/what-is-bigquery)
* [Google BigQuery Sandbox](https://console.cloud.google.com/bigquery)
* [Apache Hive Docs](https://cwiki.apache.org/confluence/display/Hive/GettingStarted)
* [Google Colab Notebooks](https://colab.sandbox.google.com)
* [Google Cloud AI Notebooks](https://cloud.google.com/ai-platform/notebooks/docs/introduction)
* [Google Cloud AI Platform](https://console.cloud.google.com/ai-platform/)
* [Apache Zeppelin](https://zeppelin.apache.org/)
* [Google Cloud Firestore](https://cloud.google.com/firestore/docs)
* [Apache HBase Docs](https://hbase.apache.org/book.html)
* [Apache Phoenix Docs](https://phoenix.apache.org/)
* [Google Cloud PubSub](https://cloud.google.com/pubsub/docs/concepts)
* [Apache Kafka Docs](https://kafka.apache.org/20/documentation.html)
* [Apache NiFi Docs](https://nifi.apache.org/docs.html)
* [Docker Docs](https://docs.docker.com/)
