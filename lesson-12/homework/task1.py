from bs4 import BeautifulSoup

with open("weather.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

rows = soup.find("table").find("tbody").find_all("tr")

weather_data = []
temperatures = []

for row in rows:
    cols = row.find_all("td")
    day = cols[0].text.strip()
    temp = int(cols[1].text.strip().replace("°C", ""))
    condition = cols[2].text.strip()

    weather_data.append({"day": day, "temperature": temp, "condition": condition})
    temperatures.append(temp)

print("Weather Forecast:")
for entry in weather_data:
    print(f"{entry['day']}: {entry['temperature']}°C, {entry['condition']}")


max_temp = max(temperatures)
max_temp_days = [entry["day"] for entry in weather_data if entry["temperature"] == max_temp]

print("\nHighest tempter:", ", ".join(max_temp_days))

sunny_days = [entry["day"] for entry in weather_data if entry["condition"] == "Sunny"]

print("Sunny days:", ", ".join(sunny_days))

average_temp = sum(temperatures) / len(temperatures)
print(f"\nAverage temper: {average_temp:.2f}°C")
