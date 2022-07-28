command = input()
company_dict = {}
while command != "End":
    company_employee_text = command.split(" -> ")
    if company_employee_text[0] not in company_dict:
        company_dict[company_employee_text[0]] = []
    if company_employee_text[1] not in company_dict[company_employee_text[0]]:
        company_dict[company_employee_text[0]].append(company_employee_text[1])
    command = input()

for final_key, final_value in company_dict.items():
    print(f"{final_key}")
    for element in range(len(final_value)):
        print(f"-- {final_value[element]}")
