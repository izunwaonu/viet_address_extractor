import os
import gdown

# Create the data directory if it doesn't exist
os.makedirs("data", exist_ok=True)

# Define the files and their Google Drive IDs
files = {
    "list_province.txt": "1oSXQHLoVSGfBOLR4NjNwQRTkDb8Zd8OU",
    "list_district.txt": "18sZoDAqJWyUfmjQN3VpKfkDHFQ-tcml6",
    "list_ward.txt": "1VfDCj7R11jf3SIZyoZdYL7fIN-AIhC-1",
    "test.json": "1PBt3U9I3EH885CDhcXspebyKI5Vw6uLB",
}

# Download each file
for filename, file_id in files.items():
    url = f"https://drive.google.com/uc?id={file_id}"
    output_path = os.path.join("data", filename)
    print(f"Downloading {filename}...")
    gdown.download(url, output_path, fuzzy=True)

print("Download complete!")
