# Self-Healing MCP Demo Project

This is a small demo project for research on:

**Failure Analysis and MCP-Based Controlled Self-Healing**

The goal is to prove this workflow:

```text
Failure log / error message
        ↓
Root cause classifier
        ↓
If root cause = application_defect
        ↓
LLM uses GitHub MCP to read repository files
        ↓
LLM generates a small code patch
        ↓
Tests validate the patch
        ↓
New branch + commit + pull request
        ↓
Developer review
```

This demo project is intentionally small so it is easy to test, break, fix, and use in your POC.

---

## Project Structure

```text
self-healing-mcp-demo/
│
├── app/
│   ├── __init__.py
│   ├── calculator.py
│   ├── user_service.py
│   └── main.py
│
├── tests/
│   ├── test_calculator.py
│   └── test_user_service.py
│
├── data/
│   └── sample_failure_dataset.csv
│
├── docs/
│   ├── FAILURE_SCENARIOS.md
│   └── MCP_SELF_HEALING_FLOW.md
│
├── .github/
│   └── workflows/
│       └── test.yml
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## How to Run Locally

### 1. Create virtual environment

```bash
python -m venv venv
```

### 2. Activate virtual environment

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run tests

```bash
pytest
```

Expected result:

```text
All tests passed
```

---

## How to Push to GitHub

### 1. Create a new GitHub repository

Example name:

```text
self-healing-mcp-demo
```

### 2. Open terminal inside this project folder

```bash
git init
git add .
git commit -m "initial self-healing POC demo project"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/self-healing-mcp-demo.git
git push -u origin main
```

Replace `YOUR_USERNAME` with your GitHub username.

---

## How to Create a Failure for the POC

Open:

```text
app/calculator.py
```

Change this correct code:

```python
return total_amount
```

Into this broken code:

```python
return total_amunt
```

Then run:

```bash
pytest
```

You should get a failure like:

```text
NameError: name 'total_amunt' is not defined
```

This is an example of:

```text
root_cause = application_defect
healing_action = code_patch
```

---

## Research Use

Use this project to test:

1. Failure generation
2. Failure log collection
3. Root cause classification
4. MCP-based repository file reading
5. LLM patch generation
6. Test validation
7. Branch + commit + pull request creation

For the first POC, MCP does not need to read failure logs. MCP is used only after the root cause is identified, so the LLM can read GitHub repository files and prepare a patch.
