
Example using XML source data from a URL
########################################

Another example (*cansas.py* in the source distribution) shows how content can be 
scraped from a URL that provides XML (using the *lxml* package) and written as a
reST table.  This particular XML uses a namespace which we setup in the 
variable ``nsmap``::

   #!/usr/bin/env python
   
   from lxml import etree
   from pyRestTable import Table
   
   xml_url = 'http://www.cansas.org/svn/1dwg/trunk/examples/cs_af1410.xml'
   nsmap = dict(cs='urn:cansas1d:1.1')
   doc = etree.parse(xml_url)
   node_list = doc.xpath('//cs:SASentry', namespaces=nsmap)
   t = Table()
   t.labels = ['entry', 'description', 'measurements']
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

The output from this code::

   10 SASentry elements in http://www.cansas.org/svn/1dwg/trunk/examples/cs_af1410.xml
   
   +-----------+--------------------------------------+--------------+
   | entry     | description                          | measurements |
   +===========+======================================+==============+
   | AF1410:10 | AF1410-10 (AF1410 steel aged 10 h)   | 2            |
   +-----------+--------------------------------------+--------------+
   | AF1410:8h | AF1410-8h (AF1410 steel aged 8 h)    | 2            |
   +-----------+--------------------------------------+--------------+
   | AF1410:qu | AF1410-qu (AF1410 steel aged 0.25 h) | 2            |
   +-----------+--------------------------------------+--------------+
   | AF1410:cc | AF1410-cc (AF1410 steel aged 100 h)  | 2            |
   +-----------+--------------------------------------+--------------+
   | AF1410:2h | AF1410-2h (AF1410 steel aged 2 h)    | 2            |
   +-----------+--------------------------------------+--------------+
   | AF1410:50 | AF1410-50 (AF1410 steel aged 50 h)   | 2            |
   +-----------+--------------------------------------+--------------+
   | AF1410:20 | AF1410-20 (AF1410 steel aged 20 h)   | 1            |
   +-----------+--------------------------------------+--------------+
   | AF1410:5h | AF1410-5h (AF1410 steel aged 5 h)    | 2            |
   +-----------+--------------------------------------+--------------+
   | AF1410:1h | AF1410-1h (AF1410 steel aged 1 h)    | 2            |
   +-----------+--------------------------------------+--------------+
   | AF1410:hf | AF1410-hf (AF1410 steel aged 0.5 h)  | 2            |
   +-----------+--------------------------------------+--------------+

The resulting table is shown:

10 SASentry elements in http://www.cansas.org/svn/1dwg/trunk/examples/cs_af1410.xml

+-----------+--------------------------------------+--------------+
| entry     | description                          | measurements |
+===========+======================================+==============+
| AF1410:10 | AF1410-10 (AF1410 steel aged 10 h)   | 2            |
+-----------+--------------------------------------+--------------+
| AF1410:8h | AF1410-8h (AF1410 steel aged 8 h)    | 2            |
+-----------+--------------------------------------+--------------+
| AF1410:qu | AF1410-qu (AF1410 steel aged 0.25 h) | 2            |
+-----------+--------------------------------------+--------------+
| AF1410:cc | AF1410-cc (AF1410 steel aged 100 h)  | 2            |
+-----------+--------------------------------------+--------------+
| AF1410:2h | AF1410-2h (AF1410 steel aged 2 h)    | 2            |
+-----------+--------------------------------------+--------------+
| AF1410:50 | AF1410-50 (AF1410 steel aged 50 h)   | 2            |
+-----------+--------------------------------------+--------------+
| AF1410:20 | AF1410-20 (AF1410 steel aged 20 h)   | 1            |
+-----------+--------------------------------------+--------------+
| AF1410:5h | AF1410-5h (AF1410 steel aged 5 h)    | 2            |
+-----------+--------------------------------------+--------------+
| AF1410:1h | AF1410-1h (AF1410 steel aged 1 h)    | 2            |
+-----------+--------------------------------------+--------------+
| AF1410:hf | AF1410-hf (AF1410 steel aged 0.5 h)  | 2            |
+-----------+--------------------------------------+--------------+
