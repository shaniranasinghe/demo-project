# MCP-Based Self-Healing Flow

In this POC, MCP is not used to read failure logs.

MCP is used only after the root cause model identifies that the failure is an application defect.

---

## Final Flow

```text
Failure log is collected manually / from dataset / from CI output
        ↓
Root cause classifier predicts the root cause
        ↓
Decision engine checks whether healing is allowed
        ↓
If root cause = application_defect
        ↓
LLM uses GitHub MCP to read repository files
        ↓
LLM generates a minimal code patch
        ↓
Tests are executed
        ↓
If tests pass, create branch + commit + pull request
        ↓
Developer review
```

---

## GitHub MCP Usage

Use GitHub MCP for:

```text
get_file_contents
search_code
create_branch
create_or_update_file
push_files
create_pull_request
```

Do not use MCP for failure log collection at the first stage.

---

## Example Prompt for LLM Agent

```text
You are a controlled self-healing code agent.

Failure ID: F001
Root cause: application_defect
Confidence: 0.92

Error:
NameError: name 'total_amunt' is not defined

Stack trace:
app/calculator.py line 17

Failed test:
tests/test_calculator.py::test_calculate_total

Task:
Use GitHub MCP to read app/calculator.py and tests/test_calculator.py.
Find the smallest safe code change.
Do not modify unrelated files.
Do not push to main.
Create a new auto-heal branch.
Commit the change.
Open a draft pull request for developer review.
```

---

## Safety Rules

```text
Never push directly to main.
Never auto-merge.
Only create a branch and pull request.
Modify minimum number of files.
Run tests before marking healing as successful.
If confidence is low, stop and request manual review.
```
