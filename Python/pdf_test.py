import PyPDF2

pdfFileObj = open('/home/ruanramos/Dropbox/UFRJ/Ciência da Computação/Livros/Livro Python for Informatics.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

print(pdfReader.numPages)

for i in range(pdfReader.numPages):
	pageObj = pdfReader.getPage(i)
	print(pageObj.extractText())

pdfFileObj.close()