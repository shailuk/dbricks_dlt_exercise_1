import dlt
from pyspark.sql.functions import lit

#Creating Streaming Table [Using AutoLoader]
@dlt.table(
    name = 'autovol_table'
)
def autovol_table():
    df = spark.readStream.format("cloudFiles")\
             .option("cloudFiles.format", "csv")\
             .load("/Volumes/dbricks_bootcamp/bronze/autovol/raw/")
    return df

#Creating treaming Table 
@dlt.table(
    name = 'autovol_table_enr'
)
def autoval_table_enr():
    df = spark.read.table("autovol_table")
    df = df.withColumn("flag", lit("Yes"))
    return df

