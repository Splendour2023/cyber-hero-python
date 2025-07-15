# 🧠 Wrong Password Checker - Cyber Hero Spell

correct_password = "OpenSesame"
tries = 0

while tries < 3:
    user_input = input("Enter the secret password: ")

    if user_input == correct_password:
        print("✅ Access Granted! Welcome, Hero.")
        break
    else:
        print("❌ Wrong password!")
        tries += 1

if tries == 3:
    print("🚨 Too many wrong tries! Alert the Cyber Guards!")
