from django.core.management.base import BaseCommand

from database.manage import DBManage # Can be remove if we don't want to delete
from database.extract import Extract
from database.transform import Transform
from database.load import Load


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        managing = DBManage() # Can be remove if we don't want to delete
        managing.delete_tables() # Can be remove if we don't want to delete
        extract = Extract()
        extract.extract()
        transform = Transform()
        transform.transform_basic()
        loading = Load()
        loading.load_data()
