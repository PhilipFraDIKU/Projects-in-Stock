from django.core.urlresolvers import reverse
from django.test import TestCase
from .models import Counselor, Project
from .views import *

#Model testing:
class Test_counselor(TestCase):
    def test_is_not_registered(self):
        counselor = Counselor(accountId=-1)
        self.assertFalse(counselor.is_registered())

    def test_is_registered(self):
        counselor = Counselor(accountId=1)
        self.assertTrue(counselor.is_registered())

#Views testing:
class Test_index_view(TestCase):
    def test_index_response(self):
        request = self.client.get(reverse('index'))
        self.assertTrue(request.status_code == 200)
        self.assertEquals(request.resolver_match.func, index)

class Test_project_list_view(TestCase):
    def test_project_list_response(self):
        request = self.client.get(reverse('project_list'))
        self.assertTrue(request.status_code == 200)
        self.assertEquals(request.resolver_match.func, project_list)

class Test_project_detail_view(TestCase):
    #"setUp" is an empty predefined in TestCase and the method below is an override.
    def setUp(self):
        project = Project()
        project.save()

    def test_project_detail_response(self):
        request = self.client.get(reverse('project_detail', args=[1]))
        self.assertTrue(request.status_code == 200)
        self.assertEquals(request.resolver_match.func, project_detail)

    def test_project_detail_404(self):
        request = self.client.get(reverse('project_detail', args=[2]))
        self.assertTrue(request.status_code == 404)

class Test_counselor_list_view(TestCase):
    def test_counselor_list_response(self):
        request = self.client.get(reverse('counselor_list'))
        self.assertTrue(request.status_code == 200)
        self.assertEquals(request.resolver_match.func, counselor_list)

class Test_counselor_detail_view(TestCase):
    def setUp(self):
        counselor = Counselor()
        counselor.save()

    def test_counselor_detail_response(self):
        request = self.client.get(reverse('counselor_detail', args=[1]))
        self.assertTrue(request.status_code == 200)
        self.assertEquals(request.resolver_match.func, counselor_detail)

    def test_counselor_detail_404(self):
        request = self.client.get(reverse('counselor_detail', args=[2]))
        self.assertTrue(request.status_code == 404)
