import dlt 

#Importing an empty streaming table 
dlt.create_streaming_table(
  name="append_table",
  comment="This is a streaming table"
)

#Creating Flow_1
@dlt.append_flow(
    target = 'append_table'
)
def flow_1():
    df = spark.readStream.format("cloudFiles")\
              .option("cloudFiles.format", "csv")\
              .load("/Volumes/dbricks_bootcamp/bronze/autovol/flow1/")
    return df

#Creating Flow_1
@dlt.append_flow(
    target = 'append_table'
)
def flow_2():
    df = spark.readStream.format("cloudFiles")\
              .option("cloudFiles.format", "csv")\
              .load("/Volumes/dbricks_bootcamp/bronze/autovol/flow2/")
    return df

