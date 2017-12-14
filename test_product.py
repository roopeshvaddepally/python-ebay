import unittest
from lxml import objectify

from ebay.product import *

categoryId = "170577"
#The Specification array of objects
spec1 = Specification(propertyName="Offset")
spec1.values = [Value(text="45.0")]
spec2 = Specification(propertyName="Rim Width")
spec2.values = [Value(text="8.0")]
spec = [spec1, spec2]



#The CompatibilityPropertyFilter array of objects
cpf1 = CompatibilityPropertyFilter(propertyName="Year")
cpf1.values = [Value(text="2006")]
cpf2 = CompatibilityPropertyFilter(propertyName="Make")
cpf2.values = [Value(text="Honda")]
cpf = [cpf1, cpf2]

dataSet = ["DisplayableProductDetails", "Searchable"]
datasetPropertyName = ["Make", "Model", "Year", "Trim", "Engine"]
exactMatch = "True"
paginationInput = {"entriesPerPage":"10", "totalPages":"10"}
sortOrder = [SortOrder(sortPriority="Sort1", order="Ascending", propertyName="Offset"), SortOrder(sortPriority="Sort2", order="Ascending", propertyName="Rim Width")]
encoding = "XML"


class TestProductApi(unittest.TestCase):
    def test_findCompatibilitiesBySpecification(self):
        result = findCompatibilitiesBySpecification(specification=spec, \
                                                    categoryId=categoryId, \
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

