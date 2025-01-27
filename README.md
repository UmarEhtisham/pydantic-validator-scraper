
# Pydantic Validation with BeautifulSoup

## Description

This project provides a simple Python-based solution to perform **Pydantic validation** alongside **BeautifulSoup** web scraping. It integrates these two libraries to facilitate data validation and scraping of web pages while ensuring the correctness of the scraped data.

## Project Setup

This project requires Python 3.13 or higher and uses the following dependencies:
- **BeautifulSoup**: For web scraping.
- **Pydantic**: For data validation.
- **Pydantic-Settings**: To manage settings with Pydantic models.
- **Requests**: To handle HTTP requests.
- **Datetime**: For handling date and time.

### Dependencies

You can install the dependencies by using **UV** package manager or by creating a virtual environment and installing the requirements manually.

#### 1. Using UV (if UV supports `pyproject.toml`):
```bash
uv install
```

#### 2. Using `pip` (with `requirements.txt`):
First, export the dependencies to `requirements.txt`:
```bash
pip install -r requirements.txt
```

Then, install the dependencies:
```bash
pip install -r requirements.txt
```

### Setting Up the Virtual Environment
It’s highly recommended to use a virtual environment to manage your dependencies.

Create and activate a virtual environment:
```bash
python -m venv venv
```

Activate the virtual environment:
- On Windows:
  ```bash
  .\venv\Scripts\activate
  ```
- On macOS/Linux:
  ```bash
  source venv/bin/activate
  ```

Once the environment is activated, run:
```bash
uv install  # or pip install -r requirements.txt if using pip
```

## Project Structure

```
pydantic-validator-scraper
project_root/
├── .env              # Environment variables (should be ignored by Git)
├── .gitignore        # Specifies intentionally untracked files that Git should ignore
├── .python-version   # Specifies the Python version for the project
├── config.py         # Configuration settings for the project
├── model.py          # Core logic/models of the project
├── pyproject.toml    # Project metadata and build system configuration (PEP 518)
├── README.md         # Project description and instructions
├── uv.lock           # Lockfile for uv dependency manager (if used)
└── __main__.py       # Main entry point of the application

```

## License

This project is licensed under the MIT License.
