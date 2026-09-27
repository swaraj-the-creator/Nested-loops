print("=== Grossary Billing Machine ===")
rice = honey_bottles = jaggery = 0
customers_served = 0
total_earned = 0
serving = True
while serving:
    print("Our store has: rice Rs 60/kg, honey Rs 45/bottle , jaggery Rs 50/kg")
    name = input("Enter customer name:")
    unt = int(input(f"Enter quantity of rice you have buyed :"))
    nt = int(input(f"Enter number of bottles of honey you have buyed :"))
    t = int(input(f"Enter quantity of jaggery you have buyed :"))
    if  unt == 0 and nt == 0 and t == 0:
        print("Please buy something to bill.\n")
        continue
    print(f"\n{name} buyed {unt} rice,{nt} bottles of honey and {t} jaggery:")
    idx = 1
    while idx <= 6:
        if idx == 1: value = 60
        elif idx == 2: value = 45
        else: value = 50
        count = value
        if count > 0:
            print(f"{count} x {value}- unit note(s) = ",count * value)
            if value == 60:rice += count
            elif value == 45:honey_bottles += count
            else: jaggery += count
        idx += 1
    customers_served += 1
    total_earned += unt * 60 + nt * 45 + 50 * t
    print(f"Billing complete,{name} !\n")
    again = input("Next customer? (yes/no)").strip().lower()
    if again != "yes":
        serving = False
print("\n=== Daily Denominator Report ===")
for slot in range(1,7):
    if slot == 1: value,total = unt * 60,rice
    elif slot == 2: value,total = nt * 45,honey_bottles
    else: value,total = t * 50,jaggery
    if total > 0:
        print(value,total,end="")
        for note in range(total):
            print("=",end="")
        print()
print("\nCustomers served : ",customers_served)
print("Total earned   : ",total_earned) 
print("Billing session closed. Goodbye")  
