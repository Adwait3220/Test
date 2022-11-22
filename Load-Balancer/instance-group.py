def GenerateConfig(context):

    resources=[{
        'name': context.env['name'],
        'type': 'compute.v1.regionInstanceGroupManager',
        'properties':{
            # 'instanceTemplate': context.properties['instanceTemplate'],
            'instanceTemplate': '$(ref.' + context.properties['instanceTemplate'] + '.selfLink)',
            'namedPorts': context.properties['namedPorts'],
            'targetSize': context.properties['targetSize'],
            'region': context.properties['region'],
            # 'disks': context.properties['disks'],
            # 'machineType': context.properties['machineType'],
            # 'metadata': context.properties['metadata'],
            # 'networkInterfaces': context.properties['networkInterfaces'],
        }
    }]
    return {'resources':resources}