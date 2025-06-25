import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
API_KEY = 'your_api_key_here'
CITY = 'Chennai'
URL = f'http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric'
response = requests.get(URL)
data = response.json()
print("API response preview:", data.get('message', 'OK'))
if 'list' in data:
    forecast_list = data['list']
    weather_data = []
    for item in forecast_list:
        dt = datetime.fromtimestamp(item['dt'])
        temp = item['main']['temp']
        description = item['weather'][0]['description']
        weather_data.append({
            'datetime': dt,
            'temperature (°C)': temp,
            'description': description
        })
    df = pd.DataFrame(weather_data)
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=df, x='datetime', y='temperature (°C)', marker='o')
    plt.title(f'5-Day Temperature Forecast for {CITY}', fontsize=16)
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

else:
    print("API Error:", data.get('message', 'Unknown error occurred'))

