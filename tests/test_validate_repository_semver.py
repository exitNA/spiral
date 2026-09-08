"""Regression coverage for plugin manifest semantic versions."""

import importlib.util
from pathlib import Path
import unittest


VALIDATOR = Path(__file__).resolve().parents[1] / "scripts/validate_repository.py"
spec = importlib.util.spec_from_file_location("validate_repository", VALIDATOR)
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


class SemanticVersionTests(unittest.TestCase):
    def test_accepts_stable_and_qualified_versions(self):
        valid_versions = (
            "0.3.0",
            "1.0.0-rc.1",
            "1.2.3+build.20260907",
            "2.0.0-beta.2+sha.5114f85",
            "0.3.0+codex.local-20260907-142530",
            "0.3.0+codex.20260907153240",
        )

        for version in valid_versions:
            with self.subTest(version=version):
                self.assertIsNotNone(validator.SEMVER.fullmatch(version))

    def test_rejects_malformed_versions(self):
        invalid_versions = (
            "",
            "1",
            "1.2",
            "v1.2.3",
            "01.2.3",
            "1.02.3",
            "1.2.03",
            "1.2.3-",
            "1.2.3+",
            "1.2.3-alpha..1",
            "1.2.3+build..1",
            "1.2.3-01",
            "1.2.3_alpha",
            "1.2٢.3",
            "1.2.3-١a",
            "1.2.3 trailing",
        )

        for version in invalid_versions:
            with self.subTest(version=version):
                self.assertIsNone(validator.SEMVER.fullmatch(version))


if __name__ == "__main__":
    unittest.main()
