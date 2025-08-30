import pandas as pd
url = "https://github.com/alixagari2000-star/myRawData/raw/refs/heads/main/titanic3.xls"
raw = pd.read_excel(url)
raw
