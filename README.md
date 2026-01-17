# secured_html

A simple Python-based web server that protects an HTML page behind a password.  
The secured content is displayed only after the correct password is entered.

This project is intended for **basic access restriction** (e.g. internal pages, demos, temporary protection), not for high-security use cases.

---

## Features

- Password-protected access to an HTML page
- Simple login page
- Lightweight and easy to modify
- Built with Python and Flask
- No database required

---

## Project Structure

```
secured_html/
├── server.py          # Main Python server
└── templates/         # HTML templates
    ├── login.html     # Login page
    └── secured.html   # Protected page
```

---

## Requirements

- Python 3.8+
- Flask

Install Flask if not already installed:

```bash
pip install flask
```

---

## Quick Start

1. Clone the repository

```bash
git clone https://github.com/HackedByTomaso/secured_html.git
cd secured_html
```

2. (Optional but recommended) Create a virtual environment

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux / macOS
source .venv/bin/activate
```

3. Install dependencies

```bash
pip install flask
```

4. Configure the password  
Open `server.py` and set the password according to how it is defined in the file
(e.g. a variable or environment value).

5. Run the server

```bash
python server.py
```

6. Open your browser and go to:

```
http://127.0.0.1:5000
```

---

## Configuration Tips

For better practice:
- Do **not** hardcode the password – use environment variables.
- Add rate limiting or delay after failed attempts.
- Do not log passwords.
- Use HTTPS if exposed publicly (e.g. behind Nginx or a reverse proxy).

---

## Security Notice

⚠️ This project **does not replace real authentication systems**.  
It is not suitable for protecting sensitive or personal data.

For production use, consider:
- Proper user authentication
- Encrypted sessions
- HTTPS
- Framework-level security features

---

## License

MIT License – feel free to use, modify, and share.
