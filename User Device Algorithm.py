# ============================================================
# Script:      user_device_algorithm.py
# Author:      Joshua Gouvisis
# Date:        March 2026
# Certificate: Google Cybersecurity Professional Certificate
# Lab:         Develop an Algorithm With Python
#
# Description: Builds an algorithm to manage approved user
#              and device lists and verify authorized access
#              using conditional logic. Checks whether a
#              user is approved AND using an approved device
#              before granting access.
# ============================================================

# --- Step 1: Define approved users and their assigned devices ---
approved_users = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab"]

approved_devices = {
    "elarson":  "IP-1",
    "bmoreno":  "IP-2",
    "tshah":    "IP-3",
    "sgilmore": "IP-4",
    "eraab":    "IP-5"
}

# --- Step 2: Define the access check function ---
def check_access(username, device_id):
    """
    Checks if a user is approved and whether the device
    they are connecting from matches their assigned device.

    Args:
        username  (str): The login username to verify.
        device_id (str): The device ID the user is connecting from.

    Returns:
        str: Access granted or denied message with reason.
    """

    # Check if user is in the approved list
    if username not in approved_users:
        return f"[DENIED]  '{username}' is not an approved user."

    # Check if the device matches the user's assigned device
    assigned_device = approved_devices.get(username)

    if device_id == assigned_device:
        return f"[GRANTED] '{username}' is approved and device '{device_id}' matches."
    else:
        return (
            f"[DENIED]  '{username}' is approved but device '{device_id}' "
            f"does not match assigned device '{assigned_device}'."
        )

# --- Step 3: Run access checks against test scenarios ---
print("=" * 60)
print("ACCESS CONTROL VERIFICATION — RESULTS")
print("=" * 60)

test_cases = [
    ("elarson",  "IP-1"),   # Valid user, correct device   -> GRANTED
    ("bmoreno",  "IP-9"),   # Valid user, wrong device     -> DENIED
    ("jdoe",     "IP-3"),   # Unknown user                 -> DENIED
    ("tshah",    "IP-3"),   # Valid user, correct device   -> GRANTED
    ("sgilmore", "IP-2"),   # Valid user, wrong device     -> DENIED
    ("eraab",    "IP-5"),   # Valid user, correct device   -> GRANTED
]

for username, device_id in test_cases:
    result = check_access(username, device_id)
    print(result)

print("=" * 60)
print("Access verification complete.")
