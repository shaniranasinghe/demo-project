# Failure Scenarios for POC

Use these scenarios to test the failure analysis and self-healing workflow.

---

## Scenario 1: Wrong Variable Name

File:

```text
app/calculator.py
```

Change:

```python
return total_amount
```

To:

```python
return total_amunt
```

Expected failure:

```text
NameError: name 'total_amunt' is not defined
```

Root cause:

```text
application_defect
```

Healing action:

```text
code_patch
```

Expected LLM fix:

```python
return total_amount
```

---

## Scenario 2: Syntax Error

File:

```text
app/calculator.py
```

Change:

```python
return a + b
```

To:

```python
return a + 
```

Expected failure:

```text
SyntaxError: invalid syntax
```

Root cause:

```text
application_defect
```

Healing action:

```text
code_patch
```

---

## Scenario 3: Wrong Test Expected Value

File:

```text
tests/test_calculator.py
```

Change:

```python
assert apply_discount(200, 10) == 180
```

To:

```python
assert apply_discount(200, 10) == 190
```

Expected failure:

```text
AssertionError
```

Root cause:

```text
test_script_issue
```

Healing action:

```text
test_patch
```

---

## Scenario 4: Missing Import

File:

```text
tests/test_calculator.py
```

Remove `calculate_total` from import list.

Expected failure:

```text
NameError or ImportError
```

Root cause:

```text
application_defect
```

Healing action:

```text
code_patch
```

---

## Notes

For the first POC, focus on application defects only.

Recommended first demo:

```text
Wrong variable name → classifier identifies application_defect → LLM uses GitHub MCP to read file → patch generated → PR created
```
