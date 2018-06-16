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
            'pos': [650, 250, -900],
            'rot': [0, -180, 0]
        },
        'cam01': {
            'fov': 40,
            'pos': [175.6419796707714, 318.31970818310407, 168.25639842151324],
            'rot': [0, -180.61599999999987, 0]
        },
        'cam02': {
            'fov': 40,
            'pos': [208.2203553085502, 336.9839218219977, -76.14368255833787],
            'rot': [0, 2.380000000000001, 0]
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

    
