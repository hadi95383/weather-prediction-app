Weather Prediction App
This is a Streamlit-based web application that allows users to fetch and visualize weather data for any city using the OpenWeatherMap API. The app provides real-time weather information, including temperature, humidity, and weather description. Users can also download the weather data as a CSV file and visualize the average temperature by city in a bar chart.

Features
Fetch Weather Data:

Enter a city name to get real-time weather information, including temperature, humidity, and weather description.

Download Weather Data:

Download the weather data for all searched cities as a CSV file.

Visualize Data:

View a bar chart showing the average temperature for all searched cities.

User-Friendly Interface:

Simple and intuitive design with a clean layout.

Prerequisites
Before running the app, ensure you have the following installed:

Python 3.7 or higher

Streamlit

Requests

Pandas

Matplotlib

Installation
Clone the repository or download the source code.

Install the required Python packages using pip:

bash
Copy
pip install streamlit requests pandas matplotlib
Obtain an API key from OpenWeatherMap. Replace the placeholder "your_api_key_here" in the code with your actual API key.

Usage
Run the Streamlit app:

bash
Copy
streamlit run weather_app.py
Open the provided URL in your web browser to access the app.

Enter a city name in the input field and click "Get Weather" to fetch the weather data.

Use the "Download Weather Data as CSV" button to download the weather data for all searched cities.

Click "Show Weather Graph" to visualize the average temperature for all searched cities in a bar chart.

Code Structure
weather_app.py: The main Streamlit application script.

Fetches weather data using the OpenWeatherMap API.

Stores searched cities and their weather data in session state.

Provides options to download data and visualize it.

Dependencies:

streamlit: For building the web app.

requests: For making API calls to OpenWeatherMap.

pandas: For handling and exporting data.

matplotlib: For plotting the bar chart.

Screenshots
Weather Data Fetching
Weather Data Fetching

CSV Download
CSV Download

Weather Graph
Weather Graph

Notes
Ensure you have a stable internet connection to fetch weather data.

The app uses the free tier of the OpenWeatherMap API, which has a limit of 60 requests per minute.

Replace the placeholder API key with your own key to avoid errors.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Author
Haider khan
hadikhan95383@gmail.com
GitHub Profile
