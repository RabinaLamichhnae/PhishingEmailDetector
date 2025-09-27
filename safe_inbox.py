from email_analyzer import analyze_email

def filter_inbox(email_files):
    safe_emails = []
    for file in email_files:
        result = analyze_email(file)
        if result["status"] == "Safe (Green)":
            safe_emails.append(file)
    return safe_emails
