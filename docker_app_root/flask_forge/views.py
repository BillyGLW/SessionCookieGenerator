from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.edit import (CreateView, DeleteView,
										UpdateView)
from django.http import JsonResponse
from django.core.exceptions import SuspiciousOperation
from .forms import FlaskSessionForm
from .flask_api import (flask_session_encode, flask_session_decode)
from .tasks import create_task, flaskencode_task, flaskdecode_task

from celery.result import AsyncResult

@csrf_exempt
def get_status(request, task_id):
    task_result = AsyncResult(task_id)
    result = {
        "task_id": task_id,
        "task_status": task_result.status,
        "task_result": task_result.result
    }
    return JsonResponse(result, status=200)

@csrf_exempt
def f_query_01(request):
	if request.POST:
		secret_key = request.POST.get('secret_key', '')
		cookie_value = request.POST.get('cookie_value', '')
		operation = request.POST.get('operation', '')
		# todo: it could be done simpler
		if secret_key and cookie_value:
			if operation == 'encode':
				res = flaskencode_task.delay(secret_key, cookie_value)
			elif operation == "decode":
				res = flaskdecode_task.delay(secret_key, cookie_value)
			else:
				raise SuspiciousOperation('Secret key or cookie value arent possible to reach.')
			return JsonResponse({"task_id": res.id, "task_status": res.status,  "task_result": res.result}, status=202)
	return JsonResponse({"Error": 1})

@csrf_exempt
def task_test(request):
	if request.POST:
		task_type = request.POST.get('test')
		new_task = create_task.delay((task_type))
		response = JsonResponse({"taks_id": new_task.id, "task_status": new_task.status,  "task_result": new_task.result}, status=202)
		print("response", response)
		return JsonResponse({"taks_id": new_task.id, "task_status": new_task.status,  "task_result": new_task.result}, status=202)
	return JsonResponse({"Error": 1})
def index(request):
	form = FlaskSessionForm(request.POST)
	context = {'form': FlaskSessionForm}
	
	if form.is_valid():
		secret_key = form.cleaned_data.get('secret_key', '').strip()
		cookie_value = form.cleaned_data.get('cookie_value', '').strip()
		operation = form.cleaned_data.get('operation', '')
		if secret_key and cookie_value:
			context['data'] = flask_session_encode(secret_key, cookie_value) \
			if int(operation) else flask_session_decode(cookie_value, secret_key) 

	return render(request, 'flask-forge-index.html', context=context)