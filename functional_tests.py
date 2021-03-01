from selenium import webdriver

browser = webdriver.Firefox()

# Lily a entendu parlé d'une application web qui permet de trouver des substituts alimentaires. Elle va y jeter un oeil en utilisant son navigateur web.
browser.get('http://localhost:8000')

# Elle voit qu'elle est au bon endroit en voyant le titre de la page. 
assert 'The Substitute' in browser.title

# On lui demande de donner un produit pour lequel elle souhaite trouver un substitut.

# Elle tape "Nutella" dans le formulaire.

# Une fois qu'elle a cliqué sur le bouton recherche une nouvelle page s'affiche. Elle y trouve une liste de substituts.

# Elle a la possibilité d'un choisir un. En cliquant sur celui qu'elle a choisit une nouvelle page s'affiche avec toute les informations concernant le produit de substitution.

# Elle voudrait bien sauvegarder ce produit. Ca tombe bien, un lien lui propose de le faire. En cliquant dessus elle arrive sur une page d'authentification.

# Sur cette page on lui propose d'entrer un login et un password, ou de créer un compte utilisateur. Comme elle n'a pas de login, elle clique sur "Créer un compte utilisateur" et elle arrive sur une nouvelle page.

# On lui demande d'entrer son prénom, un email et un password, puis on lui demande de valider. Une fois qu'elle valide une nouvelle page s'affiche.

# Sur cette page elle trouve l'aliment de substitution qu'elle avait choisi.

# Satisfaite elle quitte l'application
browser.quit()
