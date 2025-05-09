from PyPDF2 import PdfReader, PdfWriter

def extract_pages_with_annotations(input_path, output_path, page_numbers):
    reader = PdfReader(input_path)
    writer = PdfWriter()
    
    for page_num in page_numbers:
        # Page numbers are 0-based in PyPDF2
        if 0 <= page_num - 1 < len(reader.pages):
            writer.add_page(reader.pages[page_num - 1])
    
    with open(output_path, "wb") as output_pdf:
        writer.write(output_pdf)

# Usage
extract_pages_with_annotations("jl.pdf", "output.pdf", [1, 3, 5])  # extracts pages 1, 3, 5
