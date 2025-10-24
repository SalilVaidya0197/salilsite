
import fitz
import os

def extract_images_from_pdf(pdf_path, output_folder="images"):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    doc = fitz.open(pdf_path)
    for page_num in range(len(doc)):
        page = doc[page_num]
        image_list = page.get_images(full=True)

        if image_list:
            for img_index, img in enumerate(image_list):
                xref = img[0]
                base_image = doc.extract_image(xref)
                image_bytes = base_image["image"]
                image_ext = base_image["ext"]
                image_filename = os.path.join(
                    output_folder,
                    f"page{page_num + 1}_img{img_index + 1}.{image_ext}"
                )
                with open(image_filename, "wb") as img_file:
                    img_file.write(image_bytes)
    doc.close()

if __name__ == "__main__":
    extract_images_from_pdf("/Users/tushar/Downloads/salilsite/request.pdf")
