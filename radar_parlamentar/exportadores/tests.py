"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from __future__ import unicode_literals
from django.test import TestCase
from django.core import serializers
from exportadores import exportar
import os
from modelagem import models


MODULE_DIR = os.path.abspath(os.path.dirname(__file__))





class ExportadoresFileTest(TestCase):
    @classmethod
    def setUpClass(cls):
        
        partidoTest1 = models.Partido(nome = 'PMDB',numero = '40')
        partidoTest2 = models.Partido(nome = 'PT',numero = '13')
        partidoTest3 = models.Partido(nome = 'PSDB',numero = '23')
        partidoTest1.save()
        partidoTest2.save()
        partidoTest3.save()
        
        parlamentarTest1 = models.Parlamentar(id_parlamentar = '',nome = 'Ivandro Cunha Lima',genero = '')
        parlamentarTest2 = models.Parlamentar(id_parlamentar = '',nome = 'Fernando Ferro',genero = '')
        parlamentarTest3 = models.Parlamentar(id_parlamentar = '',nome = 'Humberto Costa',genero = '')
        
        parlamentarTest1.save()
        parlamentarTest2.save()
        parlamentarTest3.save()


    def test_create_file_partido(self):
        
        exportar.serialize_partido()
    	filepath = os.path.join(MODULE_DIR, 'dados/partido.xml')
    	self.assertTrue(os.path.isfile(filepath))
	
    def test_verify_file_partido(self):
        partido = models.Partido.objects.get(nome = 'PMDB')
        filepath = os.path.join(MODULE_DIR, 'dados/partido.xml')
        file_xml = open(filepath,'r')
        file_read = file_xml.read()
        self.assertTrue(file_read.find(partido.nome) > 0)
        self.assertTrue(file_read.find(str(partido.numero)) > 0)




    def test_create_file_casa_legislativa(self):
		exportar.serialize_casa_legislativa()
		filepath = os.path.join(MODULE_DIR, 'dados/casa_legislativa.xml')
		self.assertTrue(os.path.isfile(filepath))
    
    def test_create_file_parlamentar(self):
    	exportar.serialize_parlamentar()
    	filepath = os.path.join(MODULE_DIR, 'dados/parlamentar.xml')
    	self.assertTrue(os.path.isfile(filepath))
    	
    def test_virify_file_parlamentar(self):
        parlamentar = models.Parlamentar.objects.get(nome ='Humberto Costa')
        filepath = os.path.join(MODULE_DIR, 'dados/parlamentar.xml')
        file_xml = open(filepath,'r')
        file_read = file_xml.read()
        self.assertTrue(file_read.find(parlamentar.nome) > 0)
        





    def test_create_file_legislatura(self):
    	exportar.serialize_legislatura()
    	filepath = os.path.join(MODULE_DIR, 'dados/legislatura.xml')
    	self.assertTrue(os.path.isfile(filepath))
    	
    def test_create_file_proposicao(self):
    	exportar.serialize_proposicao()
    	filepath = os.path.join(MODULE_DIR, 'dados/proposicao.xml')
    	self.assertTrue(os.path.isfile(filepath))
    	
    def test_create_file_votacao(self):
    	exportar.serialize_votacao()
    	filepath = os.path.join(MODULE_DIR, 'dados/votacao.xml')
    	self.assertTrue(os.path.isfile(filepath))
    	
    def test_create_file_voto(self):
    	exportar.serialize_voto()
    	filepath = os.path.join(MODULE_DIR, 'dados/voto.xml')
    	self.assertTrue(os.path.isfile(filepath))


#class DadosExportardosTest (TestCase):
	
	

        


