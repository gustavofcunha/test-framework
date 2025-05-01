from tests.testCaseTest import TestCaseTest
from tests.testSuiteTest import TestSuiteTest
from tests.testLoaderTest import TestLoaderTest
from models.testResult import TestResult
from models.testSuite import TestSuite
from models.testLoader import TestLoader
from models.testRunner import TestRunner

"""class MyTest(TestCase):

    def set_up(self):
        print('set_up')

    def tear_down(self):
        print('tear_down')

    def test_a(self):
        print('test_a')

    def test_b(self):
        print('test_b')

    def test_c(self):
        print('test_c')


result = TestResult()

test = MyTest('test_a')
test.run(result)

test = MyTest('test_b')
test.run(result)

test = MyTest('test_c')
test.run(result)

print(result.summary())

#------------------------------------------------------------

result = TestResult()

test = TestCaseTest('test_result_success_run')
test.run(result)

test = TestCaseTest('test_result_failure_run')
test.run(result)

test = TestCaseTest('test_result_error_run')
test.run(result)

test = TestCaseTest('test_result_multiple_run')
test.run(result)

test = TestCaseTest('test_was_set_up')
test.run(result)

test = TestCaseTest('test_was_run')
test.run(result)

test = TestCaseTest('test_was_tear_down')
test.run(result)

test = TestCaseTest('test_template_method')
test.run(result)

print(result.summary())

#------------------------------------------------------------

result = TestResult()
suite = TestSuite()

suite.add_test(TestCaseTest('test_result_success_run'))
suite.add_test(TestCaseTest('test_result_failure_run'))
suite.add_test(TestCaseTest('test_result_error_run'))
suite.add_test(TestCaseTest('test_result_multiple_run'))
suite.add_test(TestCaseTest('test_was_set_up'))
suite.add_test(TestCaseTest('test_was_run'))
suite.add_test(TestCaseTest('test_was_tear_down'))
suite.add_test(TestCaseTest('test_template_method'))

suite.add_test(TestSuiteTest('test_suite_size'))
suite.add_test(TestSuiteTest('test_suite_success_run'))
suite.add_test(TestSuiteTest('test_suite_multiple_run'))

suite.run(result)
print(result.summary())

#------------------------------------------------------------

result = TestResult()
loader = TestLoader()
suite = loader.make_suite(TestLoaderTest)
suite.run(result)
print(result.summary())

#------------------------------------------------------------

loader = TestLoader()
suite = loader.make_suite(TestLoaderTest)

runner = TestRunner()
runner.run(suite)"""

#------------------------------------------------------------

loader = TestLoader()
test_case_suite = loader.make_suite(TestCaseTest)
test_suite_suite = loader.make_suite(TestSuiteTest)
test_load_suite = loader.make_suite(TestLoaderTest)

suite = TestSuite()
suite.add_test(test_case_suite)
suite.add_test(test_suite_suite)
suite.add_test(test_load_suite)

runner = TestRunner()
runner.run(suite)