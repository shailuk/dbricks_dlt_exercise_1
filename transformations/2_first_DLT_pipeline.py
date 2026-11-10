import dlt 
from pyspark.sql.functions import *

#Create Streaming table - RAW
@dlt.table(
    name = 'sales_stg'
)
def sales_stg(): 
    df = spark.readStream.option("skipChangeCommits", True)\
              .table("dbricks_bootcamp.silver.sales_enr")
    return df

#Create Mat View - ENRICHED
@dlt.table(
    name  = 'sales_trn'
)
def sales_trn():
    df = spark.read.table("sales_stg")
    df = df.withColumn( "priceAfterDiscount", (col("total_amount") - col("discount")) )
    return df

#Create Mat View - CURATED
@dlt.table(
    name = 'sales_curated'
)
def ales_cur():
    df = spark.read.table("sales_trn")
    return df 

