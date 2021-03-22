from selenium import webdriver
import unittest

class NewUser(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_user_can_create_account(self):

        self.browser.get('http://localhost:8000/search/')

        # Lilly écrit "Nutella" dans le champ de recherche et clique sur le bouton  "Chercher"

        # Une nouvelle page s’affiche avec les résultats de la recherche
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn("Résultats", header_text)

        # Cette page a comme en-tête le nom du produit cherché et indique que "Vous pouvez remplacer cet aliment par :"

        # Elle est sur son desktop et voit les résultats sous forme de tableau de 3 colonnes

        # Elle est sur son mobile et voit les résulats sous forme de tableau d'une colonne    

        # Chaque résultat (Card) contient : l’image du Product, son Nom, un lien vers sa fiche, une icône Sauvegarde, son Nutriscore.s ses favoris.


if __name__ == '__main__':
    unittest.main(warnings='ignore')