import PyPDF2

#Extract Function

def extract_information(pdf_path):
    with open(pdf_path, 'rb') as f:
        pdf = PyPDF2.PdfFileReader(f)
        information = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()

    txt = f"""
    Information about {pdf_path}: 

    Author: {information.author}
    Creator: {information.creator}
    Producer: {information.producer}
    Subject: {information.subject}
    Title: {information.title}
    Number of pages: {number_of_pages}
    """
    print(txt)
    return information

        
if __name__ == '__main__':
    path = 'C:\VS_Code_Python_POC\Visual_Test\PDF_Work\Azure.pdf'
    extract_information(path)


#PyPDF2.PdfFileReader('Azure.pdf')
