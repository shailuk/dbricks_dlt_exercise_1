import dlt
from pyspark.sql.functions import *

#Creating a staging Table - Reading data from source table
@dlt.table(
    name = "scd1_stg"
)
def scd1_stg(): 
    df = spark.readStream.table("dbricks_bootcamp.bronze.source")
    return df

#Create an empty streaming table 
dlt.create_streaming_table(
    name = "scd1_table"
)

#Create a CDC flow
dlt.create_auto_cdc_flow(
    source = "scd1_stg", 
    target = "scd1_table", 
    keys = ["product_id"], 
    sequence_by = col("processDate"), 
    stored_as_scd_type = 1
)


