import click
import requests
import logging
from logging.handlers import RotatingFileHandler

# Function to setup logging


def setup_logging(log_level=logging.INFO):
    logger = logging.getLogger()
    logger.setLevel(log_level)
    handler = RotatingFileHandler('app.log', maxBytes=10000, backupCount=5)
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)


@click.command()
@click.argument('urls', nargs=-1)
@click.option('--log-level', default='INFO', help="Set the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)")
def check_sites(urls, log_level):
    """Simple program that checks if a website is up and measures response time."""
    numeric_level = getattr(logging, log_level.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError('Invalid log level: %s' % log_level)
    setup_logging(numeric_level)

    for url in urls:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                message = f"{url} is up. Response time: {response.elapsed.total_seconds()} seconds"
                click.echo(message)
                logging.info(message)
            else:
                message = f"{url} is down. Status Code: {response.status_code}"
                click.echo(message)
                logging.warning(message)
        except requests.RequestException as e:
            message = f"{url} is down. Error: {e}"
            click.echo(message)
            logging.error(message)


if __name__ == '__main__':
    check_sites()
