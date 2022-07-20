import os
import PyPDF2 as py2
from cv2 import MergeRobertson

#Cria uma lista
FileNamesPDF =[]


def SearchFilePDF(endereco):
    for root, dirs, files in os.walk(endereco):
        for file in files:
            print(file)
            if(file.endswith(".pdf")):
                FileNamesPDF.append(file)

def MergePDFFiles(caminho, listPDF = []):
    
    

    for archives in listPDF:

        for w in range(0, len(listPDF)-1):

            ArchivePDF = open(caminho + "/" + archives,"rb")

            dataArchivePDF = py2.PdfFileReader(ArchivePDF)

            MergePDF = py2.PdfFileMerger()

            MergePDF.append(dataArchivePDF)

        #NumberPagesPDF = dataArchivePDF.numPages

        #for w in range(0, NumberPagesPDF-1):

            #ExtractPagesPDF = dataArchivePDF.getPage(w)

            #MergePDF.append(ExtractPagesPDF)

    MergePDF.write(caminho + "/"+"Novo_arquivo.pdf")

    print("Arquivo criado com sucesso!")



        






caminho = input("Digite o caminho do diretório onde estão armazenados os arquivos em PDF: ")

if caminho =="":
    print("Insira um caminho válido!")
else:
    SearchFilePDF(caminho)
    MergePDFFiles(caminho, FileNamesPDF)





#for i in FileNamesPDF:
    #print(i)

