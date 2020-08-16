from django.test import TestCase
import unittest
from LiftoffApp.static.logic import is_passed, calculate_new_weights, is_sets_valid


class TestLogic(unittest.TestCase):
    def setUp(self):
        self.test_data = {'cable butterflies': (15, [0, 0, 0, 0, 0]),
                          'benchpress': (90, [5, 4, 4, 4, 4]),
                          'row': (60, [5, 5, 5, 5, 5]),
                          'bicep curl': (12, [5, 5, 5, 5, 5])}

    def test_is_passed_when_sets_completed(self):
        test_expression = [5, 5, 5, 5, 5]
        self.assertTrue(is_passed(test_expression))

    def test_is_passed_when_sets_not_completed(self):
        test_expression = [5, 5, 5, 4, 4]
        self.assertFalse(is_passed(test_expression))

    def test_sets_validation_if_too_many_reps(self):
        test_expression = [6, 10, 5, 4, 4]
        self.assertRaises(ValueError, is_sets_valid, test_expression)

    def test_sets_validation_if_negative_reps(self):
        test_expression = [6, -1, 5, 4, 4]
        self.assertRaises(ValueError, is_sets_valid, test_expression)

    def test_new_weights_calculation(self):
        expected = {'cable butterflies': (15, [0, 0, 0, 0, 0]),
                    'benchpress': (90, [5, 4, 4, 4, 4]),
                    'row': (62.5, [0, 0, 0, 0, 0]),
                    'bicep curl': (14.5, [0, 0, 0, 0, 0])}
        actual = calculate_new_weights(self.test_data)
        self.assertEqual(expected, actual)
