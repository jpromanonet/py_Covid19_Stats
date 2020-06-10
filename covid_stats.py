# To install before using this script

## python -m pip install COVID19py
## python -m pip install matplotlib

# Now we import the libraries

import COVID19py
import matplotlib.pyplot as mpl

# Declaring and assigning variables

covid19 = COVID19py.COVID19()
data = covid19.getAll(timelines=True)
virusdetails = dict(data["latest"])
names = list(virusdetails.keys())
values = list(virusdetails.values())