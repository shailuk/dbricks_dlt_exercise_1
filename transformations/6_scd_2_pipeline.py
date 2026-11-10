import dlt
from pyspark.sql.functions import *

#Creating a staging Table - Reading data from source table
@dlt.table(
    name = "scd2_stg"
)
def scd2_stg(): 
    df = spark.readStream.table("dbricks_bootcamp.bronze.source")
    return df

#Create an empty streaming table 
dlt.create_streaming_table(
    name = "scd2_table"
)

#Create a CDC flow
dlt.create_auto_cdc_flow(
    source = "scd2_stg", 
    target = "scd2_table", 
    keys = ["product_id"], 
    sequence_by = col("processDate"), 
    stored_as_scd_type = 2, 
    except_column_list=['processDate']
)


