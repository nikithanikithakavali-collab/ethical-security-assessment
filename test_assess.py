
import unittest
from assess import check_config


class SecurityAssessmentTests(unittest.TestCase):

    def test_secure_configuration_passes(self):
        config = {
            "debug_mode": False,
            "https_enabled": True,
            "minimum_password_length": 12,
            "security_logging": True,
            "dependencies_reviewed": True
        }

        findings = check_config(config)

        self.assertEqual(len(findings), 5)
        self.assertTrue(
            all(item["status"] == "PASS" for item in findings)
        )

    def test_insecure_configuration_is_flagged(self):
        config = {
            "debug_mode": True,
            "https_enabled": False,
            "minimum_password_length": 8,
            "security_logging": False,
            "dependencies_reviewed": False
        }

        findings = check_config(config)

        self.assertTrue(
            all(item["status"] == "FINDING" for item in findings)
        )


if __name__ == "__main__":
    unittest.main()
