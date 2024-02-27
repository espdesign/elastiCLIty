# elastiCLIty

elastiCLIty is a command line application designed to learn Linux commands with repetition.

The application use-case is designed around the idea that typing Linux commands repeatedly is helpful for retention.

---

## How it works

elastiCLIty takes an input.`modules.json` and creates a menu system from the JSON data to choose a module.

Once a module is chosen, the script provides different modes to interact with that module's data.

## Installation

Tested working with Python 3.12.1

copy `elastiCLIty.py` and `modules.json` to a directory.

run the script.

ex. `python elastiCLIty.py`

## Available Modes

#### Learn

- Random questions
- Displays the correct answer when incorrect.

#### Quiz

- in development

## Customization

Although this program was designed for Linux commands, you can create custom modules with any questions.

Edit the `modules.json` file to add your own.
