#!/usr/bin/env python

from lxml import etree
from pyRestTable import Table

xml_url = 'http://www.cansas.org/svn/1dwg/trunk/examples/cs_af1410.xml'
nsmap = dict(cs='urn:cansas1d:1.1')
doc = etree.parse(xml_url)
node_list = doc.xpath('//cs:SASentry', namespaces=nsmap)
t = Table()
t.labels = ['SASentry', 'description', 'measurements']
for node in node_list:
    subnode = node.find('cs:Title', namespaces=nsmap)
    if subnode is not None:
        s = etree.tostring(subnode, method="text")
        s_name = node.attrib['name']
        count = len(node.xpath('cs:SASdata', namespaces=nsmap))
    else:
        s_name = ''
        count = ''
    title = s.strip()
    t.rows += [[s_name, title, count]]

print len(node_list), 'SASentry elements in', xml_url
print
# use "complex" since s_name might be empty string
print t.reST(fmt='complex')
