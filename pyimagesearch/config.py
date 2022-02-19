# -----------------------------
#   IMPORTS
# -----------------------------
# Import the necessary packages
import os

# Define the base path to the input dataset and then use it to derive the path to the images directory
# and  the annotation CSV file
base_path = "dataset"
images_path = os.path.join(base_path, "images")
annotations_path = os.path.join(base_path, "airplanes.csv")

# Define the path to the base output directory
base_output = "output"

# Define the path to the output serialized model, model training plot, and the testing image filenames
model_path = os.path.sep.join([base_output, "detector.h5"])
plot_path = os.path.sep.join([base_output, "plot.png"])
test_filenames = os.path.sep.join([base_output, "test_images.txt"])

# Initialize our initial learning rate, number of epochs to train for, and the batch size
alpha = 1e-4
epochs = 25
batch_size = 32
