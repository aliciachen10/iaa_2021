## Assignment #1 - SQL and NoSQL Distrubuted Databases

Please submit the code and answers to me at d.zaratsian@gmail.com as a notebook, script, Google Doc, or whatever method you prefer. I'd prefer for you to answer these questions using [Google BigQuery (free Sandbox version)](https://console.cloud.google.com/bigquery) so that you get used to this Serverless Cloud Data Warehouse. If that doesn't work, then you can use SparkSQL within [Google Colab Notebooks](https://colab.sandbox.google.com) or the docker container environments that I provide below. Here's my [starter Colab notebook](https://github.com/zaratsian/iaa_2021/blob/main/session_02/pyspark_sql.ipynb) to get you up and running. If for some reason those methods do not work, then you may use a different approach, but please specify your approach as part of your response. 

Use the San Francisco Bike sharing data to answer the following questions. There are two ways to access the data:

**Option #1 - Use Google BigQuery**: You can query the data directly in [Google Cloud BigQuery](https://console.cloud.google.com/bigquery) using a syntax such as this:

```
SELECT * FROM `bigquery-public-data.san_francisco_bikeshare.bikeshare_trips` LIMIT 1000
```

```
SELECT * FROM `bigquery-public-data.san_francisco_bikeshare.bikeshare_station_info` LIMIT 1000
```

**Option #2 - Use Colab or local environment**: Download the files from here [bikesharing_trips.csv](https://raw.githubusercontent.com/zaratsian/iaa_2021/main/session_02/bikeshare_trips.csv) and [bikesharing_stations.csv](https://raw.githubusercontent.com/zaratsian/iaa_2021/main/session_02/bikeshare_station_info.csv)

**Option #3 - Use a Docker container**: You can choose a container of your choice, but here's the process I'd take to deploy a containerized environment with Jupyter notebooks and Pyspark SQL installed: 
```
docker pull jupyter/pyspark-notebook
docker run -p 8888:8888 jupyter/pyspark-notebook
``` 

-----------------


## **Questions:**

1. Which bike station in San Francisco is the most popular when starting a trip?


2. Which routes (start to end point) are the most popular? Please list the top 5. A route is a defined as a (start_station_name, end_station_name).


3. Which stations are the furthest distance apart? Hint: If you're using BigQuery, I'd recommend calculating the distance in meters based on the longitude and latitude of the start and end points ([reference](https://cloud.google.com/bigquery/docs/reference/standard-sql/geography_functions))


-----------------

