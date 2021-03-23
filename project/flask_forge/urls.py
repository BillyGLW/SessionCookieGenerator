from django.urls import path, re_path
from .views import index, task_test, get_status, f_query_01

urlpatterns	 = [
	path('', index, name='flask-forge-index'),
	path('task/', task_test, name='task_test'),
	path('celery/tasks/f_query_01/', f_query_01, name='flask_query_01'),
	# simpler
	# path(r'^getstatus/<task_id>', get_status, name='task_get_status'),
	# or safier
	re_path(r'^getstatus/(?P<task_id>([\w]+[-]*){5})', get_status, name='task_get_status'),
]