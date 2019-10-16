
## MATLAB

In MATLAB 2019a,

    - elementwise multiplication/division must have a leading dot (i.e. `.*` and `./`)

Generate data in dot.m file

    cd matlab/gendata && ./run.sh   # The file matlab/InputData.m generated


## Python

### numpy

    python3
    >>> import numba
    >>> numpy.__version__
    '1.13.3'

### numba

> Numba is a just-in-time compiler for Python that works best on code that uses
> NumPy arrays and functions, and loops.

Install numba

    pip install --user numba

Check system information with numba

    numba -s &> python/numba_system.txt

Check installation

    python3
    >>> import numba
    >>> numba.__version__
    '0.45.1'

Resources

- [5 mins guide](https://numba.pydata.org/numba-doc/dev/user/5minguide.html)
    + See examples in `./python/numba_example`



