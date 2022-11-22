def GenerateConfig(context):

    resources=[{
        'name': context.env['name'],
        'type': 'compute.v1.regionInstanceGroupManager',
        'properties': {
            'machineType': context.properties['machineType'],
            'startup-script': context.properties['startup-script'],
            'region': context.properties['region'],
            'disks': [{
                'deviceName': 'boot',
                'type': 'PERSISTENT',
                'boot': True,
                'sizeGb': 25,
                'autoDelete': True,
                'initializeParams': {
                    'sourceImage': 'projects/ubuntu-os-cloud/global/images/family/ubuntu-1804-lts'}
                }],
           
            'metadata': {
                "items": [
                    {
                        "key": "startup-script",
                        "value": context.properties['startup-script']
                    }
                ]
            },
            'networkInterfaces': [{
                'network': 'global/networks/default',
                'accessConfigs': [{
                    'name': 'External NAT',
                    'type': 'ONE_TO_ONE_NAT'
                }]
            }],
            
        }
    }]
    return {'resources':resources}