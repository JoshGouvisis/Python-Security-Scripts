# ============================================================
# Script:      debug_security_code.py
# Author:      Joshua Gouvisis
# Date:        March 2026
# Certificate: Google Cybersecurity Professional Certificate
# Lab:         Debug Python Code
#
# Description: Applies systematic debugging strategies to
#              identify and resolve syntax errors, exceptions,
#              and logic errors in security-focused Python
#              code. Demonstrates before/after corrections
#              with explanations of each fix.
# ============================================================

# ============================================================
# SECTION 1: Syntax Error — Fixed
# Original bug: missing colon at end of for loop
# Fix: added ":" after the for statement
# ============================================================

print("=" * 50)
print("SECTION 1: Syntax Error Fix")
print("=" * 50)

usernames = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab"]

print("Authorized users:")
for username in usernames:   # Fixed: was "for username in usernames"
    print(username)

# ============================================================
# SECTION 2: Exception (Index Error) — Fixed
# Original bug: index [6] on a list with only 5 items
# Fix: changed index to [0] to access the first valid element
# ============================================================

print("\n" + "=" * 50)
print("SECTION 2: Index Error Fix")
print("=" * 50)

network_users = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab"]

# Fixed: was network_users[6], which caused an IndexError
print(f"First user in network list: {network_users[0]}")

# ============================================================
# SECTION 3: Logic Error — Fixed
# Original bug: condition used ">" instead of "<"
#               so it flagged ACTIVE sessions instead of idle
# Fix: corrected operator to "<" to properly detect
#      sessions below the minimum activity threshold
# ============================================================

print("\n" + "=" * 50)
print("SECTION 3: Logic Error Fix")
print("=" * 50)

login_attempts = {
    "elarson": 8,
    "bmoreno": 1,
    "tshah": 5,
    "sgilmore": 0,
    "eraab": 2
}

minimum_activity = 3

print("Users with low activity (potential idle/abandoned sessions):")
for user, attempts in login_attempts.items():
    if attempts < minimum_activity:   # Fixed: was ">", flagged active users incorrectly
        print(f"  [FLAG] {user} — only {attempts} login attempt(s)")

# ============================================================
# SECTION 4: Exception (Type Error) — Fixed
# Original bug: tried to concatenate a string and an integer
# Fix: wrapped the integer in str() to convert it first
# ============================================================

print("\n" + "=" * 50)
print("SECTION 4: Type Error Fix")
print("=" * 50)

failed_attempts = 5

# Fixed: was "Failed login attempts: " + failed_attempts (TypeError)
print("Failed login attempts: " + str(failed_attempts))
print("\nAll debug sections completed successfully.")
