import csv
from datetime import datetime

def export_report(results, filename="phishing_report.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["Email", "Score", "Status", "Date"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for email_file, res in results.items():
            writer.writerow({
                "Email": email_file,
                "Score": res["score"],
                "Status": res["status"],
                "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
