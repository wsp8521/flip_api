#COMANDOS PERSONALIZADOS
import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from catalogoFilmes.models import Actor


class Command(BaseCommand):
    
    #função que permite passar argumentos para os comaando
    def add_arguments(self, parser):
        parser.add_argument('file_name',type=str,help="nome do arquivo csv") #definindo argumetnos

    #função que executa o comando
    def handle(self, *args, **options): 
        file_name=options['file_name']

        with open(file_name, 'r',encoding='utf-8') as files: #abrindo arquivo csv
            readerFile = csv.DictReader(files) #lendo arquivo csv
            
            for row in readerFile: #percorrendo o arquivo csv
                nameActor = row['name']
                birthday_date = datetime.strptime(row['birthday'],'%Y-%m-%d').date()
                nationality = row['nationality']

                self.stdout.write(self.style.NOTICE(nameActor))

                Actor.objects.create( #salvando no banco de dados
                    nameActor = nameActor,
                    birthday_date = birthday_date,
                    nationality = nationality
                )

            self.stdout.write(self.style.SUCCESS("ATORES IMPORTADOS COM SUCESSO"))
            

