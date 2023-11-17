from django.test import TestCase
from .models import Discount
from .views import filtered_products

#tests unitaires

class SetupTest(TestCase):
    def set_up(self):
        # Configuration initiale avant chaque test
        pass
    
    def object_create(self):
        # Testez la création d'objet dans votre modèle
        pass

class ViewTest(TestCase):
    def setUp(self):
        # Configuration initiale avant chaque test
        pass
    
    def test_affichage_page(self):
        # Testez l'affichage de la page de votre vue
        pass
    
#tests fonctionnels
from selenium import webdriver
from django.test import LiveServerTestCase
from selenium.webdriver.common.keys import Keys

class TestSelenium(LiveServerTestCase):
    def setUp(self):
        self.selenium = webdriver.Firefox() 
        super(TestSelenium, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(TestSelenium, self).tearDown()
        

    