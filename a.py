import pandas as pd

url=r'https://www.worldometers.info/world-population/'

a=pd.read_html(url)

print(a)