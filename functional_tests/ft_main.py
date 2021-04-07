from selenium import webdriver
import unittest

from ft_home import NewVisitorTest
# from ft_search import NewSearch
# from ft_users import NewUser

class FtMain:

    def __init__(self):
        self.ft_home = NewVisitorTest()
        # self.ft_users = NewUser()
        # self.ft_search = NewSearch()
        self.test = unittest.main(warnings='ignore')

    def functional_tests(self):
        print("Tests Fonctionnels pour la HP :")
        self.ft_home(self.test)
        # self.ft_search(self.test)
        # self.ft_users(self.test)


if __name__ == "__main__":
    main = FtMain()
    main.functional_tests()