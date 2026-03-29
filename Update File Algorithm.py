# ============================================================
# Script:      update_file_algorithm.py
# Author:      Joshua Gouvisis
# Date:        March 2026
# Certificate: Google Cybersecurity Professional Certificate
# Lab:         Update a File Through a Python Algorithm
#
# Description: Parses an IP address allow list file and
#              automates the removal of addresses that no
#              longer have authorized access to restricted
#              information.
# ============================================================

# --- The allow list file and addresses to remove ---
import_file = "allow_list.txt"

remove_list = [
    "192.168.97.105",
    "192.168.158.170",
    "192.168.201.40",
    "192.168.58.57"
]

# --- Step 1: Open the allow list file and read its contents ---
with open(import_file, "r") as file:
    ip_addresses = file.read()

print("Original allow list:")
print(ip_addresses)

# --- Step 2: Convert the string into a list ---
ip_addresses = ip_addresses.split()

print("\nAllow list as a Python list:")
print(ip_addresses)

# --- Step 3: Iterate through the remove list ---
for element in remove_list:

    # --- Step 4: Remove IP addresses that are on the remove list ---
    if element in ip_addresses:
        ip_addresses.remove(element)
        print(f"\nRemoved: {element}")
    else:
        print(f"\n{element} was not found in the allow list.")

# --- Step 5: Convert the updated list back into a string ---
ip_addresses = "\n".join(ip_addresses)

# --- Step 6: Write the updated list back to the file ---
with open(import_file, "w") as file:
    file.write(ip_addresses)

print("\n--- Updated allow list written to file ---")
print(ip_addresses)
