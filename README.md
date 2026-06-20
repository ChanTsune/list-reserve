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

Return the number of item slots currently allocated for a list.

```py
from list_reserve import capacity

l = [1, 2, 3]
print(capacity(l)) # 3
```

### reserve

Reserve list capacity.

```py
from list_reserve import reserve, capacity

l = []
reserve(l, 10)

print(len(l)) # 0

print(capacity(l)) # 10
```

### allocated_bytes

Return the memory size currently allocated for list item slots.

```py
from list_reserve import allocated_bytes

l = [1, 2, 3]
print(allocated_bytes(l)) # capacity(l) * pointer size
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

## Development

This repository ships a [Dev Container](https://containers.dev). Open it in an editor that
supports Dev Containers ("Reopen in Container"), or run it headlessly with the
[Dev Containers CLI](https://github.com/devcontainers/cli):

```bash
devcontainer up --workspace-folder .
devcontainer exec --workspace-folder . python -m unittest
```

The container compiles the C extension on creation, so the tests are runnable immediately.
Since `list_reserve` is a C extension, re-run `pip install .` after editing
`src/list_reserve.c`.

## License

[MIT License](./LICENSE)
