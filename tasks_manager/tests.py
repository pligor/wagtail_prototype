from django.test import TestCase
from .models import Project


# for simple manage.py it means “test*.py under directory

# # Run all the tests in the animals.tests module
# $ ./manage.py test animals.tests
#
# # Run all the tests found within the 'animals' package
# $ ./manage.py test animals
#
# # Run just one test case
# $ ./manage.py test animals.tests.AnimalTestCase
#
# # Run just one test method
# $ ./manage.py test animals.tests.AnimalTestCase.test_animals_can_speak


# Create your tests here.
class TestBasic(TestCase):
    def setUp(self):
        Project.objects.create(
            title="Title",
            description="my descr",
            client_name="this client"
        )

    def test_basic(self):
        """test methods must start with the name test"""
        a = 1
        self.assertEqual(1, a)

    def test_silly(self):
        project = Project.objects.get(title='Title')
        self.assertEqual(project.description, 'my descr')

