import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# Set page config
st.set_page_config(page_title="Community Projects Map", layout="wide",page_icon="🌍")

st.title("📍 Community Projects in Surigao City")

# Google Sheets CSV export URL (make sure the sheet is set to 'Anyone with the link can view')
sheet_url = "https://docs.google.com/spreadsheets/d/1m0ogJcjKHu3bl9dXjEjso0RzlaktAugi2HF7xSwMzrU/export?format=csv"

# Load data
@st.cache_data
def load_data(url):
    return pd.read_csv(url)

df = load_data(sheet_url)
df.index = df.index + 1  # Make index start at 1

# Display data table
with st.expander("📊 View Raw Data"):
    st.dataframe(df)

# Create Folium map
m = folium.Map(location=[9.789, 125.49], zoom_start=13)

# Add markers
for idx, row in df.iterrows():
    popup_content = f"""
    <b>Community:</b> {row['Community']}<br>
    <b>Year:</b> {row['Year']}<br>
    <b>Service:</b> {row['Service_Type']}<br>
    <b>Population:</b> {row['Population']}<br>
    <b>Description:</b> {row['Description']}
    """
    
    folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        popup=popup_content,
        icon=folium.DivIcon(html=f"""
            <div style='background-color:blue; color:white; border-radius:50%; width:28px; height:28px; text-align:center; line-height:28px; font-size:12pt'>
                {idx + 1}
            </div>
        """)
    ).add_to(m)


# Display map
st.subheader("🗺️ Map of Services")
st.markdown("Lhoreen's Community Map")
st_folium(m, width=1200, height=600)
