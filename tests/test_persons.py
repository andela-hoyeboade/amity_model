from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from model.person import Person
from model.fellow import Fellow
from model.staff import Staff
import unittest


class TestPerson(unittest.TestCase):
    """Test cases for Person class"""
    person = Person('Adeola', 'Adedire')

    def test_new_person_class(self):
        self.assertEqual(type(self.person), Person)

    def test_new_person_first_name(self):
        self.assertEqual(self.person.fullname, 'ADEOLA ADEDIRE')

    def test_new_person_office_allocated(self):
        self.assertEqual(self.person.office_allocated, False)

    def test_new_person_office_space(self):
        self.assertEqual(self.person.office, '')

    def test_new_person_living_allocated(self):
        self.assertEqual(self.person.living_allocated, False)

    def test_new_person_living_allocated(self):
        self.assertEqual(self.person.living, '')

    def test_create_new_person_raises_error(self):
        self.assertRaises(Exception, Person, 9, 'Ade')


class TestFellow(TestPerson):
    """Test cases for Fellow class"""
    fellow = Fellow('Lovelyn', 'Tijesunimi-Israel')

    def test_new_fellow_class(self):
        self.assertEqual(type(self.fellow), Fellow)

    def test_new_fellow_full_name(self):
        self.assertEqual(self.fellow.fullname, 'LOVELYN TIJESUNIMI-ISRAEL')

    def test_new_fellow_id(self):
        self.assertTrue(self.fellow.id.startswith('F'))

    def test_new_fellow_id_length(self):
        self.assertEqual(len(self.fellow.id), 11)

    def test_new_fellow_living_allocated(self):
        self.assertEqual(self.fellow.living_allocated, False)

    def test_new_fellow_living(self):
        self.assertEqual(self.fellow.living, '')

    def test_new_fellow_office_allocated(self):
        self.assertEqual(self.fellow.office_allocated, False)

    def test_new_fellow_office(self):
        self.assertEqual(self.fellow.office, '')

    def test_create_new_fellow_raises_error(self):
        self.assertRaises(Exception, Fellow, [3, 4], 'Ade')


class TestStaff(TestPerson):
    """Test cases for Staff class"""
    staff = Staff('Ikem', 'Okonkwo')

    def test_new_staff_class(self):
        self.assertEqual(type(self.staff), Staff)

    def test_new_staff_full_name(self):
        self.assertEqual(self.staff.fullname, 'IKEM OKONKWO')

    def test_new_staff_id(self):
        self.assertTrue(self.staff.id.startswith('S'))

    def test_new_staff_living_allocated(self):
        self.assertEqual(self.staff.living_allocated, False)

    def test_new_staff_living(self):
        self.assertEqual(self.staff.living, '')

    def test_new_staff_office_allocated(self):
        self.assertEqual(self.staff.office_allocated, False)

    def test_new_staff_office(self):
        self.assertEqual(self.staff.office, '')

    def test_create_new_staffs_raises_error(self):
        self.assertRaises(Exception, Staff, {'A': 'Apple'}, 4.5677)


if __name__ == '__main__':
    unittest.main()
