# 🌦️ Weather Forecast System

A beautiful, responsive, and beginner-friendly weather forecast app built using **Python Flask**, **OpenWeatherMap API**, **Leaflet.js**, and **Tailwind CSS**. It allows users to check current weather, 5-day forecast, and view the selected location on an interactive map — no paid API keys required for the map!

---

## 📸 Screenshot

> _Add a file named `screenshot.png` in your repo root to display it here._

![Weather App Screenshot](screenshot.png)

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

setup_steps:
  - step: "Clone the Repository"
    commands:
      - git clone https://github.com/Avinash-Singh-13/Weather-Forecast-System.git
      - cd Weather-Forecast-System
    notes: "Or download the ZIP and extract it manually."

  - step: "Create a Virtual Environment"
    commands:
      - python -m venv venv
    notes: "This creates an isolated environment for Python packages."

  - step: "Activate the Virtual Environment"
    os_specific:
      windows:
        - venv\\Scripts\\activate
      mac_linux:
        - source venv/bin/activate
    notes: "You should see (venv) prefix in your terminal."

  - step: "Install Required Packages"
    commands:
      - pip install flask requests
    optional:
      - pip freeze > requirements.txt
    notes: "This installs Flask and the HTTP library `requests`."

  - step: "Configure OpenWeatherMap API Key"
    instructions:
      - "Go to https://openweathermap.org/api"
      - "Create an account and get your API key"
      - "Open templates/weather_app.html"
      - "Find the line: const API_KEY = 'your_openweathermap_api_key';"
      - "Replace it with your actual API key"
    notes: "Do not commit your actual API key to GitHub."

  - step: "Run the Flask Application"
    commands:
      - python app.py
    expected_output: "Running on http://127.0.0.1:5000/"

  - step: "Open in Browser"
    url: "http://127.0.0.1:5000"
    test_cases:
      - "Search for a city (e.g., Delhi)"
      - "Use the location button"
      - "Check forecast and map visibility"

  - step: "Troubleshooting Tips"
    issues:
      - problem: "ModuleNotFoundError for Flask"
        solution: "Run pip install flask requests"
      - problem: "'python' not recognized"
        solution: "Use 'python3' instead"
      - problem: "Flask not launching"
        solution: "Ensure venv is activated"
      - problem: "Map not displaying"
        solution: "Set CSS height for map container and use map.invalidateSize()"

  - step: "Add a .gitignore (Optional)"
    file: ".gitignore"
    contents: |
      __pycache__/
      *.pyc
      *.log
      venv/
      .env
      .vscode/
    commands:
      - git add .gitignore
      - git commit -m "Add .gitignore"
      - git push
    notes: "Helps avoid uploading unnecessary files to GitHub."

