## Environment Setup

- OS: macOS (version X.X.X)
- Python: 3.x.x (or Node.js, Java, etc.)
- Required packages:
  - numpy==1.24.0
  - pandas==2.0.0
  - (list others as needed)
git clone </Users/kristendelancey/my-repo/HW2>

## Python Virtual Environment & Install Dependencies

1. Make sure you have Python 3.x installed.
2. Create a local virtual environment:
  ```
  python3 -m venv env
  ```
3. Activate the virtual environment:
  ```
  source env/bin/activate
  ```
4. Upgrade pip and install required packages:
  ```
  python -m pip install --upgrade pip
  python -m pip install --upgrade openai "openai[voice_helpers]" sounddevice numpy python-dotenv
  ```
5. In VS Code, use the “Python: Select Interpreter” command and choose the interpreter from your new env folder (./env/bin/python).

## Environment Variables

If your project requires environment variables, set them before running your application. For example:


On macOS/Linux:

```
export VAR_NAME=value
```

On Windows (Command Prompt):

```
set VAR_NAME=value
```

Replace `VAR_NAME` and `value` with your actual variable names and values. List all required environment variables below:

- VAR_NAME: description
- ANOTHER_VAR: description