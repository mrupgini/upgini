import os

import pandas as pd
import pytest

from upgini import Dataset, FileColumnMeaningType

FIXTURE_DIR = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    "test_data/binary/",
)


@pytest.fixture
def etalon_definition():
    return {
        "phone_num": FileColumnMeaningType.MSISDN,
        "rep_date": FileColumnMeaningType.DATE,
        "target": FileColumnMeaningType.TARGET,
    }


@pytest.fixture
def etalon_search_keys():
    return [("phone_num", "rep_date")]


@pytest.mark.datafiles(os.path.join(FIXTURE_DIR, "data.csv.gz"))
def test_binary_dataset_pandas(datafiles, etalon_definition, etalon_search_keys, expected_binary_etalon_metadata):
    df = pd.read_csv(datafiles / "data.csv.gz")
    ds = Dataset(
        name="test Dataset",
        description="test",
        df=df,
        meaning_types=etalon_definition,
        search_keys=etalon_search_keys,
    )
    ds.validate()
    expected_valid_rows = 15555
    assert expected_valid_rows == ds["is_valid"].sum()
    binary_metadata = ds.calculate_metrics()
    assert expected_binary_etalon_metadata == binary_metadata


@pytest.mark.datafiles(os.path.join(FIXTURE_DIR, "data.csv"))
def test_binary_dataset_path(datafiles, etalon_definition, etalon_search_keys):
    path = datafiles / "data.csv"
    ds_path = Dataset(
        name="test Dataset",
        description="test",
        path=path,
        meaning_types=etalon_definition,
        search_keys=etalon_search_keys,
    )
    ds_path.validate()
    expected_valid_rows = 15555
    assert expected_valid_rows == ds_path["is_valid"].sum()
