from pdf2docx import Converter

# pdf文件路径
# pdf_file = 'D:/LearningJava/Java学习课程/JavaWeb_ngnix资料/笔记资料/nginx课件v1.0.pdf'
pdf_file = input('Please enter the path of the PDF document that needs to be converted:')
# 输出word文件的路径
# docx_file = 'C:/Users/22395/Desktop/hello/nginxword.docx'
docx_file = input('Please enter the path and file name to convert to Word:')
cv = Converter(pdf_file)
cv.convert(docx_file, start=0, end=None)
cv.close()