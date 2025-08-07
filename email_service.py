import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import Optional
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class EmailService:
    """Service to send email notifications"""
    
    def __init__(self):
        self.smtp_server = os.getenv('EMAIL_SMTP_SERVER', 'smtp.gmail.com')
        self.smtp_port = int(os.getenv('EMAIL_SMTP_PORT', '587'))
        self.username = os.getenv('EMAIL_USERNAME')
        self.password = os.getenv('EMAIL_PASSWORD')
        self.default_to_email = os.getenv('EMAIL_TO')
        
    def send_price_notification(self, message: str, to_email: Optional[str] = None, subject: str = "Gold Price Update") -> bool:
        """
        Send a price notification email
        
        Args:
            message: The message content to send
            to_email: Recipient email address (uses default if not provided)
            subject: Email subject line
            
        Returns:
            True if email sent successfully, False otherwise
        """
        if not self.username or not self.password:
            print("Email credentials not configured. Please set EMAIL_USERNAME and EMAIL_PASSWORD in .env file")
            return False
            
        to_email = to_email or self.default_to_email
        if not to_email:
            print("No recipient email configured. Please set EMAIL_TO in .env file or provide to_email parameter")
            return False
        
        try:
            # Create message
            msg = MIMEMultipart()
            msg['From'] = self.username
            msg['To'] = to_email
            msg['Subject'] = subject
            
            # Add body to email
            msg.attach(MIMEText(message, 'plain'))
            
            # Create SMTP session
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()  # Enable TLS security
            server.login(self.username, self.password)
            
            # Send email
            text = msg.as_string()
            server.sendmail(self.username, to_email, text)
            server.quit()
            
            print(f"Email sent successfully to {to_email}")
            return True
            
        except smtplib.SMTPAuthenticationError:
            print("SMTP Authentication failed. Please check your email credentials.")
            return False
        except smtplib.SMTPException as e:
            print(f"SMTP error occurred: {e}")
            return False
        except Exception as e:
            print(f"Error sending email: {e}")
            return False
    
    def validate_configuration(self) -> bool:
        """
        Validate that email configuration is properly set up
        
        Returns:
            True if configuration is valid, False otherwise
        """
        if not self.username:
            print("❌ EMAIL_USERNAME not configured")
            return False
        if not self.password:
            print("❌ EMAIL_PASSWORD not configured")
            return False
        if not self.default_to_email:
            print("❌ EMAIL_TO not configured")
            return False
        
        print("✅ Email configuration appears valid")
        return True