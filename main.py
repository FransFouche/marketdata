#!/usr/bin/env python3
"""
Gold Price Monitoring POC Application

This application fetches the current gold price and sends it via email.
It can be run manually or scheduled to run automatically.
"""

import argparse
import schedule
import time
from datetime import datetime
from gold_price_service import GoldPriceService
from email_service import EmailService

class GoldPriceMonitor:
    """Main application class for gold price monitoring"""
    
    def __init__(self):
        self.gold_service = GoldPriceService()
        self.email_service = EmailService()
    
    def send_price_update(self, to_email=None):
        """
        Fetch current gold price and send email notification
        
        Args:
            to_email: Optional email address to send to (uses default if not provided)
        """
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Fetching gold price...")
        
        # Fetch gold price
        price_data = self.gold_service.get_gold_price()
        
        if price_data:
            print(f"✅ Gold price fetched: ${price_data['price_usd_per_oz']:,.2f} USD/oz")
            
            # Format message
            message = self.gold_service.format_price_message(price_data)
            
            # Send email
            success = self.email_service.send_price_notification(message, to_email)
            
            if success:
                print("✅ Email notification sent successfully!")
                return True
            else:
                print("❌ Failed to send email notification")
                return False
        else:
            print("❌ Failed to fetch gold price")
            return False
    
    def validate_setup(self):
        """Validate that the application is properly configured"""
        print("🔧 Validating configuration...")
        
        # Check email configuration
        email_valid = self.email_service.validate_configuration()
        
        # Test API connection
        print("🌐 Testing API connection...")
        test_data = self.gold_service.get_gold_price()
        api_valid = test_data is not None
        
        if api_valid:
            print("✅ API connection successful")
        else:
            print("❌ API connection failed")
        
        return email_valid and api_valid
    
    def run_scheduler(self, interval_minutes=60):
        """
        Run the application on a schedule
        
        Args:
            interval_minutes: How often to check prices (in minutes)
        """
        print(f"🕐 Starting scheduled monitoring (every {interval_minutes} minutes)")
        print("Press Ctrl+C to stop")
        
        # Schedule the job
        schedule.every(interval_minutes).minutes.do(self.send_price_update)
        
        # Run initial check
        self.send_price_update()
        
        try:
            while True:
                schedule.run_pending()
                time.sleep(1)
        except KeyboardInterrupt:
            print("\n🛑 Monitoring stopped by user")

def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(description='Gold Price Monitoring POC')
    parser.add_argument('--validate', action='store_true', 
                       help='Validate configuration and test connections')
    parser.add_argument('--send-now', action='store_true', 
                       help='Send a price update immediately')
    parser.add_argument('--schedule', type=int, metavar='MINUTES', 
                       help='Run on schedule (specify interval in minutes)')
    parser.add_argument('--email', type=str, 
                       help='Email address to send to (overrides default)')
    
    args = parser.parse_args()
    
    monitor = GoldPriceMonitor()
    
    if args.validate:
        print("🔍 Validating setup...")
        if monitor.validate_setup():
            print("✅ All systems ready!")
        else:
            print("❌ Configuration issues found. Please check your .env file")
            return 1
    
    elif args.send_now:
        print("📧 Sending immediate price update...")
        success = monitor.send_price_update(args.email)
        return 0 if success else 1
    
    elif args.schedule:
        if args.schedule < 1:
            print("❌ Schedule interval must be at least 1 minute")
            return 1
        monitor.run_scheduler(args.schedule)
    
    else:
        # Show help if no arguments provided
        parser.print_help()
        print("\nExamples:")
        print("  python main.py --validate                    # Test configuration")
        print("  python main.py --send-now                    # Send price update now")
        print("  python main.py --schedule 30                 # Monitor every 30 minutes")
        print("  python main.py --send-now --email user@ex.com # Send to specific email")
    
    return 0

if __name__ == "__main__":
    exit(main())