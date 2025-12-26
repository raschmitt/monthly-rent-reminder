import smtplib
import argparse
import yaml
from email.message import EmailMessage
from pathlib import Path


def send_email(
    smtp_server: str,
    smtp_port: int,
    email_address: str,
    email_password: str,
    recipients: list[str],
    subject: str,
    content: str,
):
    msg = EmailMessage()
    msg["From"] = email_address
    msg["To"] = ", ".join(recipients)
    msg["Subject"] = subject
    msg.set_content(content)

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(email_address, email_password)
        server.send_message(msg)


def main():
    parser = argparse.ArgumentParser(description="Send an email using SMTP")

    parser.add_argument("--smtp-server", required=True)
    parser.add_argument("--smtp-port", type=int, required=True)
    parser.add_argument("--email-address", required=True)
    parser.add_argument("--email-password", required=True)
    parser.add_argument("--message-file", default="message.yml")
    parser.add_argument("--recipients-file", default="recipients.yml")

    args = parser.parse_args()

    # Load message YAML
    message = yaml.safe_load(
        Path(args.message_file).read_text(encoding="utf-8")
    )

    subject = message["subject"]
    content = message["content"]

    # Load recipients YAML
    recipients_data = yaml.safe_load(
        Path(args.recipients_file).read_text(encoding="utf-8")
    )

    recipients = recipients_data["recipients"]

    send_email(
        smtp_server=args.smtp_server,
        smtp_port=args.smtp_port,
        email_address=args.email_address,
        email_password=args.email_password,
        recipients=recipients,
        subject=subject,
        content=content,
    )

    print(f"Email sent to {len(recipients)} recipient(s)")


if __name__ == "__main__":
    main()
