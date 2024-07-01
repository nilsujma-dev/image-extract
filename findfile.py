import os
import tarfile
import tempfile
import shutil

# Define the variables here
main_tar_file_path = "exampleimage_1.tar"  # Replace with the path to your tar file
target_file_path = "/tmp/aws_key.txt"  # Replace with the file path you are looking for

def check_for_file(extracted_dir, target_file_path):
    target_file_abs_path = os.path.join(extracted_dir, target_file_path.lstrip('/'))
    if os.path.isfile(target_file_abs_path):
        print(f"Found {target_file_path} in {extracted_dir}")
        print(f"Content of {target_file_path}:")
        with open(target_file_abs_path, 'r') as file:
            print(file.read())
        return True
    return False

def extract_and_check_layers(main_tar_path, target_file_path):
    with tarfile.open(main_tar_path, 'r') as tar:
        temp_dir = tempfile.mkdtemp()
        try:
            # Extract all files to the temporary directory
            tar.extractall(temp_dir)

            # Navigate to the blobs/sha256 directory within the extracted tar structure
            layers_dir = os.path.join(temp_dir, 'blobs', 'sha256')
            if not os.path.isdir(layers_dir):
                print(f"No layers directory found in {main_tar_path}")
                return False

            # Loop through each layer file
            file_found = False
            for layer in os.listdir(layers_dir):
                layer_path = os.path.join(layers_dir, layer)
                if tarfile.is_tarfile(layer_path):
                    with tarfile.open(layer_path, 'r') as layer_tar:
                        layer_temp_dir = tempfile.mkdtemp()
                        layer_tar.extractall(layer_temp_dir)
                        if check_for_file(layer_temp_dir, target_file_path):
                            file_found = True
                            shutil.rmtree(layer_temp_dir)
                            break
                        shutil.rmtree(layer_temp_dir)
            return file_found
        finally:
            shutil.rmtree(temp_dir)

def main(main_tar_file_path, target_file_path):
    if tarfile.is_tarfile(main_tar_file_path):
        if extract_and_check_layers(main_tar_file_path, target_file_path):
            print(f"File {target_file_path} found in image {main_tar_file_path}")
        else:
            print(f"File {target_file_path} not found in any layer of image {main_tar_file_path}")
    else:
        print(f"{main_tar_file_path} is not a valid tar file")

if __name__ == "__main__":
    main(main_tar_file_path, target_file_path)
