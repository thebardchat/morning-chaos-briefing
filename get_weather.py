"""
Fetches current weather for Hazel Green / North Alabama.
Returns summary string and haul risk assessment.
Uses NWS API — no API key required.
"""

import requests

LAT = 34.9298
LON = -86.5630
NWS_URL = f"https://api.weather.gov/points/{LAT},{LON}"

def get_weather():
    try:
        r = requests.get(NWS_URL, timeout=5)
        forecast_url = r.json()["properties"]["forecast"]
        forecast = requests.get(forecast_url, timeout=5).json()
        period = forecast["properties"]["periods"][0]
        summary = period["shortForecast"]
        temp = period["temperature"]
        wind = period["windSpeed"]
        haul_risk = "YES — check conditions" if any(
            x in summary.lower() for x in ["rain", "storm", "snow", "ice", "fog"]
        ) else "LOW"
        return f"{temp}°F, {summary}, Wind: {wind}", haul_risk
    except Exception as e:
        return "Weather unavailable", f"Error: {e}"

if __name__ == "__main__":
    summary, risk = get_weather()
    print(f"Weather: {summary}")
    print(f"Haul Risk: {risk}")
