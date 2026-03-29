# ============================================================
# Script:      regex_log_parser.py
# Author:      Joshua Gouvisis
# Date:        March 2026
# Certificate: Google Cybersecurity Professional Certificate
# Lab:         Use Regular Expressions to Find Patterns
#
# Description: Uses Python regular expressions (regex) to
#              extract IP addresses and device identifiers
#              from security log data for threat investigation.
# ============================================================

import re

# --- Step 1: Define sample security log data ---
log_data = """
2026-03-01 08:14:22 User elarson logged in from 192.168.1.105 on device a-1158
2026-03-01 08:45:11 User bmoreno failed login from 10.0.0.22 on device b-2079
2026-03-01 09:03:55 User tshah logged in from 172.16.254.1 on device a-3897
2026-03-01 09:17:42 Unknown user attempted access from 192.168.58.57 on device c-9182
2026-03-01 09:45:30 User sgilmore logged in from 10.10.10.10 on device b-4421
2026-03-01 10:02:17 User eraab failed login from 192.168.201.40 on device a-7734
2026-03-01 10:30:44 Repeated failed attempts from 192.168.97.105 on device c-1023
2026-03-01 11:00:08 User jsmith logged in from 203.0.113.5 on device b-8856
"""

# --- Step 2: Extract all IP addresses using regex ---
# Pattern breakdown:
#   \d{1,3}  = 1 to 3 digits
#   \.       = literal dot
#   repeated 4 times for full IPv4 format

ip_pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
extracted_ips = re.findall(ip_pattern, log_data)

print("=" * 55)
print("EXTRACTED IP ADDRESSES FROM LOG")
print("=" * 55)
for ip in extracted_ips:
    print(f"  {ip}")

# --- Step 3: Extract all device IDs using regex ---
# Pattern breakdown:
#   [a-c]   = device prefix letter (a, b, or c)
#   -       = literal hyphen
#   \d{4}   = exactly 4 digits

device_pattern = r"[a-c]-\d{4}"
extracted_devices = re.findall(device_pattern, log_data)

print("\n" + "=" * 55)
print("EXTRACTED DEVICE IDs FROM LOG")
print("=" * 55)
for device in extracted_devices:
    print(f"  {device}")

# --- Step 4: Flag suspicious IPs from a known watchlist ---
watchlist = ["192.168.97.105", "192.168.58.57", "192.168.201.40"]

print("\n" + "=" * 55)
print("WATCHLIST CROSS-REFERENCE")
print("=" * 55)

flagged = []
for ip in extracted_ips:
    if ip in watchlist:
        flagged.append(ip)
        print(f"  [ALERT] Flagged IP detected: {ip}")

if not flagged:
    print("  No watchlist IPs detected in this log.")

# --- Step 5: Summary report ---
print("\n" + "=" * 55)
print("SUMMARY REPORT")
print("=" * 55)
print(f"  Total IPs found:        {len(extracted_ips)}")
print(f"  Total devices found:    {len(extracted_devices)}")
print(f"  Watchlist matches:      {len(flagged)}")
print("=" * 55)
print("Log analysis complete.")
