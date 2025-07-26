import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

import streamlit.components.v1 as components

# Set page config
st.set_page_config(page_title="Community Projects Map", layout="wide", page_icon="🌍")

st.title("📍 Community Projects in Surigao City")

# Google Sheets CSV export URL (make sure the sheet is set to 'Anyone with the link can view')
sheet_url = "https://docs.google.com/spreadsheets/d/1m0ogJcjKHu3bl9dXjEjso0RzlaktAugi2HF7xSwMzrU/export?format=csv"

# Load data
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
    <b>No:</b> {idx}<br>
    <b>Community:</b> {row['Community']}<br>
    <b>Year:</b> {row['Year']}<br>
    <b>Service:</b> {row['Service_Type']}<br>
    <b>Population:</b> {row['Population']}<br>
    <b>Description:</b> {row['Description']}
    """
    folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        popup=popup_content,
        icon=folium.Icon(color="blue", icon="info-sign")
    ).add_to(m)

# Display map
st.subheader("🗺️ Map")
st.markdown("Lhoreen's Community Map")
st_folium(m, width=1200, height=600)

# Reduce vertical spacing
st.markdown("<div style='margin-top: -40px;'></div>", unsafe_allow_html=True)

# Comment section
st.subheader("💬 Leave a Comment")
components.iframe(
    "https://docs.google.com/forms/d/e/1FAIpQLScktoA93f0fXcwb9xZdqmVVQRtVTKdpUrUJqTyfI9F6GIorKg/viewform?embedded=true",
    width=640,
    height=509
)
