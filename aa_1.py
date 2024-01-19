import streamlit as st

st.set_page_config(
    page_title="2018 Social Media Data",
    page_icon="👋",
)

import pandas as pd     #read from text file with comma as separator
# Data
import numpy as np
# Visualization
import matplotlib
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt  #'pyplot' module to customize plots
import seaborn as sns  #library of data visualization on top of Matplotlib for statistical graphics
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor, plot_tree
from sklearn.metrics import mean_squared_error, accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, r2_score    

# Custom CSS styling
custom_css = """
    body {
        background-color: #000000;  /* Black background color */
        font-family: 'Arial', sans-serif;  /* Set a preferred font */
        color: #ffffff;  /* Set text color to white for better visibility on black */
    }
    .stApp {
        max-width: 1200px;  /* Set a maximum width for the app */
        margin: 0 auto;
        padding: 20px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);  /* Add a subtle box shadow */
    }
    .stMarkdown {
        color: #ffffff;  /* Dark text color for section headers */
    }
    .stHeader {
        background-color: #3498db;  /* Header background color */
        color: #ffffff;  /* Header text color */
        padding: 10px;
        margin-bottom: 20px;
        border-radius: 5px;
    }
"""

# Apply custom CSS
st.markdown(f"<style>{custom_css}</style>", unsafe_allow_html=True)

df = pd.read_csv('https://raw.githubusercontent.com/r324rggf/streamlit-example/master/January%203-10%2C%202018%20-%20Core%20Trends%20Survey%20-%20CSV.csv', sep=",")
#To configure to display all columns in just one line.
#By default is true, it will display the dataset based on your screen size, if have many columns and it cannot fit into the screen, the columns will be display at the bottom.
pd.set_option('expand_frame_repr', False)
#To configure to display all the rows. By default, says if have 500 rows of data, it will show only the head & tail of the data
pd.set_option('display.max_rows', None)
#print only the top 5 rows

# Page title
st.title("Social Media Analysis - 2018")

# Section 1: Internet Usage Countplot
st.header("Internet Usage Count")
fig_internet, ax_internet = plt.subplots(figsize=(10, 5))
sns.countplot(x='eminuse', data=df, ax=ax_internet, palette='Blues')
plt.title('Internet Usage')
plt.xlabel('(1: Yes, 2: No)')
st.pyplot(fig_internet)

# Section 2: Social Media Usage Countplot
st.header("Social Media Usage Count")
fig_social_media, ax_social_media = plt.subplots(figsize=(10, 5))
sns.countplot(x='snsint2', data=df, ax=ax_social_media, palette='Greens')
plt.title('Social Media Usage')
plt.xlabel('(1: Yes, 2: No)')
st.pyplot(fig_social_media)

# Section 3: Cross-tabulation Heatmap
st.header("Cross-tabulation Heatmap")
cross_tab = pd.crosstab(df['eminuse'], df['snsint2'])
fig_cross_tab, ax_cross_tab = plt.subplots(figsize=(8, 6))
sns.heatmap(cross_tab, annot=True, fmt='d', cmap='YlGnBu', cbar=False, ax=ax_cross_tab)
plt.title('Cross-tabulation: Internet Usage vs Social Media Usage')
plt.xlabel('snsint2 (Social Media Usage)')
plt.ylabel('eminuse (Internet Usage)')
st.pyplot(fig_cross_tab)

# Section 4: Histogram of Age
st.header("Histogram of Social Media Users' Age")
fig_age, ax_age = plt.subplots(figsize=(10, 5))
sns.histplot(data=df, x='age', bins=15, kde=True, ax=ax_age, color=mcolors.TABLEAU_COLORS['tab:blue'])
plt.title("Age of Social Media Users")
plt.xlabel("Age")
plt.ylabel("Frequency")
st.pyplot(fig_age)



df = pd.read_csv('https://raw.githubusercontent.com/r324rggf/streamlit-example/master/2021aa2.csv', sep=",")
#To configure to display all columns in just one line.
#By default is true, it will display the dataset based on your screen size, if have many columns and it cannot fit into the screen, the columns will be display at the bottom.
pd.set_option('expand_frame_repr', False)
#To configure to display all the rows. By default, says if have 500 rows of data, it will show only the head & tail of the data
pd.set_option('display.max_rows', None)
#print only the top 5 rows

# Page title
st.title("Social Media Analysis - 2021")

# Section 1: Internet Usage Countplot
st.header("Internet Usage Count")
fig_internet, ax_internet = plt.subplots(figsize=(10, 5))
sns.countplot(x='eminuse', data=df, ax=ax_internet, palette='Blues')
plt.title('Internet Usage')
plt.xlabel('(1: Yes, 2: No)')
st.pyplot(fig_internet)

# Section 2: Social Media Usage Countplot
st.header("Social Media Usage Count")
fig_social_media, ax_social_media = plt.subplots(figsize=(10, 5))
sns.countplot(x='snsint2', data=df, ax=ax_social_media, palette='Greens')
plt.title('Social Media Usage')
plt.xlabel('(1: Yes, 2: No)')
st.pyplot(fig_social_media)

# Section 3: Cross-tabulation Heatmap
st.header("Cross-tabulation Heatmap")
cross_tab = pd.crosstab(df['eminuse'], df['snsint2'])
fig_cross_tab, ax_cross_tab = plt.subplots(figsize=(8, 6))
sns.heatmap(cross_tab, annot=True, fmt='d', cmap='YlGnBu', cbar=False, ax=ax_cross_tab)
plt.title('Cross-tabulation: Internet Usage vs Social Media Usage')
plt.xlabel('snsint2 (Social Media Usage)')
plt.ylabel('eminuse (Internet Usage)')
st.pyplot(fig_cross_tab)

# Section 4: Histogram of Age
st.header("Histogram of Social Media Users' Age")
fig_age, ax_age = plt.subplots(figsize=(10, 5))
sns.histplot(data=df, x='age', bins=15, kde=True, ax=ax_age, color=mcolors.TABLEAU_COLORS['tab:orange'])
plt.title("Age of Social Media Users")
plt.xlabel("Age")
plt.ylabel("Frequency")
st.pyplot(fig_age)





































df = pd.read_csv('https://raw.githubusercontent.com/r324rggf/streamlit-example/master/2021aa2.csv', sep=",")
#To configure to display all columns in just one line.
#By default is true, it will display the dataset based on your screen size, if have many columns and it cannot fit into the screen, the columns will be display at the bottom.
pd.set_option('expand_frame_repr', False)
#To configure to display all the rows. By default, says if have 500 rows of data, it will show only the head & tail of the data
pd.set_option('display.max_rows', None)
#print only the top 5 rows

# Page title
st.title("Social Media Analysis - 2021")

# Section 1: Internet Usage Countplot
st.header("Internet Usage Count")
fig_internet, ax_internet = plt.subplots(figsize=(10, 5))
sns.countplot(x='eminuse', data=df, ax=ax_internet, palette='Blues')
plt.title('Internet Usage')
plt.xlabel('(1: Yes, 2: No)')
st.pyplot(fig_internet)

# Section 2: Social Media Usage Countplot
st.header("Social Media Usage Count")
fig_social_media, ax_social_media = plt.subplots(figsize=(10, 5))
sns.countplot(x='snsint2', data=df, ax=ax_social_media, palette='Greens')
plt.title('Social Media Usage')
plt.xlabel('(1: Yes, 2: No)')
st.pyplot(fig_social_media)

# Section 3: Cross-tabulation Heatmap
st.header("Cross-tabulation Heatmap")
cross_tab = pd.crosstab(df['eminuse'], df['snsint2'])
fig_cross_tab, ax_cross_tab = plt.subplots(figsize=(8, 6))
sns.heatmap(cross_tab, annot=True, fmt='d', cmap='YlGnBu', cbar=False, ax=ax_cross_tab)
plt.title('Cross-tabulation: Internet Usage vs Social Media Usage')
plt.xlabel('snsint2 (Social Media Usage)')
plt.ylabel('eminuse (Internet Usage)')
st.pyplot(fig_cross_tab)

# Section 4: Histogram of Age
st.header("Histogram of Social Media Users' Age")
fig_age, ax_age = plt.subplots(figsize=(10, 5))
sns.histplot(data=df, x='age', bins=15, kde=True, ax=ax_age, color=mcolors.TABLEAU_COLORS['tab:orange'])
plt.title("Age of Social Media Users")
plt.xlabel("Age")
plt.ylabel("Frequency")
st.pyplot(fig_age)
