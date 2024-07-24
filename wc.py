import sys
import argparse

from io import SEEK_SET, BufferedReader


def getArgumentParser() -> argparse.ArgumentParser:
    """
    Parse namespace
    """
    parser = argparse.ArgumentParser(description="Custom WC")
    parser.add_argument(
        "-c", action="store_true", help="Count number of bytes of the file"
    )
    parser.add_argument(
        "-l", action="store_true", help="Count number of lines of the file"
    )
    parser.add_argument(
        "-m", action="store_true", help="Count number of lines of the file"
    )
    parser.add_argument("file", type=argparse.FileType("rb"), help="File to be used")

    return parser


def getNumberOfBytes(file: BufferedReader):
    """
    Return the number of bytes of the file
    """
    lines = file.readlines()
    file.seek(0, SEEK_SET)
    return sum([len(line) for line in lines])


def getNumberOfLines(file: BufferedReader):
    """
    Return the number of bytes of the file
    """
    lines = file.readlines()
    file.seek(0, SEEK_SET)
    return len(lines)


def getNumberOfCharacters(file: BufferedReader):
    """
    Return the number of characters of the file
    """

    def getCharacterCountForLine(line: bytes):
        return len(line.decode())

    return sum([getCharacterCountForLine(line) for line in file.readlines()])


if __name__ == "__main__":

    _, *args = sys.argv
    argParser = getArgumentParser()
    values = argParser.parse_args(args)

    bytes_ft = "Bytes: %s\n" % getNumberOfBytes(values.file)
    lines_ft = "Lines: %s\n" % getNumberOfLines(values.file)
    characters_ft = "Characters: %s\n" % getNumberOfCharacters(values.file)

    toPrint = ""
    toPrint += bytes_ft if values.c else ""
    toPrint += lines_ft if values.l else ""
    toPrint += characters_ft if values.m else ""

    if not toPrint:
        toPrint = bytes_ft + lines_ft + characters_ft
    print()
