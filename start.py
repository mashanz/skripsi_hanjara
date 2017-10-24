import os

file = "skripsi"

os.system("pdflatex.exe -synctex=1 -interaction=nonstopmode \"" + file +"\".tex")
os.system("pdflatex.exe -synctex=1 -interaction=nonstopmode \"" + file +"\".tex")
print("\n###############################################################################")
print("#                                    FINISH                                   #")
print("###############################################################################")

os.system("del *.aux *.log *.out *.lot *.lof *.txt *.toc *.gz")

print("\n###############################################################################")
print("#                               CLEANUP DONE                                   #")
print("###############################################################################")