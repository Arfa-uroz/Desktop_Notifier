import time
from plyer import notification

#if __name__ = "__main__":
while True:
    notification.notify(
    title = "Save your eyes",
    message = "Look 20 feet away atleast for 20 seconds",
    app_icon = "D:\Python_Programs\projectDesktopNotifier\iconfinder-bellnotificationsnoticenotifyalert-3993856_112639.ico",
    timeout = 20
    )
    time.sleep(20*60)
