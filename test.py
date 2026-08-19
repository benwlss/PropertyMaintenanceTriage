import unittest

from decision import priority_choice, contractor_choice

class Test(unittest.TestCase):
    def test_handle_low(self):
        result = priority_choice("The handle is broken")
        self.assertEqual(result, "Low")

    def test_lock_medium(self):
        result = priority_choice("The lock is broken")
        self.assertEqual(result, "Medium")

    def test_leak_urgent(self):
        result = priority_choice("There is a water leak")
        self.assertEqual(result, "Urgent")

    def test_contractor_plumber(self):
        result = contractor_choice("The toilet is blocked")
        self.assertEqual(result, "Plumber")

    def test_contractor_electrician(self):
        result = contractor_choice("There is no power")
        self.assertEqual(result, "Electrician")

    def test_contractor_GeneralHandyman(self):
        result = contractor_choice("The lock is broken")
        self.assertEqual(result, "General Handyman")

    def test_missing_description(self):
        self.assertEqual(priority_choice(""), "Unclassified")
        self.assertEqual(contractor_choice(""), "Unclassified")

    def test_capital_letters(self):
        self.assertEqual(priority_choice("THE PIPE HAS BURST"), "Urgent")

    def test_multiple_priority_words(self):
        result = priority_choice("There is a leak and my lock is broken")
        self.assertEqual(result, "Urgent")

if __name__ == "__main__":
    unittest.main()