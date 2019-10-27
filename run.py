import logging
from logging.config import dictConfig
from aiohttp import web
from app import create_app
from config import LOGGING_CONFIG


dictConfig(LOGGING_CONFIG)
app = create_app()


if __name__ == "__main__":
    web.run_app(app, host='0.0.0.0', port=5000)
else:
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
