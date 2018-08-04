import csv
import re
import PyPDF2

f = open('download_link.csv', 'r')
c_read = csv.reader(f)

website = ''

for row in c_read:
    website += row[2]

# print(website)
pattern = r'[\w_.]+@[\w_.-]'

f = open('Contact_Email_Information.pdf', 'rb')
pdf = PyPDF2.PdfFileReader(f)

# print(pdf.numPages)

for n in range(pdf.numPages):

    page = pdf.getPage(n)
    page_text = page.extractText()

    match = re.search(pattern, page_text)

    if match:
        print(match.group())
