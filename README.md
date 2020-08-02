# list-reserve

Python builtin list memory allocation library.  

[![Build Status](https://travis-ci.org/ChanTsune/list-reserve.svg?branch=master)](https://travis-ci.org/ChanTsune/list-reserve)  

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
