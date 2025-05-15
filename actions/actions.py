import requests
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

class ActionGetWeather(Action):
    def name(self) -> Text:
        return "action_get_weather"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        city = tracker.get_slot("location")
        if not city:
            dispatcher.utter_message(text="Please specify a city.")
            return []

        api_key = os.getenv("OPENWEATHER_API_KEY")
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

        try:
            response = requests.get(url)
            data = response.json()

            if data["cod"] != 200:
                dispatcher.utter_message(text="Couldn't fetch weather data. Please try another city.")
                return []

            weather = data["weather"][0]["description"]
            temp = data["main"]["temp"]
            dispatcher.utter_message(text=f"The weather in {city} is '{weather}' with a temperature of {temp}°C.")
        except Exception as e:
            dispatcher.utter_message(text="An error occurred while fetching weather.")
        return []
