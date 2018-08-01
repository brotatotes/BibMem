import requests
from bs4 import BeautifulSoup

class Bible:
    ROOTLINK = "https://www.bible.com/bible/"

    VERSIONS = {
        "esv": "59",
        "niv": "111",
        "nkjv": "114",
        "amp": "1588"
    }

    OLD_TESTAMENT = [
        "genesis",
        "exodus",
        "leviticus",
        "numbers",
        "deuteronomy",
        "joshua",
        "judges",
        "ruth",
        "1 samuel",
        "2 samuel",
        "1 kings",
        "2 kings",
        "1 chronicles",
        "2 chronicles",
        "ezra",
        "nehemiah",
        "esther",
        "job",
        "psalms",
        "proverbs",
        "ecclesiastes",
        "song of solomon",
        "isaiah",
        "jeremiah",
        "lamentations",
        "ezekiel",
        "daniel",
        "hosea",
        "joel",
        "amos",
        "obadiah",
        "jonah",
        "micah",
        "nahum",
        "habakkuk",
        "zephaniah",
        "haggai",
        "zechariah",
        "malachi"
    ]

    NEW_TESTAMENT = [
        "matthew",
        "mark",
        "luke",
        "john",
        "acts",
        "romans",
        "1 chorinthians",
        "2 chorinthians",
        "galatians",
        "ephesians",
        "philippians",
        "colossians",
        "1 thessalonians",
        "2 thessalonians",
        "1 timothy",
        "2 timothy",
        "titus",
        "philemon",
        "hebrews",
        "james",
        "1 peter",
        "2 peter",
        "1 john",
        "2 john",
        "3 john",
        "jude",
        "revelation"
    ]

    BOOKS = OLD_TESTAMENT + NEW_TESTAMENT

    CHAPTERS = [
        50, 40, 27, 36, 34, 24, 21, 4, 31, 24, 22, 25, 29, 36, 10, 13, 10, 42, 150, 31, 12, 8, 66, 52, 5, 48, 12, 14, 3, 9, 1, 4, 7, 3, 3, 3, 2, 14, 4, 28, 16, 24, 21, 28, 16, 16, 13, 6, 6, 4, 4, 5, 3, 6, 4, 3, 1, 13, 5, 5, 3, 5, 1, 1, 1, 22
    ]

    def get_book_id(self, book):
        if book in self.NEW_TESTAMENT or book in self.OLD_TESTAMENT:
            return book.replace(" ","")[:3]
        else:
            raise Exception("Unrecognized Book: {}".format(book))

    # Retrieves verse. Returns empty string upon failure.
    def get_verse(self, book, chapter, verse, version):
        link = self.ROOTLINK + self.VERSIONS[version] + '/' + self.get_book_id(book) + '.' + str(chapter) + '.' + str(verse)
        html = requests.get(link).text
        soup = BeautifulSoup(html, 'html.parser')
        verse = soup.title.text
        return verse[verse.index(';') + 2:]

    def is_book(self, book):
        return book in self.NEW_TESTAMENT or book in self.OLD_TESTAMENT

    # def capitalize(self, book):
    #     return ' '.join(word.capitalize() for word in book.split())

if __name__ == "__main__":
    b = Bible()
    print(b.get_verse("romans", 6, 5, "nkjv"))
