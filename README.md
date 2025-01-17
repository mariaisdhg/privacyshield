# PrivacyShield

## Overview
**PrivacyShield** is a Python-based program designed to enhance privacy protection by blocking tracking scripts and managing cookie settings on Windows. It acts as a local proxy server that filters out requests to known tracking domains and enforces secure cookie policies in HTTP responses.

## Features
- **Blocking Tracking Scripts:** Identifies and blocks requests to common tracking script domains such as Google Analytics, Facebook, and DoubleClick.
- **Cookie Management:** Enhances privacy by setting HTTP-only and secure flags on cookies.

## Requirements
- Python 3.x

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/privacyshield.git
   ```
2. Navigate to the project directory:
   ```bash
   cd privacyshield
   ```

## Usage
Run the PrivacyShield proxy server:
```bash
python privacy_shield.py
```
By default, the server will run on `localhost` at port `8080`. Configure your browser to use `localhost:8080` as the proxy to start filtering requests.

## Configuration
Modify the `TRACKING_PATTERNS` list in `privacy_shield.py` to add or remove domains that you wish to block.

## Disclaimer
PrivacyShield is intended for personal use to enhance privacy. Use responsibly and comply with applicable laws and regulations regarding internet traffic filtering and privacy protection.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.