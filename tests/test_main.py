import unittest
import io
import sys
from my_python_project.main import main

class TestMain(unittest.TestCase):
    def test_main(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        main()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "Hello from Jenkins CI/CD Pipeline!")

if __name__ == "__main__":
    unittest.main()
