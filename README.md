# FastAPI Learning

Small collection of FastAPI and Streamlit practice apps:

- [firstapi.py](firstapi.py) — basic FastAPI hello-world + path/query params
- [calculator_fast_api.py](calculator_fast_api.py) — FastAPI calculator API (add/subtract/multiply/divide)
- [streamlit/basic_stremlint.py](streamlit/basic_stremlint.py) — Streamlit components lab
- [streamlit/bmi_streamlint.py](streamlit/bmi_streamlint.py) — Streamlit BMI calculator
- [streamlit/steamlint_mordern_calc.py](streamlit/steamlint_mordern_calc.py) — Streamlit modern calculator UI

## Installation

### 1. Prerequisites

- Python 3.9 or higher installed and available on your PATH
- pip (comes bundled with Python)

Check your Python version:

```powershell
python --version
```

### 2. Clone / open the project

```powershell
cd "SOCIAL EAGLE TASKS\DAY-4\fast-api-learning"
```

### 3. Create a virtual environment (recommended)

```powershell
python -m venv venv
```

Activate it:

```powershell
.\venv\Scripts\Activate.ps1
```

> If activation is blocked by execution policy, run:
> `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`

### 4. Install dependencies

```powershell
pip install -r requirements.txt
```

This installs `fastapi`, `uvicorn`, and `streamlit`.

## Running the apps

### FastAPI apps

Run either FastAPI app with Uvicorn (auto-reload enabled):

```powershell
uvicorn firstapi:app --reload
```

```powershell
uvicorn calculator_fast_api:app --reload
```

Then open:

- App: http://127.0.0.1:8000
- Interactive docs (Swagger UI): http://127.0.0.1:8000/docs
- Alternative docs (ReDoc): http://127.0.0.1:8000/redoc

### Streamlit apps

Run any Streamlit app from the `streamlit/` folder:

```powershell
streamlit run streamlit/basic_stremlint.py
```

```powershell
streamlit run streamlit/bmi_streamlint.py
```

```powershell
streamlit run streamlit/steamlint_mordern_calc.py
```

Streamlit will open the app automatically in your browser (default: http://localhost:8501).

## Deactivating the virtual environment

```powershell
deactivate
```
