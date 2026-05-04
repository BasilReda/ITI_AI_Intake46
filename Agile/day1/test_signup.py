import unittest
from signup import validate_registration, UserRegistrationData

class TestRegistrationValidation(unittest.TestCase):
    
    def test_valid_registration(self):
        user = UserRegistrationData("johnDoe123", "john@example.com", "SecurePass1")
        errors = validate_registration(user)
        self.assertEqual(len(errors), 0)

    def test_invalid_username_too_short(self):
        user = UserRegistrationData("jo", "john@example.com", "SecurePass1")
        errors = validate_registration(user)
        self.assertIn("Username must be 3-20 alphanumeric characters.", errors)
        
    def test_invalid_email(self):
        user = UserRegistrationData("johnDoe", "johnexample.com", "SecurePass1")
        errors = validate_registration(user)
        self.assertIn("Invalid email format.", errors)
        
    def test_invalid_password_too_short(self):
        user = UserRegistrationData("johnDoe", "john@example.com", "Sec1")
        errors = validate_registration(user)
        self.assertIn("Password must be at least 8 characters, with 1 uppercase, 1 lowercase, and 1 number.", errors)
        
    def test_invalid_password_no_number(self):
        user = UserRegistrationData("johnDoe", "john@example.com", "SecurePassWord")
        errors = validate_registration(user)
        self.assertIn("Password must be at least 8 characters, with 1 uppercase, 1 lowercase, and 1 number.", errors)

    def test_empty_username(self):
        user = UserRegistrationData("", "john@example.com", "SecurePass1")
        errors = validate_registration(user)
        self.assertIn("Username must be 3-20 alphanumeric characters.", errors)
    
    def test_empty_email(self):
        user = UserRegistrationData("johnDoe", "", "SecurePass1")
        errors = validate_registration(user)
        self.assertIn("Invalid email format.", errors)
    
    def test_empty_password(self):
        user = UserRegistrationData("johnDoe", "john@example.com", "")
        errors = validate_registration(user)
        self.assertIn("Password must be at least 8 characters, with 1 uppercase, 1 lowercase, and 1 number.", errors)

    def test_empty_strings_handled_gracefully(self):
        user = UserRegistrationData("", "", "")
        errors = validate_registration(user)
        self.assertEqual(len(errors), 3)
        
    def test_whitespace_only_inputs(self):
        user = UserRegistrationData("   ", "   @  .com", "        ")
        errors = validate_registration(user)
        self.assertTrue(len(errors) > 0)
    
    def test_password_with_spaces(self):
        user = UserRegistrationData("johnDoe", "test@test.com", "Valid 1 Pass")
        errors = validate_registration(user)
        self.assertEqual(len(errors), 0)
    
    def test_username_below_minimum(self):
        user_too_short = UserRegistrationData("ab", "test@test.com", "SecurePass1")
        errors = validate_registration(user_too_short)
        self.assertIn("Username must be 3-20 alphanumeric characters.", errors)
    
    def test_username_below_minimum(self):
        user_too_short = UserRegistrationData("_aab", "test@test.com", "SecurePass1")
        errors = validate_registration(user_too_short)
        self.assertIn("Username must be 3-20 alphanumeric characters.", errors)

    def test_username_above_maximum(self):
        user_more_max = UserRegistrationData("a" * 21, "test@test.com", "SecurePass1")
        errors = validate_registration(user_more_max)
        self.assertIn("Username must be 3-20 alphanumeric characters.", errors)

    def test_valid_email_with_plus_sign(self):
        user = UserRegistrationData("johnDoe1", "john+newsletter@example.com", "SecurePass1")
        errors = validate_registration(user)
        self.assertEqual(len(errors), 0, "Email with '+' should be valid")
        
if __name__ == '__main__':
    unittest.main()
