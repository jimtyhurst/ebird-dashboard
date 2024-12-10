import logging

LOG_FORMAT = "%(asctime)s:%(levelname)s:%(name)s:%(funcName)s:%(message)s"
LOG_FORMATTER = logging.Formatter(LOG_FORMAT)
EBIRD_DASHBOARD_LOG_FILE_NAME = "ebird-dashboard.log"
FILE_LOG_HANDLER = logging.FileHandler(
    EBIRD_DASHBOARD_LOG_FILE_NAME,
    mode="a",
    encoding="utf-8",
)
FILE_LOG_HANDLER.setFormatter(LOG_FORMATTER)
CONSOLE_LOG_HANDLER = logging.StreamHandler()
CONSOLE_LOG_HANDLER.setFormatter(LOG_FORMATTER)
logging.basicConfig(
    format=LOG_FORMAT, handlers=[CONSOLE_LOG_HANDLER, FILE_LOG_HANDLER], level=logging.WARNING
)


def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(name)
