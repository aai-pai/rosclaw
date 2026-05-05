from setuptools import setup

package_name = 'rosclaw_bringup'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/bringup.launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Sunil Sainis',
    maintainer_email='sainis.sunil@gmail.com',
    description='Bringup for RosClaw: rosbridge, rosapi, agent, discovery.',
    license='Apache-2.0',
)
