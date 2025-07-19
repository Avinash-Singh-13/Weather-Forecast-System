# 🌦️ Weather Forecast System

A beautiful, responsive, and beginner-friendly weather forecast app built using **Python Flask**, **OpenWeatherMap API**, **Leaflet.js**, and **Tailwind CSS**. It allows users to check current weather, 5-day forecast, and view the selected location on an interactive map — no paid API keys required for the map!

---



---

## 🌟 Features

- 🔍 Search weather by city name
- 📍 Use current geolocation to get weather
- 📊 View temperature, humidity, pressure, wind speed, and “feels like”
- 📆 5-day forecast with icons
- 🗺️ Interactive map using Leaflet + OpenStreetMap (no map API key required)
- 🧊 Tailwind CSS-based responsive UI
- 🚫 Graceful error handling and loading animations

---

## 🧱 Tech Stack

| Layer       | Technology                  |
|-------------|------------------------------|
| **Frontend**| HTML5, Tailwind CSS, JavaScript |
| **Backend** | Python (Flask)              |
| **APIs**    | OpenWeatherMap              |
| **Maps**    | Leaflet.js + OpenStreetMap  |
| **Tools**   | Git, GitHub, VS Code        |

---

## 📁 Project Folder Structure

weather_app/
├── app.py # Flask backend
├── templates/
│ └── weather_app.html # Main frontend UI
├── static/ # (Optional future CSS/JS/images)
├── venv/ # Virtual environment (excluded in .gitignore)
├── .gitignore
├── README.md
└── screenshot.png # App preview (optional)


---

## 🔧 Local Setup Instructions (Step-by-Step)

### ✅ Requirements

| Tool         | How to Install |
|--------------|----------------|
| Python 3.8+  | [python.org](https://www.python.org/downloads/) |
| pip (Python package manager) | Comes with Python |
| Git (optional) | [git-scm.com](https://git-scm.com) |
| Code Editor  | [VS Code](https://code.visualstudio.com/) |

---

### ✅ Setup_Steps:
  #### - Step 1: "Clone the Repository"
    Commands:
      - git clone https://github.com/Avinash-Singh-13/Weather-Forecast-System.git
      - cd Weather-Forecast-System
    Notes: "Or download the ZIP and extract it manually."

  #### - Step 2: "Create a Virtual Environment"
    Commands:
      - python -m venv venv
    Notes: "This creates an isolated environment for Python packages."

  #### - Step 3: "Activate the Virtual Environment"
    os_specific:
      windows:
        - venv\\Scripts\\activate
      mac_linux:
        - source venv/bin/activate
    notes: "You should see (venv) prefix in your terminal."

  #### - Step 4: "Install Required Packages"
    Commands:
      - pip install flask requests
    Optional:
      - pip freeze > requirements.txt
    Notes: "This installs Flask and the HTTP library `requests`."

  #### - Step 5: "Configure OpenWeatherMap API Key"
    Instructions:
      - "Go to https://openweathermap.org/api"
      - "Create an account and get your API key"
      - "Open templates/weather_app.html"
      - "Find the line: const API_KEY = 'your_openweathermap_api_key';"
      - "Replace it with your actual API key"
    Notes: "Do not commit your actual API key to GitHub."

  #### - Step 6: "Run the Flask Application"
    Commands:
      - python app.py
    Expected_Output: "Running on http://127.0.0.1:5000/"

  #### - Step 7: "Open in Browser"
    url: "http://127.0.0.1:5000"
    Test_Cases:
      - "Search for a city (e.g., Delhi)"
      - "Use the location button"
      - "Check forecast and map visibility"

  #### - Step 8: "Troubleshooting Tips"
    Issues:
      - problem: "ModuleNotFoundError for Flask"
        solution: "Run pip install flask requests"
      - problem: "'python' not recognized"
        solution: "Use 'python3' instead"
      - problem: "Flask not launching"
        solution: "Ensure venv is activated"
      - problem: "Map not displaying"
        solution: "Set CSS height for map container and use map.invalidateSize()"

  #### - Step 9: "Add a .gitignore (Optional)"
    file: ".gitignore"
    contents: |
      __pycache__/
      *.pyc
      *.log
      venv/
      .env
      .vscode/
    Commands:
      - git add .gitignore
      - git commit -m "Add .gitignore"
      - git push
    Notes: "Helps avoid uploading unnecessary files to GitHub."

