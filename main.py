# Import functions
import pandas as pd
import heatmap as hm

# Read excel data
data=pd.read_excel("earthquake_data.xlsx")

# Function call to create and save the heatmap
hm.heatmap(data)
