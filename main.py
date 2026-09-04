import hashlib
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization


class SecureBankingModule:
    def __init__(self):
        """Initialize and generate RSA 2048-bit Private & Public Key Pair."""
        print("[+] Initializing Secure Banking Module...")
        print("[+] Generating RSA 2048-bit Key Pair...")

        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        self.public_key = self.private_key.public_key()
        print("[✓] RSA Keys generated successfully.\n")

    def generate_sha256_hash(self, data: bytes) -> str:
        """Calculate SHA-256 cryptographic hash (checksum) for data integrity."""
        hash_object = hashlib.sha256(data)
        checksum = hash_object.hexdigest()
        return checksum

    def encrypt_data(self, plaintext: bytes) -> bytes:
        """Encrypt sensitive payload using RSA Public Key with OAEP padding."""
        ciphertext = self.public_key.encrypt(
            plaintext,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return ciphertext

    def decrypt_data(self, ciphertext: bytes) -> bytes:
        """Decrypt payload using RSA Private Key."""
        decrypted_text = self.private_key.decrypt(
            ciphertext,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return decrypted_text


# --- Simulation Script ---
if __name__ == "__main__":
    # 1. Instantiate the Security Module
    bank_security = SecureBankingModule()

    # 2. Sample Financial Transaction Payload
    transaction_payload = b"Sender: Bank_A | Receiver: User_102 | Amount: $15,000 | Account: PK9876543210"
    print(f"[>] Original Transaction Data:\n    {transaction_payload.decode()}\n")

    # 3. Step 1: Generate Data Integrity SHA-256 Hash
    sender_hash = bank_security.generate_sha256_hash(transaction_payload)
    print(f"[1] SHA-256 Checksum (Sender Side):\n    {sender_hash}\n")

    # 4. Step 2: Encrypt Data with RSA Public Key
    encrypted_payload = bank_security.encrypt_data(transaction_payload)
    print(f"[2] Payload Encrypted with RSA-OAEP (Base64/Hex Sample):\n    {encrypted_payload[:32].hex()}...\n")

    # 5. Step 3: Decrypt Data with RSA Private Key
    decrypted_payload = bank_security.decrypt_data(encrypted_payload)
    print(f"[3] Decrypted Transaction Data:\n    {decrypted_payload.decode()}\n")

    # 6. Step 4: Verify Data Integrity (SHA-256 Hash Match)
    receiver_hash = bank_security.generate_sha256_hash(decrypted_payload)
    print(f"[4] SHA-256 Checksum (Receiver Side):\n    {receiver_hash}\n")

    # 7. Final Security Checks
    if sender_hash == receiver_hash and transaction_payload == decrypted_payload:
        print("==================================================")
        print("   [SUCCESS] End-to-End Data Integrity Verified!   ")
        print("   [SUCCESS] RSA Encryption & Decryption Passed!  ")
        print("==================================================")
    else:
        print("[ERROR] Data Tampering Detected or Decryption Failed!")
