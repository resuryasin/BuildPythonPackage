import unittest

from io import StringIO
from unittest.mock import patch
from package_name.modules_name.hello import print_hello


class HelloTestCase(unittest.TestCase):
    def test_hello(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print_hello()
            self.assertEqual(fake_out.getvalue().strip(), "Hello World!".strip())


if __name__ == '__main__':
    unittest.main()
