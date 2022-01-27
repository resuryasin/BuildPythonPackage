import unittest

from io import StringIO
from unittest.mock import patch

from package_name.modules_name.hello import print_hello, print_greeting

class HelloTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.name = "RandomPersonOverThere"
    def test_hello(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print_hello()
            self.assertEqual(fake_out.getvalue().strip(), "Hello World!".strip())
    def test_greeting(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print_greeting(self.name)
            self.assertEqual(fake_out.getvalue().strip(), f"Hello {self.name}!".strip())

if __name__ == '__main__':
    unittest.main()
