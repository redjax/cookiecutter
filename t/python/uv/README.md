# Python + UV Cookiecutter

A Python cookiecutter template using [uv](https://docs.astral.sh/uv/) for dependency & project management.

## Usage

```shell
cookiecutter gh:redjax/cookiecutter --directory="t/python/uv"
```

### With cookiecutter cli

#### + From a location on the file system

(Example:  `c:\git\cookiecutter\t\python\uv`):

```shell
cookiecutter c:\git\cookiecutter\t\python\uv --output-dir=some/path/to/project
```

#### + Skip cookiecutter creation prompts

Skip prompts & render template using defaults defined in [`cookiecutter.json`](./cookiecutter.json):

```shell
cookiecutter c:\git\cookiecutter\t\python\uv --no-input
```

#### + Install from a git(hub) repository

```shell
cookiecutter gh:<user>/cookiecutter --directory="path/to/template/dir/in/repo"

## OR
cookiecutter https://github.com/<user>/cookiecutter --directory="t/python/cookiecutter-python-uv"
```
