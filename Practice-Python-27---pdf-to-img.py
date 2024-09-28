# Practice-Python-27---pdf-to-img

import fitz  # PyMuPDF, imported as fitz for backward compatibility reasons
file_path = "C:/Users/user/PycharmProjects/firstProg/Coursera LFFW693DQY54.pdf"
doc = fitz.open(file_path)  # open document
for i, page in enumerate(doc):
    pix = page.get_pixmap()  # render page to an image
    pix.save(f"Coursera LFFW693DQY54.png")

# from pdf2image import convert_from_path
#
# old_pdf = convert_from_path("Policy_Certificate_49982828_25122023_policyPDF.pdf", poppler_path="C:/Users/user/PycharmProjects/firstProg/Policy_Certificate_49982828_25122023_policyPDF.pdf")
#
# for i in range(len(old_pdf)):
#     old_pdf[i].save("new"+str(i+1)+".jpg", "JPEG")



