# ============================================================
# Script:      debug_python_code.py
# Author:      Joshua Gouvisis
# Date:        March 2026
# Certificate: Google Cybersecurity Professional Certificate
# Lab:         Debug Python Code
#
# Description: Applies systematic debugging strategies to
#              identify and resolve syntax errors, indentation
#              errors, name errors, index errors, and logic
#              errors in security-focused Python code.
#              Each task presents buggy code, the fix applied,
#              and the corrected output.
# ============================================================


# ============================================================
# TASK 1 — Syntax Error: Missing Colon in for Loop
#
# Bug:  for loop header was missing its required colon
#       "for i in range(10)" raised a SyntaxError
# Fix:  Added ":" at the end of the for loop header
# ============================================================

print("=" * 55)
print("TASK 1 — Syntax Error: Missing Colon in for Loop")
print("=" * 55)

# Fixed: was "for i in range(10)" — missing colon
for i in range(10):
    print("Connection cannot be established")


# ============================================================
# TASK 2 — Syntax Error: Malformed List String Element
#
# Bug:  "zdutchma" was missing its closing quotation mark
#       and the following comma, causing a SyntaxError
# Fix:  Added the closing quote and comma after "zdutchma"
# ============================================================

print("\n" + "=" * 55)
print("TASK 2 — Syntax Error: Malformed List String Element")
print("=" * 55)

# Fixed: was ["djames", "jpark", "tbailey", "zdutchma, "esmith" ...]
usernames_list = ["djames", "jpark", "tbailey", "zdutchma", "esmith",
                  "srobinso", "dcoleman", "fbautist"]
print(usernames_list)


# ============================================================
# TASK 3 — Syntax Error: Missing Closing Parenthesis
#
# Bug:  print("update needed".upper() was missing its outer
#       closing parenthesis, causing a SyntaxError
# Fix:  Added the missing closing ")" to the print() call
# ============================================================

print("\n" + "=" * 55)
print("TASK 3 — Syntax Error: Missing Closing Parenthesis")
print("=" * 55)

# Fixed: was print("update needed".upper()  — missing final ")"
print("update needed".upper())


# ============================================================
# TASK 4 — Multiple Errors: Comparison, Indentation, Name
#
# Bug 1: "=" used instead of "==" in the if condition (SyntaxError)
# Bug 2: print() not indented inside the if block (IndentationError)
# Bug 3: "username_list" used instead of "usernames_list" (NameError)
# Fix:   Corrected operator to "==", fixed indentation,
#        and corrected the variable name spelling
# ============================================================

print("\n" + "=" * 55)
print("TASK 4 — Multiple Errors: Comparison, Indentation, Name")
print("=" * 55)

usernames_list = ["djames", "jpark", "tbailey", "zdutchma", "esmith",
                  "srobinso", "dcoleman", "fbautist"]
username = "esmith"

# Fixed: was "for name in username_list" (NameError)
for name in usernames_list:
    # Fixed: was "if name = username" (SyntaxError — should be ==)
    if name == username:
        # Fixed: was not indented (IndentationError)
        print("The user is an approved user")


# ============================================================
# TASK 5 — Index Error: Out-of-Range Index
#
# Bug:  Code used index [5] on a 5-element list.
#       Valid indices are 0-4. Raised an IndexError.
# Fix:  Changed index from [5] to [4] to access the last element
# ============================================================

print("\n" + "=" * 55)
print("TASK 5 — Index Error: Out-of-Range Index")
print("=" * 55)

usernames_list = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab"]
username = "eraab"

# Fixed: was usernames_list[5] — IndexError, valid indices are 0-4
if username == usernames_list[4]:
    print("This username is the final one in the list.")


# ============================================================
# TASK 6 — Syntax Error and NameError: with Statement and .split()
#
# Bug 1: "with" statement header missing its colon (SyntaxError)
# Bug 2: split() called as standalone function instead of
#        as a string method: split(ip_addresses) vs
#        ip_addresses.split() (NameError)
# Fix:   Added colon to "with" statement and corrected
#        split() to ip_addresses.split()
#
# Note:  This task requires "allow_list.txt" to be present.
#        A sample list is generated below for demonstration.
# ============================================================

print("\n" + "=" * 55)
print("TASK 6 — Syntax Error and NameError: with Statement")
print("=" * 55)

# Create a sample allow_list.txt for demonstration
sample_ips = """ip_address
192.168.25.60
192.168.205.12
192.168.97.225
192.168.6.9
192.168.158.170
192.168.52.90
192.168.201.40
192.168.58.57
192.168.90.124"""

with open("allow_list.txt", "w") as f:
    f.write(sample_ips)

import_file = "allow_list.txt"
remove_list = ["192.168.97.225", "192.168.158.170",
               "192.168.201.40", "192.168.58.57"]

# Fixed: was "with open(import_file, 'r') as file" — missing colon
with open(import_file, "r") as file:
    ip_addresses = file.read()

# Fixed: was split(ip_addresses) — NameError
ip_addresses = ip_addresses.split()

for element in remove_list:
    if element in ip_addresses:
        ip_addresses.remove(element)

print(ip_addresses)


# ============================================================
# TASK 7 — Logic Error: Swapped List Indices
#
# Bug:  OS 1 and OS 2 were mapped to swapped indices.
#       OS 1 used index [1] and OS 2 used index [0],
#       producing incorrect patch dates with no exception raised.
# Fix:  Corrected so OS 1 maps to index [0] and
#       OS 2 maps to index [1]. OS 3 was already correct.
# ============================================================

print("\n" + "=" * 55)
print("TASK 7 — Logic Error: Swapped List Indices")
print("=" * 55)

system = "OS 2"
patch_schedule = ["March 1st", "April 1st", "May 1st"]

# Fixed: OS 1 → index [0], OS 2 → index [1] (were swapped)
if system == "OS 1":
    print("Patch date:", patch_schedule[0])
elif system == "OS 2":
    print("Patch date:", patch_schedule[1])
elif system == "OS 3":
    print("Patch date:", patch_schedule[2])


# ============================================================
# CONCLUSION — Key Takeaways
#
# Syntax errors:     Caught before execution. Missing colons,
#                    quotes, and parentheses prevent parsing.
# Indentation errors:Python uses indentation to define blocks.
# Name errors:       Caused by undefined or misspelled names.
# Index errors:      Indexing starts at 0; max index = n-1.
# Logic errors:      Code runs but produces wrong results.
#                    Hardest to detect — test with known inputs.
# Best practice:     Fix and re-run after each correction.
# ============================================================

print("\n" + "=" * 55)
print("All 7 debug tasks completed successfully.")
print("=" * 55)
