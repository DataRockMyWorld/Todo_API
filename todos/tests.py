from django.test import TestCase
from .models import Todo
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

# Create your tests here.
class TodoModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.todo = Todo.objects.create(
            title="Test todo", 
            description="Test todo description"
        )
        
    def test_model_content(self):
        self.assertEqual(self.todo.title, "Test todo")
        self.assertEqual(self.todo.description, "Test todo description")
        self.assertEqual(str(self.todo), "Test todo")

    def test_api_listview(self): # new
        response = self.client.get(reverse("todo_list")) 
        self.assertEqual(response.status_code, status.HTTP_200_OK) 
        self.assertEqual(Todo.objects.count(), 1) 
        self.assertContains(response, self.todo)
        
    
    def test_api_detailview(self): # new 
        response = self.client.get(
            reverse("todo_detail", kwargs={"pk": self.todo.id}),
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertContains(response, "Test todo")
