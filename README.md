# Gold Price Monitoring POC

A proof-of-concept application that fetches real-time gold prices and sends email notifications.

## 🚀 Features

- **Real-time Gold Prices**: Fetches current gold prices from a free API (gold-api.com)
- **Email Notifications**: Sends formatted price updates via email
- **Flexible Scheduling**: Run manually, once, or on a schedule
- **Easy Configuration**: Interactive setup script
- **Error Handling**: Robust error handling and validation

## 📋 Requirements

- Python 3.6+
- Internet connection
- Email account with SMTP access (Gmail recommended)

## 🛠️ Quick Setup

1. **Clone and navigate to the project**:
   ```bash
   cd /workspace
   ```

2. **Run the setup script**:
   ```bash
   python setup.py
   ```
   This will:
   - Install Python dependencies
   - Help you configure email settings
   - Create a `.env` file with your credentials

3. **Test the configuration**:
   ```bash
   python main.py --validate
   ```

4. **Send a test email**:
   ```bash
   python main.py --send-now
   ```

## 📧 Email Configuration

For Gmail users:
1. Enable 2-factor authentication
2. Generate an "App Password" (not your regular password)
3. Use the app password in the setup

For other email providers, you'll need:
- SMTP server address
- SMTP port (usually 587 for TLS)
- Your email credentials

## 🔧 Usage

### Manual Commands

```bash
# Validate configuration
python main.py --validate

# Send immediate price update
python main.py --send-now

# Send to specific email
python main.py --send-now --email recipient@example.com

# Start scheduled monitoring (every 30 minutes)
python main.py --schedule 30

# View all options
python main.py --help
```

### Scheduled Monitoring

To run continuous monitoring:
```bash
python main.py --schedule 60  # Check every hour
```

Press `Ctrl+C` to stop monitoring.

## 📊 Sample Email Output

```
📈 GOLD PRICE UPDATE 📈

Current Gold Price: $2,063.45 USD per troy ounce
Last Updated: 2024-01-15 14:30:25 UTC

Symbol: XAU
Currency: USD

---
This is an automated price update from your Gold Price Monitoring POC.
```

## 🔒 Security

- Sensitive information is stored in `.env` file (excluded from git)
- Use app passwords for email authentication
- Never commit credentials to version control

## 🛡️ Error Handling

The application includes comprehensive error handling for:
- Network connectivity issues
- API failures
- Email authentication problems
- Invalid configurations

## 🔄 API Information

Currently uses the free Gold API from gold-api.com:
- **Free tier**: Unlimited requests
- **Response time**: ~100ms
- **Updates**: Real-time
- **No API key required**

## 📁 Project Structure

```
/workspace/
├── main.py                 # Main application
├── gold_price_service.py   # Gold price API integration
├── email_service.py        # Email notification service
├── setup.py               # Interactive setup script
├── requirements.txt       # Python dependencies
├── .env.example          # Example environment file
├── .env                  # Your actual environment file (created by setup)
├── .gitignore           # Git ignore file
└── README.md            # This file
```

## 🚧 Future Enhancements

This POC can be extended with:
- Multiple precious metals (silver, platinum, palladium)
- Price alerts with thresholds
- Historical price tracking
- Web dashboard
- Database storage
- Webhook notifications
- Multiple email recipients
- SMS notifications

## 🐛 Troubleshooting

**Email authentication fails**:
- For Gmail, ensure you're using an App Password, not your regular password
- Check that 2-factor authentication is enabled
- Verify SMTP settings

**API connection fails**:
- Check internet connectivity
- Verify the API service is operational

**Permission errors**:
- Ensure Python has permission to create files
- Check that you're in the correct directory

## 📞 Support

This is a proof-of-concept application. For production use, consider:
- More robust error handling
- Logging to files
- Database integration
- Rate limiting
- Monitoring and alerting