from pathlib import Path


def read_file(path: str) -> str:
    return Path(path).read_text()


def read_file_and_splitlines(path: str) -> list[str]:
    return Path(path).read_text().splitlines()
