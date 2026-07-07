from booksconv.mp3conv import BooksManager

if __name__ == "__main__":
    buff = BooksManager()
    #buff.convert_wordfile_to_mp3(book="data/Example.docx", mp3_path="output/word_test.mp3", language="en")
    buff.convert_pdf_to_mp3(pdf_filename="data/Example.pdf", mp3_filename="output/pdf_test.mp3", language="en")