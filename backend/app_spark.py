from pyspark.sql import SparkSession
from pyspark.sql.functions import current_timestamp
from pyspark.sql.functions import (
    col, rand, when, round as spark_round, expr
)

spark = SparkSession.builder \
    .appName("FraudDetectionMBA") \
    .getOrCreate()

print("Gerando transações mais realistas...")

df = (
    spark.range(0, 1000000)
    .withColumn("id_transacao", col("id").cast("string"))

    .withColumn(
        "valor",
        spark_round(
            when(rand() < 0.85, rand() * 300)
            .when(rand() < 0.97, rand() * 1000)
            .otherwise(rand() * 5000),
            2
        )
    )

    .withColumn("hora", (rand() * 24).cast("int"))
    .withColumn("tentativas", (rand() * 5).cast("int"))

    .withColumn(
        "pais",
        when(rand() < 0.1, "US")
        .when(rand() < 0.2, "GB")
        .when(rand() < 0.3, "FR")
        .when(rand() < 0.4, "DE")
        .when(rand() < 0.5, "IN")
        .when(rand() < 0.6, "CN")
        .when(rand() < 0.7, "JP")
        .when(rand() < 0.8, "CA")
        .when(rand() < 0.9, "AU")
        .otherwise("BR")
    )

    .withColumn(
        "device",
        when(rand() > 0.5, "mobile").otherwise("web")
    )

    .withColumn(
        "data_hora",
        expr("""
            current_timestamp()
            - (rand() * 30) * interval 1 day
            - (rand() * 24) * interval 1 hour
            - (rand() * 60) * interval 1 minute
            - (rand() * 60) * interval 1 second
        """)
    )
)

df_analisado = df.withColumn(
    "status",
    when(
        (col("valor") > 2000) &
        (col("pais") != "BR") &
        (col("tentativas") >= 3),
        "ALTA_SUSPEITA"
    )
    .when(
        (col("valor") > 800) &
        (col("hora") < 6) &
        (col("tentativas") >= 1),
        "MEDIA_SUSPEITA"
    )
    .otherwise("NORMAL")
)

fraudes = df_analisado.filter(
    (col("status") != "NORMAL") &
    (col("tentativas") > 0)
)

fraudes = fraudes.orderBy(col("valor").desc())

fraudes.write.mode("overwrite").json("output/fraudes")

print("Dataset gerado com sucesso!")