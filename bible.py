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
        "deuteronomy",
        "joshua",
        "judges",
        "ruth",
        "1 samuel",
        "2 samuel",
        "1 kings",
        "2 kings",
        "1 chronicles",
        "2 chronicles"
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

if __name__ == "__main__":
    b = Bible()
    print(b.get_verse("romans", 6, 5, "nkjv"))
