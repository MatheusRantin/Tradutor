from translate import Translator
import customtkinter as ctk






class TelaHome:

    def traduzir(self):
        tradutor = Translator(to_lang="pt")
        getTexto = str(self.inputTexto.get())

        #Limite de 500 Char
        saida = tradutor.translate(str(getTexto))

      
        textTranslate = ctk.CTkLabel(self.master, text=f"Traducao: {saida}")
        textTranslate.pack(padx=10, pady=10)


    def __init__ (self, master):
        self.master = master

        self.LabelTitulo = ctk.CTkLabel(master, text= "Tradutor de texto")
        self.LabelTitulo.pack(padx=10, pady=10)

        self.inputTexto = ctk.CTkEntry(master, placeholder_text="Digite o texto")
        self.inputTexto.pack(padx=10, pady=10)

        self.btnSubmit = ctk.CTkButton(master, text="Traduzir", command= self.traduzir )
        self.btnSubmit.pack(padx=10, pady=10)
        

        



if __name__ == "__main__":
    root = ctk.CTk()
    root.title("Tradução de Texto")
    root.geometry("500x500")

    chamandoTela = TelaHome(root)

    root.mainloop()



   


