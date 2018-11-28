"""
Contains ...
"""

import json

from django.core.serializers.json import DjangoJSONEncoder


# test data
cameras = {
    'cameras': {
        'default': {
            'fov': 40,
            'pos': [1789, 129, 998],
            'rot': [0, -180, 0]
        },
        'cam01': {
            'fov': 40,
            'pos': [1449, 319, 1872],
            'rot': [0, -180.61599999999987, 0]
        },
        'cam02': {
            'fov': 40,
            'pos': [874, 176, 1145],
            'rot': [0, 3.21, 0]
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

    
