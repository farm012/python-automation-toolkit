from pathlib import Path
import random


def get_folder():
    while True:
        folder = input("Folder path: ").strip('"')

        path = Path(folder)

        if path.exists() and path.is_dir():
            return path

        print("Invalid folder.\n")


def get_files(folder):

    files = [f for f in folder.iterdir() if f.is_file()]

    print("\nChoose file ordering")
    print("1) Alphabetical")
    print("2) Date Created")
    print("3) Date Modified")
    print("4) Random")

    while True:

        choice = input("\nSelection: ").strip()

        if choice == "1":
            files.sort(key=lambda f: f.name.lower())
            break

        elif choice == "2":
            files.sort(key=lambda f: f.stat().st_ctime)
            break

        elif choice == "3":
            files.sort(key=lambda f: f.stat().st_mtime)
            break

        elif choice == "4":
            random.shuffle(files)
            break

        else:
            print("Invalid choice.")

    return files

def preview(files, prefix, start):
    print("\nPreview:\n")

    for i, file in enumerate(files, start=start):
        new_name = f"{prefix}_{i:03d}{file.suffix}"
        print(f"{file.name}  ->  {new_name}")


def rename(files, prefix, start):
    for i, file in enumerate(files, start=start):
        new_name = f"{prefix}_{i:03d}{file.suffix}"
        file.rename(file.with_name(new_name))


def main():

    print("=" * 40)
    print("Bulk File Renamer")
    print("=" * 40)

    folder = get_folder()

    files = get_files(folder)

    if not files:
        print("Folder contains no files.")
        return

    prefix = input("New prefix: ").strip()

    while True:
        try:
            start = int(input("Starting number: "))
            break
        except ValueError:
            print("Enter a valid integer.")

    preview(files, prefix, start)

    answer = input("\nProceed? (y/n): ").lower()

    if answer != "y":
        print("Cancelled.")
        return

    rename(files, prefix, start)

    print(f"\nDone. Renamed {len(files)} files.")


if __name__ == "__main__":
    main()