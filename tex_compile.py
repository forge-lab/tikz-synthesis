from pdflatex import PDFLaTeX

def pdf_compile(infile):
    pdfl = PDFLaTeX.from_texfile(infile)
    pdf, log, completed_process = pdfl.create_pdf(keep_pdf_file=True, keep_log_file=True)
