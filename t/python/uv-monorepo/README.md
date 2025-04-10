# Python + UV Cookiecutter

A Python cookiecutter template using [uv](https://docs.astral.sh/uv/) for dependency & project management.

This template takes advantage of [`uv` "workspaces"](https://docs.astral.sh/uv/concepts/projects/workspaces/) to manage the project as a monorepo.

## Usage

### With cookiecutter cli

#### + From a location on the file system

(Example:  `c:\git\cookiecutter\t\python\uv-monorepo`):

```shell
cookiecutter c:\git\cookiecutter\t\python\uv-monorepo --output-dir=some/path/to/project
```

#### + Skip cookiecutter creation prompts

Skip prompts & render template using defaults defined in [`cookiecutter.json`](./cookiecutter.json):

```shell
cookiecutter c:\git\cookiecutter\t\python\uv-monorepo --no-input
```

#### + Install from a git(hub) repository

```shell
cookiecutter gh:<user>/cookiecutter --directory="t/python/uv-monorepo"

## OR
cookiecutter https://github.com/<user>/cookiecutter --directory="t/python/uv-monorepo"
```

### With nox

The included [`noxfile.py`](./{{cookiecutter.project_name}}/noxfile.py) has sessions for running cookiecutter commands.
