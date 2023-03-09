# A simple example of calling C functions from Python.

1. Create an C file (see: [lib.c](./lib.c))

2. Build a shared library
```sh
gcc -fPIC -shared -o lib.so lib.c
```

3. Load the shared library and call library functions (see: [main.py](./main.py))