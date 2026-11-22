# Playwright Python Framework

A maintainable Playwright and pytest framework using the Page Object Model.

## Structure

- `Pages/`: page objects and shared page behavior
- `Tests/`: pytest test cases
- `Utilities/`: reusable framework helpers
- `Config/`: environment-driven settings
- `Testdata/`: external test data
- `Reports/`: HTML reports, screenshots, videos, and traces

## Setup

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
playwright install
```

## Run tests

```bash
pytest
pytest -m smoke
HEADLESS=false pytest
pytest --video
```

Configure the framework with environment variables such as `BASE_URL`, `BROWSER`, `HEADLESS`, `SLOW_MO`, and `DEFAULT_TIMEOUT`.












