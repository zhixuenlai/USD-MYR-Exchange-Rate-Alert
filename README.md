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

## Run the application on a schedule by using Cron (macOS)

1. Use vim as Cron's text editor by adding the following line to your `.zshrc`:

    ```bash
    export EDITOR=vim
    ```

    The default text editor of Cron is vi and it will throw the following error on macOS:

    ```bash
    crontab: no crontab for <username> - using an empty one
    crontab: "/usr/bin/vi" exited with status 1
    ```

2. Create a Cron job. Running the following command will open the vim editor.

    ```bash
    crontab -e
    ```

3. Press `i` to enter the insert mode and add the following command to Crontab to run the application daily at 4:00 PM:

    ```bash
    0 16 * * 0-6 cd /path/to/usd_myr_exchange_rate_alert && /path/to/python3 exchange_rate_alert.py --exchange-rate <TARGET_EXCHANGE_RATE>
    ```

4. Save the file by pressing `Esc` and then `:wq`. You should see the following output on the terminal if the Cron job is started successfully:

    ```bash
    crontab: installing new crontab
    ```

    You can run `crontab -l` to list the Cron jobs that is currently running.

References:

- [Python Automation With Cron on Mac](https://www.jcchouinard.com/python-automation-with-cron-on-mac/)

- [Crontab Guru](https://crontab.guru/)
