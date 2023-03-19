#!/usr/bin/env python3

"""
exchange_rate_alert.py
---------
This script alerts the user if the current exchange rate has exceeded the target exchange rate.

Usage:

./exchange_rate_alert.py --exchange-rate <TARGET_EXCHANGE_RATE>
"""

import argparse
import logging
import requests
from requests.exceptions import HTTPError

format = "%(asctime)s: %(levelname)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

bnm_uri = "https://api.bnm.gov.my/public/kl-usd-reference-rate"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument(
        "-e", "--exchange-rate", help="The value of target exchange rate"
    )

    args = parser.parse_args()

    target_exchange_rate = float(args.exchange_rate)

    try:
        response = requests.get(
            bnm_uri,
            headers={"Accept": "application/vnd.BNM.API.v1+json"},
        )

        # If the response was successful, no Exception will be raised
        response.raise_for_status()
        json_response = response.json()
    except HTTPError as http_err:
        logging.error(f"HTTP error occurred: {http_err}")
    except Exception as err:
        logging.error(f"Other error occurred: {err}")
    else:
        logging.debug("Request succeeded")
        logging.debug(json_response)
        current_exchange_rate = float(json_response["data"]["rate"])
        if current_exchange_rate >= target_exchange_rate:
            logging.info(
                f"ALERT!!! TargetExchangeRate={target_exchange_rate},CurrentExchangeRate={current_exchange_rate}"
            )