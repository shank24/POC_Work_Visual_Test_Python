import PyPDF2

#Merge Function

def merge_pdfs(paths, output_dir):
    pdf_writer = PyPDF2.PdfFileWriter()

    for path in paths:
        
        pdf_reader =  PyPDF2.PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
            #Add each page to the writer object
            pdf_writer.addPage(pdf_reader.getPage(page))
    
    #Write out the merged pdf file
    with open(output_dir, 'wb') as out:
        pdf_writer.write(out)

if __name__ == '__main__':
    paths = ['C:\VS_Code_Python_POC\Visual_Test\PDF_Work\Azure.pdf','C:\VS_Code_Python_POC\Visual_Test\PDF_Work\Report.pdf']
    merge_pdfs(paths, output_dir='merged.pdf')
