import pandas as pd
import polars as pl
from timeit import timeit

pl_acc_data = pl.read_csv("Phones_accelerometer.csv")
pd_acc_data = pd.read_csv("Phones_accelerometer.csv")
## Pandas reading in data
timeit(
    setup= 'import pandas as pd',
    stmt= 'pd.read_csv("Phones_accelerometer.csv")',
    number=100
)
# number = 10 ---- 95.58104820799781
# number = 100 --- 1009.7089881249995


## Polars reading in data
timeit(
    setup= 'import polars as pl',
    stmt= 'pl.read_csv("Phones_accelerometer.csv")',
    number=100
)
# number = 10 ---- 37.052173083000525
# number = 100 --- 325.9771218329988

## Pandas, filtering 
pd_acc_data.groupby(["Device"])["Device"].count()

pl_acc_data.groupby(["Device"])["Device"].count()