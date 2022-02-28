import requests
from datetime import datetime
import smtplib
import time

MY_LAT = -12.389578
MY_LONG = -37.204780
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}
NOTIFIER_EMAIL = "*"
NOTIFIER_EMAIL_PASSWORD = "*"
HOST = "smtp-mail.outlook.com"


def is_iss_nearby():
    """
    No parameters needed. Makes a range comparison between current location and the current iss_location.
    :return: True if the latitude and longitude are currently between +5 or -5, False on the contrary.
    """
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    iss_data = response.json()
    iss_latitude = float(iss_data["iss_position"]["latitude"])
    iss_longitude = float(iss_data["iss_position"]["longitude"])
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True
    return False


def is_currently_dark():
    """
    Makes a comparison using the sunrise and sunset times in hour and the current system time in hour.
    :return: True if sunset hour matches system hour.
    """
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    hour_now = time_now.hour
    if (hour_now <= sunrise) or (hour_now >= sunset):
        return True
    return False


def send_notification():
    """
    If it is currently dark and the ISS is overhead, an e-mail will be sent notifying it.
    :return: Nothing
    """
    if is_iss_nearby() and is_currently_dark():
        with smtplib.SMTP(host=HOST) as connection:
            connection.starttls()
            connection.login(user=NOTIFIER_EMAIL, password=NOTIFIER_EMAIL_PASSWORD)
            connection.sendmail(from_addr=NOTIFIER_EMAIL, to_addrs=NOTIFIER_EMAIL,
                                msg="Subject:ISS Overhead Notifier\n\nThe ISS is nearby your position, better look"
                                    " up to find it in the sky!!")
    else:
        time.sleep(60)
        send_notification()


send_notification()
