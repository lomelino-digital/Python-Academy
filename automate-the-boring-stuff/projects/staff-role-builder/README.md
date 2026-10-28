# Staff Role Builder

**Early alpha — an interactive command-line tool for building AI assistant prompts.**

Staff Role Builder guides you through creating a structured prompt for an AI assistant. Choose a role and specialization, describe your context, select an output style, add special instructions, and generate a Markdown prompt to use with your preferred chatbot.

This release is shared for testing and feedback. It is not yet a production-ready application.

## Features

- Interactive role and specialization menus
- Context and output-style selection
- Optional custom output settings
- Special instructions and questioning preferences
- Structured Markdown prompt generation
- Optional clipboard copying using `pyperclip`

## Requirements

- Python 3
- Optional: [`pyperclip`](https://pypi.org/project/pyperclip/) for clipboard integration

The application can generate prompts without `pyperclip`; if it is unavailable, you can copy the output from the terminal manually.

## Running on Linux

Open a terminal in the directory containing `staff_role_builder_v2.py`.

Run it through Python:

```bash
python3 staff_role_builder_v2.py
```

Or make the script executable and run it directly:

```bash
chmod +x staff_role_builder_v2.py
./staff_role_builder_v2.py
```

The script begins with `#!/usr/bin/env python3`, which tells Linux to use an available Python 3 interpreter. **`chmod +x` only grants execute permission; it does not package the application. Python 3 must still be installed.**

For clipboard support, install `pyperclip`:

```bash
python3 -m pip install pyperclip
```

Depending on your Linux desktop environment, clipboard support may also require system clipboard utilities to be installed and configured.

## Running on Windows

Open PowerShell or Command Prompt in the directory containing `staff_role_builder_v2.py`, then run:

```powershell
py staff_role_builder_v2.py
```

For clipboard support, install `pyperclip`:

```powershell
py -m pip install pyperclip
```

If the `py` command is unavailable, install Python and make sure it is available on your PATH. You can then try:

```powershell
python staff_role_builder_v2.py
```

## How to use it

1. Start the application using the instructions for your operating system.
2. Enter a name for the assistant, or press Enter to use the default.
3. Choose a role and specialization from the menus.
4. Enter the context and goal for the assistant.
5. Select an output style, or enter custom settings.
6. Add any special instructions.
7. Choose whether the generated prompt should ask clarifying questions.
8. Review the generated prompt and choose whether to copy it to the clipboard.
9. Choose whether to build another assistant.

Press **Ctrl+C** to interrupt the application.

## Alpha status and limitations

- This is an early alpha intended for testing and feedback.
- Available roles, specializations, and their descriptions are defined in the application's dictionaries.
- Custom output settings are collected as text; they are not validated against a particular AI platform.
- Generated prompts are templates. Their results depend on the chatbot or model in which they are used.
- Clipboard functionality depends on `pyperclip` and the local operating system environment.
- The application has not been formally tested across every Linux distribution or Windows configuration.
- The script requires Python 3; it is not a standalone executable.

## Feedback

If the repository's issue tracker is enabled, please report bugs, confusing menu options, or suggestions there. Feedback will help guide future improvements.

## License

No licence is specified in this release. Unless a licence is added to the repository, normal copyright restrictions apply; reuse and redistribution are not automatically permitted.
