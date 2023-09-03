import time

# Superhero ASCII Art
ART = """
██▓███   ▄▄▄       ██████   ██████  █     █░ ▒█████   ██▀███  ▓█████▄      ▄████▄   ██░ ██  ▓█████  ▄████▄  ██ ▄█▀ ▓█████ ██▀███      
▓██░  ██ ▒████▄   ▒██    ▒ ▒██    ▒ ▓█░ █ ░█░▒██▒  ██▒▓██ ▒ ██▒▒██▀ ██▌    ▒██▀ ▀█ ▒▓██░ ██  ▓█   ▀ ▒██▀ ▀█  ██▄█▒  ▓█   ▀▓██ ▒ ██▒    
▓██░ ██▓▒▒██  ▀█▄ ░ ▓██▄   ░ ▓██▄   ▒█░ █ ░█ ▒██░  ██▒▓██ ░▄█ ▒░██   █▌    ▒▓█    ▄░▒██▀▀██  ▒███   ▒▓█    ▄▓███▄░  ▒███  ▓██ ░▄█ ▒    
▒██▄█▓▒ ▒░██▄▄▄▄██  ▒   ██▒  ▒   ██▒░█░ █ ░█ ▒██   ██░▒██▀▀█▄  ░▓█▄   ▌    ▒▓▓▄ ▄██ ░▓█ ░██  ▒▓█  ▄▒▒▓▓▄ ▄██▓██ █▄  ▒▓█  ▄▒██▀▀█▄      
▒██▒ ░  ░▒▓█   ▓██▒██████▒▒▒██████▒▒░░██▒██▓ ░ ████▓▒░░██▓ ▒██▒░▒████▓     ▒ ▓███▀  ░▓█▒░██▓▒░▒████░▒ ▓███▀ ▒██▒ █▄▒░▒████░██▓ ▒██▒    
▒▓▒░ ░  ░░▒▒   ▓▒█▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░░ ▓░▒ ▒  ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░ ▒▒▓  ▒     ░ ░▒ ▒    ▒ ░░▒░▒░░░ ▒░ ░░ ░▒ ▒  ▒ ▒▒ ▓▒░░░ ▒░ ░ ▒▓ ░▒▓░    
░▒ ░     ░ ░   ▒▒ ░ ░▒  ░ ░░ ░▒  ░ ░  ▒ ░ ░    ░ ▒ ▒░   ░▒ ░ ▒  ░ ▒  ▒       ░  ▒    ▒ ░▒░ ░░ ░ ░     ░  ▒  ░ ░▒ ▒░░ ░ ░    ░▒ ░ ▒     
░░         ░   ▒  ░  ░  ░  ░  ░  ░    ░   ░  ░ ░ ░ ▒    ░░   ░  ░ ░  ░     ░         ░  ░░ ░    ░   ░       ░ ░░ ░     ░    ░░   ░     
               ░        ░        ░      ░        ░ ░     ░        ░        ░ ░       ░  ░  ░░   ░   ░ ░     ░  ░   ░   ░     ░         

"""

def display_menu():
    print(ART)
    print("==================================")
    print("    Password Vulnerability Checker ")
    print("==================================")
    print("Enter 'q' to quit.")

def check_password(password, target_password):
    return password == target_password

def load_rockyou_wordlist(file_path):
    with open(file_path, 'r', encoding='latin-1') as f:
        return [line.strip() for line in f]

def brute_force_cracker(target_password, password_list):
    start_time = time.time()
    for password in password_list:
        if check_password(password, target_password):
            end_time = time.time()
            print(f"Password is vulnerable! Found in 'rockyou.txt' wordlist.")
            print(f"Time taken: {end_time - start_time:.2f} seconds")
            return
    end_time = time.time()
    print("Password is not found in the wordlist. It's less likely to be vulnerable to bruteforcing attacks.")
    print(f"Time taken: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    display_menu()

    while True:
        user_input = input("Enter the password you want to check (or 'q' to quit): ")

        if user_input.lower() == 'q':
            print("Goodbye!")
            break

        # Load the RockYou wordlist
        password_list = load_rockyou_wordlist("/usr/share/wordlists/rockyou.txt")

        # Check if the user's password is in the RockYou wordlist
        brute_force_cracker(user_input, password_list)
