# Smart Irrigation System

A software-based smart irrigation system that simulates farm conditions and helps make irrigation decisions using soil, weather, crop, and nutrient data.

The current version uses synthetic data, so the system can be tested without physical sensors or irrigation hardware.

## Demo

**[ project demo →](http://irrigation-dashboard-aarsh.s3-website-us-east-1.amazonaws.com/)**

## What it does

The dashboard provides an overview of simulated farm conditions, including:

- Temperature
- Soil moisture
- Crop health
- Humidity
- Rainfall
- Wind speed
- Atmospheric pressure
- Nitrogen, phosphorus, and potassium levels
- Crop growth stage
- Yield
- Water usage
- Number of irrigations
- Irrigation efficiency
- Nutrient usage
- AI-based recommendations

## Dashboard

The system displays the information through different sections.

### Weather

Shows simulated weather conditions such as temperature, humidity, rainfall, wind speed, and pressure.

The weather conditions can also affect irrigation decisions. For example, if rain is detected or expected, the system can recommend skipping irrigation.

### Soil Health

Tracks:

- Soil moisture
- Nitrogen
- Phosphorus
- Potassium

The dashboard also provides an overall soil-health status based on the available data.

### Crop Status

Displays:

- Crop health
- Growth stage
- Yield

This gives a quick view of the current simulated crop condition.

### Farm Analytics

Tracks resource usage and irrigation activity throughout the simulation:

- Water used
- Number of irrigations
- Irrigation efficiency
- Nitrogen used
- Phosphorus used
- Potassium used
- Simulation day

### AI Recommendations

The system generates recommendations based on the simulated farm conditions.

For example:

- Soil moisture is optimal
- Rain detected — skip irrigation today
- Nutrient levels are balanced

These recommendations help determine whether irrigation or other farm actions are necessary.

## How it works

```text
Synthetic Farm Data
        ↓
Weather + Soil + Crop Data
        ↓
    Data Processing
        ↓
 Farm Condition Analysis
        ↓
Irrigation Decision Logic
        ↓
 AI Recommendations
        ↓
     Dashboard
