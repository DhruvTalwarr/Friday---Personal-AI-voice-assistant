import time
import datetime
import os

current_time = datetime.datetime.now().strftime("%H:%M")
stop_time = input("Enter stop time (e.g. 10:10): ")

a = float(current_time.replace(":", "."))
b = float(stop_time.replace(":", "."))
focus_duration = round(b - a, 3)

host_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com"]

print(f"Current time: {current_time}")
print("Blocking websites...")

# Block sites
with open(host_path, "r+") as file:
    content = file.read()
    for website in website_list:
        if website not in content:
            file.write(f"{redirect} {website}\n")
            print(f"Blocked: {website}")

print("✅ Focus Mode ON!")

# Wait until stop time
while True:
    now = datetime.datetime.now().strftime("%H:%M")
    if now >= stop_time:
        with open(host_path, "r+") as file:
            lines = file.readlines()
            file.seek(0)
            for line in lines:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("🟢 Websites unblocked!")
        with open("focus.txt", "a") as f:
            f.write(f",{focus_duration}")
        break

    time.sleep(30)

