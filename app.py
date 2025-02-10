import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static

# Load the CSV file
csv_file = "addresses.csv"  # Ensure your file is in the same directory
df = pd.read_csv(csv_file)

# Create a base map centered around the average coordinates
map_center = [df["Latitude"].astype(float).mean(), df["Longitude"].astype(float).mean()]
m = folium.Map(location=map_center, zoom_start=10)

# Add markers for each address
for _, row in df.iterrows():
    folium.Marker(
        location=[float(row["Latitude"]), float(row["Longitude"])],
        popup=row["Address"],
        tooltip=row["Address"]
    ).add_to(m)

# Streamlit App
st.title("Interactive Lead Map")
st.write("This map displays all uploaded addresses.")

# Display the map
folium_static(m)





# txt_file = "ForDigitalOcean/Ravenswood.txt"

# csv_file = "ForDigitalOcean/addresses.csv"

# # Read the text file
# data = []
# with open(txt_file, "r", encoding="utf-8") as f:
#     for line in f:
#         parts = line.strip().split("|")  # Split the line by '|'
#         if len(parts) >= 6:  # Ensure it has the expected number of parts
#             address = parts[2]  # Address is the 3rd element
#             lat_lon = parts[4].split()  # Latitude and Longitude are the 5th element, split by space
#             if len(lat_lon) == 2:
#                 latitude, longitude = lat_lon[0], lat_lon[1]
#                 data.append([address, latitude, longitude])

# # Convert to a DataFrame
# df = pd.DataFrame(data, columns=["Address", "Latitude", "Longitude"])

# # Save to CSV
# df.to_csv(csv_file, index=False)

# print(f"Successfully saved {len(df)} addresses to {csv_file}")
