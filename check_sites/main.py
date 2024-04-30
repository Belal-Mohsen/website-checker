import click
import requests


@click.command()
@click.argument('urls', nargs=-1)
def check_sites(urls):
    """Simple program that checks if a website is up and measures response time."""
    for url in urls:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                click.echo(
                    f"{url} is up. Response time: {response.elapsed.total_seconds()} seconds")
            else:
                click.echo(
                    f"{url} is down. Status Code: {response.status_code}")
        except requests.RequestException as e:
            click.echo(f"{url} is down. Error: {e}")


if __name__ == '__main__':
    check_sites()
