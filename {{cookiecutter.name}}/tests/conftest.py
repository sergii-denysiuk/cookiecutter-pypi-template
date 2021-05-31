from pathlib import Path

import pytest

PROJECT_ROOT_DIR_PATH = Path(__file__).resolve().parents[1]


@pytest.fixture(
    name="test_example_params",
    params=[1, 2],
)
def get_test_example_params(
    request,
) -> int:
    n: int = request.param
    return n
