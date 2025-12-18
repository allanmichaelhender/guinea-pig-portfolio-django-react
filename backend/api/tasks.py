import requests
from .models import FtseData, Snp500Data, Nikkei225Data
from datetime import date

datefrom = "2015-01-01"

today = date.today()
dateto = today.isoformat()

api_key = "xjDy6auzJiNBaXQjmERBIGb84lN93EsR"


def create_url(symbol, datefrom, dateto, apikey):
    return (
        "https://financialmodelingprep.com/stable/historical-price-eod/full?"
        + f"apikey={apikey}"
        + f"&from={datefrom}"
        + f"&to={dateto}"
        + f"&symbol={symbol}"
    )


def fetch_daily_data():
    ftse_api_url = create_url("^FTSE", datefrom, dateto, api_key)
    ftse_response = requests.get(ftse_api_url, timeout=30)

    if ftse_response.status_code == 200:
        data = ftse_response.json()

        if isinstance(data, list):
            for item in data:
                FtseData.objects.update_or_create(
                    date=item["date"],  
                    defaults={
                        "open": item["open"],
                        "high": item["high"],
                        "low": item["low"],
                        "close": item["close"],
                        "volume": item["volume"],
                        "change": item["change"],
                        "changePercent": item.get("changePercent"),
                    },
                )

    snp500_api_url = create_url("^GSPC", datefrom, dateto, api_key)
    snp500_response = requests.get(snp500_api_url, timeout=30)

    if snp500_response.status_code == 200:
        data = snp500_response.json()

        if isinstance(data, list):
            for item in data:
                Snp500Data.objects.update_or_create(
                    date=item["date"],  
                    defaults={
                        "open": item["open"],
                        "high": item["high"],
                        "low": item["low"],
                        "close": item["close"],
                        "volume": item["volume"],
                        "change": item["change"],
                        "changePercent": item.get("changePercent"),
                    },
                )
    nikkei225_api_url = create_url("^FTSE", datefrom, dateto, api_key)
    nikkei225_response = requests.get(nikkei225_api_url, timeout=30)

    if nikkei225_response.status_code == 200:
        data = nikkei225_response.json()

        if isinstance(data, list):
            for item in data:
                Nikkei225Data.objects.update_or_create(
                    date=item["date"], 
                    defaults={
                        "open": item["open"],
                        "high": item["high"],
                        "low": item["low"],
                        "close": item["close"],
                        "volume": item["volume"],
                        "change": item["change"],
                        "changePercent": item.get("changePercent"),
                    },
                )
