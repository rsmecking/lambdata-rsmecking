


import pandas

from my_lambdata.my_mod import enlarge
from my_lambdata.my_mod import fib
from my_lambdata.my_mod import fib2
Sprint("HELLO WORLD")

df = pandas.DataFrame({"state": ["CT", "CO", "CA", "TX"]})
print (df.head())

print("-------------")


x = 5
print("NUMBER", x)
print("ENLARGED NUMBER", enlarge(x))