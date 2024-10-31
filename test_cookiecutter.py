import logging
import typing as t
from pathlib import Path

from cookiecutter.main import cookiecutter


def render_uv(output_dir: str = "test", no_input: bool = False):
    output_dir: Path = (
        Path(str(output_dir)).expanduser()
        if "~" in str(output_dir)
        else Path(str(output_dir))
    )

    if not Path(str(output_dir)).exists():
        output_dir.mkdir(parents=True, exist_ok=True)

    cookiecutter(template="t/python/uv", output_dir=output_dir, no_input=no_input)


def main(no_input: bool = False):
    render_uv(no_input=no_input)


if __name__ == "__main__":
    main(no_input=True)
