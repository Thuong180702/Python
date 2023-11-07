def extract_name_and_domain(email_list):
    name_domain_list = []

    for email in email_list:
        if "@" in email:
            name, domain = email.split("@")
            name_domain_list.append((name, domain))
        else:
            name_domain_list.append((email, ""))

    return name_domain_list


email_addresses = [
    "user@example.com",
    "john_doe@gmail.com",
    "support",
    "no_at_symbol.com",
]
result = extract_name_and_domain(email_addresses)

for name, domain in result:
    print(f"Name: {name}, Domain: {domain}")
