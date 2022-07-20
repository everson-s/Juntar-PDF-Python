import os
import PyPDF2 as py2

#Cria uma lista
FileNamesPDF =[]


def SearchFilePDF(endereco):
    for root, dirs, files in os.walk(endereco):
        for file in files:
            print(file)
            if(file.endswith(".pdf")):
                FileNamesPDF.append(file)

def MergePDFFiles(caminho, listPDF = []):
    
    MergePDF = py2.PdfFileMerger()

    for archives in listPDF:

        ArchivePDF = open(caminho + "/" + archives,"rb")

        dataArchivePDF = py2.PdfFileReader(ArchivePDF)

        MergePDF.append(dataArchivePDF)

        #NumberPagesPDF = dataArchivePDF.numPages

        #for w in range(0, NumberPagesPDF-1):

            #ExtractPagesPDF = dataArchivePDF.getPage(w)

            #MergePDF.append(ExtractPagesPDF)

    MergePDF.write(caminho + "/"+"Novo_arquivo.pdf")

    print("\nArquivo criado com sucesso!")


caminho = input("Digite o caminho do diretório onde estão armazenados os arquivos em PDF: ")

if caminho =="":
    print("Insira um caminho válido!")
else:
    SearchFilePDF(caminho)
    MergePDFFiles(caminho, FileNamesPDF)





#for i in FileNamesPDF:
    #print(i)


