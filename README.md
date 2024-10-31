# Cookiecutter

My [`cookiecutter`](https://cookiecutter.readthedocs.io/en/stable/) templates.

## Usage

Templates are in the [`t/`](./t) directory. This makes for simpler `cookiecutter` commands:
```shell
cookiecutter https://github.com/redjax/cookiecutter --directory t/python/uv
```

You can also use `cookiecutter`'s built-in `gh:<user>/<repo>` syntax:

```shell
cookiecutter gh:redjax/cookiecutter --directory t/python/uv
```
