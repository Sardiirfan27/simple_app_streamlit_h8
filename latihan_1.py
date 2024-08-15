import streamlit as st
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import time

st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

st.title('ML App')
'''
# Machine Learning Project

Aplikasi ini adalah untuk memperediksi harga rumah.
- Data Loading
- EDA
- Preprocessing & Feature Engineering
- Model ML
'''
st.markdown('# Machine Learning Project')

st.write('hello')

df= pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})
st.write(df)

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.write(chart_data)
st.line_chart(chart_data)

# make data
x = np.arange(0, 10, 2)
ay = [1, 1.25, 2, 2.75, 3]
by = [1, 1, 1, 1, 1]
cy = [2, 1, 2, 1, 2]
y = np.vstack([ay, by, cy])

# plot
fig, ax = plt.subplots()

ax.stackplot(x, y)

ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))

st.pyplot(fig)

option= st.sidebar.selectbox(
    'which number do you like best?',
    df['first column']
)

'You selected:', option
st.write('You selected:', option)

left_column, right_column = st.columns(2)
pressed = left_column.button('Press me?')
if pressed:
  right_column.write("Woohoo!")

expander = st.expander("FAQ")
expander.markdown(''' 
# syarat
Here you could put in some really, really long explanation''')


if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')

agree = st.checkbox('I agree')
if agree:
    st.write('Great!')

options= ('Comedy', 'Drama', 'Documentary')
genre = st.sidebar.radio(
    "What's your favorite movie genre",
    options)
if genre == 'Comedy':
    st.write('You selected comedy.')
elif genre=='Drama':
    st.write('You selected drama.')
else:
    st.write("You didn't select comedy.")
    
option = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))
st.write('You selected:', option)

options = st.multiselect(
    'Nama Kolom yang di pilih',
    ['nama', 'usia', 'pekerjaan'],
    ['nama', 'usia'])

values = st.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)

start_color, end_color = st.select_slider(
    'Select a range of color wavelength',
    options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'],
    value=('red', 'blue'))
st.write('You selected wavelengths between', start_color, 'and', end_color)

title = st.text_input('Movie title', 'Life of Brian')
st.write(title)

number = st.number_input('Insert a number')
st.write('The current number is ', number)

import datetime
d = st.date_input(
    "When's your birthday",
    datetime.date(2019, 7, 6))
st.write('Your birthday is:', d)

t = st.time_input('Set an alarm for', datetime.time(8, 45))
st.write('Alarm is set for', t)

df= pd.DataFrame(
    {'nama':['joko','jojon','irwan','tono'],
    'usia':[23,24,25,26],
    'pekerjaan':['guru','pilot','polisi','petani']})

st.dataframe(df[options])


uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, index_col=0)
    st.write(df)
    
@st.cache_data
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')
csv = convert_df(df)

col1, col2, col3 = st.columns(3)
with col1:
  st.header("A cat")
  st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
  st.header("A dog")
  st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
  st.header("An owl")
  st.image("https://static.streamlit.io/examples/owl.jpg")
  
col1, col2 = st.columns([3, 1])
data = np.random.randn(10, 1)

col1.subheader("A wide column with a chart")
col1.line_chart(data)

col2.subheader("A narrow column with the data")
col2.write(data)
  
st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='large_df.csv',
    mime='text/csv',
)