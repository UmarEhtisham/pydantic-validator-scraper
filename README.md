
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

## Usage

### Example Code

Here’s a simple example to scrape a webpage and validate the scraped data using Pydantic.

```python
from bs4 import BeautifulSoup
import requests
from pydantic import BaseModel, ValidationError

class ScrapedData(BaseModel):
    title: str
    description: str

def scrape_and_validate(url: str):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    title = soup.find('title').get_text() if soup.find('title') else ''
    description = soup.find('meta', {'name': 'description'})['content'] if soup.find('meta', {'name': 'description'}) else ''
    
    try:
        data = ScrapedData(title=title, description=description)
        print("Scraped and validated data:", data)
    except ValidationError as e:
        print("Validation error:", e)

# Example usage
scrape_and_validate('https://example.com')
```

## Project Structure

```
pydantic-validation-beautifulsoup/
├── pyproject.toml
├── README.md
├── main.py
└── venv/
```

- `pyproject.toml`: Project configuration file.
- `README.md`: Documentation for the project (this file).
- `main.py`: The main script that contains the web scraping and validation logic.
- `venv/`: The virtual environment directory.

## Contributing

Feel free to fork the repository and create a pull request with improvements or bug fixes. Contributions are always welcome.

## License

This project is licensed under the MIT License.
