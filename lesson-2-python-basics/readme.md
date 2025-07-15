# Lesson 2: Python Basics for Cyber Heroes

This script lets a user try to guess the secret password. If they get it wrong 3 times, they are blocked!

## 🧠 How the Code Works (Explained like a kid):

```python
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
