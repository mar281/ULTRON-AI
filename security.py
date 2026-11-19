
# ULTRON AI SECURITY SYSTEM

CREATOR = "Emmanuel Cornelius"

def check_permission(action):
    print("\nULTRON SECURITY SYSTEM")
    print("Requested action:", action)

    approval = input("Do you approve this action? (yes/no): ")

    if approval.lower() == "yes":
        print("Permission granted.")
        return True

    print("Permission denied.")
    return False


def security_status():
    print("Security: ACTIVE")
    print("Permission checks: ENABLED")
    print("Unauthorized actions: BLOCKED")

