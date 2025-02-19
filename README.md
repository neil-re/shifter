# Shifter

A lightweight Python program that keeps your system active by discreetly simulating keyboard activity.

## Quick Usage (Executable)

1. Download shifter.exe from the dist folder
2. Run as administrator from command line:

```bash
# Basic usage (stops at 18:00/6:00 PM)
shifter.exe

# Specify end time and interval
shifter.exe --hora 17:30 --intervalo 2
```

## Parameters

- `--hora`: End time in 24-hour format (HH:MM). Default: 18:00
- `--intervalo`: Minutes between activities. Default: 4

## Development (Source Code)

1. Clone the repository
2. Install dependencies:
```bash
pip install keyboard
```
3. Run the script:
```bash
python main.py --hora 17:30 --intervalo 2
```

## How it Works

- Uses discrete Shift key presses to simulate activity
- No mouse movement or visible screen changes
- Automatically stops at specified time
- Can be manually stopped with Ctrl+C

## Requirements

- Windows OS
- Python 3.x (if running from source)
- Administrator privileges

## Features

- Customizable end time
- Adjustable activity intervals
- Zero visible impact
- Low resource usage
- Automatic shutdown at specified time

## Technical Notes

- Requires admin privileges for keyboard simulation
- Uses the keyboard library for key simulation
- Clean command-line interface
- All parameters are optional with sensible defaults

## Warning

Use this tool responsibly and in accordance with your organization's policies.
