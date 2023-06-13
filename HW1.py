import re

def extract_domains(emails):
    domains = set()
    pattern = r"@([\w\.-]+)"

    for email in emails:
        match = re.search(pattern, email)
        if match:
            domain = match.group(1)
            domains.add(domain)

    return domains

email_list = [
    "email1@hotmail.com",
    "email2@gmail.com",
    "email3@ok.kz",
    "email4@gmail.com"
]

result = extract_domains(email_list)
print(result)
input("press any key to close window")
