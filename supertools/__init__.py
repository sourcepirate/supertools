
import inspect
from functools import reduce
from multiprocessing import cpu_count
from concurrent.futures import ThreadPoolExecutor, as_completed

CPU_COUNT = cpu_count()

def group_args(args, n):
    i = 0
    groups = []
    while i < len(args):
        groups.append(args[i:i+n])
        i = i+n
    return groups

def apply_it(func, h_func, arg_group):
    value = h_func(func, arg_group)
    if hasattr(value, "__iter__"):
        value = list(value)
    return value

def _execute(func, h_func, args):
    """execute the given functions in set and blocks"""
    group_len = int(len(args) / CPU_COUNT)
    arg_groups = group_args(args, group_len)
    with ThreadPoolExecutor(max_workers=CPU_COUNT) as executor:
        futures = {executor.submit(apply_it, func, h_func, group): i for i, group in enumerate(arg_groups)}
        values = []
        for future in as_completed(futures):
            index = futures[future] 
            data = future.result()
            values.append((index, data))
        sorted_value = sorted(values, key=lambda x: x[0])
        # lets examine the type of data
        # if the data is a list we need to concatinate the datas as whole
        # else we need to assosiative fold it.
        if isinstance(sorted_value[0][1], (list, tuple, )):
            ret = []
            for i, value in sorted_value:
                ret.extend(value)
            return ret
        else:
            ret =[]
            for i, value in sorted_value:
                ret.append(value)
            return h_func(func, ret)

def smap(func, values):
    return _execute(func, map, values)

def sfilter(func, values):
    return _execute(func, filter, values)

def sreduce(func, values):
    return _execute(func, reduce, values)