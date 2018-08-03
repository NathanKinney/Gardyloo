import PyPDF2




# opening and reading pdf
# f = open('Working_Business_Proposal.pdf', 'rb')
# pdf_reader = PyPDF2.PdfFileReader(f)
#
# pdf_reader.numPages
#
# page_one = pdf_reader.getPage(0)
# page_one_text = page_one.extractText()

#appending to pdf
# f = open('Working_Business_Proposal.pdf', 'rb')
# pdf_reader = PyPDF2.PdfFileReader(f)
# first_page = pdf_reader.getPage(0)
# pdf_writer = PyPDF2.PdfFileWriter()
# pdf_writer.addPage(first_page)
# pdf_output = open('Some_NEW_FILE.PDF', 'wb')
# pdf_writer.write(pdf_output)
# f.close()
# pdf_output.close()
# print(pdf_output)

f = open('Working_Business_Proposal.pdf', 'rb')

pdf_text = []

pdf_reader = PyPDF2.PdfFileReader(f)

for p in range(pdf_reader.numPages):
    page = pdf_reader.getPage(p)
    pdf_text.append(page.extractText())

for line in pdf_text:
    print(line)

