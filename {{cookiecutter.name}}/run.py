import logging
import logging.config

from argparse import ArgumentParser
from pathlib import Path

from {{cookiecutter.name}}.{{cookiecutter.entrypoint_file_name}} import example

logging.config.fileConfig(str(Path(__file__).resolve().parent / "logging.ini"))
logger = logging.getLogger(f"{Path(__file__).stem}.Run")


if __name__ == "__main__":
    argparse = ArgumentParser()
    argparse.add_argument("example_param", type=int, help="Example parameter.")
    argparse.add_argument(
        "--print", action="store_true", help="Print results to the console."
    )
    args = argparse.parse_args()

    result = example(args.example_param)

    if args.print:
        logger.debug("The results is {results}.")
