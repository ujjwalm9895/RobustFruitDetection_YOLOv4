import os

# Initialize an empty list to store image file paths
image_files = []

# Change the current working directory to "data/obj"
os.chdir(os.path.join("data", "obj"))

# Loop through files in the current directory
for filename in os.listdir(os.getcwd()):
    # Get the current working directory path
    path1 = os.getcwd()
    
    # Define the path to the "data/obj" directory
    path = os.path.join("data", "obj")
    
    # Check if the file has a ".jpg" extension
    if filename.endswith(".jpg"):
        # Append the full path of the image file to the list
        image_files.append(path1 + '/' + path + '/' + filename)

# Change the working directory back to the parent directory
os.chdir("..")

# Create and open a text file "train.txt" in write mode
with open("train.txt", "w") as outfile:
    # Loop through the list of image file paths
    for image in image_files:
        # Write each image path to the text file
        outfile.write(image)
        outfile.write("\n")
    
    # Close the output file
    outfile.close()

# Change the working directory back to the parent directory
os.chdir("..")
