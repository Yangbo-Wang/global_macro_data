import requests
import pandas as pd
import os
from datetime import datetime

CSV_URL = "https://www.globalmacrodata.com/GMD.csv"

def get_data(cache=True, cache_dir="data/", filename=None):
    if cache:
        if not os.path.exists(cache_dir):
            os.makedirs(cache_dir)

        if filename is None:
            filename = "GMD_latest.csv"
        
        file_path = os.path.join(cache_dir, filename)

        # 如果本地已有缓存，直接读取
        if os.path.exists(file_path):
            print(f"📂 使用缓存数据: {file_path}")
            return pd.read_csv(file_path)

    # 下载数据
    print(f"🌍 正在从 {CSV_URL} 下载数据...")
    response = requests.get(CSV_URL)

    if response.status_code == 200:
        df = pd.read_csv(pd.compat.StringIO(response.text))  # 直接读取 CSV 内容
        if cache:
            df.to_csv(file_path, index=False)
            print(f"✅ 数据已缓存至: {file_path}")
        return df
    else:
        raise Exception(f"❌ 下载失败，HTTP 状态码: {response.status_code}")