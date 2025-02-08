# Musical Analysis Application 🎵

A web application for analyzing and visualizing musical data, offering insights into various aspects of songs and their characteristics.

## Features

- Interactive visualization of musical attributes
- Song analysis and comparison tools
- Real-time data visualization
- User-friendly interface for music exploration

## Getting Started

The application is available at [Musical Analysis App](https://malmak-musical-analysis.streamlit.app)  

Its documentation at [Documentation](https://mal-mak.github.io/musical-analysis-app/)  

## Usage

1. Navigate to the main dashboard
2. Select genre for analysis
3. Explore various visualization options
4. Use the interactive tools to compare and analyze musical attributes

## Project Structure

```
musical_analysis_app/
├── README.md
├── docs/
├── poetry.lock
├── pyproject.toml
├── requirements.txt
├── src
│   └── musical_analysis_app
│       ├── __init__.py
│       ├── app.py
│       ├── dashboard_tabs
│       │   ├── __init__.py
│       │   ├── caracteristics_tab.py
│       │   ├── popularity_tab.py
│       │   ├── recommendations_tab.py
│       │   └── tendances_tab.py
│       ├── data
│       │   └── spotify_tracks.csv
│       ├── pages
│       │   ├── __init__.py
│       │   └── dashboard.py
│       └── utils
│           ├── __init__.py
│           ├── dashboard_utils.py
│           └── features.py
└── tests
    ├── __init__.py
    └── test_dashboard_utils.py
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.