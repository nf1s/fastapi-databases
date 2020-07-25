# -*- coding: utf-8 -*-
"""
"""

from databases import Database
import sqlalchemy

__author__ = "Ahmed Nafies Okasha Mohamed <ahmed.nafies@gmail.com>"
__copyright__ = "Copyright 2020, Ahmed Nafies Okasha Mohamed"
__license__ = "MIT"
__version__ = "0.1.1"


class FastAPIDatabases(Database):
    def __init__(self, url=None):
        super().__init__(url=url)
        self._metadata = sqlalchemy.MetaData()

    def init_app(self, app):
        @app.on_event("startup")
        async def startup():
            await self.connect()

        @app.on_event("shutdown")
        async def shutdown():
            await self.disconnect()

    @property
    def metadata(self):
        return self._metadata
