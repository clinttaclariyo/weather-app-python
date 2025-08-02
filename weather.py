import tkinter as tk
import requests
from PIL import Image, ImageTk
from io import BytesIO

def get_weather():
    city = city_entry.get().strip()
    api_key = "4cab2115c811be567a446acc1c57652d"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] == 200:
            weather = data["weather"][0]["description"].title()
            temp = data["main"]["temp"]
            icon_code = data["weather"][0]["icon"]
            result = f"{city.title()}\n{weather}\n{temp}°C"

            icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"
            icon_response = requests.get(icon_url)
            icon_data = icon_response.content

            image = Image.open(BytesIO(icon_data))
            image = image.resize((80, 80))
            photo = ImageTk.PhotoImage(image)

            icon_label.config(image=photo)
            icon_label.image = photo
        else:
            result = "City not found."
            icon_label.config(image="")
    except:
        result = "Network error."
        icon_label.config(image="")

    result_label.config(text=result)

root = tk.Tk()
root.title("☁️ Weather App")
root.geometry("350x400")
root.configure(bg="#d0e7f9")

tk.Label(root, text="Weather Finder", font=("Helvetica", 16, "bold"), bg="#d0e7f9").pack(pady=10)
tk.Label(root, text="Enter City Name:", font=("Helvetica", 12), bg="#d0e7f9").pack()
city_entry = tk.Entry(root, font=("Helvetica", 12), justify="center")
city_entry.pack(pady=5)
tk.Button(root, text="Get Weather", font=("Helvetica", 12), command=get_weather, bg="#4da6ff", fg="white").pack(pady=10)

icon_label = tk.Label(root, bg="#d0e7f9")
icon_label.pack(pady=5)

result_label = tk.Label(root, text="", font=("Helvetica", 14), bg="#d0e7f9", fg="#333")
result_label.pack(pady=10)

root.mainloop()