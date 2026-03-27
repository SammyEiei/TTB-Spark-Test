def simpleCipher(encrypted: str, k: int) -> str:
    """
    Decrypt a string by shifting each character k steps counterclockwise
    on the alphabet wheel (A-Z).
    """
    result = []
    for char in encrypted:
        # Shift counterclockwise = subtract k, wrap around with modulo 26
        decrypted_char = chr((ord(char) - ord('A') - k) % 26 + ord('A'))
        result.append(decrypted_char)
    return ''.join(result)


# Test the example from the assignment
if __name__ == "__main__":
    encrypted = "VTAOG"
    k = 2
    print(f"Encrypted : {encrypted}")
    print(f"k         : {k}")
    print(f"Decrypted : {simpleCipher(encrypted, k)}")  # Expected: TRYME
