import os
def list_items(path):
    if not os.path.exists(path):
        print("The specified path does not exist")
        return

    print("\nOnly Directories:")
    directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    print(directories)

    print("\nOnly Files:")
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    print(files)

    print("\nAll Directories & Files:")
    all_items = os.listdir(path)
    print(all_items)
specified_path = input()
list_items(specified_path)