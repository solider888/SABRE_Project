# SABR Webapp

A web application that provides SABR (Society for American Baseball Research) intelligence and analysis.

## Features

- **Home Page**: Landing page with project information
- **SABR Smile**: Analysis of the SABR smile volatility surface
- **Surface**: Surface analysis and visualization
- **Graphs**: Interactive graphs and charts

## Project Structure

```
├── app.py                 # Main application file
├── requirements.txt       # Python dependencies
├── lib/
│   └── sabr.py           # SABR pricing and analysis library
└── pages/
    ├── landing.py        # Landing page
    ├── smile.py          # SABR smile page             
    └── surface.py        # Surface analysis page
```

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python app.py
```

3. Open your browser and navigate to:
```
http://localhost:8050
```

## Technologies

- **Dash**: Interactive web framework for Python
- **Dash Bootstrap Components**: Bootstrap styling for Dash
- **SABR Model**: For interest rate derivatives analysis

## Navigation

The sidebar provides quick access to all available pages:
- Home
- SABR Smile
- Surface
- Graphs
