#! /usr/bin/env python
import datetime

class Snap():

    '''
    Snap Model
    Base properties and funcctions
    '''

    def __init__(self,db,id):
        self._db = db
        snap = self.get_one(id)

    @property
    def db(self):
        return self._db
        
    def id(self):
        return self._id

    @property
    def snap_time(self):
        return self._snap_time

    @property
    def create_time(self):
        return self._create_time
        
    @property
    def update_time(self):
        return self._update_time    

    @property
    def creator(self):
        return self._creator

    @property
    def members(self):
        return self._members

    @property
    def members(self):
        return self._contents

    def get_one(self,id):
        self._id = id
        snap = self.db.snap.find_one({'id' : self.id})
        if snap:
            self._snap_time = snap['snap_time']
            self._creator = snap['creator']
            self._members = snap['members']
            self._contents = snap['contents']
            self._create_time = snap['create_time']
            self._update_time = snap['update_time']
        else:
            self._snap_time = ''
            self._creator = ''
            self._members = []
            self._contents = []
            self._create_time = datetime.datetime.utcnow()
            self._update_time = datetime.datetime.utcnow()
            
    def get_properties(self):
        properties = {
            'id': self.id,
            'snap_time': self.snap_time,
            'creator': self.creator,
            'members': self.members,
            'contents': self.contents,
            'create_time': self.create_time,
            'update_time': self.update_time
        }
        return properties

    def save(self):
        properties = self.get_properties()
        properties['update_time'] = datetime.datetime.utcnow()
        self.db.snap.update({'id': self.id}, properties, upsert=True)

    

            

