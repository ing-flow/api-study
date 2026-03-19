import logging
import os
import sys
from pythonjsonlogger import jsonlogger

from app.core.settings import settings
from app.middleware.request_id import request_id_var


LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)


class RequestIdFilter(logging.Filter):
    def filter(self, record):
        record.request_id = request_id_var.get()
        return True


def setup_logging():

    root_logger = logging.getLogger()
    root_logger.setLevel(settings.log_level)

    formatter = jsonlogger.JsonFormatter(
        "%(asctime)s %(levelname)s %(name)s %(message)s %(request_id)s",
        rename_fields={
            "asctime": "time",
            "levelname": "level",
            "name": "logger"
        }
    )

    request_filter = RequestIdFilter()

    # -------------------------
    # stdout（本番でも使う）
    # -------------------------
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    console_handler.addFilter(request_filter)

    root_logger.addHandler(console_handler)

    # -------------------------
    # local環境のみファイル
    # -------------------------
    if settings.env == "local":

        # app log
        app_handler = logging.FileHandler(f"{LOG_DIR}/app.log")
        app_handler.setFormatter(formatter)
        app_handler.addFilter(request_filter)

        # error log
        error_handler = logging.FileHandler(f"{LOG_DIR}/error.log")
        error_handler.setLevel(logging.ERROR)
        error_handler.setFormatter(formatter)
        error_handler.addFilter(request_filter)

        root_logger.addHandler(app_handler)
        root_logger.addHandler(error_handler)

    # -------------------------
    # access logger
    # -------------------------
    access_logger = logging.getLogger("access")
    access_logger.setLevel(settings.log_level)

    # stdout（本番）
    access_stream = logging.StreamHandler(sys.stdout)
    access_stream.setFormatter(formatter)
    access_stream.addFilter(request_filter)

    access_logger.addHandler(access_stream)

    # localのみファイル
    if settings.env == "local":
        access_file = logging.FileHandler(f"{LOG_DIR}/access.log")
        access_file.setFormatter(formatter)
        access_file.addFilter(request_filter)

        access_logger.addHandler(access_file)

    # rootに流さない（超重要）
    access_logger.propagate = False