print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

print("CRISIS ALERT: Attempting access to 'lost_archive.txt'...")
try:
    with open("lost_archive.txt", "r") as lost_file:
        data = lost_file.read()
        print(f"SUCCESS: Archive recovered - {data}")
except FileNotFoundError:
    print("RESPONSE: Archive not found in storage matrix")
print("STATUS: Crisis handled, system stable")

print("\nCRISIS ALERT: Attempting access to 'classified_vault.txt'...")
try:
    with open("classified_vault.txt", "r") as classified_file:
        data = classified_file.read()
        print(f"SUCCESS: Archive recovered - {data}")
except PermissionError:
    print("RESPONSE: Security protocols deny access")
except FileExistsError:
    print("RESPONSE: Security protocols deny access")
print("STATUS: Crisis handled, security maintained")

print("\nROUTINE ACCESS: Attempting access to 'standard_archive.txt'...")
with open("standard_archive.txt", "r") as standard_file:
    try:
        data = standard_file.read()
        print(f"SUCCESS:  Archive recovered - ``{data}''")
    except FileNotFoundError:
        print("RESPONSE: Archive not found")
    except Exception:
        print("RESPONSE: Unexpected error")
print("STATUS: Normal operations resumed")

print("\nAll crisis scenarios handled successfully. Archives secure.")