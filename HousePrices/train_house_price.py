import numpy as np
import pandas as pd

import os
# 파일 경로 설정
file_path = os.path.join('data', 'house_prices.csv')

# 파일 읽기
try:
    data = pd.read_csv(file_path)
    print("파일 로드 성공:", file_path)
except FileNotFoundError:
    print("파일을 찾을 수 없습니다:", file_path)
except Exception as e:
    print("파일 로드 중 오류 발생:", e)


