import dlt

#Create a Streaming Table 
@dlt.table(
    name = "demo_stream_table"
)
def demo_stream_table(): 
    df = spark.readStream.table("dbricks_bootcamp.silver.sales_enr")
    return df
              
#Create Materialized View 
@dlt.table(
    name = 'demo_mat_view'
)
def demo_mat_view():
    df = spark.read.table("dbricks_bootcamp.silver.sales_enr")
    return df

#Create Temporary View (Batch) 
@dlt.view(
    name = 'demo_temp_view'
)
def demo_temp_view():
    df = spark.read.table("dbricks_bootcamp.silver.sales_enr")
    return df

#Creating Stream View 
@dlt.view(
    name = 'demo_stream_view'
)
def demo_stream_view():
    df = spark.readStream.table("dbricks_bootcamp.silver.sales_enr")
    return df

