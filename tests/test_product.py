import unittest
from lxml import objectify

from ebay.product import *

specification = ""
categoryId = ""
compatibilityPropertyFilter = ""
dataSet = ""
datasetPropertyName = ""
exactMatch = ""
paginationInput = ""
sortOrder = ""
encoding = "XML"

class TestProductApi(unittest.TestCase):
    def test_findCompatibilitiesBySpecification(self):
        result = findCompatibilitiesBySpecification(specification, \
                                                    categoryId, \
                                                    compatibilityPropertyFilter=None, \
                                                    dataSet=None, \
                                                    datasetPropertyName=None, \
                                                    exactMatch=None, \
                                                    paginationInput=None, \
                                                    sortOrder=None, \
                                                    encoding=encoding)
        root = objectify.fromstring(result)
        ack = root.ack.text
        self.assertEqual(ack, "Success")


if __name__ == '__main__':
    unittest.main()

