# Tech Support System

A Python + MS SQL Server terminal application for managing IT support tickets.

## Setup After Cloning

```bash
git clone <your-repo-url>
cd Project
```

### Step 1 — Create the database

```bash
sqlcmd -U sa -P examlyMssql@123 -i setup.sql
```

> This creates the `appdb` database and the `SupportTickets` table in one shot.

### Step 2 — Install dependencies

```bash
pip install -r requirements.txt
```

### Step 3 — Run tests

```bash
python3 -m pytest tests.py -v
```

### Step 4 — Run the app

```bash
python3 main.py
```

---

## Project Structure

```
Project/
├── exception/
│   └── ticket_not_found_exception.py
├── model/
│   └── ticket.py
├── repository/
│   └── ticket_management.py
├── util/
│   └── db_util.py
├── main.py
├── tests.py
├── setup.sql
├── requirements.txt
└── README.md
```
