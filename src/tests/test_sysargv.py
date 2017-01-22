import unittest
import sys


class SysArgvTests(unittest.TestCase):
    """Test sys.argv state."""
    def testSysArgvState(self):
        """Test sys.argv state."""
        argv = sys.argv
        import clr
        self.assertTrue(argv == sys.argv)


def test_suite():
    return unittest.makeSuite(SysArgvTests)


def main():
    unittest.TextTestRunner().run(test_suite())


if __name__ == '__main__':
    main()