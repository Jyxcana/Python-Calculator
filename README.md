# Python-Calculator
It supports any valid infix expression, using reverse Poland algorithm to calculate.
Operations: +-*/^%()
Feature: Unsafe checking included

To support more operators, you only need to:
  add priority order of that operator in the 'order' dictionary in the code
  add the operator into the op_string
  add elif branch in cal() function for that operator
