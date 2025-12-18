import requests
from .models import EuroStoxxData, FtseData, Snp500Data, Nikkei225Data, HsiData
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
    nikkei225_api_url = create_url("^N225", datefrom, dateto, api_key)
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

    eurostoxx_api_url = create_url("^STOXX50E", datefrom, dateto, api_key)
    eurostoxx_response = requests.get(eurostoxx_api_url, timeout=30)

    if eurostoxx_response.status_code == 200:
        data = eurostoxx_response.json()

        if isinstance(data, list):
            for item in data:
                EuroStoxxData.objects.update_or_create(
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

    hsi_api_url = create_url("^VIX", datefrom, dateto, api_key)
    hsi_response = requests.get(hsi_api_url, timeout=30)

    if hsi_response.status_code == 200:
        data = hsi_response.json()

        if isinstance(data, list):
            for item in data:
                HsiData.objects.update_or_create(
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
