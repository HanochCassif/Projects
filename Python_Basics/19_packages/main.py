# A package is a folder containing __init__.py file  and then includes modules files
# User can Create it by right clicking on project name and then either 'Python Package'
# or create new folder and within this new folder create a new file names __init__.py
# in both cases python project will know to relate this folder as a package


# 1st method : import the whole module within a package then use its function
# import ecommerce.shipping
# print("import a module of a package then use it functions" )
# ecommerce.shipping.shipping()
# ecommerce.shipping.tax_calc()


# 2nd method - import functions from module
# print("import a specific functions from a  module of a package ")
# from ecommerce.shipping import shipping_calc, tax_calc
# shipping_calc()
# tax_calc()


# 3rd method - import the  module in a package in refer all functions of it with a '.'

print("import a module in a package and use its functions")
from ecommerce import shipping
shipping.shipping_calc()
shipping.tax_calc()
