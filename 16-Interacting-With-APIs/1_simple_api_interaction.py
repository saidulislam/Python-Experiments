import requests

APP_ID = "7d65e6ed74wd4ww4d5w4w54w5w"
ENDPOINT = "https://openexchangerates.org/api/latest.json"

response = requests.get(f"{ENDPOINT}?app_id={APP_ID}")
exchange_rates = response.json()


usd_amount = 1000
gbp_amount = usd_amount * exchange_rates['rates']['GBP']


print(f"USD: {usd_amount} is GBP: {gbp_amount}")
print("\n")
print(exchange_rates)