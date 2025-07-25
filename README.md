
# 🖨️ Smart Print Monitoring on Windows 11 IoT

This project demonstrates a secure and auditable printing system built for Windows 11 IoT using only built-in Windows tools, Python, and mobile alerts via [ntfy.sh](https://ntfy.sh/).

## 🚀 Features
- Monitor all print jobs via spool folder.
- Secure log storage (admin-only access).
- Block user tampering (Task Manager, CMD, etc.).
- Alert admin if a file is printed more than 2 times.
- Works with ntfy.sh for mobile push notifications.

## 🧩 Use Cases
- Factories with 3D printers
- Admin or HR offices
- Label printers in logistics
- Any Windows IoT or embedded setup

## 📜 How it works

1. **Python script** monitors spool folder.
2. Logs are written to a secure shared folder (`Z:\Logs`).
3. If print count > 2, alert is sent via ntfy.
4. Users can't terminate or bypass the script (via GPO).

## 📷 Visual Overview
![Diagram](A_digital_infographic_features_a_smart_print_monit.png)

## 📦 Installation
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
