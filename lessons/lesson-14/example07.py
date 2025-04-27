# запуск тестов doctest из unittest

import doctest
import unittest
import example03


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(example03))
    tests.addTests(doctest.DocFileSuite('prime.md'))
    return tests


if __name__ == '__main__':
    unittest.main()
