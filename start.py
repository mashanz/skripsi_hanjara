import os

file = "skripsi"

os.system("pdflatex.exe -synctex=1 -interaction=nonstopmode \"" + file +"\".tex")
os.system("pdflatex.exe -synctex=1 -interaction=nonstopmode \"" + file +"\".tex")
print("\n###############################################################################")
print("#                                    FINISH                                   #")
print("###############################################################################")