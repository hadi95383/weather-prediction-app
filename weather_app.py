import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
import os

# Load API key from environment variable (safer than hardcoding)
API_KEY = os.getenv("OPENWEATHER_API_KEY", "640c0e3522649003e29ef45734a1c3a0")  # Use env var or fallback

# Function to fetch weather data
def get_weather(city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",
    }
    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if data.get("cod") == 200:
            weather_desc = data["weather"][0]["description"]
            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            result = f"The weather in {city} is currently {weather_desc} with a temperature of {temp}°C and humidity of {humidity}%."

            # Store the city and temperature in session state
            if "weather_searches" not in st.session_state:
                st.session_state.weather_searches = []
            st.session_state.weather_searches.append({"City": city, "Temperature": temp, "Humidity": humidity})

            return result
        else:
            return f"Error: {data.get('message', 'Unknown error')}. Try again with a valid city name."
    except Exception as e:
        return f"Could not fetch weather details. Error: {e}"

# Streamlit App
def main():
    st.title("Weather Prediction App 🌦️")

    # Display a background image (alternative method)
    st.image("wolfgang-hasselmann-bR_-gllg7Bs-unsplash.jpg", use_container_width=True)

    city = st.text_input("Enter the city name:", placeholder="e.g., London")

    if st.button("Get Weather"):
        if city:
            st.write(f"Fetching weather for {city}...")
            st.write(get_weather(city))
        else:
            st.warning("Please enter a city name.")

    if st.button("Download Weather Data as CSV"):
        if "weather_searches" in st.session_state and st.session_state.weather_searches:
            df = pd.DataFrame(st.session_state.weather_searches)
            csv = df.to_csv(index=False, encoding="utf-8")
            st.download_button("Download CSV", csv, "weather_data.csv", "text/csv")
        else:
            st.warning("No weather data to download.")

    if st.button("Show Weather Graph"):
        if "weather_searches" in st.session_state and st.session_state.weather_searches:
            df = pd.DataFrame(st.session_state.weather_searches)
            avg_temp = df.groupby("City")["Temperature"].mean()

            fig, ax = plt.subplots(figsize=(8, 5))
            avg_temp.plot(kind="bar", color="skyblue", edgecolor="black", ax=ax)
            ax.set_title("Average Temperature by City", fontsize=14)
            ax.set_ylabel("Temperature (°C)", fontsize=12)
            ax.set_xlabel("City", fontsize=12)
            ax.tick_params(axis="x", rotation=45)
            ax.grid(axis="y", linestyle="--", alpha=0.7)

            st.pyplot(fig)
        else:
            st.warning("No weather data to display.")

# Corrected main block
if __name__== "_main_":
    main()