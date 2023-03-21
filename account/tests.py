from rest_framework.test import APITestCase, APIRequestFactory
from account.views import RegisterAPIView
from django.contrib.auth import get_user_model

User = get_user_model()

class AccountTest(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()

    def test_create_user(self):
        data = {
            'email': 'test@test.com',
            'password': 'test123',
            'password2': 'test123',
            'is_active': True
        }
        request = self.factory.post('api/v1/account/register/', data)
        view = RegisterAPIView.as_view()
        response = view(request)

        assert response.status_code == 201
        assert User.objects.filter(email='test@test.com').exists()
