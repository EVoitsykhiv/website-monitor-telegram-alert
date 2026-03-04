import time
import requests
import asyncio
from config import WEBSITE_URL, CHECK_INTERVAL
from telegram_alert import send_alert


def check_website():

    try:
        response = requests.get(WEBSITE_URL, timeout=10)

        if 200 <= response.status_code < 400:
            return True

        return False

    except requests.exceptions.RequestException:
        return False


async def main():

    print("Website monitor started")

    last_status = True

    while True:

        status = check_website()

        if not status and last_status:

            message = f"🚨 WEBSITE DOWN: {WEBSITE_URL}"

            print(message)

            await send_alert(message)

        elif status and not last_status:

            message = f"✅ WEBSITE RECOVERED: {WEBSITE_URL}"

            print(message)

            await send_alert(message)

        last_status = status

        await asyncio.sleep(CHECK_INTERVAL)


if __name__ == "__main__":

    asyncio.run(main())
