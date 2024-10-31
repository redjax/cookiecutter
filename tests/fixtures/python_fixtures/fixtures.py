import typing as t
from pytest import fixture


@fixture
def sandbox_dir(fs):
    ## Add templates directory to the fake filesystem
    fs.add_real_directory("t", lazy_read=False)

    sandbox = fs.create_dir("/sandbox")

    return sandbox


@fixture
def uv_template() -> t.Literal["t/python/uv"]:
    return "/t/python/uv"


@fixture
def pdm_template() -> t.Literal["t/python/pdm"]:
    return "/t/python/pdm"
