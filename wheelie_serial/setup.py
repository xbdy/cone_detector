from setuptools import setup

package_name = 'wheelie_serial'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
         ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    author='Conroy Cheers',
    author_email='cheers.conroy@gmail.com',
    maintainer='Conroy Cheers',
    maintainer_email='cheers.conroy@gmail.com',
    keywords=['ROS'],
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description='Serial communications for wheeliebot',
    license='',
    tests_require=[],
    entry_points={
        'console_scripts': [
            'wheelie_serial_node = wheelie_serial.wheelie_serial_node:main',
        ],
    },
)
