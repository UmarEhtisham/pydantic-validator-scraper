"""
Configuration Module for TalkPython API Client

This module provides a configuration class using Pydantic for managing settings and a cached utility function for efficient retrieval.

Usage:
1. Add a `.env` file with:
   ```env
   base_url=https://example.com
   episodes_path=/api/episodes
   api_key=your_api_key_here
   ```
2. Access configuration via:
   ```python
   from config import get_config
   config = get_config()
   print(config.page_url)
   ```
"""

from functools import lru_cache
from pydantic_settings import BaseSettings

class Config(BaseSettings):
    """
    Configuration class for the TalkPython API Client.

    Attributes:
    - base_url: Base URL of the site.
    - episodes_path: Path for episodes API.
    - api_key: API key for authentication.
    - headers: Default request headers.

    Methods:
    - page_url: Constructs the full episodes URL.
    """

    base_url: str  # Base URL for the site
    episodes_path: str  # Path for all episodes
    api_key: str  # API key for authentication (empty by default)
    headers: dict = {"User-Agent": "TalkPython API Client"}  # Default headers

    model_config = {
        "env_file": ".env"  # Specify the environment file location
    }

    @property
    def page_url(self) -> str:
        """
        Returns the full URL for accessing episodes.
        """
        return f"{self.base_url}{self.episodes_path}"

@lru_cache
def get_config() -> Config:
    """
    Returns a cached instance of the Config class.
    """
    return Config()

# Make the config globally available
config = get_config()

# Example usage
if __name__ == "__main__":
    print("Base URL:", config.base_url)
    print("Episodes Path:", config.episodes_path)
    print("Full Episodes URL:", config.page_url)
