from plyer import notification
import psutil
import time
seconds=300
while True:
    battery=psutil.sensors_battery()
    percent=battery.percent
    if percent>=90:
        pluged=battery.power_plugged
        plug="Plugged In" if pluged else "Plugged Not In"
        if plug=="Plugged In":
            notification.notify(title=f"Battery Percentage Reaches to {percent}%",
                                message="Please Remove The Plug!!",
                                app_icon="C:/Users/Dell/Downloads/bat.ico",
                                timeout=15)
            time.sleep(600)
    else:
        pluged = battery.power_plugged
        plug = "Plugged In" if pluged else "Plugged Not In"
        if plug == "Plugged In":
            notification.notify(title=f"Battery Percentage Reaches to {percent}%",
                                message="Please Don't Remove The Plug!!",
                                app_icon="C:/Users/Dell/Downloads/low.ico",
                                timeout=15)
            time.sleep(600)
        else:
            notification.notify(title=f"Battery Percentage is LOW : {percent}%",
                                message="Please Connect to the The Plug!!",
                                app_icon="C:/Users/Dell/Downloads/low.ico",
                                timeout=15)
            time.sleep(600)
