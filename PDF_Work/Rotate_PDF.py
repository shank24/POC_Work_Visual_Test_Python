import PyPDF2

#Rotate Function

def rotate_pages(pdf_path):
    pdf_writer = PyPDF2.PdfFileWriter()
    pdf_reader = PyPDF2.PdfFileReader(pdf_path)
    #Rotate page 90 Degrees to the right
    page_1 = pdf_reader.getPage(0).rotateClockwise(90)
    pdf_writer.addPage(page_1)
    #Rotate page 90 Degrees to the left
    page_2 = pdf_reader.getPage(1).rotateCounterClockwise(90)
    pdf_writer.addPage(page_2)
    # Add a page in normal orientation
    #pdf_writer.addPage(pdf_reader.getPage(2))

    with open('rotate_pages.pdf', 'wb') as fh:
        pdf_writer.write(fh)


if __name__ == '__main__':
    path = 'C:\VS_Code_Python_POC\Visual_Test\PDF_Work\Azure.pdf'
    rotate_pages(path)


