
#######################################################################
#
#   Assignment #1 Solution
#
#   This SQL has been tested within Google Cloud BigQuery
#
#######################################################################


# Question 1: Which bike station in Austin is the most popular when starting a trip?
#
# Answer:
# San Francisco Caltrain (Townsend at 4th)      72683
# San Francisco Caltrain 2 (330 Townsend)       56100
# Harry Bridges Plaza (Ferry Building)          49062
# Embarcadero at Sansome                        41137
# 2nd at Townsend                               39936


SELECT
    start_station_name,
    count(*) as freq
FROM `bigquery-public-data.san_francisco_bikeshare.bikeshare_trips`
GROUP BY
    start_station_name
ORDER BY
    freq desc
LIMIT 5


# Question #2: Which routes (start to end point) are the most popular? List the top 5.
#
# Answer:
# start_station_name	                    end_station_name	                    freq
# Harry Bridges Plaza (Ferry Building)	    Embarcadero at Sansome	                9150
# San Francisco Caltrain 2 (330 Townsend)	Townsend at 7th	                        8508
# 2nd at Townsend	                        Harry Bridges Plaza (Ferry Building)	7620
# Harry Bridges Plaza (Ferry Building)	    2nd at Townsend	                        6888
# Embarcadero at Sansome	                Steuart at Market	                    6874

SELECT
    start_station_name,
    end_station_name,
    count(*) as freq
FROM `bigquery-public-data.san_francisco_bikeshare.bikeshare_trips`
GROUP BY
    start_station_name,
    end_station_name
ORDER BY freq desc
LIMIT 5


# Question 3: Which stations are the furthest distance apart?
# Hint: I'd calculated the distance in meters based on the longitue and latitute of the start and end points.
# https://towardsdatascience.com/using-bigquerys-new-geospatial-functions-to-interpolate-temperatures-d9363ff19446
# https://cloud.google.com/bigquery/docs/reference/standard-sql/geography_functions
#
# Answer:
# Lake Austin & Enfield     Capital Metro HQ - East 5th at Broadway     8246.260917924477
# Lake Austin & Enfield     East 6th & Pedernales St.                   7709.260055350502
# Lake Austin & Enfield     East 6th at Robert Martinez                 7281.816803608255

# Here's what I would do if I joined both tables
SELECT
    c.start_station_name,
    c.end_station_name,
    ST_Distance(ST_GeogPoint(d.lon, d.lat), ST_GeogPoint(start_longitude, start_latitude)) AS dist_meters
FROM
    (
    SELECT
        a.*,
        b.lat as start_latitude,
        b.lon as start_longitude
    FROM
        `bigquery-public-data.san_francisco_bikeshare.bikeshare_trips` a
    LEFT JOIN
        `bigquery-public-data.san_francisco_bikeshare.bikeshare_station_info` b
    ON a.start_station_id = b.station_id
    ) c
LEFT JOIN
    `bigquery-public-data.san_francisco_bikeshare.bikeshare_station_info` d
ON safe_cast(c.end_station_id as STRING) = safe_cast(d.station_id as STRING)
ORDER BY dist_meters DESC
LIMIT 3


# Alternative solution - Here's what I would do if I focused on the trips table only.
SELECT
    start_station_name,
    end_station_name,
    ST_Distance(ST_GeogPoint(end_station_longitude, end_station_latitude), ST_GeogPoint(start_station_longitude, start_station_latitude)) AS dist_meters
FROM `bigquery-public-data.san_francisco_bikeshare.bikeshare_trips`
WHERE start_station_latitude is not null and start_station_longitude is not null and end_station_latitude is not null and end_station_longitude is not null
ORDER BY dist_meters desc


# Alternative solution - As you may have noticed, can directly assess the distance
# from station to station using code similar to the follow. However, beware that
# crossjoins are very compute intensive and expensive, so on larger tables this would
# not be ideal.

SELECT a.name, b.name, ST_DISTANCE(a.station_geom, b.station_geom) as Distance
FROM
    `bigquery-public-data.san_francisco_bikeshare.bikeshare_station_info` as a,
    `bigquery-public-data.san_francisco_bikeshare.bikeshare_station_info` as b
ORDER BY Distance desc


#ZEND
