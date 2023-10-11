from PyPDF2 import PdfMerger


def merge_pdfs(pdfs):
    merger = PdfMerger()
    for pdf in pdfs:
        merger.append(pdf)
    with open("Merged_File.pdf", 'wb') as f:
        merger.write(f)
        merger.close()


pdf_paths = [
    'files/atv-03-empreend.pdf',
    'files/horario.pdf',
]

pdf_files = []

for path in pdf_paths:
    pdf_files.append(open(path, 'rb'))

merge_pdfs(pdf_files)

for pdf in pdf_files:
    pdf.close()
