# ============================================================
# Script:      import_and_parse_a_text_file.py
# Author:      Joshua Gouvisis
# Date:        March 2026
# Certificate: Google Cybersecurity Professional Certificate
# Lab:         Import and Parse a Text File
#
# Description: Uses Python's built-in file-handling functions
#              to import and parse security log files. Covers
#              read, append, and write file modes, the with
#              statement, .read(), .split(), and .write() to
#              prepare log data and an IP allow list for
#              security analysis.
# ============================================================


# ============================================================
# TASK 1 — Open a Security Log File
#
# The "with" statement is the preferred pattern for file
# handling in Python. It automatically closes the file after
# the indented block completes, even if an exception occurs.
# open() is called with "r" (read mode) as the second argument.
# ============================================================

print("=" * 55)
print("TASK 1 — Open a Security Log File")
print("=" * 55)

# --- Create the login.txt file for demonstration ---
login_data = """username,ip_address,time,date
tshah,192.168.92.147,15:26:08,2022-05-10
dtanaka,192.168.98.221,9:45:18,2022-05-09
tmitchel,192.168.110.131,14:13:41,2022-05-11
daquino,192.168.168.144,7:02:35,2022-05-08
eraab,192.168.170.243,1:45:14,2022-05-11
jlansky,192.168.238.42,1:07:11,2022-05-11
acook,192.168.52.90,9:56:48,2022-05-10
asundara,192.168.58.217,23:17:52,2022-05-12
jclark,192.168.214.49,20:49:00,2022-05-10
cjackson,192.168.247.153,19:36:42,2022-05-12
jclark,192.168.197.247,14:11:04,2022-05-12
apatel,192.168.46.207,17:39:42,2022-05-10
mabadi,192.168.96.244,10:24:43,2022-05-12
iuduike,192.168.131.147,17:50:00,2022-05-11
abellmas,192.168.60.111,13:37:05,2022-05-10
gesparza,192.168.148.80,6:30:14,2022-05-11
cgriffin,192.168.4.157,23:04:05,2022-05-09
alevitsk,192.168.210.228,8:10:43,2022-05-08
eraab,192.168.24.12,11:29:27,2022-05-11
jsoto,192.168.25.60,5:09:21,2022-05-09"""

with open("login.txt", "w") as f:
    f.write(login_data)

# Assign import_file to the name of the security log text file
import_file = "login.txt"

# Open the file for reading using a with statement
with open(import_file, "r") as file:
    pass  # file body completed in Task 2

print("login.txt opened successfully in read mode.")


# ============================================================
# TASK 2 — Read the File Into a String
#
# The .read() method converts the contents of an open file
# object into a single string. The result is stored in "text"
# and then printed.
# ============================================================

print("\n" + "=" * 55)
print("TASK 2 — Read the File Into a String")
print("=" * 55)

import_file = "login.txt"

with open(import_file, "r") as file:
    text = file.read()

print(text)


# ============================================================
# TASK 3 — Split the String Into a List of Lines
#
# Calling .split() with no arguments splits on any whitespace
# (including newlines), returning a list where each element
# represents one log entry. Note: .split() does not mutate
# "text" — reassignment would be needed to store the result.
# ============================================================

print("\n" + "=" * 55)
print("TASK 3 — Split the String Into a List of Lines")
print("=" * 55)

import_file = "login.txt"

with open(import_file, "r") as file:
    text = file.read()

print(text.split())


# ============================================================
# TASK 4 — Append a Missing Log Entry
#
# One log entry was not recorded in the original file.
# open() with "a" (append mode) adds content to the end of
# the file without overwriting existing data. A leading "\n"
# ensures the new entry begins on its own line.
# ============================================================

print("\n" + "=" * 55)
print("TASK 4 — Append a Missing Log Entry")
print("=" * 55)

import_file = "login.txt"
missing_entry = "jrafael,192.168.243.140,4:56:27,2022-05-09"

# Append the missing entry on a new line
with open(import_file, "a") as file:
    file.write("\n" + missing_entry)

# Read and display the updated file to confirm the addition
with open(import_file, "r") as file:
    text = file.read()

print(text)


# ============================================================
# TASK 5 — Define the Allow-List File and IP Addresses
#
# Two variables are initialised: import_file holds the target
# filename and ip_addresses holds the space-separated string
# of IP addresses permitted to access restricted information.
# ============================================================

print("\n" + "=" * 55)
print("TASK 5 — Define the Allow-List File and IP Addresses")
print("=" * 55)

# Name of the file to create
import_file = "allow_list.txt"

# Space-separated string of allowed IP addresses
ip_addresses = (
    "192.168.218.160 192.168.97.225 192.168.145.158 192.168.108.13 "
    "192.168.60.153 192.168.96.200 192.168.247.153 192.168.3.252 "
    "192.168.116.187 192.168.15.110 192.168.39.246"
)

print(import_file)
print(ip_addresses)


# ============================================================
# TASK 6 — Write IP Addresses to the Allow-List File
#
# open() with "w" (write mode) creates the file if it does
# not exist, or overwrites it if it does. The .write() method
# writes the IP address string to the file.
# This task produces no printed output.
# ============================================================

print("\n" + "=" * 55)
print("TASK 6 — Write IP Addresses to the Allow-List File")
print("=" * 55)

import_file = "allow_list.txt"

ip_addresses = (
    "192.168.218.160 192.168.97.225 192.168.145.158 192.168.108.13 "
    "192.168.60.153 192.168.96.200 192.168.247.153 192.168.3.252 "
    "192.168.116.187 192.168.15.110 192.168.39.246"
)

with open(import_file, "w") as file:
    file.write(ip_addresses)

print("IP addresses written to allow_list.txt successfully.")


# ============================================================
# TASK 7 — Read Back and Verify the Allow-List File
#
# After writing, the file is immediately re-opened in read
# mode to confirm its contents match the expected IP address
# string.
# ============================================================

print("\n" + "=" * 55)
print("TASK 7 — Read Back and Verify the Allow-List File")
print("=" * 55)

import_file = "allow_list.txt"

ip_addresses = (
    "192.168.218.160 192.168.97.225 192.168.145.158 192.168.108.13 "
    "192.168.60.153 192.168.96.200 192.168.247.153 192.168.3.252 "
    "192.168.116.187 192.168.15.110 192.168.39.246"
)

# Write the IP addresses to the file
with open(import_file, "w") as file:
    file.write(ip_addresses)

# Read the file back and display its contents to verify
with open(import_file, "r") as file:
    text = file.read()

print(text)


# ============================================================
# CONCLUSION — Key Takeaways
#
# with statement: Preferred file-handling pattern. Closes the
#                 file automatically when the block exits.
# "r" read mode:  Opens an existing file for reading.
#                 Use .read() to load full contents as a string.
# "w" write mode: Creates a new file or overwrites existing.
#                 Use when producing a fresh file from scratch.
# "a" append mode:Opens file and places write cursor at end,
#                 preserving all prior content. Use "\n" +
#                 entry to start new records on their own line.
# .split():       Transforms a flat string into a structured
#                 list for iteration and filtering of log data.
# ============================================================

print("\n" + "=" * 55)
print("All 7 tasks completed successfully.")
print("=" * 55)
