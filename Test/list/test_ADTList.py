"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """


import unittest 
import config 
from DataStructures import listiterator as it
from DataStructures import liststructure as lt


class insertionSortTest (unittest.TestCase):

    def setUp (self):
        self.book1 = {'book_id':'1', 'book_title':'Title 1', 'author':'author 1'}
        self.book2 = {'book_id':'2', 'book_title':'Title 2', 'author':'author 2'}
        self.book3 = {'book_id':'3', 'book_title':'Title 3', 'author':'author 3'}
        self.book4 = {'book_id':'4', 'book_title':'Title 4', 'author':'author 4'}
        self.book5 = {'book_id':'5', 'book_title':'Title 5', 'author':'author 5'}
        self.book6 = {'book_id':'6', 'book_title':'Title 6', 'author':'author 1'}
        self.book7 = {'book_id':'7', 'book_title':'Title 7', 'author':'author 2'}
        self.book8 = {'book_id':'8', 'book_title':'Title 8', 'author':'author 3'}
        self.book9 = {'book_id':'9', 'book_title':'Title 9', 'author':'author 4'}
        self.book10 = {'book_id':'10', 'book_title':'Title 10', 'author':'author 5'}

    def tearDown (self):
        pass


    def test_arrayAddFirst (self):
        """
         Lista con elementos en orden aleatorio
        """
        self.lst = lt.newList('ARRAY_LIST')
        lt.addFirst (self.lst, self.book1)
        self.assertEqual (lt.size(self.lst), 1)
        lt.addFirst (self.lst, self.book2)
        self.assertEqual (lt.size(self.lst), 2)
        book = lt.firstElement(self.lst)
        self.assertDictEqual (book, self.book2)

    def test_listAddFirst (self):
        """
         Lista con elementos en orden aleatorio
        """
        self.lst = lt.newList()
        lt.addFirst (self.lst, self.book1)
        self.assertEqual (lt.size(self.lst), 1)
        lt.addFirst (self.lst, self.book2)
        self.assertEqual (lt.size(self.lst), 2)
        book = lt.firstElement(self.lst)
        self.assertDictEqual (book, self.book2)


if __name__ == "__main__":
    unittest.main()
