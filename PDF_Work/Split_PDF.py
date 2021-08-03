import PyPDF2

#Split Function

def split(path, name_of_split):
    pdf = PyPDF2.PdfFileReader(path)
    for page in range(pdf.getNumPages()):
        pdf_writer = PyPDF2.PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))

        output_dir = f'{name_of_split}{page}.pdf'
        with open(output_dir, 'wb') as output_pdf:
            pdf_writer.write(output_pdf)
    
if __name__ == '__main__':
    path = 'C:\VS_Code_Python_POC\Visual_Test\PDF_Work\Azure.pdf'
    split(path, 'Azure_page')