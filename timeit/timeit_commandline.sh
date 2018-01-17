python3 -m timeit -s \
    "d={}" \
    "for i in range(1000):" \
    "  d[str(i)] = i"
