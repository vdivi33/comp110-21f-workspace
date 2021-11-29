class Foo:
    bar: int = 0
    
    def __init__(self, i: int) -> None:
        self.bar = i
    

    def __str__(self) -> str:
        return f"{self.bar}"

f: Foo = Foo(10)
print(f)