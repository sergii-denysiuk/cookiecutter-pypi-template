import logging

logger = logging.getLogger(__name__)


def example(n: int) -> int:
    logger.debug("Running example function ...")
    return n
