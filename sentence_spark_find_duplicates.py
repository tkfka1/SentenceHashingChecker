from pyspark.sql import SparkSession
from pyspark.sql.functions import sha2, col, count

def find_duplicates(spark, input_path):
    # 데이터 읽기 Spark DataFrame으로 로드
    df = spark.read.text(input_path)

    # 각 문장에 대한 SHA-256 해시값 계산
    df_with_hash = df.withColumn("hash_value", sha2(col("value"), 256))

    # 해시값을 기준으로 그룹화하고 중복 수 계산
    duplicates = (df_with_hash.groupBy("hash_value")
                 .agg(count("value").alias("count"))
                 .filter(col("count") > 1))

    # 결과 출력
    duplicates.show()

if __name__ == "__main__":
    # SparkSession 초기화
    spark = SparkSession.builder.appName("FindDuplicates").getOrCreate()

    # 입력 파일 경로
    input_path = "path_to_your_data.txt"

    find_duplicates(spark, input_path)

    spark.stop()
