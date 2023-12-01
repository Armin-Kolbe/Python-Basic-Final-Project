# python Basic Final Project
# Python CLI Tools for File Manipulation

In this project, we will develop a Python Command Line Interface (CLI) tool that facilitates file manipulation and directory navigation, similar to command-line functionalities in Unix-like operating systems. A key component of our tool will be an advanced logs system that tracks each command's usage.

# Setup

Ensure Python 3.11 or higher is installed on your system.

# positional arguments:

  command               Select your command: path, ls / lsh / cd / mkdir / rmdir / rm / cp / mv / find /cat / logs
  source_path           Type your source path or nothing for current directory as default
  target_path           Type your target path or nothing for current directory as default

# options:

  -h, --help            show this help message and exit
  -r RECURSIVE, --recursive RECURSIVE
                        Remove the directory and its contents recursively
  -p PATTERN, --pattern PATTERN
                        Your pattern to find files or directories
  -f FILE, --file FILE  Your filename to show its contents


# Usage

Run the "project.py" script using Python3 with the desired arguments:

python3 project.py -h or --help                   --> Display help
python3 project.py path                           --> Display current path
python3 project.py ls                             --> Display List of files and directories at current path, but not hiddens
python3 project.py ls [path]                      --> Display List of files and directories at path, but not hiddens
python3 project.py lsh                            --> Display List of files and directories at current path, plus hiddens
python3 project.py lsh [path]                     --> Display List of files and directories at path, plus hiddens
python3 project.py cd [path]                      --> Change directory
python3 project.py mkdir [path]                   --> Make directory
python3 project.py rmdir [path]                   --> Remove only an empty directory from path
python3 project.py rm [file]                      --> Remove a file from path
python3 project.py rm -r [directory]              --> Remove a directory with all its files and subdirectories from path
python3 project.py cp [source path] [target path] --> Copy a file or directory from source path to target path
python3 project.py mv [source path] [target path] --> Move a file or directory from source path to target path
python3 project.py find [path] -p [pattern]       --> Search for files or directories matchin 'pattern' starting from 'path'
python3 project.py cat [file]                     --> Display the contents of the file
python3 project.py logs                           --> Display the contents of the command.logs


## Logs

Logs of the executed commands are stored in `command.log`, with each entry timestamped.

## Path

The current Path is stored in `path.json`.


Enjoand Thanks
