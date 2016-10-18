import unittest

from .. import Foo

class FooTest(unittest.TestCase):
    def test_bar(self):
        foo = Foo()
        self.assertEquals("bar", foo.bar())
