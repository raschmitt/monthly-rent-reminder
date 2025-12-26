# 📧 Monthly Email Sender

This project is a **simple, configurable Python script** that sends emails using SMTP.
It is designed to:

* Read the **email message** from a YAML file
* Read the **recipients list** from a YAML file
* Use **environment variables** for credentials and sender address
* Run **locally** or **automatically via GitHub Actions**

## ⚙️ How It Works

1. `send_email.py`:

   * Loads the email **subject** and **content** from `message.yml`
   * Loads the list of recipients from `recipients.yml`
   * Reads SMTP credentials and sender email from environment variables
   * Sends the email using Python’s `smtplib`

2. GitHub Actions:

   * Runs the script automatically
   * Executes **every 10th day of the month**
   * Uses GitHub **Secrets** for sensitive data
   * Uses GitHub **Variables** for non-sensitive configuration

## 🔐 Environment Variables

### Required Variables

| Variable Name    | Type     | Description                         |
| ---------------- | -------- | ----------------------------------- |
| `EMAIL_ADDRESS`  | Variable | Sender email address                |
| `EMAIL_PASSWORD` | Secret   | SMTP password or app password       |
| `SMTP_SERVER`    | Variable | SMTP server (e.g. `smtp.gmail.com`) |
| `SMTP_PORT`      | Variable | SMTP port (usually `587`)           |


## ▶️ Running Locally

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

### 2️⃣ Create a virtual environment (optional but recommended)

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Export environment variables

```bash
export EMAIL_ADDRESS="your-email@gmail.com"
export EMAIL_PASSWORD="your-email-password"
export SMTP_SERVER="smtp.gmail.com"
export SMTP_PORT="587"
```

### 5️⃣ Run the script

```bash
python send_email.py
```
