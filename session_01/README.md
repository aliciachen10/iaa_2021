## IAA Module - Session 1 - Platform Overview
---

[Google Slides](https://docs.google.com/presentation/d/1CC03MXct8pW9DblZ4i7sICcYlbXg81xgyB1DLtDh_ig/edit?usp=sharing)

## [Google Colab Notebooks](https://colab.sandbox.google.com/)
Colaboratory is a free Jupyter notebook environment that requires no setup, offers free GPU support (with constraints, and runs entirely in the Cloud.
* [Getting Started with BigQuery](https://colab.sandbox.google.com/notebooks/bigquery.ipynb)
* [Retraining an Image Classifier](https://colab.research.google.com/github/tensorflow/hub/blob/master/examples/colab/tf2_image_retraining.ipynb) Build a Keras model on top of a pre-trained image classifier.
* [Text Classification](https://colab.research.google.com/github/tensorflow/hub/blob/master/examples/colab/tf2_text_classification.ipynb) Classifies movie reviews as positive or negative.
* [Style Transfer](https://tensorflow.org/hub/tutorials/tf2_arbitrary_image_stylization): Use deep learning to transfer style between images.
* [Multilingual Universal Sentence Encoder Q&A](https://tensorflow.org/hub/tutorials/retrieval_with_tf_hub_universal_encoder_qa): Use a machine learning model to answer questions from the SQuAD dataset.
* [Video Interpolation](https://tensorflow.org/hub/tutorials/tweening_conv3d): Predict what happened in a video between the first and the last frame.

## Qwiklabs
* [Exploring NCAA Data with BigQuery](https://www.qwiklabs.com/focuses/984?parent=catalog)
* [Bracketology with Google Machine Learning](https://www.qwiklabs.com/focuses/4336?parent=catalog)
* [Machine Learning with Spark on Google Cloud Dataproc](https://www.qwiklabs.com/focuses/3383?parent=catalog)
* [Distributed Machine Learning with Google Cloud ML](https://www.qwiklabs.com/focuses/3382?parent=catalog)
* [Predict Baby Weight with TensorFlow on AI Platform]()


## Google Cloud Dataproc

To Launch a Google Cloud Dataproc cluster, execute these commands:
```
git clone https://github.com/zaratsian/IAA_Sessions.git
cd iaa_2021/session_01/
```
Create the 3+ node cluster (with parameters as specified in the bash script)
```
./dataproc_1_create_cluster.sh
```
To run a test PySpark script, run:
```
./dataproc_2_spark_submit.sh
```
Demo flow once Dataproc has launched:
```
# PySpark Shell - Connected as client to the  Yarn master
/usr/lib/spark/bin/pyspark --deploy-mode client --master yarn --name spark_example
```
```
# Step through ./spark_test_script.py within the PySpark shell

# Optional: For testing purposes, you can also create a Spark DF from python lists:
df = spark.createDataFrame([(1,'nc'),(2,'ca'),(3,'ny')], ['id','state'])
```
```
# Save sim DF as table
sim.write.mode("overwrite").saveAsTable('sim_table')
sim.write.mode("overwrite").format('orc').saveAsTable('sim_table_orc')
```
```
# Execute queries in Hive
/usr/lib/hive/bin/beeline -u jdbc:hive2://localhost:10000/default
# It's recommended to use the JDBC connection, but you can also directly connect to hive via:
#/usr/lib/hive/bin/hive

show tables;
describe formatted sim_table;
```

---

## References:
* [Google Colab Notebooks](https://colab.sandbox.google.com/)
* [Apache Spark Docs](https://spark.apache.org/docs/latest/)
* [Google Cloud BigQuery](https://cloud.google.com/bigquery/what-is-bigquery)
* [Google Cloud PubSub](https://cloud.google.com/pubsub/docs/concepts)
* [Google Cloud Firestore](https://cloud.google.com/firestore/docs)
* [Apache Kafka Docs](https://kafka.apache.org/20/documentation.html)
* [Apache NiFi Docs](https://nifi.apache.org/docs.html)
* [Apache Hive Docs](https://cwiki.apache.org/confluence/display/Hive/GettingStarted)
* [Apache HBase Docs](https://hbase.apache.org/book.html)
* [Apache Phoenix Docs](https://phoenix.apache.org/)
* [Docker Docs](https://docs.docker.com/
)
