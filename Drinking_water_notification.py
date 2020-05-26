import time

from plyer import notification

if __name__ == '__main__':
	while True:
		notification.notify(
			title = "PLEASE DRINK WATER !!",
			message = "A total daily intake of around 2.7 liters (91 ounces) for women and 3.7 liters (125 ounces) for men can meet most adults' needs (19).",
			app_icon  = "/home/dev/Desktop/food/icon.ico",
			timeout = 12

			)
		time.sleep(6)