#!/usr/bin/env python3
"""
Demo script for Gold Price Monitoring POC

This script demonstrates the core functionality without requiring email setup.
"""

from gold_price_service import GoldPriceService
from datetime import datetime

def demo():
    """Demonstrate the POC functionality"""
    print("🏆 Gold Price Monitoring POC - Demo")
    print("=" * 50)
    print()
    
    # Initialize the service
    print("🔧 Initializing Gold Price Service...")
    service = GoldPriceService()
    print("✅ Service initialized")
    print()
    
    # Fetch current gold price
    print("🌐 Fetching current gold price...")
    price_data = service.get_gold_price()
    
    if price_data:
        print("✅ Gold price data retrieved successfully!")
        print()
        
        # Display raw data
        print("📊 Current Gold Price Data:")
        print(f"   Symbol: {price_data['symbol']}")
        print(f"   Price: ${price_data['price_usd_per_oz']:,.2f} USD per troy ounce")
        print(f"   Currency: {price_data['currency']}")
        print(f"   Last Updated: {price_data['formatted_timestamp']}")
        print()
        
        # Show formatted email message
        print("📧 Sample Email Message:")
        print("-" * 30)
        message = service.format_price_message(price_data)
        print(message)
        print("-" * 30)
        print()
        
        print("✨ Demo completed successfully!")
        print()
        print("🚀 Next Steps:")
        print("   1. Run 'python setup.py' to configure email")
        print("   2. Run 'python main.py --validate' to test configuration")
        print("   3. Run 'python main.py --send-now' to send actual email")
        print("   4. Run 'python main.py --schedule 60' for hourly monitoring")
        
    else:
        print("❌ Failed to fetch gold price data")
        print("   - Check internet connection")
        print("   - Verify API service is operational")

if __name__ == "__main__":
    demo()