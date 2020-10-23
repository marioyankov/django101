from unittest import TestCase

from django.core.exceptions import ValidationError

from testing.validators import contains_only_digits


class ContainsOnlyDigitsValidatorTests(TestCase):
    def test_validate_whenOnlyDigits_shouldDoNothing(self):
        contains_only_digits('123')

    def test_validate_whenValueIsEmpty_shouldDoNothing(self):
        contains_only_digits('')

    def test_validate_whenValueContainsALetter_shouldRaise(self):
        with self.assertRaises(ValidationError) as context:
            contains_only_digits('a')

        self.assertIsNotNone(context.exception)
