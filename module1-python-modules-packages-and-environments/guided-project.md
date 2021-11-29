# Sprint 1 Module 1 Guided Project Notes

## Before Lecture

>In order to follow along fully with today's Guided Project, please install the following tools from: [this document](https://github.com/BloomInstituteOfTechnology/DS-Unit-3-Setup).
>
>- VS Code
>- Git Bash
>- Python
>- Pipenv

## Notebooks vs Local Development

Colab Notebook Advantages:

- Minimal learning curve
- High degree of visibility and shareability
- Effective presentation when code mixed with markdown and data visualizations
- GPU / TPU processing power

Colab Notebook Disadvantages:

- Can only write and execute Python code, not other languages
- Minimal processing power and parallel processing capabilities (excluding GPU / TPU)
- Relatively low ability to manage files and credentials
- Relatively low degree of customization
- Unable to run certain kinds of apps, like web apps written in the Flask framework

Local Development Advantages:

- Can write and execute code written in many different languages and frameworks
- Greater ability to manage files and credentials
- Greater degree of customization / control
- Greater privacy (not managed by Google)
- More processing power and parallel processing capabilities (excluding GPU / TPU)

Local Development Disadvantages:

- Steeper learning curve, likely many tools to learn
- Not as immediately shareable, unless pushing code to GitHub or a remote server

## Local Development Tools

Category | Recommended Tool(s) | Purpose
--- | --- | ---
Text Editor or IDE | VS Code | For creating, reading, editing, and deleting files of text and code.
Command-line Application | Mac Terminal, Windows Git Bash, the built-in terminal in VS Code, or whatever you can get to work! | For interfacing with the computer in programmatic ways (i.e. installing and running software).
Programming Language | Python (`python`) | For executing software written in a given programming language.
Programming Language Virtual Environment Manager | Anaconda (`conda`) or Pipenv (`pipenv`) | For installing different versions of a programming language, to suit project-specific purposes, because sometimes you might need to use a different version.
Programming Language Package Manager | Pip (`pip`) in general and in Anaconda environments, but replaced by `pipenv` for Pipenv environments. | For installing third-party packages written in a given programming language.
Version Control Utility | Git (`git`) | For incrementally saving different versions of software files, and interfacing with GitHub, which is an online place to share code repositories.
Server Management Utility | Heroku (`heroku`) | For provisioning and managing remote servers on which to run software.

## Using the Command Line (Git Bash or Terminal)

### Vital Commands

Command | Explanation
--- | ---
`pwd` | "Print Working Directory" Displays the path of the current working directory
`cd <directory>` | "Change Directory" will change your working directory to whatever one you specify. If this directory is not within the current working directory you will need ot provide the full path to it.
`cd ..` | Navigate to the parent directory. (Go up one level in the directory structure, kind of like saying "go back").
`ls` | The "list" command displays the contents of the working directory (whatever directory you're in at the moment).
`mkdir <directory>` | Makes a new directory (folder) inside of the current working directory.
`touch <filename>` | Creates inside the current working directory if it doesn't exist.
`rm <filename>` | Deletes or "removes" a specific file.
`rm -r <directory>` | Deletes a directory. The `-r` is what's called a "flag" and it modifies the original command. In this case this flag is indicating a "recursive" delete, meaning that the command line will go through all of the contents of the directory and delete them in a memory efficient fashion before deleting the container directory itself.
`rm -rf <directory>` | Deletes a directory but the additional `-f` flag (combined with `-r` makes `-rf`) "force deletes" the file. This willl delete the file no matter what even if it is being used by another program. Sometimes windows thinks that files are being used by programs when they're not, using this flag we can get around that frustration to delete things.

For more commands find a [Command Line Cheat Sheet](https://www.git-tower.com/blog/command-line-cheat-sheet/) that you like.

## Scripts, Modules, Packages and Libraries

### The Python REPL

REPL stands for "Read Evaluate Print Loop" and starting up a Python REPL using the command `python` is one of the most basic and direct ways that we can interact with our locally installed python interpreter. A REPL acts kind of like a notebook where any variables run are stored in a global namespace and the result of each command is printed out whereupon the user is prompted again in a repeated fashion.

### Scripts

A script is a python file that is meant to be run directly. We can execute any python file from the command line by running the command  `python <my_script.py>` where you will insert the name of your python file in place of my_script.py

Scripts are meant to directly accomplish some task and usually include lots of code that is outside of the scope of (not inside of) any classes or functions. Those lines of code will simply be read from top to bottom until entire file has been executed.

A script is not meant to be imported into any other file or tool. It's just some code to be run. Functions created within the script are typically for use within the script itself.

### Modules

A module is a Python file that's intended to be imported into other scripts, modules, projects, etc. Any functions or classes that are defined within the module will be available to other files that import the module.

### Packages

A Package is a directory (folder) of Python Modules. A Package must include a `__init__.py`
to distinguish it from other directories that just hold Python Scripts. Any code that is in the `__init__.py` file will be executed right when the package is imported.

### Libraries

A library is a loose term that's used to refer to large groups of packages and modules usually that serve a specific purpose. Pandas, NumPy, Scipy, etc. Are all referred to as libraries even though under the hood they may technically just be big packages or modules.

## Extra Resources

- [Command Line Cheat Sheet](https://www.git-tower.com/blog/command-line-cheat-sheet/)
- [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)
- [Joel Grus - "I don't like notebooks"](https://www.youtube.com/watch?v=7jiPeIFXb6U)
- [Scripts, Modules, Packages and Libraries](https://realpython.com/lessons/scripts-modules-packages-and-libraries/)
- [Corey Schafer - "virtualenv and why you should use virtual environments"](https://www.youtube.com/watch?v=N5vscPTWKOk)
  - virtualenv is an alternative to pipenv, but performs the same function. Focus on the "why" of using virtual environments from this video.
- [Mike Rossetti's Helpful Sprint 1 Documentation](https://github.com/s2t2/lambda-ds-3-1)
