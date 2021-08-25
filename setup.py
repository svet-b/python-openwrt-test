from setuptools import setup, find_packages

setup(
    name='Python',
    version='1.0.0',
    url='https://github.com/svet-b/python-openwrt-test.git',
    author='Svet Bajlekov',
    author_email='tomatoman@gmail.com',
    description='Test',
    packages=find_packages(),    
    install_requires=['paho-mqtt'],
    py_modules=[
        'mqtt_sub',
    ],
    entry_points={
        'console_scripts': [
            'mqtt_sub = mqtt_sub:main',
        ]
    },
)