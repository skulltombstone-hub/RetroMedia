import fitz

class PDFBook:

    def __init__(self, path):

        self.doc = fitz.open(path)

    def page_count(self):

        return len(self.doc)

    def render_page(self, index):

        page = self.doc[index]

        pix = page.get_pixmap()

        return pix
