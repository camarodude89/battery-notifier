import psutil as ps
import pystray
from PIL import Image
import time
import tkinter
from tkinter import messagebox

class Notification():

    def __init__(self, battery_thresholds=[30, 15], critical_battery_threshold=10, persistent=False):

        battery_thresholds.sort(reverse=True)
        self.battery_thresholds = battery_thresholds
        self.critical_battery_threshold = critical_battery_threshold
        self.persistent = persistent

    def notification_window(self, percentage=None):

        root = tkinter.Tk()
        root.withdraw()

        if not self.persistent:
            msg =  f'Your battery percentage is {percentage}%. Please consider charging your laptop.'
            messagebox.showwarning('Low Battery Warning', msg)
        else:
            msg = (f'Your battery percentage is critically low at {percentage}%. Please plug in your laptop '
                    'to clear this notification.')

def callback(icon):

    battery = ps.sensors_battery()
    noti = Notification()
    cleared_noti_list = []

    while True:

        if battery.power_plugged:

            if cleared_noti_list:
                noti.battery_thresholds = cleared_noti_list
                cleared_noti_list = []

            time.sleep(1)
            continue
        try:
            if battery.percent <= noti.battery_thresholds[0]:
                noti.notification_window(battery.percent)
                cleared_noti_list.append(noti.battery_thresholds.pop(0))
                time.sleep(1)
                continue
        except IndexError:
            if battery.percent <= noti.critical_battery_threshold:
                noti.persistent = True
                noti.notification_window(battery.percent)

if __name__ == '__main__':
    image = Image.open("battery_icon.png")
    icon = pystray.Icon('Battery Notifier', image)

    icon.visible = True
    icon.run(setup=callback)
