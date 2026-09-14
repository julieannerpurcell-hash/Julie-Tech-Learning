import re

def check_strength(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    levels = {0: "Very Weak", 1: "Weak", 2: "Fair", 3: "Good", 4: "Strong", 5: "Very Strong"}
    return levels[score]

if __name__ == "__main__":
    pw = input("Enter a password to check: ")
    print(f"Strength: {check_strength(pw)}")