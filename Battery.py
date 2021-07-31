# Import the following modules
from plyer import notification  # pip install plyer
import psutil  # pip install psutil
import time

seconds = 300

# Run a infinite loop to update you in every 300 seconds
while True:
    # Give you the tuple that consists the following items: (percent=20, secsleft=4600, power_plugged=False)
    battery = psutil.sensors_battery()
    percent = battery.percent  # Give you the battery percent

    if percent >= 90:
        pluged = battery.power_plugged  # Check whether the plugged in or not
        plug = "Plugged In" if pluged else "Plugged Not In"

        if plug == "Plugged In":
            # Producing a notification with the Battery percentage and a Icon
            notification.notify(title=f"Battery Percentage Reaches to {percent}%",
                                message="Please Remove The Plug!",
                                app_icon=r"C:\Users\Dell\Downloads\Battery_Charge_Notifier-main\Icons\bat.ico",
                                timeout=15)
            time.sleep(600)

    else:
        pluged = battery.power_plugged
        plug = "Plugged In" if pluged else "Plugged Not In"
        if plug == "Plugged In":
            notification.notify(title=f"Battery Percentage Reaches to {percent}%",
                                message="Please Don't Remove The Plug!",
                                app_icon=r"C:\Users\Dell\Downloads\Battery_Charge_Notifier-main\Icons\low.ico",
                                timeout=15)
            time.sleep(600)

        else:
            notification.notify(title=f"Battery Percentage is LOW: {percent}%",
                                message="Please Connect to the The Plug!",
                                app_icon=r"C:\Users\Dell\Downloads\Battery_Charge_Notifier-main\Icons\low.ico",
                                timeout=15)
            time.sleep(600)
