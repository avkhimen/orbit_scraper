import time
from datetime import datetime

def send_text_notification(session):
	while True:
		try:
			text_notification = TextNotification()
		except Exception as e:
			print(e)
		else:
			text_notification.check_notification()
			time.sleep(10)
			now = datetime.now()
			current_time = now.strftime("%H:%M:%S")
			print("Send notification sleep 10s " + current_time)
		finally:
			True

class TextNotification():
	def __init__(self):
		pass

	def send_notification(self):
		if self.check_notification():
			pass

	def check_notification(self):
		pass
