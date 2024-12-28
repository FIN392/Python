import os
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class GetContact():
    """Request contact information on screen
    
    Attributes:
        Name (str): The contact's name
        Address (str): The contact's address
        Phone (str): The contact's phone number
    
    Examples:
        >>> Contact = GetContact()
        >>> print( f"Name: {Contact.Name}" )
        >>> print( f"Address: {Contact.Address}" )
        >>> print( f"Phone: {Contact.Phone}" )
        Name: Fin392
        Address: fin392@gmail.com
        Phone: 555-555-555
    """
    
    def __init__( self ):
        # Font to be used
        CUSTOM_FONT = ( "Comic Sans MS", 12, "normal" )
        
        # Get script path
        strScriptPath = os.path.dirname(os.path.realpath(__file__))

        # Create window and a frame
        self.ttkWindow = ttk.Window( themename = "darkly" )
        self.ttkWindow.overrideredirect( True )
        self.ttkWindow.geometry( "+200+100" )
        self.ttkWindow.resizable( False, False )
        self.ttkWindow.title( "myPYApplication (powered by ttkbootstrap)" )
        self.ttkWindow.iconbitmap( strScriptPath+"\\..\\Assets\\myPYApplication.ico" )
        ttkFrame = ttk.Frame( self.ttkWindow, padding=10 )
        ttkFrame.pack( fill=ttk.BOTH, expand=ttk.YES )
        
        # Variables
        self.Name    = ttk.StringVar(value="")
        self.Address = ttk.StringVar(value="")
        self.Phone   = ttk.StringVar(value="")
        
        # Cabecera del formulario
        ttkLblHearder = ttk.Label( ttkFrame, text = "Please enter your contact information", font=CUSTOM_FONT, bootstyle=DEFAULT )
        
        # Etiquetas
        ttkLblName    = ttk.Label( ttkFrame, text = "Name",    font=CUSTOM_FONT, bootstyle=DEFAULT )
        ttkLblAddress = ttk.Label( ttkFrame, text = "Address", font=CUSTOM_FONT, bootstyle=DEFAULT )
        ttkLblPhone   = ttk.Label( ttkFrame, text = "Phone",   font=CUSTOM_FONT, bootstyle=DEFAULT )
        
        # Entradas
        ttkEntName    = ttk.Entry( ttkFrame, textvariable=self.Name   , font=CUSTOM_FONT, bootstyle=DEFAULT )
        ttkEntAddress = ttk.Entry( ttkFrame, textvariable=self.Address, font=CUSTOM_FONT, bootstyle=DEFAULT )
        ttkEntPhone   = ttk.Entry( ttkFrame, textvariable=self.Phone  , font=CUSTOM_FONT, bootstyle=DEFAULT )
        
        # Botones
        ttkBtnCancelar = ttk.Button( ttkFrame, text="Cancelar", bootstyle=DANGER,  command=self.on_cancelar )
        ttkBtnEnviar   = ttk.Button( ttkFrame, text="Enviar",   bootstyle=SUCCESS, command=self.on_enviar )
        
        # Coloca los elementos
        ttkLblHearder.grid(  row=1, column=1, columnspan=3, padx=10, pady=10, sticky="nswe" )
        ttkLblName.grid(     row=2, column=1, columnspan=1, padx=10, pady=10, sticky="nswe" )
        ttkLblAddress.grid(  row=3, column=1, columnspan=1, padx=10, pady=10, sticky="nswe" )
        ttkLblPhone.grid(    row=4, column=1, columnspan=1, padx=10, pady=10, sticky="nswe" )
        ttkEntName.grid(     row=2, column=2, columnspan=2, padx=10, pady=10, sticky="nswe" )
        ttkEntAddress.grid(  row=3, column=2, columnspan=2, padx=10, pady=10, sticky="nswe" )
        ttkEntPhone.grid(    row=4, column=2, columnspan=2, padx=10, pady=10, sticky="nswe" )
        ttkBtnCancelar.grid( row=5, column=2, columnspan=1, padx=10, pady=10, sticky="nswe" )
        ttkBtnEnviar.grid(   row=5, column=3, columnspan=1, padx=10, pady=10, sticky="nswe" )
        
        # Inicia la ventana
        self.ttkWindow.mainloop()
        
    def on_cancelar(self ):
        self.Name = None
        self.Address = None
        self.Phone = None
        self.ttkWindow.quit()
    
    def on_enviar(self):
        self.Name = self.Name.get()
        self.Address = self.Address.get()
        self.Phone = self.Phone.get()
        self.ttkWindow.quit()
    
def main():
    Contact = GetContact()
    
    if Contact.Name is not None:
        print( f"Name   : {Contact.Name}" )
        print( f"Address: {Contact.Address}" )
        print( f"Phone  : {Contact.Phone}" )
    else:
        print( "No values returned" )

if __name__ == "__main__":
    main()
