# list-reserve

Python builtin list memory allocation library.  

[![PyPI - License](https://img.shields.io/pypi/l/list_reserve)](https://pypi.org/project/list-reserve/)
![Test](https://github.com/ChanTsune/list-reserve/workflows/Test/badge.svg)
[![PyPI](https://img.shields.io/pypi/v/list_reserve)](https://pypi.org/project/list-reserve/)
[![Downloads](https://pepy.tech/badge/list-reserve)](https://pepy.tech/project/list-reserve)

## Getting it

```bash
pip install list_reserve
```

### capacity

Return allocated list memory size.

```py
from list_reserve import capacity

l = [1, 2, 3]
print(capacity(l)) # 3
```

### reserve

Reserve list memory.

```py
from list_reserve import reserve, capacity

l = []
reserve(l, 10)

print(len(l)) # 0

print(capacity(l)) # 10
```

### shrink_to_fit

*since 0.1.0*  
shrink to fit list capacity.

```py
from list_reserve import capacity, shrink_to_fit

l = list(range(100))

print(capacity(l)) # 118

shrink_to_fit(l)

print(capacity(l)) # 100
```

## License

[MIT License](./LICENSE)
