from classes import Escritor
from classes import Caneta
from classes import MaquinaDeEscrever

escritor = Escritor('joãozinho')
caneta = Caneta('BIC')
máquina = MaquinaDeEscrever()


escritor.ferramenta = caneta
escritor.ferramenta.escrever()

escritor.ferramenta = máquina
escritor.ferramenta.escrever()
