import unittest
from sympy import symbols, pi, sin, cos
from Input_Proccessing import Expression
class TestExpression(unittest.TestCase):
    def test_variable_extraction(self):
        expr = Expression("2*x + y")
        self.assertEqual(expr._variables, symbols("x y"), "Variable extraction failed.")

    def test_reserved_keywords_exclusion(self):
        expr = Expression("e*x + y + sin(z)")
        self.assertEqual(expr._variables, symbols("x y z"), "Reserved keywords not excluded correctly.")

    def test_lambda_function_creation(self):
        expr = Expression("2*x + y")
        func = expr.f()
        result = func(2, 3)  # x=2, y=3
        self.assertEqual(result, 7, "Lambda function evaluation failed.")

    def test_expression_with_constants(self):
        expr = Expression("pi*x + 3")
        func = expr.f()
        result = func(2)  # x=2
        self.assertAlmostEqual(result, pi * 2 + 3, delta=1e-9, msg="Expression with constants failed.")

    def test_expression_with_reserved_functions(self):
        expr = Expression("sin(x) + cos(y)")
        func = expr.f()
        result = func(0, 0)  # x=0, y=0
        self.assertEqual(result, 1, "Expression with reserved functions failed.")

    def test_invalid_expression(self):
        with self.assertRaises(Exception, msg="Invalid expressions should raise an error."):
            Expression("2*/x")  # Invalid expression

if __name__ == "__main__":
    unittest.main()
