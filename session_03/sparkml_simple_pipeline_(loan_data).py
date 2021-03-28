
'''
Download Data:
wget https://raw.githubusercontent.com/zaratsian/iaa_2020/master/data/loan_200k.csv


Spark-Submit Syntax:

/usr/lib/spark/bin/spark-submit --master local[*] sparkml_simple_pipeline_loan.py



gcloud dataproc jobs submit pyspark \
    sparkml_simple_pipeline_loan.py \
    --cluster=iaa-spark-cluster  \
    --region=us-east1


'''

# Import Dependencies
import datetime
from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *
from pyspark.ml.linalg import Vectors
from pyspark.ml.regression import DecisionTreeRegressor, GBTRegressor, LinearRegression, GeneralizedLinearRegression
from pyspark.ml.classification import GBTClassifier
from pyspark.ml.feature import VectorIndexer, VectorAssembler, StringIndexer, OneHotEncoder
from pyspark.ml import Pipeline
from pyspark.ml.evaluation import RegressionEvaluator, MulticlassClassificationEvaluator, BinaryClassificationEvaluator
from pyspark import SparkFiles

"""## **Initialize Spark Session**"""

#spark = SparkSession.builder.appName("Spark ML Pipeline Example").master("local[*]").getOrCreate()
spark = SparkSession.builder.appName("Spark ML Pipeline Example").getOrCreate()

"""## **Read CSV into Spark**"""
data_url = 'https://raw.githubusercontent.com/zaratsian/iaa_2020/master/data/loan_200k.csv'
spark.sparkContext.addFile(data_url)

loan_rawdata = spark.read.load("file://"+SparkFiles.get("loan_200k.csv"), format="csv", header=True, inferSchema=True)
#loan_rawdata = spark.read.load('file:///home/dzaratsian/loan_200k.csv', format="csv", header=True, inferSchema=True)  # Alternative, this works as well.


"""## **Display first few records**"""

loan_rawdata.show(5, truncate=False)

loan_rawdata.dtypes

"""## **Light Data Exploration**"""

loan_rawdata.groupby(loan_rawdata.default).count().show(20,False)

"""## **Split Data into Training and Test**"""

traindata, testdata = loan_rawdata.randomSplit([0.80, 0.20])

print('Training Data: {}'.format(traindata.count()))
print('Test Data:     {}'.format(testdata.count()))

traindata.groupby(traindata.default).count().show(20,False)

testdata.groupby(testdata.default).count().show(20,False)

"""## **Create Transform Objects**
These can be used within your feature engineering and model pipeline.
"""

si  = StringIndexer(inputCol="purpose", outputCol="purpose_index")
hot = OneHotEncoder(inputCol="purpose_index", outputCol="purpose_features")
va  = VectorAssembler(inputCols=["loan_amnt", "interest_rate", "employment_length", "home_owner", "income", "verified", "open_accts", "credit_debt", "purpose_features"], outputCol="features")
dtr = DecisionTreeRegressor(featuresCol="features", labelCol="default", predictionCol="prediction", maxDepth=2, varianceCol="variance")
gbr = GBTRegressor(featuresCol="features", labelCol="default", predictionCol="prediction", maxDepth=5, maxBins=32, maxIter=20, seed=12345)
gbc = GBTClassifier(featuresCol="features", labelCol="default", predictionCol="prediction", maxDepth=5, maxIter=20, seed=12345)

pipeline = Pipeline(stages=[si, hot, va, gbc])

model = pipeline.fit(traindata)

predictions = model.transform(testdata)

predictions.select(['id','loan_amnt','default','prediction']).show(10,False)

predictions.groupBy(predictions['default'],predictions['prediction']).count().show()

evaluator = MulticlassClassificationEvaluator(predictionCol="prediction", labelCol="default")
evaluator.evaluate(predictions, {evaluator.metricName: "accuracy"})

# Save model object
model.save("loan_default_model")

!zip -r loan_default_model.zip loan_default_model

from pyspark.ml.pipeline import PipelineModel
persistedModel = PipelineModel.load('loan_default_model')

test_df = spark.read.load('loan_200k.csv', format="csv", header=True, inferSchema=True)

# predict
predictionsDF = persistedModel.transform(test_df)
predictionsDF.show()