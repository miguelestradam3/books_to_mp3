class BooksManager:
    # Attributes
    success = False
    content = ''

    #Methods
    def __init__(self):
        self.os = __import__("os")
        from gtts import gTTS
        from PyPDF2 import PdfReader
        import docx
        self.PdfReader = PdfReader
        self.gTTS = gTTS
        self.docx = docx
        print("Starting book conversion to MP3...")

    def convert_wordfile_to_mp3(self, book:str, mp3_path:str, language:str)->None:
        try:
            doc = self.docx.Document(book)
            fullText = []
            delimiter = " " # Define a delimiter
            for para in doc.paragraphs:
                fullText.append(para.text)
            self.content = delimiter.join(fullText)
            myobj = self.gTTS(text=self.content, lang=language, slow=False)
            myobj.save(mp3_path)
            self.success = True
        except Exception as Error:
            print("ERROR: {}".format(Error))
            self.success = False

    def convert_pdf_to_mp3(self, pdf_filename:str, mp3_filename:str, language:str)->None:
        try:
            text = ""
            with open(pdf_filename, "rb") as file:
                reader = self.PdfReader(file)
                number_of_pages = len(reader.pages)
                for page in range(number_of_pages):
                    text += reader.pages[page].extract_text()
            speech = self.gTTS(text=text, lang=language, slow=False)
            speech.save(mp3_filename)
            self.success = True
        except Exception as Error:
            print("ERROR: {}".format(Error))
            self.success = False

    def __del__(self):
        if self.success:
            print ("The process was a success...")
        else:
            print("It was not possible to do the conversion...")