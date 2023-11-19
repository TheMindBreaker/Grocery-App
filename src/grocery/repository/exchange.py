import requests
from fastapi import HTTPException
from config import EXCHANGE_KEY

def convert_currency(amount: float, from_currency: str = "USD", to_currency: str = "MXN") -> float:
    response = requests.get(f"https://api.freecurrencyapi.com/v1/latest?apikey={EXCHANGE_KEY}&base_currency={from_currency}&currencies={to_currency}")
    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Error fetching currency conversion rate")

    rates = response.json().get('data', {})
    conversion_rate = rates.get(to_currency)

    if conversion_rate is None:
        raise HTTPException(status_code=500, detail="Error fetching currency conversion rate")

    return amount * conversion_rate