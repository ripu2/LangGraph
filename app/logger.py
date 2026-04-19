import logging
import sys


def setup_logger(name: str = None, level: int = logging.DEBUG) -> logging.Logger:
    """
    Creates and returns a configured logger instance.

    Args:
        name: Logger name (usually __name__ of the calling module).
              If None, configures the root logger.
        level: Logging level (default: DEBUG to capture full agentic flow).

    Returns:
        Configured logging.Logger instance.
    """
    logger = logging.getLogger(name)

    # Avoid adding duplicate handlers if logger already has them
    if logger.handlers:
        return logger

    logger.setLevel(level)

    # Console handler with detailed formatting
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(level)

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)-8s | %(name)-30s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    console_handler.setFormatter(formatter)

    logger.addHandler(console_handler)

    # Prevent log propagation to avoid duplicate messages
    logger.propagate = False

    return logger
