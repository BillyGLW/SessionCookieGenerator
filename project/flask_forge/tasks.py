import time
from .flask_api import (flask_session_encode, flask_session_decode)
try:
	from celery import shared_task
except Exception as e:
	raise Exception(e)

@shared_task
def create_task(task_type):
	time.sleep(int(task_type) * 10)
	return True

@shared_task
def flaskencode_task(secret, data):
	return flask_session_encode(secret, data)

@shared_task
def flaskdecode_task(encoded, cookie_val=None):
	return flask_session_decode(encoded, cookie_val)