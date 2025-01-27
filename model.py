"""
Episode Model for TalkPython API Client

Defines the `Episode` model with attributes for episode details.

Usage:
------
1. Import the model:
   ```python
   from episode import Episode
   ```
2. Create an instance:
   ```python
   episode = Episode(
       show_number=1,
       date="2025-01-27",
       title="Introduction to Python",
       url="https://example.com/episode/1",
       guest="John Doe"
   )
   ```
"""

from pydantic import BaseModel, AnyHttpUrl
from datetime import date

class Episode(BaseModel):
    """
    Represents a podcast episode with details.

    Attributes:
    - show_number: Episode number.
    - date: Release date.
    - title: Title of the episode.
    - url: URL to access the episode.
    - guest: Guest featured in the episode.
    """

    show_number: int  # Episode number
    date: date  # Release date
    title: str  # Episode title
    url: AnyHttpUrl  # URL of the episode
    guest: str  # Guest featured in the episode

# Example usage
if __name__ == "__main__":
    example_episode = Episode(
        show_number=1,
        date="2025-01-27",
        title="Introduction to Python",
        url="https://example.com/episode/1",
        guest="John Doe"
    )
    print(example_episode)
