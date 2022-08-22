from django.test import TestCase
from aluraflix.models import Programa
from aluraflix.serializers import ProgramaSerializer

class ProgramaSerializerTestCase(TestCase):

    def setUp(self):
        self.programa = Programa(
            titulo = 'Procurando ninguém em latim',
            data_lancamento =  '2003-07-04',
            tipo = 'F',
            likes= 2344,
            dislikes=21, 
        )
        self.serializer = ProgramaSerializer(instance=self.programa)
        
    def test_serialized_fields(self):
        """Verifies serialized fields"""
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['titulo', 'data_lancamento', 'tipo', 'likes']))
    
    def test_serialized_content(self):
        """Verifies the content from serialized fields"""
        data = self.serializer.data
        self.assertEqual(data['titulo'], self.programa.titulo)
        self.assertEqual(data['data_lancamento'], self.programa.data_lancamento)
        self.assertEqual(data['tipo'], self.programa.tipo)
        self.assertEqual(data['likes'], self.programa.likes)

