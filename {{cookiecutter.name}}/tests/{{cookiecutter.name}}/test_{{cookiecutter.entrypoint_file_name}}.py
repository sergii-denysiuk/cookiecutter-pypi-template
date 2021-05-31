import logging

from {{cookiecutter.name}}.{{cookiecutter.entrypoint_file_name}} import example

logger = logging.getLogger(__name__)


def test_example(test_example_params: int) -> None:
    logger.debug("Running test for parameter {test_example_params} ...")
    assert example(test_example_params) == test_example_params
