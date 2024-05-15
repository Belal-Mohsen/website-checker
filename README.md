# Website Checker

## Description

Website Checker is a Python command-line tool that checks the availability and response time of websites. This tool utilizes the power of `requests` and `click` libraries to provide a user-friendly command-line interface for checking the status of one or more URLs.

## Features

- Check multiple URLs in a single command
- Configurable logging levels
- Detailed log output with response time and status codes

## Installation

### Prerequisites

- Python 3.10+
- pip

### Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/website-checker.git
   cd website-checker
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. (Optional) Build and run using Docker:
   ```bash
   docker build -t website-checker .
   docker run -p 80:80 website-checker
   ```

## Usage

Run the tool from the command line:

```bash
python -m check_sites.main --urls [URL1] [URL2] ... [--log-level LEVEL]
```

Replace `[URL1] [URL2] ...` with the URLs you want to check and `LEVEL` with your desired log level (DEBUG, INFO, WARNING, ERROR, CRITICAL).

### Examples

```bash
python -m check_sites.main --urls http://example.com http://example.org --log-level INFO
```

## Testing

To run tests, navigate to the project directory and execute:

```bash
pytest
```

## CI/CD

This project is configured with GitHub Actions to ensure code quality and perform automated tests. The workflow details can be found under `.github/workflows/python-app.yml`.

## Development

### Adding new features

1. Create a new branch:
   ```bash
   git checkout -b feature/your-new-feature
   ```
2. Implement your feature and commit changes:
   ```bash
   git commit -am "Add some feature"
   ```
3. Push to the branch:
   ```bash
   git push origin feature/your-new-feature
   ```
4. Submit a pull request.

### Reporting issues

Please use GitHub Issues to report any bugs or feature requests.
