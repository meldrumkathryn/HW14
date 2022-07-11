import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        testcase = BookLover("bob","bob.email","mystery")
        testcase.add_book('Book1',1)
        self.assertTrue(testcase.has_read('Book1'))

    def test_2_add_book(self):
        testcase = BookLover("bob","bob.email","mystery")
        testcase.add_book('Book1',1)
        testcase.add_book('Book1',1)
        test = (len([x for x in list(testcase.book_list['book_name'].values) if x == 'Book1'])==1)
        self.assertTrue(test)
                
    def test_3_has_read(self): 
        testcase = BookLover("bob","bob.email","mystery")
        testcase.add_book('Book1',1)
        self.assertTrue(testcase.has_read('Book1'))
        
    def test_4_has_read(self):
        testcase = BookLover("bob","bob.email","mystery")
        self.assertFalse(testcase.has_read('Book2'))
        
    def test_5_num_books_read(self): 
        testcase = BookLover("bob","bob.email","mystery")
        self.assertTrue((testcase.num_books_read()==testcase.num_books))

    def test_6_fav_books(self):
        testcase = BookLover("bob","bob.email","mystery")
        testcase.add_book('Book2', 2)
        testcase.add_book('Book3', 3)
        testcase.add_book('Book4', 4)
        test = (len(testcase.fav_books())==1)
        self.assertTrue(test)

if __name__ == '__main__':
    
    unittest.main(verbosity=3)