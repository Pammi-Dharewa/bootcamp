import os
import shutil

# Create directories
os.makedirs("test_dir/sub_dir", exist_ok=True)

# Delete directories
shutil.rmtree("test_dir")
