from ebay.product import findCompatibilitiesBySpecification, getProductCompatibilities

from ebay.utils import Specification, Value 

spec1 = Specification(propertyName="Offset")
spec1.values = [Value(text="45.0")]
spec2 = Specification(propertyName="Rim Width")
spec2.values = [Value(text="8.0")]
spec = [spec1, spec2]

print findCompatibilitiesBySpecification(specification=spec, categoryId="170577") 
#print getProductCompatibilities()

# print findProducts()
# print findProductsByCompatibility()
# print getProductDetails()