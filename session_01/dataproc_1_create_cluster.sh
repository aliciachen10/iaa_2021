CLUSTER_NAME=iaa-gccluster
PYSPARK_SCRIPT=spark_test_script.py

# Spin up Dataproc Cluster on Google Cloud
gcloud dataproc clusters create $CLUSTER_NAME \
    --region us-central1 \
    --master-machine-type n1-standard-2 --master-boot-disk-size 500 \
    --num-workers 4 --worker-machine-type n1-standard-2 --worker-boot-disk-size 500 \
    --num-secondary-workers 3 \
    --project zproject201807

# Submit pyspark job
#gcloud dataproc jobs submit pyspark --region us-central1 --cluster=$CLUSTER_NAME $PYSPARK_SCRIPT

# Cleanup / Remove Dataproc Cluster
#gcloud dataproc clusters delete --region us-central1 $CLUSTER_NAME

#ZEND
