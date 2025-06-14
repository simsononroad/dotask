from docx.shared import Mm
from docxtpl import DocxTemplate, InlineImage
import os
import subprocess

megoldokulcs_base = "base.docx"
feladatlap_base = "base_feladat.docx"
output_dir = "feladatlap"

class Create_task():
    def __init__(self, file_name, file_desc, kerdes_valasz: list, feladatsor_neve, egybe):
       self.file_name = file_name
       self.file_desc = file_desc
       self.kerdes_valasz = list(kerdes_valasz)
       self.feladatsor_neve = feladatsor_neve
       self.egybe = dict(egybe)
       
       
    def chose(self):
        a = input("(Ú)j kérdés, (G)enerálás, (K)ilépés\n>>>")
        print()
        if a.upper() == 'Ú':
            Create_task(self.file_name, self.file_desc, self.kerdes_valasz, self.feladatsor_neve, egybe=self.egybe).new_task()
        elif a.upper() == 'G':
            Create_task(self.file_name, self.file_desc, self.kerdes_valasz, self.feladatsor_neve, egybe=self.egybe).gen_file()
        else:
            Create_task(file_name=self.file_name, file_desc=self.file_desc, kerdes_valasz=self.kerdes_valasz, feladatsor_neve=self.feladatsor_neve, egybe=self.egybe).chose()
        
    # Fájlok kigenerálása
    def gen_file(self):
        while True:
            try:
                print(f"==================\n\tFájl neve: {self.file_name}\n\tFájl leírása: {self.file_desc}\n==================\n")
                doc = DocxTemplate(megoldokulcs_base)
                context = {
                    'feladat_neve': self.feladatsor_neve,
                    'feladatsor_leirasa': self.file_desc,
                    'feladat_szam': len(self.kerdes_valasz),
                    'kerdes_valasz': self.kerdes_valasz
                }
                doc.render(context)
                doc.save(self.file_name)
                docx_2_pdf(self.file_name, f"{output_dir}/megoldokulcs.pdf")
                doc1 = DocxTemplate(feladatlap_base)
                context = {
                    'feladat_neve': self.feladatsor_neve,
                    'feladatsor_leirasa': self.file_desc,
                    'feladat_szam': len(self.kerdes_valasz),
                    'kerdes_valasz': self.egybe
                }
                doc1.render(context)
                doc1.save(self.file_name)
                docx_2_pdf(self.file_name, f"{output_dir}/feladatsor.pdf") # docx átalakítása pdf formátumba
                os.system("clear")
                break
            except:
                os.mkdir("feladatlap")
    
    
    # Új feladat hozzáadása
    def new_task(self):
        kerdes = input("Mi legyen a kérdés?\n>>>")
        valasz_lehetosegek = input("válasz lehetőségek vesszővel elválasztva a helyes válasz után tegyél egy '$' jelet.\npl: egy, ketto$, harom\n>>>")
        
        valasz_lehetosegek_lista = valasz_lehetosegek.split(",")
        helyes_valasz_lista = []
        
        itt = list()
        
        for i in valasz_lehetosegek_lista:
            if "$" in i:
                print(itt)
                itt.append(i[:-1])
            else:
                print(itt)
                itt.append(i)
        self.egybe[kerdes] = itt
        print(self.egybe)
        
                
        for lehetoseg in valasz_lehetosegek_lista:
            if lehetoseg[-1] == "$":
                helyes_valasz_lista.append(lehetoseg[:-1])
                valasz_lehetosegek_lista.remove(lehetoseg)
        
        self.kerdes_valasz.append({kerdes: [[valasz_lehetosegek_lista], [helyes_valasz_lista]]})
        Create_task(file_name=self.file_name, file_desc=self.file_desc, kerdes_valasz=self.kerdes_valasz, feladatsor_neve=self.feladatsor_neve, egybe=self.egybe).chose()
        
        
            

def main():
    a = "tempalaryx.docx"
    b = input("Mi legyen a feladatsor neve?: ")
    c = input("Mi legyen a feladatsor leírása?: ")
    Create_task(file_name=a, file_desc=c, kerdes_valasz=[], feladatsor_neve=b, egybe={}).chose()
   


def docx_2_pdf(input_file, output_file):
    subprocess.run(['libreoffice', '--headless', '--convert-to', 'pdf', input_file, '--outdir', 'tmp'], check=True) # Átalakítás docx formátumból pdf formázumba
    print(f'tmp/{input_file[:-4]}pdf', {output_file})
    os.rename(f'tmp/{input_file[:-4]}pdf', output_file) # fájl átnevezése
    os.remove(input_file) # input fájl kitörlése




if __name__  == '__main__':
    main()
    
    
"""

    doc = DocxTemplate('test.docx')
    nev = input("Írj be egy nevet: ")
    context = {
        'name': nev
    }

    doc.render(context)
    doc.save('kimenet.docx')
    
"""