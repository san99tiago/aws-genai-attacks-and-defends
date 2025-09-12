#!/usr/bin/env python3
import os
import markdown
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import black, blue
import re


def markdown_to_pdf(md_file, pdf_file):
    # Read markdown file
    with open(md_file, "r", encoding="utf-8") as f:
        md_content = f.read()

    # Convert markdown to HTML
    html = markdown.markdown(md_content)

    # Create PDF
    doc = SimpleDocTemplate(
        pdf_file,
        pagesize=letter,
        rightMargin=0.5 * inch,
        leftMargin=0.5 * inch,
        topMargin=0.5 * inch,
        bottomMargin=0.5 * inch,
    )

    # Get styles
    styles = getSampleStyleSheet()

    # Custom styles - reduced spacing and font sizes
    title_style = ParagraphStyle(
        "CustomTitle",
        parent=styles["Heading1"],
        fontSize=14,
        spaceAfter=3,
        textColor=black,
        fontName="Helvetica-Bold",
    )

    subtitle_style = ParagraphStyle(
        "CustomSubtitle",
        parent=styles["Normal"],
        fontSize=10,
        spaceAfter=6,
        textColor=blue,
        fontName="Helvetica-Bold",
    )

    heading_style = ParagraphStyle(
        "CustomHeading",
        parent=styles["Heading2"],
        fontSize=10,
        spaceAfter=3,
        spaceBefore=6,
        textColor=black,
        fontName="Helvetica-Bold",
    )

    normal_style = ParagraphStyle(
        "CustomNormal",
        parent=styles["Normal"],
        fontSize=8,
        spaceAfter=2,
        fontName="Helvetica",
    )

    # Parse content
    story = []
    lines = md_content.split("\n")

    for line in lines:
        line = line.strip()
        if not line:
            continue

        if line.startswith("# "):
            # Main title
            name = line[2:].strip()
            story.append(Paragraph(name, title_style))
        elif line.startswith("**") and line.endswith("**") and "DevOps" in line:
            # Job title
            title = line[2:-2]
            story.append(Paragraph(title, subtitle_style))
        elif line.startswith("## "):
            # Section headers
            header = line[3:].strip()
            story.append(Paragraph(header, heading_style))
        elif line.startswith("**") and line.endswith("**"):
            # Bold text (job titles, companies)
            bold_text = line[2:-2]
            story.append(Paragraph(f"<b>{bold_text}</b>", normal_style))
        elif line.startswith("- "):
            # Bullet points
            bullet = line[2:].strip()
            story.append(Paragraph(f"• {bullet}", normal_style))
        elif line.startswith("📧") or line.startswith("📱") or line.startswith("🌐"):
            # Contact info
            story.append(Paragraph(line, normal_style))
        elif line and not line.startswith("#"):
            # Regular text
            story.append(Paragraph(line, normal_style))

    # Build PDF
    doc.build(story)
    print(f"Generated: {pdf_file}")


def main():
    md_dir = "pdf-injections/original-cvs"

    # Process all markdown files
    for filename in os.listdir(md_dir):
        if filename.endswith(".md"):
            md_file = os.path.join(md_dir, filename)
            pdf_file = os.path.join(md_dir, filename.replace(".md", ".pdf"))
            markdown_to_pdf(md_file, pdf_file)


if __name__ == "__main__":
    main()
