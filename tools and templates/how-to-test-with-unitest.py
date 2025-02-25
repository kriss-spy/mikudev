import unittest
from module import function
class TestMyModule(unittest.TestCase):
    def test_my_function(self):
        self.assertEqual(function(parameters), expected_result)
if __name__ == '__main__':
    unittest.main()