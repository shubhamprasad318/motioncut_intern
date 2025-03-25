import random
import string

# Pre-defined lists of adjectives and nouns
adjectives = ["Cool", "Happy", "Fast", "Brave", "Clever", "Chilly", "Funky", "Witty", "Zany", "Sly"]
nouns = ["Tiger", "Dragon", "Panda", "Knight", "Falcon", "Wizard", "Ninja", "Rider", "Phantom", "Pirate"]
special_chars = "!@#$%^&*"

def generate_default_username(include_numbers, include_special_chars):
    """Generate a username using the default structure: adjective + noun."""
    username = random.choice(adjectives) + random.choice(nouns)
    if include_numbers:
        username += str(random.randint(0, 999))
    if include_special_chars:
        username += random.choice(special_chars)
    return username

def generate_custom_username(pattern, include_numbers, include_special_chars):
    """Generate a username based on a custom pattern with placeholders."""
    # Replace placeholders for adjectives and nouns.
    username = pattern.replace("{adj}", random.choice(adjectives)).replace("{noun}", random.choice(nouns))
    
    # Replace {num} placeholder: if numbers are included, substitute with a random number; otherwise, remove.
    if "{num}" in username:
        replacement = str(random.randint(0, 999)) if include_numbers else ""
        username = username.replace("{num}", replacement)
    
    # Replace {spec} placeholder: if special characters are included, substitute with one; otherwise, remove.
    if "{spec}" in username:
        replacement = random.choice(special_chars) if include_special_chars else ""
        username = username.replace("{spec}", replacement)
        
    return username

def adjust_length(username, desired_length):
    """Trim or pad the username to match the desired length."""
    if len(username) > desired_length:
        # Trim to the desired length.
        username = username[:desired_length]
    elif len(username) < desired_length:
        # Pad with random letters and digits.
        pad_length = desired_length - len(username)
        username += ''.join(random.choices(string.ascii_letters + string.digits, k=pad_length))
    return username

def save_usernames(usernames, filename="usernames.txt"):
    """Append generated usernames to a text file."""
    with open(filename, "a") as file:
        for username in usernames:
            file.write(username + "\n")
    print(f"{len(usernames)} usernames saved to {filename}.")

def main():
    print("Welcome to the Random Username Generator!")
    try:
        num_usernames = int(input("How many usernames would you like to generate? "))
        
        include_numbers = input("Include numbers? (yes/no): ").strip().lower() == "yes"
        include_special_chars = input("Include special characters? (yes/no): ").strip().lower() == "yes"
        
        # Ask if the user wants to specify a custom pattern.
        use_custom_pattern = input("Would you like to define a custom username pattern? (yes/no): ").strip().lower() == "yes"
        pattern = ""
        if use_custom_pattern:
            print("\nUse the following placeholders in your pattern:")
            print("  {adj}  - Random adjective")
            print("  {noun} - Random noun")
            print("  {num}  - Random number (if numbers included)")
            print("  {spec} - Special character (if special characters included)")
            pattern = input("Enter your custom pattern: ").strip()
        
        # Ask if the user wants to set a desired length.
        set_length = input("Would you like to set a desired username length? (yes/no): ").strip().lower() == "yes"
        desired_length = None
        if set_length:
            desired_length = int(input("Enter the desired length: "))
        
        # Generate the list of usernames.
        usernames = []
        for _ in range(num_usernames):
            if use_custom_pattern:
                uname = generate_custom_username(pattern, include_numbers, include_special_chars)
            else:
                uname = generate_default_username(include_numbers, include_special_chars)
            
            if desired_length:
                uname = adjust_length(uname, desired_length)
            usernames.append(uname)
        
        # Display generated usernames.
        print("\nGenerated Usernames:")
        for uname in usernames:
            print(uname)
        
        # Save usernames to file if requested.
        save_option = input("\nWould you like to save these usernames to a file? (yes/no): ").strip().lower()
        if save_option == "yes":
            save_usernames(usernames)
    
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
