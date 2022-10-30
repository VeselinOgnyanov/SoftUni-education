import re

number_of_barcodes = int(input())
collected_barcodes = []
current_group = ""
pattern = r"@#+\b[A-Z][A-Za-z0-9]{4,}[A-Z]\b@#+"

for _ in range(number_of_barcodes):
    current_barcode = input()
    founded_barcodes = re.findall(pattern, current_barcode)
    if founded_barcodes:
        for single_char in founded_barcodes:
            for single_element in single_char:
                if single_element.isdigit():
                    current_group += single_element
        if len(current_group) > 0:
            print(f"Product group: {current_group}")
            current_group = ""
        else:
            print("Product group: 00")
    else:
        print("Invalid barcode")






