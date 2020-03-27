from django.test import TestCase, Client
from django.urls import reverse

from tasks.models import Task


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.index_url = reverse("list")
        self.task1 = Task.objects.create(
            title="task1"
        )
        self.update_url = reverse("update_task", args=[1])
        self.delete_url = reverse("delete_task", args=[1])

    def test_index_GET(self):
        response = self.client.get(self.index_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "tasks/list.html")
    
    def test_index_add_task_POST(self):
        response = self.client.post(self.index_url, {
            "title":"task1"
        })
        
        self.assertEquals(response.status_code, 302)
        self.assertEquals(Task.objects.count(), 2)

    def test_index_add_task_POST_no_data(self):
        response = self.client.post(self.index_url)

        self.assertEquals(response.status_code, 302)
        self.assertEquals(Task.objects.count(), 1)

    def test_update_task_GET(self):
        response = self.client.get(self.update_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "tasks/update_task.html")

    def test_update_task_POST(self):
        response = self.client.post(self.update_url, {
            "title":"task2",
            "completed":True
        })
        
        self.assertEquals(response.status_code, 302)
        self.assertEquals(Task.objects.filter(completed=True).count(), 1)

    def test_update_task_POST_no_data(self):
        response = self.client.post(self.update_url,{
            "completed":True
        })
        
        self.assertEquals(response.status_code, 302)
        self.assertEquals(Task.objects.filter(completed=True).count(), 0)

    def test_delete_task_GET(self):
        response = self.client.get(self.delete_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "tasks/delete_task.html")

    def test_delete_task_POST(self):
        response = self.client.post(self.delete_url)
        
        self.assertEquals(response.status_code, 302)
        self.assertEquals(Task.objects.count(), 0)