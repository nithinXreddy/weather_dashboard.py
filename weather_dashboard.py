import streamlit as st
import pandas as pd
import requests
import matplotlib.pyplot as plt
import seaborn as sns

# API Setup
API_KEY = "YOUR_API_KEY"
CITY = "Bangalore"
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(URL)
data = response.json()

# Extract data
weather_info = {
    "City": data["name"],
    "Temperature (°C)": data["main"]["temp"],
    "Humidity (%)": data["main"]["humidity"],
    "Pressure (hPa)": data["main"]["pressure"],
    "Wind Speed (m/s)": data["wind"]["speed"]
}

df = pd.DataFrame([weather_info])

# Streamlit UI
st.title("Weather Dashboard 🌤")
st.write(f"### Weather in {CITY}")
st.table(df)

# Visualization
st.write("### Weather Parameters")
fig, ax = plt.subplots()
sns.barplot(x=df.columns[1:], y=df.iloc[0, 1:], palette="coolwarm", ax=ax)
st.pyplot(fig)


# import requests
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# API_KEY = "YOUR_API_KEY"
# CITY = "Bangalore"
# URL = f"https://api.openweathermap.org/data/2.5/weather?q=bangalore&appid=2631fe899efced49d84f92c52d44cfd7&units=metric"

# response = requests.get(URL)
# data = response.json()

# # Extracting necessary details
# weather_info = {
#     "City": data["name"],
#     "Temperature (°C)": data["main"]["temp"],
#     "Humidity (%)": data["main"]["humidity"],
#     "Pressure (hPa)": data["main"]["pressure"],
#     "Wind Speed (m/s)": data["wind"]["speed"]
# }

# # Convert to Pandas DataFrame
# df = pd.DataFrame([weather_info])
# print(df)


# plt.figure(figsize=(8,5))
# sns.barplot(x=df.columns[1:], y=df.iloc[0, 1:], palette="coolwarm")
# plt.xlabel("Weather Parameters")
# plt.ylabel("Values")
# plt.title(f"Weather Conditions in {CITY}")
# plt.show()


# #an Interactive Dashboard
# import streamlit as st
# st.title("Weather Dashboard 🌤")
# st.write(f"### Weather in {CITY}")
# st.table(df)
# # Display chart
# st.bar_chart(df.iloc[:, 1:])

# website url- https://weather-dashboard-4jq5er3fldvbj3jbnxu79b.streamlit.app/