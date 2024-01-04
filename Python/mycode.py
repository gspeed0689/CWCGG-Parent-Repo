import inspect

def ppgm(igmo):
    """Pretty print inspect.getmembers() reports"""
    max_key = max([len(x[0]) for x in igmo])
    for item in igmo:
        print(f"{item[0]:>{max_key}} -- {item[1][:{76-max_key}]}")

