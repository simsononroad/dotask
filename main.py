from docx.shared import Mm
from docxtpl import DocxTemplate, InlineImage

class Create_task():
    def __init__(self, file_name, file_desc, kerdes_valasz: list):
       self.file_name = file_name
       self.file_desc = file_desc
       self.kerdes_valasz = list(kerdes_valasz)
    def chose(self):
        
        a = input("(Ú)j kérdés, (G)enerálás, (K)ilépés")
        print()
        if a.upper() == 'Ú':
            Create_task(self.file_name, self.file_desc, self.kerdes_valasz).new_task()
        elif a.upper() == 'G':
            Create_task(self.file_name, self.file_desc, self.kerdes_valasz).gen_file()
        else:exit()
    
    def gen_file(self):
        
        
        print(f"==================\n\tFájl neve: {self.file_name}\n\tFájl leírása: {self.file_desc}\n==================\n")
        for feladatok in self.kerdes_valasz:
            for key,value in dict(feladatok).items():
                rossz_valaszok = value[0][0]
                helyes_valaszok = value[1][0]
                print(f"{key}:")
                
                
    def new_task(self):
        kerdes = input("Mi legyen a kérdés?\n>>>")
        valasz_lehetosegek = input("válasz lehetőségek vesszővel elválasztva a helyes válasz után tegyél egy '$' jelet.\npl: egy, ketto$, harom\n>>>")
        valasz_lehetosegek_lista = valasz_lehetosegek.split(",")
        helyes_valasz_lista = []
        
        for lehetoseg in valasz_lehetosegek_lista:
            if lehetoseg[-1] == "$":
                helyes_valasz_lista.append(lehetoseg[:-1])
                valasz_lehetosegek_lista.remove(lehetoseg)
        print(valasz_lehetosegek_lista)
        print(helyes_valasz_lista)
        self.kerdes_valasz.append({kerdes: [[valasz_lehetosegek_lista], [helyes_valasz_lista]]})
        print(self.kerdes_valasz)
        Create_task(file_name=self.file_name, file_desc=self.file_desc, kerdes_valasz=self.kerdes_valasz).chose()
        
        
            

def main():
    a = input("Mi legyen a file neve?: ")
    b = input("Mi legyen a leírása?: ")
    Create_task(file_name=a, file_desc=b, kerdes_valasz={}).chose()
   

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