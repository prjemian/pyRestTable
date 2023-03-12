import pytest
from ..rest_table import Table


def test_dict_to_table():
    dd = dict(a=[1, 2, 3], b=[-1, 0, 1], c=[], d="one two".split())
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
