import re

# Load phishing keywords
with open("data/phishing_keywords.txt") as f:
    phishing_keywords = [line.strip().lower() for line in f]

suspicious_domains = ["bit.ly", "tinyurl.com", "short.ly"]

def analyze_email_content(email_content):
    content = email_content.lower()
    score = 0

    # Keyword analysis
    for kw in phishing_keywords:
        if kw in content:
            score += 1

    # Link analysis
    urls = re.findall(r'https?://[^\s]+', content)
    for url in urls:
        if any(domain in url for domain in suspicious_domains):
            score += 2

    # Determine status (matches CSS classes)
    if score >= 5:
        status = "red"
    elif score >= 2:
        status = "yellow"
    else:
        status = "green"

    return {"score": score, "status": status}
