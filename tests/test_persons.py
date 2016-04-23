from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from model.person import Person
from model.fellow import Fellow
from model.staff import Staff
import unittest

class TestPerson(unittest.TestCase):
    person = Person('Adeola','Adedire')

    def test_new_person_class(self):
        self.assertIsInstance(self.person, Person)
    def test_new_person_first_name(self):
        self.assertEqual(self.person.fullname, 'Adeola Adedire')

class TestFellow(unittest.TestCase):
    fellow = Fellow('Lovelyn','Tijesunimi-Israel')
    def test_new_fellow_class(self):        
        self.assertIsInstance(self.fellow, Fellow)
    def test_new_fellow_first_class(self):
        self.assertEqual(self.fellow.fullname, 'Lovelyn Tijesunimi-Israel')
        
class TestStaff(unittest.TestCase):
    staff = Staff('Ikem','Okonkwo')
    def test_new_fellow_class(self):        
        self.assertIsInstance(self.staff, Staff)
    def test_new_fellow_first_class(self):
        self.assertEqual(self.staff.fullname, 'Ikem Okonkwo')


if __name__ == '__main__':
    unittest.main()