## How is this repo structured: 

This is the standard `pytest` recommended repo structure, where `tests` is outside of the package. The package is also set up with a `src` structure.

```
src/
    __init__.py
    mypkg/
        __init__.py
        app.py

tests/
    __init__.py
    test_mypkg/
        __init__.py
        test_app.py 
pyproject.toml
Dockerfile    
```

Here `test_service1` is setup to test `service1` and so on. 

## How to run: 


To run testing: 

```
# At the directory containing src and tests
poetry run pytest
```