import pytest

from ..rest_table import Table
from ..rest_table import kv_table


def test_dict_to_table():
    dd = {"a": [1, 2, 3], "b": [-1, 0, 1], "c": [], "d": ["one", "two"]}
    table = Table(dd)
    assert len(table.labels) == len(dd)
    nrows = max([len(v) for v in dd.values()])
    assert len(table.rows) == nrows

    table.dict_to_table(dd)  # append rows to the table
    assert len(table.labels) == len(dd)
    assert len(table.rows) == 2 * nrows

    dd["extra"] = ["another thing"]
    with pytest.raises(KeyError) as exinfo:
        table.dict_to_table(dd)
    assert "New dictionary keys do not match" in str(exinfo.value)


def test_kv_table():
    table = kv_table({"a": 1, "b": "bb"})

    assert table.labels == ["key", "value"]
    assert table.rows == [["a", 1], ["b", "bb"]]
    assert table.reST() == "=== =====\nkey value\n=== =====\na   1    \nb   bb   \n=== =====\n"


def test_kv_table_custom_labels():
    table = kv_table({"a": 1}, key_label="name", value_label="data")

    assert table.labels == ["name", "data"]
    assert table.rows == [["a", 1]]


def test_kv_table_empty_dict():
    table = kv_table({})

    assert table.labels == ["key", "value"]
    assert table.rows == []
    assert table.reST() == "=== =====\nkey value\n=== =====\n=== =====\n"
