# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 17:51:02 2024

@author: Hxtreme
"""

from PIL import Image

def encrypt(image_path, output_path, key):
    # Open an image file
    with Image.open(image_path) as img:
        # Convert image to RGB mode
        img = img.convert("RGB")
        # Load pixel data
        pixels = img.load()

        # Encrypt the image by modifying pixel values
        for i in range(img.width):
            for j in range(img.height):
                r, g, b = pixels[i, j]
                pixels[i, j] = ((r + key) % 256, (g + key) % 256, (b + key) % 256)

        # Save the encrypted image
        img.save(output_path)

def decrypt(image_path, output_path, key):
    # Open an image file
    with Image.open(image_path) as img:
        # Convert image to RGB mode
        img = img.convert("RGB")
        # Load pixel data
        pixels = img.load()

        # Decrypt the image by modifying pixel values
        for i in range(img.width):
            for j in range(img.height):
                r, g, b = pixels[i, j]
                pixels[i, j] = ((r - key) % 256, (g - key) % 256, (b - key) % 256)

        # Save the decrypted image
        img.save(output_path)

def main():
    choice = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt: ").strip().lower()
    image_path = input("Enter the path of the image: ").strip()
    output_path = input("Enter the path for the output image: ").strip()
    key = int(input("Enter the key (integer value): ").strip())

    if choice == 'encrypt':
        encrypt(image_path, output_path, key)
        print(f"Encrypted image saved to {output_path}")
    elif choice == 'decrypt':
        decrypt(image_path, output_path, key)
        print(f"Decrypted image saved to {output_path}")
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
