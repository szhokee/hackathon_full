from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate
from category.models import Category
from category.views import CategoryAPIView
from django.contrib.auth import get_user_model

User = get_user_model()

class CategoryTest(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        category = [
            Category(title='category1'),
            Category(title='category2'),
            Category(title='category3'),
        ]
        Category.objects.bulk_create(category)

        self.setup_user()

    def setup_user(self):
        self.user = User.objects.create_user(
            email='test@test.com',
            password='test123',
            is_active=True
        )

    def test_get_category(self):
        request = self.factory.get('api/v1/category/category/')
        view = CategoryAPIView.as_view({'get': 'list'})
        response = view(request)
        assert response.status_code == 200
        assert len(response.data) == 3
        assert response.data[0]['title'] == 'category1'

    def test_post_category(self):
        data = {
            'title': 'category4'
        }
        request = self.factory.post('api/v1/category/category/', data)
        force_authenticate(request, self.user)
        view = CategoryAPIView.as_view({'post': 'create'})
        response = view(request)

        assert response.status_code == 201
        assert Category.objects.filter(title='category4').exists()
