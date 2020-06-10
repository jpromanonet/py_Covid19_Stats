# To install before using this script

## python -m pip install COVID19py
## python -m pip install matplotlib

# Now we import the libraries

import COVID19Py
import matplotlib.pyplot as mpl

# Declaring and assigning variables

covid19 = COVID19Py.COVID19()
data = covid19.getAll(timelines=True)
virusdetails = dict(data["latest"])
names = list(virusdetails.keys())
values = list(virusdetails.values())

# Now we add the matplotlib magic!

mpl.bar(range(len(virusdetails)),values, tick_label = names)
mpl.show()

# Now we print the virus details
print(virusdetails)