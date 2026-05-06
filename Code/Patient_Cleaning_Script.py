from pyspark.sql.functions import col, trim, upper

df_clean = df \
    .filter(col("PatientID").isNotNull()) \
    .filter(col("Name").isNotNull()) \
    .filter(trim(col("Name")) != "") \
    .filter(col("Age").isNotNull()) \
    .filter(col("Age") > 0) \
    .filter(col("Cost").isNotNull()) \
    .filter(col("Cost") > 0) \
    .withColumn("Name", upper(trim(col("Name")))) \
    .fillna({"Disease": "Unknown"}) \
    .dropDuplicates(["PatientID"])

df_clean.show(20)
print("Raw count:", df.count())
print("Clean count:", df_clean.count())
