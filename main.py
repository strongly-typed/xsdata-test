from pathlib import Path

from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
config = ParserConfig(fail_on_unknown_properties=True)
parser = XmlParser(config=config)

from btlx import btlx_11

fname = 'whole-log-wall.btlx'

# Validate BTLx against XSD
validate = True
if validate:
    from lxml import etree
    from lxml import objectify
    xmlschema_doc = etree.parse('btlx_11.xsd')
    xmlschema = etree.XMLSchema(xmlschema_doc)

    tree = objectify.parse(fname)
    xmlschema.assertValid(tree)

# Use xsd
from btlx import btlx_11
fpath = Path(fname)
btlx = parser.from_path(fpath, btlx_11)

print(btlx.project.name)
