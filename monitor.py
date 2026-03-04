import time
import requests
import asyncio
from config import WEBSITE_URL, CHECK_INTERVAL
from telegram_alert import send_alert


def check_website():

    try:
        response = requests.get(WEBSITE_URL, timeout=10)

        if response.status_code == 200:
            return True

        return False

    except requests.exceptions.RequestException:
        return False


async def main():

    print("Website monitor started")

    while True:

        status = check_website()

        if not status:

            message = f"⚠️ WEBSITE DOWN: {WEBSITE_URL}"

            print(message)

            await send_alert(message)

        else:

            print(f"Website OK: {WEBSITE_URL}")

        await asyncio.sleep(CHECK_INTERVAL)


if __name__ == "__main__":

    asyncio.run(main())
