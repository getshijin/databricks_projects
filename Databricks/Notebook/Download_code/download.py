import kagglehub

# Download latest version
path = kagglehub.dataset_download("conorsully1/simulated-transactions")

print("Path to dataset files:", path)