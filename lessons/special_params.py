"""Examples of optional parameters and Union Squares."""


from typing import Union


def hello(lhs: float  = 0.0, name: Union[str, int] = "World") -> str:
    """A delightful greeting."""
    greeting: str = "Hello, "
    if isinstance(name, str):
        greeting: str = "Hello, " + name
    else:
        greeting += "Comp " + str(name)
    return greeting

print(hello(110, "Sally"))

# No argument
print(hello())

# int Argument works too!
print(hello(110))