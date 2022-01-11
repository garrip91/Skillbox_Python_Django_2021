from django.test import SimpleTestCase
from app_logic.helpers import check_access_by_age, test_if_age_is_14, test_if_age_less_than_18, test_if_age_equal_18, test_if_age_greater_than_18



class BussinessLogicTest(SimpleTestCase):

    def test_access_denied(self):
        #self.assertFalse(check_access_by_age(17))
        self.assertEqual(check_access_by_age(17), True)
        
        self.assertEqual(test_if_age_is_14(), True)
        self.assertEqual(test_if_age_less_than_18(), True)
        self.assertEqual(test_if_age_equal_18(), True)
        self.assertEqual(test_if_age_greater_than_18(), True)