# Copyright 2016 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Creates the Bucket."""


def GenerateConfig(context):
  """Creates the Bucket 2"""

  resources = [{
      'name': 'a-cludnuro-bucket-v1',
      'type': 'compute.v1.firewall',
      'properties': {
          'location': 'us-east-1',
          'versioning': [{
              'enabled': 'True',
          }]
      }
  }]
  return {'resources': resources}