from __future__ import annotations

import shutil
import sys
import tempfile
import unittest
from pathlib import Path


def main() -> int:
    project_root = Path(__file__).resolve().parents[1]
    source_tests = project_root / "tests"

    with tempfile.TemporaryDirectory(prefix="list-reserve-tests-") as tmp:
        tmp_path = Path(tmp)
        copied_tests = tmp_path / "tests"
        shutil.copytree(
            source_tests,
            copied_tests,
            ignore=shutil.ignore_patterns("__pycache__"),
        )

        sys.path = [
            entry for entry in sys.path if Path(entry or ".").resolve() != project_root
        ]
        sys.path.insert(0, str(tmp_path))

        suite = unittest.defaultTestLoader.discover(
            str(copied_tests),
            pattern="test_*.py",
            top_level_dir=str(tmp_path),
        )
        result = unittest.TextTestRunner(verbosity=2).run(suite)
        return int(not result.wasSuccessful())


if __name__ == "__main__":
    raise SystemExit(main())
