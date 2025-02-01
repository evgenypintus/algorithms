import inspect
from typing import Callable

import math
import os
import random
import re
import sys
from typing import Callable
import inspect


def get_doc(fun: Callable) -> str:
    signature = inspect.signature(fun)
    func_name = fun.__name__
    params_info = []
    example_args = []
    count_str = 0
    # Start parameters with 2
    count_int = 2

    for param in signature.parameters.values():
        # Assuming that types can be only str and int
        param_type = param.annotation.__name__
        params_info.append(f"{param.name} {param_type}")

        # Generate example params
        if param_type == 'str':
            letter = chr(97 + (count_str % 26))  # Get letter in alphabetical order
            count_str += 1
            example_args.append(letter + letter + letter)
        else:
            example_args.append(count_int)
            count_int += 1

    return_type = signature.return_annotation.__name__

    param_list = ', '.join(map(str, example_args))
    example_call = f"{func_name}({param_list})"

    example_result = fun(*example_args)

    # Constructing the doc string to match the test cases
    docstring = f"""function name
    {func_name}
params ({len(params_info)})"""
    # If there are no params - don't print anything
    if len(params_info) > 0:
        docstring += '\n    ' + f"{('\n'+ '    ').join(params_info)}"

    docstring += f"""
return type
    {return_type}
example usage
    {example_call} -> {example_result}
    """
    return docstring

# Example function
def example_func(aaa: str, bbb: str, age: int) -> str:
    return f'{aaa} {bbb}, {age}'

if __name__ == '__main__':

    print(get_doc(example_func))
