from setuptools import setup

package_name = 'eyes_disp_system_node'
submodules = 'eyes_disp_system_node/serialModule'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name, submodules],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ubuntu',
    maintainer_email='maoroboto@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'eyes_disp_system_node = eyes_disp_system_node.eyes_disp_system_node:main'
        ],
    },
)
