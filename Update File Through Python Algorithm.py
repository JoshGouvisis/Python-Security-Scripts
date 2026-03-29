# ============================================================
# Script:      update_file_through_python_algorithm.py
# Author:      Joshua Gouvisis
# Date:        March 2026
# Certificate: Google Cybersecurity Professional Certificate
# Lab:         Algorithm for File Updates in Python
#
# Description: Demonstrates a Python algorithm that manages
#              an IP address allow list by importing and
#              parsing a text file, then removing IP addresses
#              that no longer have authorized access to
#              restricted information. Builds the algorithm
#              step by step from opening the file through to
#              writing the updated allow list back to disk.
# ============================================================


# --- Create allow_list.txt for demonstration ---
sample_allow_list = """ip_address
192.168.25.60
192.168.205.12
192.168.97.225
192.168.6.9
192.168.158.170
192.168.52.90
192.168.201.40
192.168.90.124
192.168.186.176
192.168.133.188
192.168.203.198
192.168.218.219
192.168.52.37
192.168.156.224
192.168.60.153
192.168.69.116
192.168.58.57"""

with open("allow_list.txt", "w") as f:
    f.write(sample_allow_list)


# ============================================================
# STEP 1 — Open the File That Contains the Allow List
#
# The algorithm begins by assigning the allow list filename
# and the list of IP addresses to be removed to their
# respective variables. open() is called with "r" (read mode)
# to open the file for reading inside a with statement.
# ============================================================

print("=" * 55)
print("STEP 1 — Open the File That Contains the Allow List")
print("=" * 55)

# Assign import_file to the name of the file
import_file = "allow_list.txt"

# Assign remove_list to a list of IPs no longer allowed
remove_list = ["192.168.97.225", "192.168.158.170",
               "192.168.201.40", "192.168.58.57"]

# First line of with statement — opens the file for reading
with open(import_file, "r") as file:
    pass  # file reading completed in Step 2

print(f"Opened '{import_file}' successfully in read mode.")
print(f"IP addresses to remove: {remove_list}")


# ============================================================
# STEP 2 — Read the File Contents
#
# The .read() method is applied to the file object to read
# the entire contents and store them as a string in the
# ip_addresses variable. print() displays the contents
# for verification.
# ============================================================

print("\n" + "=" * 55)
print("STEP 2 — Read the File Contents")
print("=" * 55)

# Assign import_file to the name of the file
import_file = "allow_list.txt"

# Assign remove_list to a list of IPs no longer allowed
remove_list = ["192.168.97.225", "192.168.158.170",
               "192.168.201.40", "192.168.58.57"]

# Build with statement to read in the initial contents of the file
with open(import_file, "r") as file:
    # Use .read() to read the file and store in ip_addresses
    ip_addresses = file.read()

# Display ip_addresses
print(ip_addresses)


# ============================================================
# STEP 3 — Convert the String Into a List
#
# The .split() method converts the ip_addresses string into
# a list, allowing each IP address to be accessed and
# evaluated individually.
# ============================================================

print("\n" + "=" * 55)
print("STEP 3 — Convert the String Into a List")
print("=" * 55)

# Assign import_file to the name of the file
import_file = "allow_list.txt"

# Assign remove_list to a list of IPs no longer allowed
remove_list = ["192.168.97.225", "192.168.158.170",
               "192.168.201.40", "192.168.58.57"]

# Build with statement to read in the initial contents of the file
with open(import_file, "r") as file:
    # Use .read() to read the file and store in ip_addresses
    ip_addresses = file.read()

# Use .split() to convert ip_addresses from a string to a list
ip_addresses = ip_addresses.split()

# Display ip_addresses
print(ip_addresses)


# ============================================================
# STEP 4 — Iterate Through the Remove List
#
# A for loop iterates through each element in ip_addresses,
# making each individual IP address available for evaluation
# against the remove list.
# ============================================================

print("\n" + "=" * 55)
print("STEP 4 — Iterate Through the Remove List")
print("=" * 55)

# Assign import_file to the name of the file
import_file = "allow_list.txt"

# Assign remove_list to a list of IPs no longer allowed
remove_list = ["192.168.97.225", "192.168.158.170",
               "192.168.201.40", "192.168.58.57"]

# Build with statement to read in the initial contents of the file
with open(import_file, "r") as file:
    # Use .read() to read the file and store in ip_addresses
    ip_addresses = file.read()

# Use .split() to convert ip_addresses from a string to a list
ip_addresses = ip_addresses.split()

# Build iterative statement — loop variable named "element"
for element in ip_addresses:
    # Display element in every iteration
    print(element)


# ============================================================
# STEP 5 — Remove IP Addresses That Are on the Remove List
#
# A conditional statement inside the loop checks whether each
# element in ip_addresses exists in remove_list. If the
# condition evaluates to True, .remove() removes that IP
# address from the list.
# ============================================================

print("\n" + "=" * 55)
print("STEP 5 — Remove Unauthorized IP Addresses")
print("=" * 55)

# Assign import_file to the name of the file
import_file = "allow_list.txt"

# Assign remove_list to a list of IPs no longer allowed
remove_list = ["192.168.97.225", "192.168.158.170",
               "192.168.201.40", "192.168.58.57"]

# Build with statement to read in the initial contents of the file
with open(import_file, "r") as file:
    # Use .read() to read the file and store in ip_addresses
    ip_addresses = file.read()

# Use .split() to convert ip_addresses from a string to a list
ip_addresses = ip_addresses.split()

# Build iterative statement
for element in ip_addresses:
    # Build conditional statement
    # If current element is in remove_list, remove it
    if element in remove_list:
        ip_addresses.remove(element)

# Display updated ip_addresses
print(ip_addresses)


# ============================================================
# STEP 6 — Update the File With the Revised List
#
# After removing unauthorized IP addresses, .join() converts
# the updated list back into a string. A second with statement
# opens the file in write mode ("w") and overwrites the
# original contents with the revised IP address string.
# ============================================================

print("\n" + "=" * 55)
print("STEP 6 — Update the File With the Revised List")
print("=" * 55)

# Assign import_file to the name of the file
import_file = "allow_list.txt"

# Assign remove_list to a list of IPs no longer allowed
remove_list = ["192.168.97.225", "192.168.158.170",
               "192.168.201.40", "192.168.58.57"]

# Build with statement to read in the initial contents of the file
with open(import_file, "r") as file:
    # Use .read() to read the file and store in ip_addresses
    ip_addresses = file.read()

# Use .split() to convert ip_addresses from a string to a list
ip_addresses = ip_addresses.split()

# Build iterative statement
for element in ip_addresses:
    # Build conditional statement
    if element in remove_list:
        ip_addresses.remove(element)

# Convert ip_addresses back to a string for writing to the file
ip_addresses = " ".join(ip_addresses)

# Build with statement to rewrite the original file
with open(import_file, "w") as file:
    # Rewrite the file, replacing its contents with ip_addresses
    file.write(ip_addresses)

# Read back and display the updated file to confirm changes
with open(import_file, "r") as file:
    text = file.read()

print("Updated allow_list.txt contents:")
print(text)


# ============================================================
# SUMMARY
#
# This algorithm opens allow_list.txt, reads its content into
# ip_addresses, and converts it from a string to a list using
# .split(). A for loop iterates through the list and removes
# any IP address found in remove_list using .remove(). Once
# all matches are removed, " ".join() converts the list back
# to a string. Finally, the file is opened in write mode and
# overwritten with the updated string — ensuring the file
# contains only currently authorized IP addresses.
#
# Completed as part of the Google Cybersecurity Professional
# Certificate — March 2026
# ============================================================

print("\n" + "=" * 55)
print("All 6 steps completed successfully.")
print("=" * 55)
