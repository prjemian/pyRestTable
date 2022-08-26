#!/usr/bin/env python

import io
import lxml.etree
import pyRestTable
import urllib.request

# SVN_BASE_URL = "http://www.cansas.org/svn/1dwg/trunk"
CANSAS_URL = (
    "https://raw.githubusercontent.com/"
    "canSAS-org/1dwg/master/"
    "examples/cs_af1410.xml"
)


def main():
    nsmap = dict(cs="urn:cansas1d:1.1")

    r = urllib.request.urlopen(CANSAS_URL).read().decode("utf-8")
    doc = lxml.etree.parse(io.StringIO(r))

    node_list = doc.xpath("//cs:SASentry", namespaces=nsmap)
    t = pyRestTable.Table()
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


if __name__ == "__main__":
    table = main()
    # use "complex" since s_name might be empty string
    print(table.reST(fmt="complex"))
