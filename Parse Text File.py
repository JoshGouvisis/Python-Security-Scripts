# ============================================================
# Script:      parse_text_file.py
# Author:      Joshua Gouvisis
# Date:        March 2026
# Certificate: Google Cybersecurity Professional Certificate
# Lab:         Import and Parse a Text File
#
# Description: Imports and parses a security log text file
#              to extract and process structured login data
#              for security analysis.
# ============================================================

# --- Step 1: Define the security log file to import ---
import_file = "login_attempts.txt"

# --- Step 2: Open and read the file ---
with open(import_file, "r") as file:
    file_text = file.read()

print("Raw file contents:")
print(file_text)
print("-" * 50)

# --- Step 3: Split the file text into a list of lines ---
usernames = file_text.split()

print(f"\nTotal login entries found: {len(usernames)}")
print("\nParsed login entries:")
print(usernames)

# --- Step 4: Count how many times a specific user appears ---
target_user = "jsmith"
login_count = usernames.count(target_user)

print(f"\nLogin count for '{target_user}': {login_count}")

# --- Step 5: Flag if login count exceeds threshold ---
login_threshold = 3

if login_count > login_threshold:
    print(f"\n[ALERT] '{target_user}' has exceeded the login threshold of {login_threshold}.")
    print("Flagging for security review.")
else:
    print(f"\n'{target_user}' is within normal login activity.")

# --- Step 6: Parse and display all unique users from the log ---
unique_users = list(set(usernames))
print(f"\nUnique users in log ({len(unique_users)} total):")
for user in sorted(unique_users):
    count = usernames.count(user)
    print(f"  {user}: {count} login attempt(s)")
