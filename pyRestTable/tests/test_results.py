import io
import urllib.request

import lxml.etree
import pytest

from .. import Table
from ..rest_table import _prepare_results_
from ..rest_table import example_basic
from ..rest_table import example_minimal
from . import CANSAS_RESULT
from . import EXAMPLE_BASIC_RESULT
from . import EXAMPLE_COMPLICATED_RESULT
from . import EXAMPLE_MINIMAL_RESULT
from . import MINIMAL_GRID_RESULT
from . import MINIMAL_HTML_RESULT
from . import MINIMAL_LISTTABLE_RESULT
from . import MINIMAL_MARKDOWN_RESULT
from . import MINIMAL_SIMPLE_RESULT

CANSAS_URL = (
    "https://raw.githubusercontent.com/"
    "canSAS-org/1dwg/master/"
    "examples/cs_af1410.xml"
)


def cansas():
    nsmap = dict(cs="urn:cansas1d:1.1")

    r = urllib.request.urlopen(CANSAS_URL).read().decode("utf-8")
    doc = lxml.etree.parse(io.StringIO(r))

    node_list = doc.xpath("//cs:SASentry", namespaces=nsmap)
    t = Table()
    t.labels = ["SASentry", "description", "measurements"]
    for node in node_list:
        s_name, count = "", ""
        subnode = node.find("cs:Title", namespaces=nsmap)
        if subnode is not None:
            s = lxml.etree.tostring(subnode, method="text")
            s_name = node.attrib["name"]
            count = len(node.xpath("cs:SASdata", namespaces=nsmap))
        title = s.strip().decode()
        t.rows += [[s_name, title, count]]

    return t


# These tables are in the documentation.
complicated_labels = [
    "Name\nand\nAttributes",
    "Type",
    "Units",
    "Description\n(and Occurrences)",
]
complicated_rows = [
    ["one,\ntwo", "buckle my", "shoe.\n\n\nthree,\nfour", "..."],
    ["class", "NX_FLOAT", "", None],
    list(range(0, 4)),
    [None, {"a": 1, "b": "dreamy"}, 1.234, list(range(3))],
]
population_labels = ["City name", "Area", "Population", "Annual Rainfall"]
population_rows = [
    ["Adelaide", 1295, 1158259, 600.5],
    ["Brisbane", 5905, 1857594, 1146.4],
    ["Darwin", 112, 120900, 1714.7],
]
simple_labels = "one two three".split()
simple_rows = [[f"{r},{c}" for c in [1, 2, 3]] for r in [1, 2, 3, 4]]


@pytest.mark.parametrize(
    "fmt, labels, rows, longtable, alignment, expected",
    [
        [
            "simple",
            simple_labels,
            simple_rows,
            False,
            None,
            (
                "=== === =====\n"
                "one two three\n"
                "=== === =====\n"
                "1,1 1,2 1,3\n"
                "2,1 2,2 2,3\n"
                "3,1 3,2 3,3\n"
                "4,1 4,2 4,3\n"
                "=== === ====="
            ),
        ],
        [
            "plain",
            simple_labels,
            simple_rows,
            False,
            None,
            (
                "one two three\n"
                "1,1 1,2 1,3\n"
                "2,1 2,2 2,3\n"
                "3,1 3,2 3,3\n"
                "4,1 4,2 4,3"
            ),
        ],
        [
            "grid",
            simple_labels,
            simple_rows,
            False,
            None,
            (
                "+-----+-----+-------+\n"
                "| one | two | three |\n"
                "+=====+=====+=======+\n"
                "| 1,1 | 1,2 | 1,3   |\n"
                "+-----+-----+-------+\n"
                "| 2,1 | 2,2 | 2,3   |\n"
                "+-----+-----+-------+\n"
                "| 3,1 | 3,2 | 3,3   |\n"
                "+-----+-----+-------+\n"
                "| 4,1 | 4,2 | 4,3   |\n"
                "+-----+-----+-------+"
            ),
        ],
        [
            "markdown",
            simple_labels,
            simple_rows,
            False,
            None,
            (
                "| one | two | three |\n"
                "| --- | --- | ----- |\n"
                "| 1,1 | 1,2 | 1,3   |\n"
                "| 2,1 | 2,2 | 2,3   |\n"
                "| 3,1 | 3,2 | 3,3   |\n"
                "| 4,1 | 4,2 | 4,3   |"
            ),
        ],
        [
            "list-table",
            simple_labels,
            simple_rows,
            False,
            None,
            (
                ".. list-table::\n"
                "   :header-rows: 1\n"
                "   :widths: 3 3 5\n"
                "\n"
                "   * - one\n"
                "     - two\n"
                "     - three\n"
                "   * - 1,1\n"
                "     - 1,2\n"
                "     - 1,3\n"
                "   * - 2,1\n"
                "     - 2,2\n"
                "     - 2,3\n"
                "   * - 3,1\n"
                "     - 3,2\n"
                "     - 3,3\n"
                "   * - 4,1\n"
                "     - 4,2\n"
                "     - 4,3\n"
            ),
        ],
        [
            "html",
            simple_labels,
            simple_rows,
            False,
            None,
            (
                "<table>\n"
                "  <tr>\n"
                "    <th>one</th>\n"
                "    <th>two</th>\n"
                "    <th>three</th>\n"
                "  </tr>\n"
                "  <tr>\n"
                "    <td>1,1</td>\n"
                "    <td>1,2</td>\n"
                "    <td>1,3</td>\n"
                "  </tr>\n"
                "  <tr>\n"
                "    <td>2,1</td>\n"
                "    <td>2,2</td>\n"
                "    <td>2,3</td>\n"
                "  </tr>\n"
                "  <tr>\n"
                "    <td>3,1</td>\n"
                "    <td>3,2</td>\n"
                "    <td>3,3</td>\n"
                "  </tr>\n"
                "  <tr>\n"
                "    <td>4,1</td>\n"
                "    <td>4,2</td>\n"
                "    <td>4,3</td>\n"
                "  </tr>\n"
                "</table>\n"
            ),
        ],
        [
            "simple",
            population_labels,
            population_rows,
            False,
            None,
            (
                "========= ==== ========== ===============\n"
                "City name Area Population Annual Rainfall\n"
                "========= ==== ========== ===============\n"
                "Adelaide  1295 1158259    600.5          \n"
                "Brisbane  5905 1857594    1146.4         \n"
                "Darwin    112  120900     1714.7         \n"
                "========= ==== ========== ===============\n"
            ),
        ],
        [
            "plain",
            population_labels,
            population_rows,
            False,
            None,
            (
                "City name Area Population Annual Rainfall\n"
                "Adelaide  1295 1158259    600.5          \n"
                "Brisbane  5905 1857594    1146.4         \n"
                "Darwin    112  120900     1714.7         \n"
            ),
        ],
        [
            "grid",
            population_labels,
            population_rows,
            False,
            None,
            (
                "+-----------+------+------------+-----------------+\n"
                "| City name | Area | Population | Annual Rainfall |\n"
                "+===========+======+============+=================+\n"
                "| Adelaide  | 1295 | 1158259    | 600.5           |\n"
                "+-----------+------+------------+-----------------+\n"
                "| Brisbane  | 5905 | 1857594    | 1146.4          |\n"
                "+-----------+------+------------+-----------------+\n"
                "| Darwin    | 112  | 120900     | 1714.7          |\n"
                "+-----------+------+------------+-----------------+\n"
            ),
        ],
        [
            "simple",
            complicated_labels,
            complicated_rows,
            True,
            None,
            (
                # ".. tabularcolumns:: |l|L|c|r|\n"
                # "    :longtable:\n"
                # "\n"
                "========== ======================= ====== =================\n"
                "Name       Type                    Units  Description      \n"
                "and                                       (and Occurrences)\n"
                "Attributes                                                 \n"
                "========== ======================= ====== =================\n"
                "one,       buckle my               shoe.  ...              \n"
                "two                                                        \n"
                "                                                           \n"
                "                                   three,                  \n"
                "                                   four                    \n"
                "class      NX_FLOAT                       None             \n"
                "0          1                       2      3                \n"
                "None       {'a': 1, 'b': 'dreamy'} 1.234  [0, 1, 2]        \n"
                "========== ======================= ====== ================="
            ),
        ],
        [
            "grid",
            complicated_labels,
            complicated_rows,
            True,
            None,
            (
                "+------------+-------------------------+--------+-------------------+\n"
                "| Name       | Type                    | Units  | Description       |\n"
                "| and        |                         |        | (and Occurrences) |\n"
                "| Attributes |                         |        |                   |\n"
                "+============+=========================+========+===================+\n"
                "| one,       | buckle my               | shoe.  | ...               |\n"
                "| two        |                         |        |                   |\n"
                "|            |                         |        |                   |\n"
                "|            |                         | three, |                   |\n"
                "|            |                         | four   |                   |\n"
                "+------------+-------------------------+--------+-------------------+\n"
                "| class      | NX_FLOAT                |        | None              |\n"
                "+------------+-------------------------+--------+-------------------+\n"
                "| 0          | 1                       | 2      | 3                 |\n"
                "+------------+-------------------------+--------+-------------------+\n"
                "| None       | {'a': 1, 'b': 'dreamy'} | 1.234  | [0, 1, 2]         |\n"
                "+------------+-------------------------+--------+-------------------+"
            ),
        ],
        [
            "list-table",
            complicated_labels,
            complicated_rows,
            True,
            None,
            (
                ".. list-table::\n"
                "   :header-rows: 1\n"
                "   :widths: 10 23 6 17\n"
                "\n"
                "   * - Name\n"
                "       and\n"
                "       Attributes\n"
                "     - Type\n"
                "     - Units\n"
                "     - Description\n"
                "       (and Occurrences)\n"
                "   * - one,\n"
                "       two\n"
                "     - buckle my\n"
                "     - shoe.\n"
                "\n"
                "\n"
                "       three,\n"
                "       four\n"
                "     - ...\n"
                "   * - class\n"
                "     - NX_FLOAT\n"
                "     -\n"
                "     -\n"
                "   * - 0\n"
                "     - 1\n"
                "     - 2\n"
                "     - 3\n"
                "   * - None\n"
                "     - {'a': 1, 'b': 'dreamy'}\n"
                "     - 1.234\n"
                "     - [0, 1, 2]"
            ),
        ],
    ],
)
def test_parametrized(fmt, labels, rows, longtable, alignment, expected):
    assert isinstance(longtable, bool)

    t = Table()
    t.labels = labels
    for row in rows:
        assert len(row) == len(labels)
        t.addRow(row)
    t.setLongtable(longtable)
    if alignment is not None:
        t.setTabularColumns(state=True, column_spec=alignment)
    s = t.reST(fmt=fmt)
    assert len(s.strip().splitlines()) == len(expected.splitlines())
    for r, e in zip(s.strip().splitlines(), expected.splitlines()):
        assert r.rstrip() == e.rstrip(), f"{r=!r}, {e=!r}"


@pytest.mark.parametrize(
    "source, reference_text, style",
    [
        [example_minimal, MINIMAL_SIMPLE_RESULT, None],
        [example_minimal, MINIMAL_GRID_RESULT, "complex"],
        [example_minimal, MINIMAL_GRID_RESULT, "grid"],
        [example_minimal, MINIMAL_MARKDOWN_RESULT, "markdown"],
        [example_minimal, MINIMAL_HTML_RESULT, "html"],
        [example_minimal, MINIMAL_MARKDOWN_RESULT, "md"],
        [example_minimal, MINIMAL_LISTTABLE_RESULT, "list-table"],
        [cansas, CANSAS_RESULT, "complex"],
    ],
)
def test_variations_example_minimal(source, reference_text, style):
    table = source()
    text = table.reST(fmt=style)
    assert text == reference_text
    assert text.strip() == reference_text.strip()


def test_example_basic():
    results = _prepare_results_(example_basic()).strip().splitlines()
    expected = EXAMPLE_BASIC_RESULT.strip().splitlines()
    for r, e in zip(results, expected):
        assert r == e, r


def test_example_complicated():
    from ..rest_table import example_complicated

    t = example_complicated()
    s = t.reST(fmt="grid").strip()
    if s != EXAMPLE_COMPLICATED_RESULT:
        print("")
        print(f"expected: {len(EXAMPLE_COMPLICATED_RESULT)}")
        print(EXAMPLE_COMPLICATED_RESULT)
        print("")
        print(f"received: {len(s)}")
        print(s)
    assert s == EXAMPLE_COMPLICATED_RESULT


def test_example_minimal():
    results = _prepare_results_(example_minimal())
    assert results == EXAMPLE_MINIMAL_RESULT


def test_zero_width_column():
    t = Table()
    # fmt: off
    t.labels = ("", "two")
    t.rows.append(["", "1,2"])
    t.rows.append(["", "2,2"])
    # fmt: on
    s = t.reST(fmt="simple")
    expected = " ===\n"
    expected += " two\n"
    expected += " ===\n"
    expected += " 1,2\n"
    expected += " 2,2\n"
    expected += " ===\n"
    assert s == expected


def test_zero_columns():
    t = Table()
    t.labels = ()
    t.rows.append([])
    t.rows.append([])
    s = t.reST(fmt="simple")
    expected = "\n\n\n"
    assert s == expected


def test_num_col_labels_different_from_col_width_specifiers():
    # Number of column labels is different from column width specifiers
    t = Table()
    t.use_tabular_columns = True
    t.alignment = "lll"
    t.longtable = True
    t.labels = ("one", "two")
    t.rows.append(["1,1", "1,2"])
    t.rows.append(["2,1", "2,2"])
    with pytest.raises(IndexError):
        t.reST(fmt="list-table")

    # now fix and proceed
    t.alignment = "ll"
    s = t.reST(fmt="list-table")
    expected = ""
    expected += ".. list-table::\n"
    expected += "   :header-rows: 1\n"
    expected += "   :widths: 3 3\n"
    expected += "\n"
    expected += "   * - one\n"
    expected += "     - two\n"
    expected += "   * - 1,1\n"
    expected += "     - 1,2\n"
    expected += "   * - 2,1\n"
    expected += "     - 2,2"
    assert s == expected


def test_default_str():
    t = example_minimal()
    s = str(t)
    assert s == MINIMAL_SIMPLE_RESULT, "string representation"


def test_issue_31():
    table = Table()
    table.labels = ["h", "k", "l", "mu", "omega", "chi", "phi", "gamma", "delta"]
    table.addRow(
        [
            0,
            1,
            1,
            0.0,
            3.4824458166048444,
            22.712897698011936,
            0.0,
            0.0,
            13.799774663132288,
        ]
    )
    table.addRow(
        [
            0.0,
            8.0,
            0.0,
            0.0,
            22.31594087562736,
            89.13769999977886,
            0.0,
            0.0,
            45.158571742842376,
        ]
    )
    table.addRow(
        [
            0.0,
            12.0,
            1.0,
            0.0,
            34.963469180020944,
            78.33265876350477,
            0.0,
            0.0,
            71.80070421791422,
        ]
    )

    result = str(table).splitlines()

    assert len(result) == 7
    columns = result[0].split()
    assert len(columns) == 9

    # this was the first problem in issue #31
    assert columns[0] == "===", "width of h column should be three"

    expected = [
        "=== ==== === === ================== ================== === ===== ==================",
        "h   k    l   mu  omega              chi                phi gamma delta             ",
        "=== ==== === === ================== ================== === ===== ==================",
        "0   1    1   0.0 3.4824458166048444 22.712897698011936 0.0 0.0   13.799774663132288",
        "0.0 8.0  0.0 0.0 22.31594087562736  89.13769999977886  0.0 0.0   45.158571742842376",
        "0.0 12.0 1.0 0.0 34.963469180020944 78.33265876350477  0.0 0.0   71.80070421791422 ",
        "=== ==== === === ================== ================== === ===== ==================",
    ]

    # check the column labels are identical
    for s, e in zip(result[1].split(), expected[1].split()):
        assert s == e, s

    # floating point numbers might be truncated but otherwise OK
    # check that values match to roundoff precision
    digits = 9
    for row in (3, 4, 5):
        for s, e in zip(result[row].split(), expected[row].split()):
            assert round(float(s), digits) == round(float(e), digits)
