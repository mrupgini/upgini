import numpy as np
import pandas as pd
import pytest

from upgini import Dataset, FileColumnMeaningType, FileMetrics


@pytest.fixture
def etalon():
    data = pd.DataFrame(
        [
            [2000000, 3, 0, 0.5],
            [2000000, 3, 0, 0.5],
            [2000000, 4, 1, None],
            [2000000, 5, None, 0.5],
            [2000000, 6, None, 0.5],
            [None, 7, 1, 0.5],
            ["", 8, 1, 0.5],
            [2000000, 9, np.Inf, 0.5],
            [2000000, 10, np.NaN, 0.5],
        ],
        columns=["timestamp", "msisdn", "target", "score"],
    )

    definition = {
        "msisdn": FileColumnMeaningType.MSISDN,
        "timestamp": FileColumnMeaningType.DATE,
        "target": FileColumnMeaningType.TARGET,
        "score": FileColumnMeaningType.SCORE,
    }
    search_keys = [("msisdn", "timestamp")]
    etalon = Dataset(
        name="test_etalon", description="test etalon", df=data, meaning_types=definition, search_keys=search_keys
    )
    return etalon


@pytest.fixture
def expected_binary_etalon_metadata():
    metadata = {
        "task_type": "BINARY",
        "label": "auc",
        "count": 15555,
        "valid_count": 15555,
        "valid_rate": 100.0,
        "avg_target": 0.5014464802314368,
        "cuts": [
            1541017353600.0,
            1543204800000.0,
            1545379200000.0,
            1547553600000.0,
            1549728000000.0,
            1551902400000.0,
            1554076800000.0,
        ],
        "interval": [
            {"date_cut": 1542111076799.0, "count": 2998.0, "valid_count": 2998.0, "avg_target": 0.5},
            {"date_cut": 1544292000000.0, "count": 3000.0, "valid_count": 3000.0, "avg_target": 0.5},
            {"date_cut": 1546466400000.0, "count": 2996.0, "valid_count": 2996.0, "avg_target": 0.49966622162883845},
            {"date_cut": 1548640800000.0, "count": 1791.0, "valid_count": 1791.0, "avg_target": 0.5147962032384142},
            {"date_cut": 1550815200000.0, "count": 1770.0, "valid_count": 1770.0, "avg_target": 0.49830508474576274},
            {"date_cut": 1552989600000.0, "count": 3000.0, "valid_count": 3000.0, "avg_target": 0.5},
        ],
    }
    return FileMetrics.parse_obj(metadata)
