import fitz  # PyMuPDF

def extract_pages_with_annotations(input_path, output_path, page_numbers):
    # Open the input PDF
    input_pdf = fitz.open(input_path)
    
    # Create a new PDF for output
    output_pdf = fitz.open()
    
    # Convert 1-based page numbers to 0-based and handle negative indices
    for page_num in page_numbers:
        # Adjust for 0-based indexing and check bounds
        adjusted_num = page_num - 1
        if 0 <= adjusted_num < len(input_pdf):
            # Insert the page into the output PDF
            output_pdf.insert_pdf(input_pdf, from_page=adjusted_num, to_page=adjusted_num)
    
    # Save the output PDF
    output_pdf.save(output_path)
    output_pdf.close()
    input_pdf.close()

# Usage (same as before)
# extract_pages_with_annotations("jl.pdf", "output.pdf", [i for i in range(68,80)])

extract_pages_with_annotations("jl.pdf", "output.pdf", [i for i in range(68,80)])  # 54-67 68-80
