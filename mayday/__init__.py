import os
import json
import logging


class Config:

    def __init__(self):

        # AWS
        self.aws_access_key = os.environ.get('AWS_ACCESS_KEY')
        self.aws_access_secret_key = os.environ.get('AWS_ACCESS_SECRET_KEY')
        self.aws_s3_bucket = os.environ.get('AWS_S3_BUCKET')
        self.aws_s3_log_prefix = os.environ.get('AWS_S3_LOG_PREFIX')

        # API
        self.api_host = os.environ.get('api_host', 'localhost')
        self.api_port = os.environ.get('api_port', 10000)

        # FluentD
        self.fluentd_host = os.environ.get('fluentd_host', 'fluentd.cooomma.info')
        self.fluentd_port = os.environ.get('fluentd_port', 24224)

        # Redis
        self.redis_host = os.environ.get('REDIS_HOST', 'localhost')
        self.redis_port = os.environ.get('REDIS_PORT', 6627)
        self.redis_db = os.environ.get('REDIS_DB', 0)

        # Telegram
        self.telegram_token = os.environ['TELEGRAM_TOKEN']

    @property
    def aws_config(self) -> dict:
        return dict(
            access_key=self.aws_access_key,
            access_secret_key=self.aws_access_secret_key,
            s3_bucket=self.aws_s3_bucket,
            s3_log_prefix=self.aws_s3_log_prefix
        )

    @property
    def api_config(self) -> dict:
        return dict(host=self.api_host, port=self.api_port)

    @property
    def redis_config(self) -> dict:
        return dict(
            host=self.redis_host,
            port=self.redis_port,
            db=self.redis_db
        )

    @property
    def mongo_config(self) -> dict:
        return dict(hos=self.fluentd_host, port=self.fluentd_port)

    @property
    def telegram_config(self) -> dict:
        return dict(token=self.telegram_token)


STAGE = os.environ.get('stage', 'test').upper()
LOG_JSON_FORMAT = dict(
    ts='%(asctime)s',
    level='%(levelname)s',
    module='%(module)s.%(funcName)s',
    line_num='%(lineno)s',
    message='%(message)s'
)


def default_formatter() -> logging.Formatter:
    return logging.Formatter(
        fmt=json.dumps(LOG_JSON_FORMAT, ensure_ascii=False, sort_keys=True),
        datefmt='%Y-%m-%d %H:%M:%S'
    )


def console_handler() -> logging.Handler:
    handler = logging.StreamHandler()
    handler.setFormatter(LOG_JSON_FORMAT)
    return handler


def fluentd_handler() -> logging.Handler:
    # FIXME: add fluentd handler
    pass


def get_default_logger(log_name: str, log_level: int = logging.DEBUG) -> logging.Logger:
    logger = logging.getLogger(log_name)
    if STAGE == 'PRODUCTION':
        log_level = logging.INFO
    logger.setLevel(log_level)
    logger.addHandler(console_handler)
    return logger
