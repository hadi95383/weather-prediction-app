# Weather Prediction App

This Python application uses Streamlit, requests, pandas, and matplotlib to fetch and display weather information for cities worldwide. It leverages the OpenWeatherMap API to retrieve real-time weather data and presents it in a user-friendly interface.  Users can search for weather by city name, download the search history as a CSV file, and visualize the average temperature for searched cities in a bar graph.

## Features

* **Real-time Weather Data:** Fetches current weather conditions, including temperature and description, from the OpenWeatherMap API.
* **City Search:** Allows users to search for weather information by city name.
* **Data Storage:** Stores the history of weather searches in a Streamlit session, enabling data download and visualization.
* **CSV Download:** Provides a button to download the weather search history as a CSV file for further analysis.
* **Temperature Visualization:** Generates a bar graph showing the average temperature for the cities searched.
* **User-Friendly Interface:** Uses Streamlit to create an interactive and easy-to-use web application.
* **API Key Management:** Securely manages the OpenWeatherMap API key using environment variables.

## Requirements

* Python 3.7 or higher
* Streamlit
* requests
* pandas
* matplotlib

You can install the required libraries using pip:

```bash
pip install streamlit requests pandas matplotlib
Setup and Usage
Clone the Repository:

Bash

git clone [https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git](https://www.google.com/search?q=https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git)  # Replace with your repo URL
cd YOUR_REPOSITORY_NAME
Set API Key:

Create an account at OpenWeatherMap and obtain an API key.
Set the API key as an environment variable named OPENWEATHER_API_KEY. This is the recommended approach for security. In Linux/macOS:
Bash

export OPENWEATHER_API_KEY="YOUR_API_KEY"
In Windows:
PowerShell

$env:OPENWEATHER_API_KEY = "YOUR_API_KEY"
Alternatively, you can set the API key as the default value in the script (less secure):
Python

API_KEY = os.getenv("OPENWEATHER_API_KEY", "YOUR_API_KEY") # Not recommended for production
Run the App:

Bash

streamlit run your_script_name.py  # Replace your_script_name.py with the actual name
Access the App:
Open your web browser and go to the URL displayed in the terminal (usually http://localhost:8501).

Code Explanation
get_weather(city): This function fetches weather data from the OpenWeatherMap API using the provided city name. It handles API requests, error checking, and data extraction. It also stores the search results in the Streamlit session state.
main(): This function sets up the Streamlit user interface, including text input for city name, buttons for fetching weather and downloading data, and the display area for results and graphs.
Session State: Streamlit's session state is used to store the history of weather searches, making it available for download and visualization.
Data Visualization: The code uses matplotlib to create a bar graph of average temperatures.
CSV Download: The st.download_button is used to provide a convenient way to download the search data as a CSV file.
Example
Enter a city name in the text input box.
Click the "Get Weather" button. The current weather information for the city will be displayed.
Repeat step 1 and 2 for other cities.
Click the "Download Weather Data as CSV" button to download the search history.
Click the "Show Weather Graph" button to visualize the average temperature for the searched cities.
Contributing
Contributions are welcome! Please feel free to submit pull requests or open issues.
