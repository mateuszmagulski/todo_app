from django.test import SimpleTestCase

from tasks.forms import TaskForm


class TestForms(SimpleTestCase):

    def test_task_form_valid_data(self):
        form = TaskForm(data={
            "title":"task1"
        })

        self.assertTrue(form.is_valid())

    def test_city_form_no_data(self):
        form = TaskForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)