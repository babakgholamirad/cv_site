from django.test import TestCase
from models import Project

# Create your tests here.
 # write Test for Project model
class ProjectTest(TestCase):
    def test_str(self):
        project = Project(name='Test Project')
        self.assertEqual(str(project), project.name)
     