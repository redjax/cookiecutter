# Docker Compose Basic Cookiecutter

A `cookiecutter` template to get started with a Docker Compose file. Initializes a directory with a `.gitignore`, `.env.example`, `compose.yml`, and `README.md`.

## Usage

```shell
cookiecutter gh:redjax/cookiecutter --directory="t/docker/compose-basic"
```

### With cookiecutter CLI

#### + From a location on the file system

(Example: c:\git\cookiecutter\t\docker\compose-basic):

```shell
cookiecutter c:\git\cookiecutter\t\docker\compose-basic --output=some/path/to/project
```

#### + Skip cookiecutter creation prompts

Skip prompts & render template using defaults defined in [`cookiecutter.json`](./cookiecutter.json):

```shell
cookiecutter c:\git\cookiecutter\t\docker\compose-basic --no-input
```

#### + Install from a git(hub) repository

```shell
cookiecutter gh:<user>/cookiecutter --directory="path/to/template/dir/in/repo"
```
