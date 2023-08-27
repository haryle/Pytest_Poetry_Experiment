## How is this repo structured: 

Different services are stored in `src` with a mirroring version in `tests`. For example,

```
src/
    service1/
        service1/
            __init__.py
            app.py
        __init__.py
        pyproject.toml
        Dockerfile

    service2/
        service2
            __init__.py
            app.py
        __init__.py
        pyproject.toml
        Dockerfile  
tests/
    __init__.py
    test_service1/
        __init__.py
        test_app.py 
    
    test_service2/
        __init__.py
        test_app.py
```

Here `test_service1` is setup to test `service1` and so on. 

## How to run: 

In `pyproject.toml`, `testpaths` is set to `tests`. 

To run testing: 

```
# At pwd=src
poetry run pytest
```