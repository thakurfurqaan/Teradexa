from django.conf import settings

db_name = "productdb"
app_name = "Product"

class ProductRouter(object):
    
    def db_for_read(self, model, **hints):
        if db_name not in settings.DATABASES:
            return None
        if model._meta.app_label == app_name:
            return db_name
        return None

    def db_for_write(self, model, **hints):
        
        if db_name not in settings.DATABASES:
            return None
        if model._meta.app_label == app_name:
            return db_name
        return None

    def allow_relation(self, obj1, obj2, **hints):
        
        if db_name not in settings.DATABASES:
            return None
        if obj1._meta.app_label == app_name or obj2._meta.app_label == app_name:
            return True
        return None

    def allow_syncdb(self, db, model):
        
        if db_name not in settings.DATABASES:
            return None
        if db == db_name:
            return model._meta.app_label == app_name
        elif model._meta.app_label == app_name:
            return False
        return None