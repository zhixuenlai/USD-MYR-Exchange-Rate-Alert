# USD MYR Exchange Rate Alert

This application requests the USD/MYR Reference Rate from the [BNM (Bank Negara Malaysia) OpenAPI](https://apikijangportal.bnm.gov.my/) and alerts the user if the current exchange rate has exceeded the target exchange rate.

## Setup

Run the following command to install the required Python modules:

```bash
pip install -r requirements.txt
```

## Usage

```bash
./exchange_rate_alert.py --exchange-rate <TARGET_EXCHANGE_RATE>

Example:
./exchange_rate_alert.py --exchange-rate 4.60
```
