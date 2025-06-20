def show_ethics_warning():
    print("WARNING: This tool simulates ransomware behavior.")
    print("Use for ethical education only on non-sensitive test data.")
    confirm = input("Type 'I AGREE' to continue: ")
    if confirm.strip() != 'I AGREE' and confirm.strip() != 'i agree':
        print("Aborted for safety.")
        exit()
