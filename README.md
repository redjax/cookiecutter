# Cookiecutter

My [`cookiecutter`](https://cookiecutter.readthedocs.io/en/stable/) templates. All templates are organized under the [`t/`](./t/) directory. Each directory under `t/` is a template category/group, and each directory under a category/group is a `cookiecutter` template.

## Requirements

- The [`cookiecutter` package](https://cookiecutter.readthedocs.io/en/stable/installation.html)

## Usage

Templates are in the [`t/`](./t) directory. This makes for simpler `cookiecutter` commands:
```shell
cookiecutter https://github.com/redjax/cookiecutter --directory t/python/uv
```

You can also use `cookiecutter`'s built-in `gh:<user>/<repo>` syntax:

```shell
cookiecutter gh:redjax/cookiecutter --directory t/python/uv
```

If a template has not been merged into the `main` branch, you can also specify a tag, commit, or branch with `--checkout`:

```shell
cookiecutter gh:redjax/cookiecutter --checkout dev --directory t/unmerged_template
```

## Templates

    NOTE:

    This list may not be complete. The template I personally use most frequently will be listed here, but you should click through templates in the [`t/`](./t/) path for a full listing.

- [Docker templates](./t/docker/)
  - [Docker Compose Basic](./t/docker/compose-basic/)
- [Python template](./t/python/)
  - [Python PDM project](./t/python/pdm/)
  - [Python UV project](./t/python/uv/)
