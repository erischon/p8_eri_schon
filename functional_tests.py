from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_find_a_substitute_and_add_it_as_favorite(self):
        
        # Lily a entendu parlé d'une application web qui permet de trouver des substituts alimentaires. Elle va y jeter un oeil en utilisant son navigateur web.
        self.browser.get('http://localhost:8000')

        # Elle voit qu'elle est au bon endroit en voyant le titre de la page.
        self.assertIn('The Substitute', self.browser.title) 
        self.fail('Finish the test!')

        # Elle est satisfaite en lisant le slogan qui lui parle vraiment.
        # > h2 + text

        # Comme elle est curieuse elle regarde tous les choix qui s'offrent à elle.

        # En haut de la page il y a un menu.
        # > id 

        # A gauche de ce menu elle voit le logo et le nom du site.
        # > img
        # > h2 + text

        # A droite elle voit dans l'ordre : un formulaire de recherche et une icone "Créer Mon Compte".
        # > form
        # > url

        # Dans la page, sous le titre et le sous-titre, elle découvre un formulaire de recherche.
        # > form

        # Plus bas elle lit l'histoire de Colette et de Rémy, les créateurs.
        # > class

        # Sous cette partie elle tombe sur les coordonnées de contact : un numéro de téléphone et un email.
        # > class
        # text

        # Pour finir en bas de la page elle trouve les mentions légales ainsi qu'un lien vers la partie contact (qui est juste au-dessus en faite). 
        # class footer
        # link

        # Elle se dit que cela fait sérieux et elle se lance en entrant "Nutella" dans le champs de recherche. Elle clic sur le bouton "Chercher" et cela lui ouvre une nouvelle page.

if __name__ == '__main__':
    unittest.main(warnings='ignore')