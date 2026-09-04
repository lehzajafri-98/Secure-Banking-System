# Secure Banking System (RSA Encryption & Data Integrity)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)
![Encryption](https://img.shields.io/badge/Asymmetric-RSA--2048%20%2F%204096-brightgreen?style=for-the-badge)
![Integrity](https://img.shields.io/badge/Hashing-SHA--256-orange?style=for-the-badge)
![Security](https://img.shields.io/badge/Module-Financial%20Security-red?style=for-the-badge)

A Python backend security module designed to handle safe financial transactions, secure sensitive user data, and guarantee end-to-end data integrity across banking operations.

## 🚀 Key Features

- **Asymmetric Data Encryption**: Employs RSA public-key cryptography to encrypt sensitive user payloads and personal financial details before transmission or storage.
- **Data Integrity Verification**: Uses SHA-256 cryptographic hashing to generate unique digital fingerprints (checksums) for transactions, ensuring payload protection against tampering.
- **Secure Key Management**: Automated generation and loading of PEM-encoded RSA Public and Private key pairs using OAEP padding.
- **End-to-End Transaction Safeguards**: Ensures Confidentiality, Authenticity, and Integrity across user financial operations.

## 🛠 Tech Stack

- **Language**: Python 3.8+
- **Security Library**: `cryptography` (`hazmat.primitives.asymmetric.rsa`, `padding`, `hashes`)
- **Key Encoding**: `serialization` (PEM format)

## 📊 Module Architecture & Capabilities

| Security Component | Algorithm / Protocol | Primary Purpose |
| :--- | :--- | :--- |
| **Payload Encryption** | RSA (with OAEP & SHA-256) | Safeguards sensitive transaction details and user IDs |
| **Integrity Hashing** | SHA-256 | Validates that financial data is unchanged during transit |
| **Key Pairs** | RSA 2048-bit / 4096-bit | Public key for encryption, Private key for decryption |

## ⚙️ Installation & Prerequisites

### 1. Requirements & System Setup
Make sure you have **Python 3.8+** and `pip` installed on your system.

### 2. Step-by-Step Installation

```bash
# Step 1: Clone the Repository
git clone [https://github.com/lehzajafri-98/Secure-Banking-System.git](https://github.com/lehzajafri-98/Secure-Banking-System.git)
cd Secure-Banking-System

# Step 2: (Optional) Create and activate a Virtual Environment
# On Windows:
python -m venv venv
venv\Scripts\activate

# On Linux / macOS:
python3 -m venv venv
source venv/bin/activate

# Step 3: Install Required Dependencies
pip install cryptography
