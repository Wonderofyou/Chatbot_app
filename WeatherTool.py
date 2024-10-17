import requests
from langchain.agents import Tool
import os
import dotenv

dotenv.load_dotenv()


visual_crossing_api_key= os.getenv('VISUAL_CROSSING_API')

#Custom tool for weather data, using api of visual crossing
def get_historical_weather_vc(city_name: str, date: str) -> str:
    try:
        # Fetch wather data
        weather_data = requests.get(
            f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city_name}/{date}/{date}?unitGroup=metric&include=days&key={visual_crossing_api_key}&contentType=json"
        )

        if weather_data.status_code != 200:
            return "Could not retrieve historical weather data. Please try again."

        data = weather_data.json()
        weather = data['days'][0]['conditions']
        temp = round(data['days'][0]['temp'])
        return f"The weather in {city_name} on {date} was {weather} with a temperature of {temp}°C."

    except Exception as e:
        return str(e)
    
#tool config 
historical_weather_tool_vc = Tool(
    name="Historical Weather (Visual Crossing)",
    func=lambda city_date: get_historical_weather_vc(city_date.split(",")[0].strip(), city_date.split(",")[1].strip()),
    description="Use this tool to get the historical weather for a city on a specific date. Input format: 'City, YYYY-MM-DD'."
)
