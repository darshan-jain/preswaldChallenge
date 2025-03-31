from preswald import text, plotly, connect, get_df, table,query
import pandas as pd
import plotly.express as px


text("Darshan Manoj - Online Challenge")

# Load the CSV
connect() # load in all sources, which by default is the sample_csv
df = get_df("sample_csv") #tried with dataset.csv which is a dataset regarding chennai rainfalls, but it doesn't seem to work in this online IDE.

text("Full Dataset")
table(df)

sql = "SELECT * FROM sample_csv WHERE value > 50"
filtered_df = query(sql,"sample_csv")
text("Filtered Dataset where value is Greater than 50.")
table(filtered_df)

#interactive UI - There seems to be some error with respect to view (from preswald import view) since my deployment and preview fails.
# threshold = slider("Threshold",min_val = 0 , max_val = 100, default=50)
# table(df[df["value"]> threshold], title = "Dynamic Data View")


# Graphs and Charts 
text("Scatter Plot")
fig = px.scatter(df,x="quantity",y="value",color = "item")
plotly(fig)

