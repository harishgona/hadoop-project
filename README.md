# hadoop-project

## Hadoop MapReduce CSV Analysis

This project reads the data from __/data/nyc/nyc-traffic.csv__ which has the data of accidents occured in new york city and gives the total count of each vehicle type involved in an accident.

1. Load the mapper.py and reducer.py scripts to local storage.
2. Use the following script to _hadoop fs -cat /data/nyc/nyc-traffic.csv | python <location of mapper.py> | sort | python <location of reducer.py> > results.txt_ get the vehicle count and store locally.
3. Then, hadoop jar /opt/hadoop-2.7.1/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar \
-file /home/$USER/mapper.py    -mapper /home/$USER/mapper.py \
-file /home/$USER/reducer.py   -reducer /home/$USER/reducer.py \
-input /data/books/ulysses.txt  -output /user/$USER/traffic

