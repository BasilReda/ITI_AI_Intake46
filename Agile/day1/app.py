from signup import UserRegistrationData, validate_registration

def main():
    print("=== User Registration CLI ===")
    username = input("Enter username: ").strip()
    email = input("Enter email: ").strip()
    password = input("Enter password: ").strip()
    if not username or not email or not password:
        print("\nError: All fields are required and cannot be empty.")
        return

    user_data = UserRegistrationData(username, email, password)
    errors = validate_registration(user_data)
    
    if errors:
        print("\nRegistration failed! Please fix the following errors:")
        for error in errors:
            print(f"- {error}")
    else:
        print("\nRegistration Successful! Welcome, " + username)

if __name__ == "__main__":
    while True:
        main()
        retry = input("\nTry again? (y/n): ").strip().lower()
        if retry != 'y':
            break