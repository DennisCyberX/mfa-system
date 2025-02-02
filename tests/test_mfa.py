
```python
import unittest
from src.mfa_system import MFA

class TestMFA(unittest.TestCase):
    def setUp(self):
        self.mfa = MFA("test@example.com")

    def test_totp_generation_and_verification(self):
        totp_code = self.mfa.generate_totp()
        self.assertTrue(self.mfa.verify_totp(totp_code))

    def test_sms_code_simulation(self):
        code = self.mfa.send_sms_code("1234567890")
        self.assertEqual(len(str(code)), 6)

    def test_email_code_simulation(self):
        code = self.mfa.send_email_code()
        self.assertEqual(len(str(code)), 6)

if __name__ == '__main__':
    unittest.main()
