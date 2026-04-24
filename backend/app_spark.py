from pyspark.sql import SparkSession
from pyspark.sql.functions import col, rand, when, round as spark_round # Import correto
import json

spark = SparkSession.builder \
    .appName("MBABigData") \
    .config("spark.driver.extraJavaOptions", "--add-exports=java.base/sun.nio.ch=ALL-UNNAMED --add-opens=java.base/java.lang=ALL-UNNAMED --add-opens=java.base/java.util=ALL-UNNAMED") \
    .getOrCreate()

print("Gerando 1.000.000 de transações...")

# Gerar Volume (1 Milhão de registros)
df = spark.range(0, 1000000) \
    .withColumn("valor", spark_round(rand() * 1000, 2)) \
    .withColumn("id_transacao", col("id").cast("string"))

# Lógica de Fraude
df_analisado = df.withColumn("status", 
    when(col("valor") > 950, "SUSPEITA").otherwise("NORMAL"))

# Filtrar para o Dashboard (Top 100)
fraudes = df_analisado.filter(col("status") == "SUSPEITA").limit(100).toPandas()

# 4. Salvar JSON
result = fraudes.to_dict(orient='records')
with open('data_results.json', 'w') as f:
    json.dump(result, f)

print("Backend Concluído: data_results.json gerado com sucesso!")