
# Northstar-dashboard

Northstar Retail Co. Support Deflection MVP - Self-Serve Dashboard

---

## Team Members

| Name | Role |
| :--- | :--- |
| Olang'o Benony Joseph | Data Engineer |
| Sithandekile Ndhlovu | API Engineer |
| Michael Onyango | Frontend UI |
| Deborah Russell-Abia | Integrator/QA & Process Owner |

---

## Categories Covered

-  **Order Status** – "Where is my order?" / "Has this shipped yet?"
-  **Returns & Refunds** – "How do I return this?" / "When will I get my refund?"

---

## Project Structure

```
northstar-dashboard/
├── .gitignore
├── requirements.txt
├── README.md
├── app.py
├── orders.json
├── returns.json
├── index.html
├── style.css
├── script.js
└── go_live_draft.txt
```

---

## How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/debbieruss-hub/northstar-dashboard.git
cd northstar-dashboard
```

### 2. Create and Activate a Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python app.py
```

### 5. Open Your Browser

Navigate to: [http://localhost:5000](http://localhost:5000)

---

## How to Test

| Order ID | Email | Expected Result |
| :--- | :--- | :--- |
| `ORD-101` | `alice@mail.com` | Order details + Refund status |
| `ORD-105` | `eve@mail.com` | Order details only (no refund) |
| `ORD-999` | `test@mail.com` | "Order ID not found" |

---

## Workflow

- Each person works on their own feature branch
- All changes go through Pull Requests into `dev`
- Integrator reviews and merges all PRs
- `dev` merges into `main` at submission deadline

---

## Commit Message Format

Every commit follows:

```
<type>: <what changed> - <why it matters>
```

| Type | Use For | Example |
| :--- | :--- | :--- |
| `feat:` | New feature | `feat: add order lookup endpoint - allows dashboard to fetch shipping status` |
| `fix:` | Bug fix | `fix: handle invalid order ID - prevents server crash` |
| `docs:` | Documentation | `docs: update README - adds project structure and setup instructions` |
| `chore:` | Maintenance | `chore: set up project foundation - adds gitignore and requirements` |
| `style:` | CSS/UI | `style: improve dashboard layout - makes it easier to read results` |

**Never use:** `wip`, `updates`, `fix` (without context)

---

## Contributors

- [Olang'o Benony Joseph](https://github.com/KingBen-coder) – Data Engineer
- [Sithandekile Ndhlovu](https://github.com/sithandekile) – API Engineer
- [Michael Onyango](https://github.com/okech-michael) – Frontend UI
- [Deborah Russell-Abia](https://github.com/debbieruss-hub) – Integrator/QA & Process Owner

---

## License

This project was completed as part of the **Northstar Sprint** assignment for the **Power Learn Project**.
```

---

