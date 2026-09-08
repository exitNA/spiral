"""Contract checks for the canonical Loop task template."""

from pathlib import Path
import unittest


TEMPLATE = (
    Path(__file__).resolve().parents[1]
    / "loop"
    / "skills"
    / "loop"
    / "templates"
    / "LOOP.md"
)


class LoopTemplateIdentityTests(unittest.TestCase):
    def setUp(self):
        self.template = TEMPLATE.read_text(encoding="utf-8")

    def test_identity_uses_plain_separate_fields(self):
        self.assertIn("- Task ID:\n", self.template)
        self.assertIn("- Created:\n", self.template)
        self.assertIn("- Updated:\n", self.template)
        self.assertNotIn("- Task ID (", self.template)
        self.assertNotIn("- Created / updated", self.template)

    def test_identity_documents_value_formats(self):
        self.assertIn("YYYYMMDD-HHmmss-short-semantic-slug", self.template)
        self.assertIn("current environment's local time", self.template)
        self.assertIn("ISO 8601", self.template)
        self.assertIn("UTC offset", self.template)


if __name__ == "__main__":
    unittest.main()
