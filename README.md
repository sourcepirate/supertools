## Supertools

Turn you functional tools to super.


Provides ```smap```, ```sfilter```, ```sreduce``` functions to do I/O bound operations effectively. 

*NOTE:not for CPU bound operations* 

![](https://raw.githubusercontent.com/sourcepirate/supertools/master/assets/super.gif)

## Usage

```python

from supertools import smap, sfilter

def io_bound_function(arg):
    # do something here
    pass

smap(io_bound_function, args)

```


## Benchmarking

![Benchmarked with timeit](https://raw.githubusercontent.com/sourcepirate/supertools/master/assets/benchmark.png)