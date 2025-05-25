from PyPDF2 import PdfReader

def check_formatting(uploaded_file):
    reader = PdfReader(uploaded_file)
    format_issues = {
        "font_sizes": set(),
        "section_headers": [],
        "layout_issues": []
    }

    for page in reader.pages:
        try:
            text = page.extract_text()
            if "contact" not in text.lower():
                format_issues["layout_issues"].append("Missing 'Contact' section")
            if "experience" not in text.lower():
                format_issues["layout_issues"].append("Missing 'Experience' section")
            if "education" not in text.lower():
                format_issues["layout_issues"].append("Missing 'Education' section")
        except:
            format_issues["layout_issues"].append("Error reading formatting on page")

    return format_issues
