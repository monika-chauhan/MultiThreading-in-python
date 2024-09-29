import threading
import shutil
import os

# Barrier to synchronize threads
def copy_file(source_file, destination_file, barrier):
    """Function to copy file data from source to destination"""
    try:
        shutil.copy(source_file, destination_file)
        print(f"Copied: {source_file} to {destination_file}")
    except Exception as e:
        print(f"Error copying {source_file}: {e}")
    finally:
        barrier.wait()  # Ensures all threads reach this point before continuing

def copy_files_concurrently(files_to_copy, dest_folder):
    """
    Copies multiple files concurrently using threading
    Args:
    - files_to_copy: List of file paths to copy
    - dest_folder: Destination folder where files will be copied
    """
    num_files = len(files_to_copy)
    barrier = threading.Barrier(num_files)

    # Create destination folder if not exists
    os.makedirs(dest_folder, exist_ok=True)

    threads = []
    for file_path in files_to_copy:
        destination_file = os.path.join(dest_folder, os.path.basename(file_path))
        t = threading.Thread(target=copy_file, args=(file_path, destination_file, barrier))
        threads.append(t)
        t.start()

    # Wait for all threads to complete
    for t in threads:
        t.join()

    print("All files copied successfully!")

# Example Usage
if __name__ == "__main__":
    files_to_copy = ["file1.txt", "file2.txt", "file3.txt"]  # Example files
    dest_folder = "destination_folder"
    copy_files_concurrently(files_to_copy, dest_folder)
