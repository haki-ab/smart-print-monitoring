import requests

csv_file = r"C:\Program Files (x86)\PaperCut Print Logger\logs\csv\papercut-print-log-all-time.csv"
target_keyword = "salary 2025".lower()
threshold = 2
ntfy_topic = "https://ntfy.sh/haki-lab"

count = 0

with open(csv_file, "r", encoding="utf-8", errors="ignore") as f:
    for line in f:
        if target_keyword in line.lower():
            count += 1

if count > threshold:
    msg = f"🚨 Sensitive document '{target_keyword}' printed {count} times!"
    requests.post(ntfy_topic, data=msg.encode("utf-8"))
    with open("alerts.log", "a", encoding="utf-8") as log:
        log.write(f"{msg}\n")
    print("✅ Notification sent.")
else:
    print(f"ℹ️ Under threshold: {count} times.")
