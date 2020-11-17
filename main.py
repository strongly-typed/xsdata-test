import requests
import traceback

from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
config = ParserConfig(fail_on_unknown_properties=True)
parser = XmlParser(config=config)

from lxml import etree
from lxml import objectify
xmlschema_doc = etree.parse('btlx_11.xsd')
xmlschema = etree.XMLSchema(xmlschema_doc)

from btlx.btlx_11 import Btlx

fname = 'btlx_filelist.txt'

with open(fname, 'r') as fd:
    for url in fd.readlines():
        try:
            if url.startswith('#'):
                continue
            
            url = url.strip()

            r = requests.get(url, allow_redirects=True)

            # Upgrade to BTLx 1.1
            btlx_str = r.text.replace('Version="1.0"', 'Version="1.1"')

            # Validate BTLx against XSD
            # fromstring complains when we have UTF declaration like
            # `<?xml version="1.0" encoding="utf-8" ?>`, so we use bytes instead
            # https://stackoverflow.com/a/38244227
            btlx_bytes = bytes(bytearray(btlx_str, encoding='utf-8'))
            
            tree = objectify.fromstring(btlx_bytes)
            xmlschema.assertValid(tree)

            # Use xsd
            btlx = parser.from_bytes(btlx_bytes, Btlx)

            print('✔️  {}'.format(url))
        except Exception as e:
            traceback.print_exc()
            print('❌  {}'.format(url))
