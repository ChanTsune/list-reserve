# list-reserve

Python builtin list memory allocation library.  

[![PyPI version](https://img.shields.io/pypi/v/list-reserve.svg)](https://pypi.org/project/list-reserve/)
[![Python versions](https://img.shields.io/pypi/pyversions/list-reserve.svg)](https://pypi.org/project/list-reserve/)
[![Wheel](https://img.shields.io/pypi/wheel/list-reserve.svg)](https://pypi.org/project/list-reserve/)
[![Downloads](https://static.pepy.tech/badge/list-reserve)](https://pepy.tech/project/list-reserve)
[![License](https://img.shields.io/pypi/l/list-reserve.svg)](https://github.com/ChanTsune/list-reserve/blob/master/LICENSE)
[![Test](https://github.com/ChanTsune/list-reserve/workflows/Test/badge.svg)](https://github.com/ChanTsune/list-reserve/actions)

## Why?

Python lists over-allocate internally to make repeated append operations efficient.
`list-reserve` exposes a small set of CPython-specific helpers for inspecting and
controlling that capacity.

## Platform support

Prebuilt wheels are provided for CPython on Linux, macOS, and Windows.

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

### stats

Return list memory statistics in one call.

```py
from list_reserve import reserve, stats

l = []
reserve(l, 10)

print(stats(l))
# {'length': 0, 'capacity': 10, 'allocated_bytes': 80,
#  'overhead': 10, 'utilization': 0.0}
```

## Development

This repository ships a [Dev Container](https://containers.dev). Open it in an editor that
supports Dev Containers ("Reopen in Container"), or run it headlessly with the
[Dev Containers CLI](https://github.com/devcontainers/cli):

```bash
devcontainer up --workspace-folder .
devcontainer exec --workspace-folder . python tools/run_installed_tests.py
```

The container installs the package in editable mode on creation, so the tests are
runnable immediately. Since `list_reserve` includes a C extension, re-run
`pip install -e .` after editing `src/list_reserve.c`.

## License

[MIT License](./LICENSE)
