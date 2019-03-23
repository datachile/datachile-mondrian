#!/usr/bin/env python3

import unittest


def test():
    """Runs the unit tests."""

    tests = unittest.TestLoader().discover('cubes', pattern='*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    return 0 if result.wasSuccessful() else 1


if __name__ == '__main__':
    test()
