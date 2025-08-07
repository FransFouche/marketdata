import requests
import json
from datetime import datetime
from typing import Dict, Optional

class GoldPriceService:
    """Service to fetch gold prices from gold-api.com"""
    
    def __init__(self):
        self.base_url = "https://api.gold-api.com/price"
        
    def get_gold_price(self) -> Optional[Dict]:
        """
        Fetch current gold price from the API
        
        Returns:
            Dict containing gold price data or None if failed
        """
        try:
            response = requests.get(f"{self.base_url}/XAU", timeout=10)
            response.raise_for_status()
            
            data = response.json()
            
            # Format the response for our application
            formatted_data = {
                'symbol': data.get('symbol', 'XAU'),
                'price_usd_per_oz': data.get('price'),
                'currency': data.get('currency', 'USD'),
                'timestamp': data.get('timestamp'),
                'formatted_timestamp': datetime.fromtimestamp(data.get('timestamp', 0)).strftime('%Y-%m-%d %H:%M:%S UTC') if data.get('timestamp') else 'Unknown',
                'raw_data': data
            }
            
            return formatted_data
            
        except requests.exceptions.RequestException as e:
            print(f"Error fetching gold price: {e}")
            return None
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON response: {e}")
            return None
        except Exception as e:
            print(f"Unexpected error: {e}")
            return None
    
    def format_price_message(self, price_data: Dict) -> str:
        """
        Format price data into a readable message
        
        Args:
            price_data: Dictionary containing price information
            
        Returns:
            Formatted string message
        """
        if not price_data:
            return "Unable to fetch current gold price data."
        
        price = price_data.get('price_usd_per_oz', 'N/A')
        timestamp = price_data.get('formatted_timestamp', 'Unknown')
        
        message = f"""
📈 GOLD PRICE UPDATE 📈

Current Gold Price: ${price:,.2f} USD per troy ounce
Last Updated: {timestamp}

Symbol: {price_data.get('symbol', 'XAU')}
Currency: {price_data.get('currency', 'USD')}

---
This is an automated price update from your Gold Price Monitoring POC.
        """
        
        return message.strip()