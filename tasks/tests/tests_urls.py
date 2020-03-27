from django.test import SimpleTestCase
from django.urls import reverse, resolve

from tasks.views import index, updateTask, deleteTask


class TestUrls(SimpleTestCase):

    def test_index_url_resolves(self):
        url = reverse('list')
        self.assertEquals(resolve(url).func, index)

    def test_update_task_url_resolves(self):
        url = reverse('update_task', args=[1])
        self.assertEquals(resolve(url).func, updateTask)

    def test_delete_task_url_resolves(self):
        url = reverse('delete_task', args=[1])
        self.assertEquals(resolve(url).func, deleteTask)