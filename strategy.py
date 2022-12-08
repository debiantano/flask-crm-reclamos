from abc import ABCMeta, abstractmethod

class Context():
    @staticmethod
    def request(strategy):
        return strategy()

class IMensaje(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def __str__():
        "Implementacion mensaje de alerta"

class Exito(IMensaje):
    def __str__(self):
        return '''<div id="overlay" class="fixed z-40 w-screen h-screen inset-0 bg-gray-900 bg-opacity-60"></div><div id="dialogo" class="fixed z-50 top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-96 bg-white rounded-md px-8 py-6 space-y-5 drop-shadow-lg"><div class="mx-auto flex items-center justify-center h-12 w-12 rounded-full bg-green-100"><svg class="h-6 w-6 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg></div><div class="py-5 border-t border-b border-gray-300 text-center"><p>Validación exitosa</p></div><div class="flex justify-end"><button id="close" class="px-5 py-2 bg-pink-500 hover:bg-pink-700 text-white cursor-pointer rounded-md">Aceptar</button></div></div>'''

class Error(IMensaje):
    def __str__(self):
        return '''<div id="overlay" class="fixed z-40 w-screen h-screen inset-0 bg-gray-900 bg-opacity-60"></div><div id="dialogo" class="fixed z-50 top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-96 bg-white rounded-md px-8 py-6 space-y-5 drop-shadow-lg"><div class="mx-auto flex items-center justify-center h-12 w-12 rounded-full bg-red-100"><svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 24 24" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M11.001 10h2v5h-2zM11 16h2v2h-2z"></path><path d="M13.768 4.2C13.42 3.545 12.742 3.138 12 3.138s-1.42.407-1.768 1.063L2.894 18.064a1.986 1.986 0 0 0 .054 1.968A1.984 1.984 0 0 0 4.661 21h14.678c.708 0 1.349-.362 1.714-.968a1.989 1.989 0 0 0 .054-1.968L13.768 4.2zM4.661 19 12 5.137 19.344 19H4.661z"></path></svg></div><div class="py-5 border-t border-b border-gray-300 text-center"><p>Los datos del cliente no han sido encontrados</p></div><div class="flex justify-end"><button id="close" class="px-5 py-2 bg-pink-500 hover:bg-pink-700 text-white cursor-pointer rounded-md">Aceptar</button></div></div>'''

class Mensaje(IMensaje):
    def __str__(self):
        return '''<div id="overlay" class="fixed z-40 w-screen h-screen inset-0 bg-gray-900 bg-opacity-60"></div><div id="dialogo" class="fixed z-50 top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-96 bg-white rounded-md px-8 py-6 space-y-5 drop-shadow-lg"><div class="mx-auto flex items-center justify-center h-12 w-12 rounded-full bg-green-100"><svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 24 24" height="45px" width="45px" xmlns="http://www.w3.org/2000/svg"><path d="M20 2H4c-1.103 0-2 .897-2 2v12c0 1.103.897 2 2 2h3v3.767L13.277 18H20c1.103 0 2-.897 2-2V4c0-1.103-.897-2-2-2zm0 14h-7.277L9 18.233V16H4V4h16v12z"></path><path d="m17.207 7.207-1.414-1.414L11 10.586 8.707 8.293 7.293 9.707 11 13.414z"></path></svg></div><div class="py-5 border-t border-b border-gray-300 text-center"><p>Reclamo enviado satisfactoriamente</p></div><div class="flex justify-end"><button id="close" class="px-5 py-2 bg-pink-500 hover:bg-pink-700 text-white cursor-pointer rounded-md">Aceptar</button></div></div>'''

# The Client
#CONTEXT = Context()

#print(CONTEXT.request(Exito))
#print(CONTEXT.request(Error))
#print(CONTEXT.request(Mensaje))