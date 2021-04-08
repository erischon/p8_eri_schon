from django.core.management.base import BaseCommand, CommandError

from database.manage import DBManage
from database.extract import Extract
from database.transform import Transform
from database.load import Load

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        managing = DBManage()
        # managing.delete_tables()
        extract = Extract()
        extract.extract()
        transform = Transform()
        transform.transform_basic()
        loading = Load()
        loading.load_data()
