import os
from pdf2image import convert_from_bytes
import streamlit as st
import cv2
import numpy as np
from PIL import Image

# Set the Poppler path (update the path as necessary)
os.environ["PATH"] += os.pathsep + r"C:\path\to\poppler\bin"

def process_pdf(uploaded_file):
    try:
        images = convert_from_bytes(uploaded_file.read())
        return images
    except Exception as e:
        st.error(f"Error processing PDF: {str(e)}")

def convert_to_black_and_white(image):
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)
    # Apply thresholding to convert to binary (negative)
    _, binary_image = cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY_INV)
    return binary_image

def save_images_to_pdf(images, original_filename):
    # Generate the output filename
    output_pdf_name = original_filename.replace('.pdf', '_neg.pdf')
    # Convert the images back to PIL format
    pil_images = [Image.fromarray(image) for image in images]
    # Save as a PDF
    pil_images[0].save(output_pdf_name, save_all=True, append_images=pil_images[1:], resolution=100.0)
    return output_pdf_name

def main():
    st.title("PDF to Black and White Converter")
    st.write("Once the processing is complete, you will be able to view both the original and processed slides. Scroll down to find the 'Save PDF' button, and click it to save your processed PDF.")


    uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])
    
    if uploaded_file:
        original_filename = uploaded_file.name
        images = process_pdf(uploaded_file)
        if images:
            processed_images = []  # To store the processed images
            for i, image in enumerate(images):
                st.image(image, caption=f"Original Page {i + 1}", use_column_width=True)
                # Convert the image to black and white
                bw_image = convert_to_black_and_white(image)
                processed_images.append(bw_image)  # Store processed image
                st.image(bw_image, caption=f"Black and White Page {i + 1}", use_column_width=True)

            if st.button("Save to PDF"):
                output_pdf_name = save_images_to_pdf(processed_images, original_filename)
                st.success(f"Saved processed images to {output_pdf_name}")

if __name__ == "__main__":
    main()
