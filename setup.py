#!/usr/bin/env python3
"""
Setup script for Gold Price Monitoring POC

This script helps users configure their environment variables.
"""

import os
import getpass
import shutil

def create_env_file():
    """Interactive setup for .env file"""
    print("🔧 Gold Price Monitoring POC - Setup")
    print("=" * 50)
    print()
    
    # Check if .env already exists
    if os.path.exists('.env'):
        response = input("⚠️  .env file already exists. Overwrite? (y/N): ").strip().lower()
        if response != 'y':
            print("Setup cancelled.")
            return
    
    print("📧 Email Configuration")
    print("Note: For Gmail, you'll need to use an 'App Password' instead of your regular password.")
    print("See: https://support.google.com/accounts/answer/185833")
    print()
    
    # Get email configuration
    email_server = input("SMTP Server (default: smtp.gmail.com): ").strip() or "smtp.gmail.com"
    email_port = input("SMTP Port (default: 587): ").strip() or "587"
    email_username = input("Your email address: ").strip()
    
    if not email_username:
        print("❌ Email address is required!")
        return
    
    email_password = getpass.getpass("Email password (or app password): ").strip()
    
    if not email_password:
        print("❌ Email password is required!")
        return
    
    email_to = input("Recipient email address (default: same as sender): ").strip() or email_username
    
    # Create .env file
    env_content = f"""# Email Configuration
EMAIL_SMTP_SERVER={email_server}
EMAIL_SMTP_PORT={email_port}
EMAIL_USERNAME={email_username}
EMAIL_PASSWORD={email_password}
EMAIL_TO={email_to}

# API Configuration (currently not needed for gold-api.com)
GOLD_API_KEY=
"""
    
    try:
        with open('.env', 'w') as f:
            f.write(env_content)
        
        print()
        print("✅ .env file created successfully!")
        print()
        print("🔒 Security Note:")
        print("   - Your .env file contains sensitive information")
        print("   - Make sure it's not committed to version control")
        print("   - The .gitignore file should exclude .env files")
        print()
        print("🚀 Next steps:")
        print("   1. Test configuration: python main.py --validate")
        print("   2. Send test email: python main.py --send-now")
        print("   3. Start monitoring: python main.py --schedule 60")
        
    except Exception as e:
        print(f"❌ Error creating .env file: {e}")

def install_dependencies():
    """Install Python dependencies"""
    print("📦 Installing dependencies...")
    
    if shutil.which('pip'):
        os.system('pip install -r requirements.txt')
    elif shutil.which('pip3'):
        os.system('pip3 install -r requirements.txt')
    else:
        print("❌ pip not found. Please install dependencies manually:")
        print("   pip install -r requirements.txt")

def main():
    """Main setup function"""
    print("Welcome to Gold Price Monitoring POC Setup!")
    print()
    
    # Check if requirements.txt exists
    if os.path.exists('requirements.txt'):
        install_deps = input("📦 Install Python dependencies? (Y/n): ").strip().lower()
        if install_deps != 'n':
            install_dependencies()
    
    print()
    create_env_file()

if __name__ == "__main__":
    main()