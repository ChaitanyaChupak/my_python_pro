import unittest
import sys
import os

# Add `src/` to PYTHONPATH manually
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

# Now import your function
from my_python_project.main import main

class TestMain(unittest.TestCase):
    def test_main(self):
        from io import StringIO
        sys.stdout = StringIO()
        main()
        output = sys.stdout.getvalue().strip()
        sys.stdout = sys.__stdout__
        self.assertEqual(output, "Hello from Jenkins CI/CD Pipeline!")

if __name__ == "__main__":
    unittest.main()
