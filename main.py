from PyQt5 import uic, QtWidgets, QtGui
from PyQt5.QtCore import QEventLoop, QTimer
import requests

def consulta_cep():

	retorno.show()

	cep_input = front.lineEdit.text()

	if len(cep_input) != 8:
		retorno.listWidget.clear()
		retorno.listWidget.addItem('CEP incorreto, tente novamente.')
		loop = QEventLoop()
		QTimer.singleShot(5000, loop.quit)
		loop.exec_()
		retorno.close()
	else:
		()
		request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep_input))

		address_data = request.json()

		if 'erro' not in address_data:
			retorno.listWidget.clear()
			retorno.listWidget.addItem(' CEP: {} '.format(address_data['cep']))
			retorno.listWidget.addItem(' Logradouro: {} '.format(address_data['logradouro']))
			retorno.listWidget.addItem(' Bairro: {} '.format(address_data['bairro']))
			retorno.listWidget.addItem(' Cidade: {} '.format(address_data['localidade']))
			retorno.listWidget.addItem(' Estado: {} '.format(address_data['uf']))

		else:
			retorno.listWidget.clear()
			retorno.listWidget.addItem(' CEP inválido, tente novamente.')

def fim_consulta():
	front.lineEdit.setText('')
	retorno.close()

app = QtWidgets.QApplication([])
front = uic.loadUi('src/front.ui')
retorno = uic.loadUi('src/retorno.ui')
front.pushButton_2.clicked.connect(consulta_cep)
retorno.pushButton_2.clicked.connect(fim_consulta)

front.setWindowTitle('- Consulta de CEP')
front.setWindowIcon(QtGui.QIcon('icone/icon.ico'))
retorno.setWindowTitle('- Resultado do CEP')
retorno.setWindowIcon(QtGui.QIcon('icone/icon.ico'))

front.show()
app.exec()