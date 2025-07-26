import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# Set page config with custom theme
st.set_page_config(page_title="Community Projects Map", layout="wide", page_icon="🌍")

# Title and description section
st.markdown("""
    <h1 style='text-align: center; color: #2c3e50;'>📍 Community Projects in Surigao City</h1>
    <p style='text-align: center; color: #7f8c8d; font-size: 18px;'>
        An interactive map for Surigao City(Eyyy).
    </p>
""", unsafe_allow_html=True)

# Google Sheets CSV export URL (make sure the sheet is set to 'Anyone with the link can view')
sheet_url = "https://docs.google.com/spreadsheets/d/1m0ogJcjKHu3bl9dXjEjso0RzlaktAugi2HF7xSwMzrU/export?format=csv"

# Load data
@st.cache_data
def load_data(url):
    return pd.read_csv(url)

df = load_data(sheet_url)

# Display data table
with st.expander("📊 Click to view full raw data", expanded=False):
    st.dataframe(df, use_container_width=True, height=350)

# Create Folium map
m = folium.Map(location=[9.789, 125.49], zoom_start=13)

# Add markers to map
for _, row in df.iterrows():
    popup_content = f"""
    <div style="font-size: 14px;">
        <b>Community:</b> {row['Community']}<br>
        <b>Year:</b> {row['Year']}<br>
        <b>Service:</b> {row['Service_Type']}<br>
        <b>Population:</b> {row['Population']}<br>
        <b>Description:</b> {row['Description']}
    </div>
    """
    folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        popup=popup_content,
        icon=folium.Icon(color="blue", icon="info-sign")
    ).add_to(m)

# Display map
st.subheader("🗺️ Interactive Map of Community Services")
st.markdown("<p style='color: #95a5a6;'>Zoom or click markers for more information.</p>", unsafe_allow_html=True)
st_folium(m, width=1200, height=600)
