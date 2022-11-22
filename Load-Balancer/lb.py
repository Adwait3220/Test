def GenerateConfig(context):

    resources=[{
        'name': context.env['name'],
        'type': 'compute.v1.regionInstanceGroupManager',
        'properties':{
            'instanceTemplate': context.properties['instanceTemplate'],
            'namedPorts': context.properties['namedPorts'],
            'targetSize': context.properties['targetSize'],
            'region': context.properties['region']
        }
    }]
    return {'resources': resources}