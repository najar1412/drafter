"""
Contains modules
"""

import json

from django.core.serializers.json import DjangoJSONEncoder


# test data
cameras = {
    'cameras': {
        'default': {
            'fov': 40,
            'pos': [650, 250, -900],
            'rot': [0, -180, 0]
        },
        'cam01': {
            'fov': 40,
            'pos': [0, 0, 0],
            'rot': [0, 0, 100]
        },
        'cam02': {
            'fov': 40,
            'pos': [500, 500, 500],
            'rot': [100, 0, 0]
        },
    },    
}


class SceneData():
    def _to_dict(self, row=None):
        """returns a dict repr of a sqlalchemy row"""
        if row:
            pass

        else:
            return {
                'cameras': cameras['cameras']
            }


    def _encode_dict(self, params):
        return json.dumps(dict(params), cls=DjangoJSONEncoder)


    def encode_cameras(self, encode=True):
        if encode:
            return self._encode_dict(self._to_dict())

        else:
            return self._to_dict()

    
