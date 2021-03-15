CLUSTER_NAME=iaa-gccluster
PYSPARK_SCRIPT=spark_test_script.py

# Submit pyspark job
gcloud dataproc jobs submit pyspark -region us-central1 --cluster=$CLUSTER_NAME $PYSPARK_SCRIPT

#ZEND
