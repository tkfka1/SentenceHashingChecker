#!/bin/bash

# Spark의 경로가 PATH에 포함되어 있지 않다면 아래 줄의 경로를 알맞게 수정하세요.
SPARK_HOME="/path/to/your/spark/directory"

# 스크립트 실행
$SPARK_HOME/bin/spark-submit sentence_spark_find_duplicates.py