import logging
import sys


class ColorFormatter(logging.Formatter):
    RESET = "\033[0m"
    LEVEL_COLORS = {
        logging.DEBUG: "\033[33m",
        logging.INFO: "\033[32m",
        logging.WARNING: "\033[33m",
        logging.ERROR: "\033[31m",
        logging.CRITICAL: "\033[31m",
    }

    def format(self, record: logging.LogRecord) -> str:
        color = self.LEVEL_COLORS.get(record.levelno, self.RESET)
        record.levelname_colored = f"{color}{record.levelname:<8}{self.RESET}"
        return super().format(record)


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

    formatter = ColorFormatter(
        fmt="%(asctime)s | %(levelname_colored)s | %(name)-30s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    console_handler.setFormatter(formatter)

    logger.addHandler(console_handler)

    # Prevent log propagation to avoid duplicate messages
    logger.propagate = False

    return logger
