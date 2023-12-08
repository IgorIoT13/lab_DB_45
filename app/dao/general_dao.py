from abc import ABC

from sqlalchemy import inspect

from app import db


class GeneralDAO(ABC):

    _domain_type = None
    _session = db.session

    def find_all(self):
        return self._session.query(self._domain_type).all()

    def find_by_id(self, key):
        return self._session.query(self._domain_type).get(key)

    def create(self, obj):
        self._session.add(obj)
        self._session.commit()
        return obj

    def create_all(self, obj_list):
        self._session.add_all(obj_list)
        self._session.commit()
        return obj_list

    def update(self, key, in_obj):
        domain_obj = self._session.query(self._domain_type).get(key)
        mapper = inspect(type(in_obj))
        columns = mapper.columns._collection
        for column_name, column_obj,  *_ in columns:
            if not column_obj.primary_key:
                value = getattr(in_obj, column_name)
                setattr(domain_obj, column_name, value)
        self._session.commit()

    def patch(self, key, field_name, value):
        domain_obj = self._session.query(self._domain_type).get(key)
        setattr(domain_obj, field_name, value)
        self._session.commit()

    def delete(self, key):
        domain_obj = self._session.query(self._domain_type).get(key)
        self._session.delete(domain_obj)
        try:
            self._session.commit()
        except Exception:
            self._session.rollback()
            raise

    def delete_all(self):
        self._session.query(self._domain_type).delete()
        self._session.commit()