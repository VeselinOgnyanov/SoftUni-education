destination = input()
total_savings = 0

while destination != "End":
    budget = float(input())

    while total_savings < budget:
        savings = float(input())
        total_savings += savings
    print(f"Going to {destination}!")
    destination = input()

    total_savings = 0

