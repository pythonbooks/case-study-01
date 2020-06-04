
import requests
from bs4 import BeautifulSoup
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
import plotly.io as pio


DATA_URL = "https://simple.wikipedia.org/wiki/List_of_U.S._states_by_population"
html = requests.get(DATA_URL).text
soup = BeautifulSoup(html, "lxml")
my_table = soup.find("table",{"class":"wikitable sortable"})
my_trs = my_table.findAll("tr")
state_pop_list = []

for tr in my_trs[1:]:                          # skip the header row
    my_tds = tr.findAll("td")
    state = my_tds[2].text.strip()             # strip away the non-sense characters
    pop = my_tds[3].text.strip()
    state_pop = [state, pop]
    state_pop_list.append(state_pop)

df = pd.DataFrame(state_pop_list, columns=["State", "Population"])

df = df[:-5]
df["Population"] = df["Population"].apply(lambda pop: int(pop.replace(",","")))
df = df.sort_values(by=["Population"],ascending=False)

state_fips = pd.read_csv("states.txt", sep="\t", header=None)
state_fips.columns = ["State", "FIPS", "ST"]
df = pd.merge(df, state_fips, on="State", how="inner")
    
def get_bar():

    bar = px.bar(df, y="State", x="Population", orientation='h', height=800)

    bar.update_layout(
        title='US Population by States',
        yaxis=dict(
            tickangle=0,
            showticklabels=True,
            type='category',
           # title='Xaxis Name',
            tickmode='linear'
        )
    )

    return bar


def get_cmap():

    cmap = px.choropleth(df,  
                    locations='ST', 
                    color='Population',
                    color_continuous_scale="Viridis",
                    scope="usa",
                    hover_name="State",
                    locationmode = 'USA-states',
                    labels={'ST':'State'}
    )

    cmap.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

    return cmap
    
 

