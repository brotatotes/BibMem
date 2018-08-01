import difflib
import string

class Diff:
    exclude = string.punctuation

    def __init__(self, actual='', typed=''):
        if actual:
            self.set_actual(actual)
        if typed:
            self.set_typed(typed)

    def set_actual(self, actual):
        self.actual = ''.join([c for c in actual.lower() if c not in self.exclude]).split()

    def set_typed(self, typed):
        self.typed = ''.join([c for c in typed.lower() if c not in self.exclude]).split()

    def generate_html(self):
        diff = difflib.HtmlDiff().make_file(self.actual, self.typed)
        return diff

if __name__ == '__main__':
    d = Diff("I am trying to compare two text files and output the first string iasdn the comparison file that does not match buasdf t am having difficulty since I am very new to python. Can anybody please give me a sample way to use this module.", "I am trying to compare two text files and output the first string in the comparison file that does not match butm aving difficulty since I am very new to python. Can anybody pse give me a sample way to use this module.")
    d.generate_html()
