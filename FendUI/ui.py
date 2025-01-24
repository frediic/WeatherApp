import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from weather_api import get_weather, get_forecast


class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather App")
        self.root.geometry("800x600")
        self.root.resizable(False, False)

        self.background = Image.open("assets/background1.jpg")
        self.background = self.background.resize((800, 600), Image.Resampling.LANCZOS)
        self.bg_image = ImageTk.PhotoImage(self.background)
        bg_label = tk.Label(root, image=self.bg_image)
        bg_label.place(x=0, y=0)

        self.main_frame = tk.Frame(root, bg="#87CEEB", highlightthickness=0)
        self.main_frame.place(relx=0.5, rely=0.5, anchor="center")

        self.city_entry = tk.Entry(self.main_frame, bg="#87CEEB", font=("Arial", 16), width=20, justify="center", fg="grey")
        self.city_entry.insert(0, "Enter city name...")
        self.city_entry.bind("<FocusIn>", self.clear_placeholder)
        self.city_entry.bind("<FocusOut>", self.add_placeholder)
        self.city_entry.grid(row=0, column=0, padx=10, pady=10)

        self.search_button = tk.Button(self.main_frame, text="Get Weather", font=("Arial", 12), command=self.fetch_weather)
        self.search_button.grid(row=0, column=1, padx=10, pady=10)

        self.weather_label = tk.Label(self.main_frame, text="", font=("Arial", 20), bg="#87CEEB", fg="#000000", justify="center")
        self.weather_label.grid(row=1, column=0, columnspan=2, pady=20)

        self.icon_label = tk.Label(self.main_frame, bg="#87CEEB")
        self.icon_label.grid(row=2, column=0, columnspan=2, pady=10)

        self.forecast_frame = tk.Frame(self.main_frame, bg="#87CEEB")
        self.forecast_frame.grid(row=3, column=0, columnspan=2, pady=10)

    def clear_placeholder(self, event):
        if self.city_entry.get() == "Enter city name...":
            self.city_entry.delete(0, tk.END)
            self.city_entry.config(fg="black")

    def add_placeholder(self, event):
        if not self.city_entry.get():
            self.city_entry.insert(0, "Enter city name...")
            self.city_entry.config(fg="grey")

    def fetch_weather(self):
        city = self.city_entry.get()
        if city == "Enter city name..." or not city.strip():
            messagebox.showwarning("Warning", "Please enter a valid city name!")
            return

        weather = get_weather(city)
        forecast = get_forecast(city)

        if "error" in weather or "error" in forecast:
            messagebox.showerror("Error", weather.get("error") or forecast.get("error"))
        else:
            self.display_weather(weather)
            self.display_forecast(forecast)

    def display_weather(self, weather):
        self.weather_label.config(
            text=f"{weather['city']}\n{weather['temperature']}°C\n{weather['description'].capitalize()}"
        )

        icon_path = f"FendUI/icons/{weather['icon']}.png"
        try:
            icon_image = Image.open(icon_path).resize((50, 50), Image.Resampling.LANCZOS)
            icon = ImageTk.PhotoImage(icon_image)
            self.icon_label.config(image=icon)
            self.icon_label.image = icon
        except FileNotFoundError:
            self.icon_label.config(image="")

    def display_forecast(self, forecast):
        for widget in self.forecast_frame.winfo_children():
            widget.destroy()

        for i in range(5):
            day = forecast[i * 8]
            date_label = tk.Label(self.forecast_frame, text=day['datetime'].split(" ")[0], font=("Arial", 12), bg="#87CEEB")
            date_label.grid(row=i, column=0, padx=5, pady=5)

            icon_path = f"FendUI/icons/{day['icon']}.png"
            try:
                icon_image = Image.open(icon_path).resize((30, 30), Image.Resampling.LANCZOS)
                icon = ImageTk.PhotoImage(icon_image)
                icon_label = tk.Label(self.forecast_frame, image=icon, bg="#87CEEB")
                icon_label.image = icon
                icon_label.grid(row=i, column=1, padx=5, pady=5)
            except FileNotFoundError:
                pass

            temp_label = tk.Label(self.forecast_frame, text=f"{day['temperature']}°C", font=("Arial", 12), bg="#87CEEB")
            temp_label.grid(row=i, column=2, padx=5, pady=5)