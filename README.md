
# Ethical Security Assessment and Remediation

## Overview
A beginner-friendly Python project for reviewing security
configuration, documenting findings, recommending remediation,
and retesting configuration after changes.

## Features
- Configuration security checks
- Evidence-based findings
- Remediation recommendations
- Automated unit tests
- JSON assessment report
- Retesting support

## Requirements
Python 3.10 or later.

## Run the assessment
```bash
python assess.py
```

## Run the tests
```bash
python -m unittest
```

## Output
The program creates `assessment_report.json`.

## Retesting
1. Save the initial report.
2. Correct the flagged settings in `security_config.json`.
3. Run the assessment again.
4. Run the automated tests.
5. Compare the initial and retest results.
6. Document any remaining findings.

## Disclaimer
This educational tool checks supplied configuration values.
It does not conduct penetration testing or verify an entire
application. Use real systems only with explicit authorization.
