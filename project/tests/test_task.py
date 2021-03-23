from django.urls import reverse

def test_index(client):
	url = reverse("flask_forge:flask-forge-index")
	response = client.get(url)
	assert response.status_code == 200
	