import argparse, os, json, datetime
import shutil       # Refrence: https://sentry.io/answers/delete-a-file-or-folder-in-python/
                    # Refrence: https://note.nkmk.me/en/python-shutil-copy-copytree/
                    # Refrence: https://note.nkmk.me/en/python-shutil-move/

import fnmatch      # Refrence: https://realpython.com/working-with-files-in-python/#filename-pattern-matching

def write_path(path):             # write the path on the file: path.jason ,infact change directory too
    with open("path.json", "w") as f1:
        json.dump({"path":path}, f1)

def read_path():                  # give us the path frome file path.json
    if os.path.exists("path.json"):
        with open("path.json", "r") as f2:
            data = json.load(f2)
            return data.get("path")
    return os.getcwd()

def ls(path):                     # List of files and directories, but not hiddens
    endpath = os.path.join(read_path() , path)
    if os.path.exists(endpath):
        try:
            for item in os.listdir(endpath):
                if not item.startswith("."):
                    print(item)
        except Exception as e:
            print(e.__class__.__name__, e)
    else:
        print(f"Error! >>> The path: {endpath} existiert nicht!")
        return

def lsh(path):                    # List of files and directories plus hiddens
    endpath = os.path.join(read_path() , path)
    if os.path.exists(endpath):
        try:
            for item in os.listdir(endpath):
                print(item)
        except Exception as e:
            print(e.__class__.__name__, e) 
    else:
        print(f"Error! >>> The path: {endpath} existiert nicht!")
        return

def cd(path):                     # Change directory
    if os.path.exists(path):
        print(f"Error! >>> The path: {path} existiert nicht!")
        return
    print(f"You are now in this path: {path}")
    write_path(path)

def mkdir(path):                  # Make directory
    endpath = os.path.join(read_path() , path)
    if os.path.exists(endpath):
        try:
            os.makedirs(endpath, exist_ok = True)
            print(f"The directory: {path} is created at this path: {endpath}")
        except Exception as e:
            print(e.__class__.__name__, e)
    else:
        print(f"Error! >>> The path: {endpath} existiert nicht!")
        return

def rm_emptydir(path):             # Remove only an empty directory
    endpath = os.path.join(read_path() , path)
    if os.path.exists(endpath):
        try:
            os.rmdir(endpath)
            print(f"The directory: {path} is deleted from this path: {endpath}")
        except Exception as e:
            print(e.__class__.__name__, e)
    else:
        print(f"Error! >>> The path: {endpath} existiert nicht!")
        return    

def rm_nonemptydir(path):           # with shutil : Refrence: https://sentry.io/answers/delete-a-file-or-folder-in-python/
    endpath = os.path.join(read_path() , path)
    if os.path.exists(endpath):
        try:
            shutil.rmtree(endpath)
            print(f"The directory: {path} and all its contents are deleted from this path: {endpath}")
        except Exception as e:
            print(e.__class__.__name__, e)
    else:
        print(f"Error! >>> The path: {endpath} existiert nicht!")
        return 

def rm_file(path):                   # Remove a file
    endpath = os.path.join(read_path() , path)
    if os.path.exists(endpath):    
        try:
            os.remove(endpath)
            print(f"The file: {path} is deleted from this path: {endpath}")
        except Exception as e:
            print(e.__class__.__name__, e)
    else:
        print(f"Error! >>> The path: {endpath} existiert nicht!")
        return 

def cp(spath, tpath):                # Copy a file, Refrence: https://note.nkmk.me/en/python-shutil-copy-copytree/
    endspath = os.path.join(read_path() , spath)
    endtpath = os.path.join(read_path() , tpath)
    if os.path.exists(endspath) or os.path.exists(endtpath): 
        try:
            shutil.copy2(endspath, endtpath)
            print(f"The file: {endspath} is copied to this path: {endtpath}")            
        except Exception as e:
            print(e.__class__.__name__, e)
    else:
        print(f"Error! >>> The path: {endspath} or {endtpath} existiert nicht!")
        return 

def mv(spath, tpath):                # Move a file, Refrence: https://note.nkmk.me/en/python-shutil-move/
    endspath = os.path.join(read_path() , spath)
    endtpath = os.path.join(read_path() , tpath)
    if os.path.exists(endspath) or os.path.exists(endtpath): 
        try:
            shutil.move(endspath, endtpath)
            print(f"The file: {endspath} is moved to this path: {endtpath}") 
        except Exception as e:
            print(e.__class__.__name__, e)
    else:
        print(f"Error! >>> The path: {endspath} or {endtpath} existiert nicht!")
        return 

def finding(path, pattern):          # with fnmatch: Find files or directories match to pattern
                                     # Refrence: https://realpython.com/working-with-files-in-python/#filename-pattern-matching
    endpath = os.path.join(read_path() , path)
    matching_lists = []

    if os.path.exists(endpath):    
        try:
            for root, dirs, files in os.walk(endpath):
                for file_or_dir in fnmatch.filter(files + dirs, pattern):
                    matching_lists.append(os.path.join(root, file_or_dir))
        except Exception as e:
            print(e.__class__.__name__, e)
    else:
        print(f"Error! >>> The path: {endpath} existiert nicht!")
        return 

    if matching_lists:
        print(f"start search: '{endpath}' , Pattern: '{pattern}'")
        print("Matching files or directories: ")
        for item in matching_lists:
            print(f">>> {item}")
    else:
        print(f"start search: '{endpath}' , Pattern: '{pattern}'")
        print(f">>> No matching files or directories founded")

def cat(file):                        # View the contents of the file
    endpath = os.path.join(read_path() , file)

    if os.path.exists(endpath):    
        try:
            with open(endpath, "r") as f3:
                print(f3.read())
        except Exception as e:
            print(e.__class__.__name__, e)     
    else:
        print(f"Error! >>> The file: {endpath} existiert nicht!")
        return 
    
def logs():                           # View the file logs.log
    if os.path.exists("commands.log"):
        with open("commands.log", "r") as f4:
            print(f4.read())
    else:
        print(f"Error! >>> The logs existiert nicht!")
        return 

def append_log(cmd, run, error):      # Write history in the file logs.log
    with open("commands.log", "a") as f5:
        timestamp = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        f5.write(f"{timestamp} , Command: {cmd} , Run? {run} , Error? {error} \n")

def setup():                          # Refrence: https://docs.python.org/3/library/argparse.html

    parser = argparse.ArgumentParser (description = "Python CLI Tools for File Manipulation")
    parser.add_argument ("command", help = "Select your command: path, ls / lsh / cd / mkdir / rmdir / rm / cp / mv / find /cat / logs")
    parser.add_argument ("source_path", nargs = '?', default = '.', help = "Type your source path or nothing for current directory as default")
    parser.add_argument ("target_path", nargs='?', default = '.', help = "Type your target path or nothing for current directory as default")
    parser.add_argument ("-r", "--recursive", help = "Remove the directory and its contents recursively")
    parser.add_argument ("-p", "--pattern", help = "Your pattern to find files or directories")    
    parser.add_argument ("-f", "--file", help = "Your filename to show its contents ")
    
    return parser

# -------------------------- main ------------------------------

parser = setup()
args = parser.parse_args()

try:
    match args.command:

        case "path":
            print(f"Your current path is: {os.getcwd()}")
        
        case "ls":
            ls(args.source_path)

        case "lsh":
            lsh(args.source_path)

        case "cd":
            cd(args.source_path)
        
        case "mkdir":
            mkdir(args.source_path) 

        case "rmdir":
            rm_emptydir(args.source_path) 

        case "rm":
            if args.recursive:
                rm_nonemptydir(args.source_path)
            else:
                rm_file(args.source_path)

        case "cp":
            cp(args.source_path, args.target_path) 

        case "mv":
            mv(args.source_path, args.target_path) 

        case "find":
            finding(args.source_path, args.pattern)

        case "cat":
            cat(args.file)

        case "logs":
            logs()

        case _:
            append_log(args.command, "No", "Command not found! ")
            print ("Command not found! Type -h or --help to see all commands")
    
    append_log(args.command, "Yes", "No Error")
except Exception as e:
    print(e.__class__.__name__, e)
    append_log(args.command, "No", str(e))
