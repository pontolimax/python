'''Een lijst woorden uit een URL ophalen en afdrukken.'''
import sys
from typing import Iterable
from urllib.request import urlopen


def fetch_words(url: str) -> list[str]:
    '''Een lijst woorden uit een URL ophalen.'''
    with urlopen(url) as story:
        story_words: list[str] = []
        for line in story:
            line_words: list[str] = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words


def print_items(items: Iterable) -> None:
    '''Een lijst afdrukken.'''
    for item in items:
        print(item)


def main(url: str) -> None:
    '''Een lijst woorden uit een URL ophalen en afdrukken.'''
    words: list[str] = fetch_words(url)
    print_items(words)


if __name__ == '__main__':
    main(sys.argv[1])
