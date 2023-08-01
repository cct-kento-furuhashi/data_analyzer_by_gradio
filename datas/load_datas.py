import tempfile
from typing import Optional

import pandas as pd


def load_csv(csv_file: tempfile._TemporaryFileWrapper) -> Optional[pd.DataFrame]:  # type: ignore
    """CSVファイルを読み込みDataFrameに変換する

    Args:
        csv_file (tempfile._TemporaryFileWrapper): 入力ファイル

    Returns:
        pd.DataFrame: DataFrame
    """
    if csv_file is None:
        return None
    df = pd.read_csv(csv_file.name)
    return df
