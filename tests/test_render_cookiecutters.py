import pytest
import os
from pathlib import Path

from template_ctl import render_cookicutter


def test_render_uv_template(sandbox_dir, uv_template):
    try:
        # Render the template
        render_cookicutter(
            template=uv_template, output_dir=str(sandbox_dir.path), no_input=True
        )

        # Define the expected directory name
        expected_dir = Path(sandbox_dir.path) / "python-uv-base"

        # Check if the expected directory exists
        assert expected_dir.is_dir(), f"The directory '{expected_dir}' was not created."

    except Exception as exc:
        pytest.fail(f"Rendering template '{uv_template}' failed with error: {exc}")


def test_render_pdm_template(sandbox_dir, pdm_template):
    try:
        # Render the template
        render_cookicutter(
            template=pdm_template, output_dir=str(sandbox_dir.path), no_input=True
        )

        # Define the expected directory name
        expected_dir = Path(sandbox_dir.path) / "python-pdm-base"

        # Check if the expected directory exists
        assert expected_dir.is_dir(), f"The directory '{expected_dir}' was not created."

    except Exception as exc:
        pytest.fail(f"Rendering template '{pdm_template}' failed with error: {exc}")
