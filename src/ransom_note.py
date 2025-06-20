import os

def drop_note(folder_path):
    note = """
    Your files have been encrypted!
    
    To recover them:
    1. Send 10 BTC to FAKE_ADDRESS
    2. Re-run this program and select option 2.
    3. Type 'YES' when asked if you've paid.

    This is a simulation. No real harm has occurred.
    """
    try:
        with open(os.path.join(folder_path, "READ_ME.txt"), "w") as f:
            f.write(note)
            print(note)
    except Exception as e:
        print(f"[!] Failed to create ransom note: {e}")
