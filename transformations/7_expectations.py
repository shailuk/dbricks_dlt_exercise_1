import dlt

table_name = spark.conf.get("table_name")

expectations = {
    "rule1" : "product_id IS NOT NULL", 
    "rule2" : "category IS NOT NULL"
}

@dlt.table(
    name = 'expect_table'
)
@dlt.expect_all(expectations)
def expect_table(): 
    df = spark.read.table(f"dbricks_bootcamp.silver.{table_name}")
    return df
