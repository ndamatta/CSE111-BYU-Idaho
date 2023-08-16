import pytest
import pandas as pd
from table_from_csv import *

FILENAME = "car_financing.csv"
DATAFRAME =  creates_dataframe(FILENAME)
COLUMNS = tuple(DATAFRAME.columns)

def test_creates_dataframe():
    df = creates_dataframe(FILENAME)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(df, pd.DataFrame)

def test_select_column():
    df = creates_dataframe(FILENAME)
    assert COLUMNS in DATAFRAME
    assert COLUMNS in DATAFRAME


pytest.main(["-v", "--tb=line", "-rN", __file__])