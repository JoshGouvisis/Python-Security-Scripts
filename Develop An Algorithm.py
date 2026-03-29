# ============================================================
# Script:      develop_an_algorithm.py
# Author:      Joshua Gouvisis
# Date:        March 2026
# Certificate: Google Cybersecurity Professional Certificate
# Lab:         Develop an Algorithm — User & Device Verification
#
# Description: Builds a step-by-step algorithm in Python to
#              verify that a user is approved to access a
#              system and that the device they are using is
#              the one assigned to them. Culminates in a
#              reusable login() function covering all three
#              access scenarios.
# ============================================================


# ============================================================
# TASK 1 — Exploring List Indices
#
# Two parallel lists store approved usernames and their
# corresponding device IDs. The element at index n in
# approved_users corresponds to the element at index n
# in approved_devices.
# ============================================================

print("=" * 55)
print("TASK 1 — Exploring List Indices")
print("=" * 55)

approved_users = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab"]
approved_devices = ["8rp2k75", "hl0s5o1", "2ye3lzg", "4n482ts", "a307vir"]

print(approved_users[0])   # elarson
print(approved_devices[1]) # hl0s5o1


# ============================================================
# TASK 2 — Adding a New User
#
# A new employee joins the organization. Use .append() to
# add their username and device ID to the respective lists.
# ============================================================

print("\n" + "=" * 55)
print("TASK 2 — Adding a New User")
print("=" * 55)

approved_users = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab"]
approved_devices = ["8rp2k75", "hl0s5o1", "2ye3lzg", "4n482ts", "a307vir"]

new_user = "gesparza"
new_device = "3rcv4w6"

approved_users.append(new_user)
approved_devices.append(new_device)

print(approved_users)
print(approved_devices)


# ============================================================
# TASK 3 — Removing a Departed User
#
# An employee has left the team. Use .remove() to delete
# their username and device ID from both lists.
# ============================================================

print("\n" + "=" * 55)
print("TASK 3 — Removing a Departed User")
print("=" * 55)

approved_users = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab", "gesparza"]
approved_devices = ["8rp2k75", "hl0s5o1", "2ye3lzg", "4n482ts", "a307vir", "3rcv4w6"]

removed_user = "tshah"
removed_device = "2ye3lzg"

approved_users.remove(removed_user)
approved_devices.remove(removed_device)

print(approved_users)
print(approved_devices)


# ============================================================
# TASK 4 — Checking User Approval
#
# Conditional statement that checks whether a given username
# exists in approved_users and displays an appropriate message.
# ============================================================

print("\n" + "=" * 55)
print("TASK 4 — Checking User Approval")
print("=" * 55)

approved_users = ["elarson", "bmoreno", "sgilmore", "eraab", "gesparza"]
approved_devices = ["8rp2k75", "hl0s5o1", "4n482ts", "a307vir", "3rcv4w6"]

username = "sgilmore"

if username in approved_users:
    print("The user", username, "is approved to access the system.")
else:
    print("The user", username, "is not approved to access the system.")


# ============================================================
# TASK 5 — Finding a User's Index
#
# Use .index() to find the position of username within
# approved_users and store it in a variable named ind.
# ============================================================

print("\n" + "=" * 55)
print("TASK 5 — Finding a User's Index")
print("=" * 55)

approved_users = ["elarson", "bmoreno", "sgilmore", "eraab", "gesparza"]
approved_devices = ["8rp2k75", "hl0s5o1", "4n482ts", "a307vir", "3rcv4w6"]

username = "sgilmore"
ind = approved_users.index(username)
print(ind)  # Output: 2


# ============================================================
# TASK 6 — Cross-Referencing the Device List
#
# Use the index from Task 5 to retrieve the corresponding
# device ID from approved_devices, demonstrating how the
# two parallel lists can be cross-referenced.
# ============================================================

print("\n" + "=" * 55)
print("TASK 6 — Cross-Referencing the Device List")
print("=" * 55)

approved_users = ["elarson", "bmoreno", "sgilmore", "eraab", "gesparza"]
approved_devices = ["8rp2k75", "hl0s5o1", "4n482ts", "a307vir", "3rcv4w6"]

username = "sgilmore"
ind = approved_users.index(username)
print(approved_devices[ind])  # Output: 4n482ts


# ============================================================
# TASK 7 — Verifying Username and Device Together
#
# Conditional using the "and" logical operator to verify
# that the username is approved AND the device ID matches
# the one assigned to that user.
# ============================================================

print("\n" + "=" * 55)
print("TASK 7 — Verifying Username and Device Together")
print("=" * 55)

approved_users = ["elarson", "bmoreno", "sgilmore", "eraab", "gesparza"]
approved_devices = ["8rp2k75", "hl0s5o1", "4n482ts", "a307vir", "3rcv4w6"]

username = "sgilmore"
device_id = "4n482ts"
ind = approved_users.index(username)

if username in approved_users and approved_devices[ind] == device_id:
    print("The username", username, "is approved to access the system.")
    print(device_id, "is the assigned device for", username)


# ============================================================
# TASK 8 — Handling a Device Mismatch
#
# Extends the conditional with an elif branch to handle the
# case where the username is approved but the device ID
# does not match the assigned one.
# ============================================================

print("\n" + "=" * 55)
print("TASK 8 — Handling a Device Mismatch")
print("=" * 55)

approved_users = ["elarson", "bmoreno", "sgilmore", "eraab", "gesparza"]
approved_devices = ["8rp2k75", "hl0s5o1", "4n482ts", "a307vir", "3rcv4w6"]

username = "sgilmore"
device_id = "8rp2k75"  # intentionally incorrect device
ind = approved_users.index(username)

if username in approved_users and device_id == approved_devices[ind]:
    print("The user", username, "is approved to access the system.")
    print(device_id, "is the assigned device for", username)
elif username in approved_users and approved_devices[ind] != device_id:
    print("The user", username, "is approved to access the system.")
    print(device_id, "is not their assigned device for", username)


# ============================================================
# TASK 9 — The Complete login() Function
#
# All previous logic combined into a reusable login()
# function. A nested conditional handles all three cases:
#   1. Unapproved user
#   2. Approved user with correct device
#   3. Approved user with incorrect device
# ============================================================

print("\n" + "=" * 55)
print("TASK 9 — The Complete login() Function")
print("=" * 55)

approved_users = ["elarson", "bmoreno", "sgilmore", "eraab", "gesparza"]
approved_devices = ["8rp2k75", "hl0s5o1", "4n482ts", "a307vir", "3rcv4w6"]


def login(username, device_id):
    """
    Verifies whether a user is approved to access the system
    and whether they are using their assigned device.

    Args:
        username  (str): The username attempting to log in.
        device_id (str): The device ID the user is presenting.
    """
    if username in approved_users:
        print("The user", username, "is approved to access the system.")
        ind = approved_users.index(username)
        if device_id == approved_devices[ind]:
            print(device_id, "is the assigned device for", username)
        else:
            print(device_id, "is not their assigned device.")
    else:
        print("The username", username, "is not approved to access the system.")


# --- Example calls ---
print("\n--- Test Case 1: Typo in username (not approved) ---")
login("elarsen", "8rp2k75")   # typo — not in approved_users

print("\n--- Test Case 2: Approved user, wrong device ---")
login("bmoreno", "4n482ts")   # approved user, wrong device

print("\n--- Test Case 3: Approved user, wrong device ---")
login("eraab", "hl0s5o1")     # approved user, wrong device


# ============================================================
# CONCLUSION — Key Takeaways
#
# Parallel lists:        Two synced lists act as a lightweight
#                        key-value store for user-device pairs.
# List mutation:         .append() and .remove() keep both
#                        lists in sync at runtime.
# Conditional logic:     "in", comparison operators, and "and"
#                        enable multi-factor access checks.
# Nested conditionals:   Separate device-match and mismatch
#                        scenarios without repeating the
#                        username check.
# Encapsulation:         login() makes the algorithm reusable,
#                        testable, and easy to extend.
# ============================================================

print("\n" + "=" * 55)
print("All 9 tasks completed successfully.")
print("=" * 55)
