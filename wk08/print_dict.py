#!/usr/bin/env python3

d = {
    'key': 'value',
    'Andrew': 'green',
    'Anne': 'red',
    'John': 'blue',
}

def print_dict(d):
    # for key in d:
    #     print(f'[{key}] => {d[key]}')

    # for x in d.items():
    #     print(f'[{x[0]}] => {x[1]}')

    for k, v in d.items():
        print(f'[{k}] => {v}')

print_dict(d)