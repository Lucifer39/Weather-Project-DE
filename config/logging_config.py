import logging.config

class ProgressFilter(logging.Filter):
    def filter(self, record):
        message = record.getMessage()
        return any(keyword in message for keyword in ("SUCCESS", "FAILED", "Task completed"))

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,

    "formatters": {
        "standard": {
            "format": "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
        }
    },

    "filters": {
        "progress_only": {
            "()": "config.logging_config.ProgressFilter"
        }
    },

    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "standard",
            "filters": ["progress_only"],
            "stream":  "ext://sys.stdout"
        },
        "file": {
            "class": "logging.FileHandler",
            "level": "INFO",
            "formatter": "standard",
            "filename": "logs/fetch_weather.log",
            "mode": "a"
        }
    },

    "root": {
        "level": "INFO",
        "handlers": ["console", "file"]
    }
}

def setup_logging():
    import os
    os.makedirs("logs", exist_ok=True)
    logging.config.dictConfig(LOGGING_CONFIG)
