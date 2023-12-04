import tkinter as tk
from tkinter import messagebox
import  requests

class WeatherApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Weather App")

        self.label_location = tk.Label(master, text="Enter location:")
        self.entry_location = tk.Entry(master)
        self.btn_get_weather = tk.Button(master, text="Get Weather", command=self.get_weather)
        self.label_result = tk.Label(master, text="")
        
        self.label_location.grid(row=0, column=0, pady=(10, 0), sticky="e")
        self.entry_location.grid(row=0, column=1, pady=(10, 0), sticky="w")
        self.btn_get_weather.grid(row=1, column=0, columnspan=2, pady=10)
        self.label_result.grid(row=2, column=0, columnspan=2)

    def get_weather(self):
        location = self.entry_location.get()
        api_key = "YOUR_OPENWEATHERMAP_API_KEY"  # Replace with your API key

        if not location:
            messagebox.showerror("Error", "Please enter a location.")
            return

        base_url = "http://api.openweathermap.org/data/2.5/weather"
        params = {"q": location, "appid": api_key, "units": "metric"}

        try:
            response = requests.get(base_url, params=params)
            data = response.json()

            if response.status_code == 200:
                self.display_weather(data)
            else:
                messagebox.showerror("Error", f"Error: {data['message']}")
        except requests.RequestException as e:
            messagebox.showerror("Error", f"Error: {e}")

    def display_weather(self, weather_data):
        if weather_data:
            temperature = weather_data["main"]["temp"]
            humidity = weather_data["main"]["humidity"]
            weather_description = weather_data["weather"][0]["description"]

            result_text = (
                f"Temperature: {temperature}°C\n"
                f"Humidity: {humidity}%\n"
                f"Condition: {weather_description}"
            )

            self.label_result.config(text=result_text)
        else:
            self.label_result.config(text="Weather data not available.")

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()
