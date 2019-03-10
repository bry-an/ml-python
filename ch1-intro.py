import pandas as pd
from IPython.display import display

#create simplle dataset of people

data = {'Name': ["Jeremy", "Caitlin", "Susan", "Bryan"], 'Location': ["St. Paul", "Madison", "Duluth", "Denver"], 'Age': [40, 38, 71, 34]}

data_pandas = pd.DataFrame(data)
# IPyton.display allows "pretty prining" of dataframes
print(display(data_pandas))