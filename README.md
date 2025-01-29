# README - Automated Message Sending with Mobile Connectée / Link to Windows

## Description
This script utilizes Selenium to automate message sending via **Mobile Connectée / Link to Windows**. It reads phone numbers from a `numbers.txt` file and sends predefined messages to each contact.

⚠ **Warning**:
- **Do not overuse this tool**! It is limited to a maximum of **400 different recipients** to prevent being blocked by Microsoft.
- It works **only on Windows**.
- **A laptop is required** since you need to scan a QR code for the first login.

## Prerequisites
### 1. System Requirements
- **Windows** (this script has not been tested on other OS)
- **Microsoft Edge or Chrome** installed
- **WebDriver for Edge or ChromeDriver** matching your browser version (should be in the PATH or the script folder)

### 2. Required Python Libraries
Ensure you have Selenium installed:
```bash
pip install selenium
```

## Features
1. **First-time connection**:
   - Opens Mobile Connectée / Link to Windows in your browser.
   - Requires scanning a QR code for authentication.
   - After logging in, press **Enter** to start sending messages.

2. **Automated message sending**:
   - Reads phone numbers from `numbers.txt`.
   - Selects each contact and sends a predefined message.
   - Default message:
     ```
     Hi, reply if you received this message. I am developing a tool to send thousands of messages to strangers. Here is my Discord: __eeva
     ```
   - **You can modify this message in the script**.

3. **Customizing phone numbers**:
   - The script can send messages to numbers starting with `06` or `07`. You can modify this in `numbers.txt`.
   - If `numbers.txt` does not exist, you can generate numbers using a **Number Generator**.

## Usage
### Step 1: Add phone numbers
Create a `numbers.txt` file in the same directory as the script and add a list of phone numbers (one per line):
```
0601020304
0612345678
0711223344
```

### Step 2: Run the script
#### First login (with graphical interface)
```bash
python script.py
```
🚀 **Do not use headless mode for the first login!**

#### Subsequent logins (optional headless mode)
Set `user_wants_headless = True` in the script to run it without opening the browser window.

### Step 3: Verification & Best Practices
- **Do not exceed 400 messages** to avoid being blocked.
- **Ensure valid phone numbers are used**.
- **Test with a small number of contacts before sending bulk messages**.

## Common Errors & Troubleshooting
### Error: WebDriver Not Found
- Check if you have downloaded [WebDriver for Edge](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/) or [ChromeDriver](https://sites.google.com/chromium.org/driver/) and that its version matches your browser.
- Add WebDriver to your system PATH or place it in the script directory.

### Error: Mobile Connectée / Link to Windows Not Loading
- Ensure you have scanned the QR code and are logged into Mobile Connectée / Link to Windows.
- Restart the script after verifying your login status.

### Error: The script stops after a few messages
- Microsoft might be restricting your activity. Reduce the message frequency or limit the number of recipients.
- If necessary, use a VPN or try another Microsoft account.

### Error: Input element not found
- Mobile Connectée / Link to Windows may have updated its interface. Try updating Selenium and checking the correct XPATH for elements.

## Frequently Asked Questions (FAQ)
### 1. Can I send messages to more than 400 contacts?
No, sending messages to more than 400 different recipients may result in your account being flagged. This limit is set to prevent excessive usage.

### 2. Can I change the message text?
Yes! You can modify the message inside the script before running it.

### 3. Can I use this on Mac or Linux?
No, this script is designed specifically for Windows.

### 4. What if I get logged out of Mobile Connectée / Link to Windows?
If you are logged out, simply restart the script and follow the login process again.

### 5. How can I generate a list of phone numbers?
You can use a **Number Generator** to create a list of random phone numbers and save them in `numbers.txt`.

### 6. Do I need a phone to run this?
Yes, you need a phone with Mobile Connectée / Link to Windows set up to scan the QR code and link your account.

### 7. Can I change the `06` or `07` prefix?
Yes! Simply modify the numbers in `numbers.txt`.


# License

Please just don't steal my code..
---
🚀 **Use this tool responsibly and avoid excessive usage!**

