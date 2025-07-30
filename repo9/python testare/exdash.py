from os import waitstatus_to_exitcode

import pandas as pd
import plotly
import plotly.express as px
import plotly.io as pio

colors = [
    '#ff0000',  # roșu intens
    '#e60019',
    '#cc0033',
    '#b3004d',
    '#990066',
    '#800080',
    '#660099',
    '#4d00b3',
    '#3300cc',
    '#1900e6',
]

data ={ 'Language': ['English', 'Mandarin', 'Hindi', 'Spanish', 'French', 'Arabic', 'Bengali', 'Russian', 'Portuguese', 'Others'],
  'Speakers (millions)': [1500, 1117, 615, 534, 280, 274, 273, 258, 234, 1000],
  'Region/Countries': [ 'Worldwide', 'China, Taiwan, Singapore', 'India, Nepal, Fiji', 'Spain, Latin America', 'France, Canada, Africa', 'Middle East, North Africa', 'Bangladesh, India', 'Russia, Eastern Europe', 'Brazil, Portugal, Africa', 'Various' ],
  'Dialects': [160, 10, 50, 20, 30, 25, 12, 15, 21, 100] }
#
datad=pd.DataFrame(data)
# data2=datad.sort_values['Speakers (millions)']
# for data2 in range(5):
#     datafin=data2

datafin=datad.head(5)

#antrenare date

print(data)

# pie_chart=px.pie(
#     data_frame=datafin,
#     values='Speakers (millions)',
#     names='Language',
#     hover_name='Region/Countries',
#     hover_data=['Region/Countries','Dialects'],
#    # color_discrete_sequence=['#FFA500','blue','purple','yellow','pink','brown'],
#     color_discrete_sequence=colors,
#     labels='Language',
#     title='Language spoken around the Globe',
#     template='presentation'
# )
# pie_chart.update_traces(textposition='inside',textinfo='percent+label',
#                         hovertemplate="<b>%{label}</b><br>Speakers: %{value}M<br>Region: %{customdata[0][0]}<br>Dialects: %{customdata[0][1]}",
#                         pull=[0,0,0,0.2,0,0,0.4,0,0,0])
#
# pie_chart.show()

pie_chart=px.pie(
     data_frame=datafin,
    values='Speakers (millions)',
     names='Language',
     hover_name='Region/Countries',
     hover_data=['Region/Countries','Dialects'],
    # color_discrete_sequence=['#FFA500','blue','purple','yellow','pink','brown'],
     color_discrete_sequence=colors,
     labels='Language',
     title='Language spoken around the Globe',
     template='presentation'
 )
pie_chart.update_traces(textposition='inside',textinfo='percent+label',
                         hovertemplate="<b>%{label}</b><br>Speakers: %{value}M<br>Region: %{customdata[0][0]}<br>Dialects: %{customdata[0][1]}",
                         pull=[0,0,0,0.2,0,0,0.4,0,0,0])

pie_chart.show()