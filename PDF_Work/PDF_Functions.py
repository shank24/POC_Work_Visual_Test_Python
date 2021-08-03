import PyPDF2

#object = PyPDF2.PdfFileReader('C:\VS_Code_Python_POC\Visual_Test\PDF_Work\Azure.pdf')

# print(object.documentInfo)
# print(object.getNumPages())
# print(object.getPage(1).extractText())


def extract_information(pdf_path):
    with open(pdf_path, 'rb') as f:
        pdf = PyPDF2.PdfFileReader(f)
        information = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()
        page_1_text = pdf.getPage(1).extractText()

    txt = f"""
    Information about {pdf_path}: 

    Author: {information.author}
    Creator: {information.creator}
    Producer: {information.producer}
    Subject: {information.subject}
    Title: {information.title}
    Number of pages: {number_of_pages}
    Page 1 Text : {[page_1_text]}
    """
    print(txt)
    return information

        
if __name__ == '__main__':
    path = 'C:\VS_Code_Python_POC\Visual_Test\PDF_Work\Azure.pdf'
    extract_information(path)
