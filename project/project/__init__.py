try:
	from .celery import app as celery_app
	__all__ = ['celery_app',]
except Exception as e:
	raise Exception(e)
