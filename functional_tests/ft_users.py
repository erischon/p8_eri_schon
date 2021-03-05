from selenium import webdriver
import unittest

class NewUser(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_hp_look_great(self):
        
        # Lily va sur la page proposée pour créer son compte utilisateur
        self.browser.get('http://localhost:8000/users/signup/')

        # Elle voit qu'elle est au bon endroit.
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn("Je crée Mon Compte", header_text)

        # Elle suit les instructions qu'on lui donne

        # Elle donne son prénom

        # Elle donne un mot de passe

        # Elle clique sur le bouton "créer mon compte"

        # Là elle est redirigée vers sa page Mon Compte

        # Pour vérifier si elle est bien inscrite, elle clique sur le lien "Me déconnecter"

        # Elle se retrouve sur la page principale

        # Dans le menu du haut elle clique sur le lien "Me connecter"

        # Elle arrive sur une page qui lui demande d'entrer son prénom et son mot de passe

        # Elle clique et arrive bien sur sa page Mon Compte

        # Elle remarque que le menu supérieur a changé. Elle y voit maintenant un lien vers ses favoris.


if __name__ == '__main__':
    unittest.main(warnings='ignore')