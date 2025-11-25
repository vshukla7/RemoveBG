import utils.session
import sys
import os
import io
import requests
from rembg import remove
from PIL import Image 


url = input("Enter a URL: ")

def main():
    print("Starting background removal script...")
    input_data = None
    output_filename = "output.png"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        input_data = response.content
        output_filename = os.path.basename(url.split('?')[0])
        if '.' not in output_filename:
            output_filename = "downloaded_image.png"
        output_filename = "from_url_" + os.path.splitext(output_filename)[0] + "_output.png"
    except requests.exceptions.RequestException as e:
        print(f"Error fetching image from URL: {e}")
        sys.exit(1)

    if input_data:
        print("Attempting to remove the background...")
        try:
            output_data = remove(input_data)
            output_image = Image.open(io.BytesIO(output_data))
            output_image.save(output_filename)
            print(f"Successfully processed image and saved to '{output_filename}'.")
            print("Process complete.")
        except Exception as e:
            print(f"An error occurred during background removal: {e}")

if __name__ == "__main__":
    main()

