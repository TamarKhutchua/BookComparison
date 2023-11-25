

def load_book(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read().lower()
        words = set(word for word in content.split() if word.isalpha())
        
    return words



b1 = load_book("poirot.txt")
b2 = load_book("mysterious.txt")
b3 = load_book("secret.txt")


print(f"Words Poirot: {len(b1)}")
print(f"Words Mysterious: {len(b2)}")
print(f"Words Secret: {len(b3)}")


print(f"Shared words for both books: {len(b1 & b2 & b3)}")
print(f"Unique words for both books: {len(b1 | b2 | b3)}")

print(f"Words which are not in book2: {len(b1 - b2)}")
print(f"Words which are not in book3: {len(b1 - b3)}")
print(f"Words which are not in book1: {len(b2 - b1)}")
print(f"Words which are not in book3: {len(b2 - b3)}")
print(f"Words which are not in book1: {len(b3 - b1)}")
print(f"Words which are not in book2: {len(b3 - b2)}")

print(f"Symmetric difference: {len(b1 ^ b2) + len(b1 ^ b3)}")