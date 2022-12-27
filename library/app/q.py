data = {'a': 1, 'b': 2}



from dataclasses import dataclass


@dataclass
class Data:
    a: int
    b: int



da = Data(a=1, b=2)

print(da.a, da.b)
print(data['a'], data['b'])