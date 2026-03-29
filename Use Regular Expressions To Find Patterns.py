# ============================================================
# Script:      use_regular_expressions_to_find_patterns.py
# Author:      Joshua Gouvisis
# Date:        March 2026
# Certificate: Google Cybersecurity Professional Certificate
# Lab:         Use Regular Expressions to Find Patterns
#
# Description: Uses Python's re module to extract device IDs
#              and IP addresses from security log data. Covers
#              re.findall(), pattern building with \w, \d, \.,
#              and quantifiers (+, {1,3}), and cross-references
#              extracted IPs against a flagged address list for
#              automated security triage.
# ============================================================


# ============================================================
# TASK 1 — Import the re Module
#
# Before using regular expressions, import Python's built-in
# re module, which provides all the functions needed
# throughout this lab.
# ============================================================

print("=" * 55)
print("TASK 1 — Import the re Module")
print("=" * 55)

import re

print("re module imported successfully.")


# ============================================================
# TASK 2 — Examine the Device ID Log
#
# A log of device IDs is stored in the variable devices.
# Display the full string to understand its structure before
# writing an extraction pattern.
# ============================================================

print("\n" + "=" * 55)
print("TASK 2 — Examine the Device ID Log")
print("=" * 55)

# Assign devices to a string containing space-separated device IDs
devices = ("r262c36 67bv8fy 41j1u2e r151dm4 1270t3o 42dr56i r15xk9h "
           "2j33krk 253be78 ac742a1 r15u9q5 zh86b2l ii286fq 9x482kt "
           "6oa6m6u x3463ac i4l56nq g07h55q 081qc9t r159r1u")

print(devices)


# ============================================================
# TASK 3 — Build the Device ID Pattern
#
# Write a regex that matches device IDs beginning with "r15".
# \w matches any alphanumeric character or underscore.
# + means one or more occurrences of the preceding element.
#
# Pattern:  r15\w+
# Removing r15  → matches every device ID, not just r15 ones
# Removing \w   → matches r1 followed by one or more literal 5s
# Removing +    → matches only r15 + exactly one character
# ============================================================

print("\n" + "=" * 55)
print("TASK 3 — Build the Device ID Pattern")
print("=" * 55)

# Pattern matches any device ID that starts with "r15"
# followed by one or more alphanumeric characters
target_pattern = r"r15\w+"

print(f"Pattern defined: {target_pattern}")


# ============================================================
# TASK 4 — Extract Matching Device IDs
#
# Use re.findall() with the pattern from Task 3 to extract
# all device IDs that start with "r15" from the devices string.
# ============================================================

print("\n" + "=" * 55)
print("TASK 4 — Extract Matching Device IDs")
print("=" * 55)

import re

devices = ("r262c36 67bv8fy 41j1u2e r151dm4 1270t3o 42dr56i r15xk9h "
           "2j33krk 253be78 ac742a1 r15u9q5 zh86b2l ii286fq 9x482kt "
           "6oa6m6u x3463ac i4l56nq g07h55q 081qc9t r159r1u")

target_pattern = r"r15\w+"

print(re.findall(target_pattern, devices))


# ============================================================
# TASK 5 — Examine the Network Login Log
#
# A network security log is stored in log_file. Each entry
# contains a username, date, login time, and IP address.
# Some entries contain invalid IP addresses due to
# data-collection issues. Display the log to examine its
# structure.
# ============================================================

print("\n" + "=" * 55)
print("TASK 5 — Examine the Network Login Log")
print("=" * 55)

import re

log_file = (
    "eraab 2022-05-10 6:03:41 192.168.152.148 \n"
    "iuduike 2022-05-09 6:46:40 192.168.22.115 \n"
    "smartell 2022-05-09 19:30:32 192.168.190.178 \n"
    "arutley 2022-05-12 17:00:59 1923.1689.3.24 \n"
    "rjensen 2022-05-11 0:59:26 192.168.213.128 \n"
    "aestrada 2022-05-09 19:28:12 1924.1680.27.57 \n"
    "asundara 2022-05-11 18:38:07 192.168.96.200 \n"
    "dkot 2022-05-12 10:52:00 1921.168.1283.75 \n"
    "abernard 2022-05-12 23:38:46 19245.168.2345.49 \n"
    "cjackson 2022-05-12 19:36:42 192.168.247.153 \n"
    "jclark 2022-05-10 10:48:02 192.168.174.117 \n"
    "alevitsk 2022-05-08 12:09:10 192.16874.1390.176 \n"
    "jrafael 2022-05-10 22:40:01 192.168.148.115 \n"
    "yappiah 2022-05-12 10:37:22 192.168.103.10654 \n"
    "daquino 2022-05-08 7:02:35 192.168.168.144"
)

print(log_file)


# ============================================================
# TASK 6 — Build a Strict Three-Digit IP Pattern
#
# Write a pattern to match IP addresses in the form
# xxx.xxx.xxx.xxx — exactly three digits per segment.
# \d matches a single digit 0-9.
# \. matches a literal period (escapes the regex wildcard).
# ============================================================

print("\n" + "=" * 55)
print("TASK 6 — Build a Strict Three-Digit IP Pattern")
print("=" * 55)

# Each \d matches one digit; \. matches a literal period.
# This pattern requires exactly three digits in every segment.
pattern = r"\d\d\d\.\d\d\d\.\d\d\d\.\d\d\d"

print(f"Pattern defined: {pattern}")


# ============================================================
# TASK 7 — Extract IPs With the Strict Pattern
#
# Apply the three-digits-per-segment pattern to log_file
# using re.findall() and observe which addresses are returned.
#
# Note: 192.168.22.115 is NOT returned — its second segment
# has only two digits. It is the only valid IP address missed
# by this strict pattern.
# ============================================================

print("\n" + "=" * 55)
print("TASK 7 — Extract IPs With the Strict Pattern")
print("=" * 55)

pattern = r"\d\d\d\.\d\d\d\.\d\d\d\.\d\d\d"

print(re.findall(pattern, log_file))


# ============================================================
# TASK 8 — Relax the Pattern With + (One or More Digits)
#
# Update the pattern to allow one or more digits per segment
# by replacing each \d\d\d group with \d+. This captures all
# IP-like structures including invalid ones with too many
# digits — it over-matches and must be refined further.
# ============================================================

print("\n" + "=" * 55)
print("TASK 8 — Relax the Pattern With + (One or More Digits)")
print("=" * 55)

# \d+ matches one or more consecutive digits per segment
pattern = r"\d+\.\d+\.\d+\.\d+"

print(re.findall(pattern, log_file))


# ============================================================
# TASK 9 — Refine With Curly-Bracket Quantifiers {1,3}
#
# Replace + with {1,3} to enforce a range of one to three
# digits per segment. {m,n} means between m and n occurrences
# of the preceding element. Results are stored in
# valid_ip_addresses.
#
# Compared to Task 7: correctly includes 192.168.22.115
# Compared to Task 8: correctly excludes 1923.1689.3.24
#                     and other malformed addresses
# ============================================================

print("\n" + "=" * 55)
print("TASK 9 — Refine With Curly-Bracket Quantifiers {1,3}")
print("=" * 55)

# {1,3} enforces a minimum of 1 and maximum of 3 digits per segment
pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"

valid_ip_addresses = re.findall(pattern, log_file)

print(valid_ip_addresses)


# ============================================================
# TASK 10 — Load the Flagged Address List
#
# A list of IP addresses previously flagged for unusual
# activity is stored in flagged_addresses. Display it to
# confirm its contents before running the comparison loop.
# ============================================================

print("\n" + "=" * 55)
print("TASK 10 — Load the Flagged Address List")
print("=" * 55)

flagged_addresses = [
    "192.168.190.178",
    "192.168.96.200",
    "192.168.174.117",
    "192.168.168.144"
]

print(flagged_addresses)


# ============================================================
# TASK 11 — Flag Analysis: Compare Extracted IPs Against
#           the Flagged List
#
# Iterate over valid_ip_addresses and check each address
# against flagged_addresses. Print an appropriate message
# depending on whether the address requires further
# investigation.
# ============================================================

print("\n" + "=" * 55)
print("TASK 11 — Flag Analysis: Cross-Reference Results")
print("=" * 55)

import re

log_file = (
    "eraab 2022-05-10 6:03:41 192.168.152.148 \n"
    "iuduike 2022-05-09 6:46:40 192.168.22.115 \n"
    "smartell 2022-05-09 19:30:32 192.168.190.178 \n"
    "arutley 2022-05-12 17:00:59 1923.1689.3.24 \n"
    "rjensen 2022-05-11 0:59:26 192.168.213.128 \n"
    "aestrada 2022-05-09 19:28:12 1924.1680.27.57 \n"
    "asundara 2022-05-11 18:38:07 192.168.96.200 \n"
    "dkot 2022-05-12 10:52:00 1921.168.1283.75 \n"
    "abernard 2022-05-12 23:38:46 19245.168.2345.49 \n"
    "cjackson 2022-05-12 19:36:42 192.168.247.153 \n"
    "jclark 2022-05-10 10:48:02 192.168.174.117 \n"
    "alevitsk 2022-05-08 12:09:10 192.16874.1390.176 \n"
    "jrafael 2022-05-10 22:40:01 192.168.148.115 \n"
    "yappiah 2022-05-12 10:37:22 192.168.103.10654 \n"
    "daquino 2022-05-08 7:02:35 192.168.168.144"
)

pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
valid_ip_addresses = re.findall(pattern, log_file)

flagged_addresses = [
    "192.168.190.178",
    "192.168.96.200",
    "192.168.174.117",
    "192.168.168.144"
]

for address in valid_ip_addresses:
    if address in flagged_addresses:
        print("The IP address", address, "has been flagged for further analysis.")
    else:
        print("The IP address", address, "does not require further analysis.")


# ============================================================
# CONCLUSION — Key Takeaways
#
# re module:         Provides re.findall() which returns all
#                    non-overlapping pattern matches as a list.
# \w and +:          \w matches alphanumeric/underscore chars.
#                    + matches one or more — ideal for device IDs.
# \d and \.:         \d matches a single digit 0-9.
#                    \. escapes the period as a literal character.
# Quantifier choice: \d\d\d = exactly 3 digits (too strict).
#                    \d+    = one or more (over-matches).
#                    \d{1,3}= one to three digits (correct).
# Iterative design:  Effective regex requires testing edge cases
#                    and adjusting quantifiers incrementally.
# Regex + list check:Combining re.findall() with a flagged list
#                    inside a loop is a reusable pattern for
#                    log analysis and alert triage.
# ============================================================

print("\n" + "=" * 55)
print("All 11 tasks completed successfully.")
print("=" * 55)
