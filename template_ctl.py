import logging
import typing as t
from pathlib import Path

from cookiecutter.main import cookiecutter

log = logging.getLogger(__name__)

SANDBOX_DIR = Path("sandbox")


def prepare_sandbox(sandbox_dir: str = SANDBOX_DIR):
    if not Path(str(sandbox_dir)).exists():
        Path(str(sandbox_dir)).mkdir(parents=True, exist_ok=True)


def render_cookicutter(
    template: str,
    output_dir: str = ".",
    template_dir: str | None = None,
    extra_context: dict | None = None,
    checkout_branch: str | None = None,
    no_input: bool = False,
    overwrite: bool = False,
):

    log.info(
        f"Rendering cookiecutter template '{template}' to output directory '{output_dir}'"
    )
    try:
        cookiecutter(
            template=template,
            checkout=checkout_branch,
            no_input=no_input,
            extra_context=extra_context,
            overwrite_if_exists=False,
            output_dir=output_dir,
            directory=template_dir,
        )
    except Exception as exc:
        msg = f"({type(exc)}) Error rendering cookiecutter template. Details: {exc}"
        log.error(msg)

        raise exc


def main(no_input: bool = False):
    UV_TEMPLATE_PATH = "t/python/uv"
    PDM_TEMPLATE_PATH = "t/python/pdm"

    ## Test rendering Python UV cookiecutter
    render_cookicutter(
        template=UV_TEMPLATE_PATH, no_input=no_input, output_dir=SANDBOX_DIR
    )

    ## Test rendering Python PDM cookiecutter
    render_cookicutter(
        template=PDM_TEMPLATE_PATH, no_input=no_input, output_dir=SANDBOX_DIR
    )


if __name__ == "__main__":
    logging.basicConfig(
        level="INFO",
        format="%(asctime)s | [%(levelname)s] > %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S",
    )

    main(no_input=True)
