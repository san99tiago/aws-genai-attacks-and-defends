#!/usr/bin/env python3
import os
import sys

def extract_pdf_content(pdf_path):
    """Extract text content from PDF using available methods"""
    try:
        # Try with pdfplumber first
        import pdfplumber
        with pdfplumber.open(pdf_path) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text() or ""
            return text
    except ImportError:
        pass
    
    try:
        # Try with PyPDF2
        import PyPDF2
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
            return text
    except ImportError:
        pass
    
    try:
        # Try with pymupdf (fitz)
        import fitz
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            text += page.get_text()
        doc.close()
        return text
    except ImportError:
        pass
    
    # Fallback: try to read corresponding markdown file
    base_name = os.path.splitext(os.path.basename(pdf_path))[0]
    md_path = f"../cvs-sources/{base_name}.md"
    if os.path.exists(md_path):
        with open(md_path, 'r', encoding='utf-8') as f:
            return f.read()
    
    return "Could not extract content from PDF"

def analyze_cvs():
    """Analyze all CVs in the cvs-injected directory"""
    cvs_dir = "/Users/santigrc/Desktop/programming/aws-genai-attacks-and-defends/pdf-injections/cvs-injected"
    
    if not os.path.exists(cvs_dir):
        print("CVs directory not found!")
        return
    
    cv_data = {}
    
    # Extract content from all PDFs
    for filename in sorted(os.listdir(cvs_dir)):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(cvs_dir, filename)
            print(f"Processing: {filename}")
            print("=" * 50)
            
            content = extract_pdf_content(pdf_path)
            cv_data[filename] = content
            print(content)
            print("\n" + "=" * 50 + "\n")
    
    return cv_data

if __name__ == "__main__":
    analyze_cvs()
