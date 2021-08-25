from setuptools import setup, find_packages

setup(
    name='openwrt-test',
    version='0.1',
    url='https://github.com/svet-b/python-openwrt-test.git',
    author='Svet Bajlekov',
    author_email='tomatoman@gmail.com',
    description='OpenWRT Test for Python package',
    python_requires='~=3.7',
    packages=find_packages(),    
    install_requires=['paho-mqtt'],
    py_modules=[
        'mqtt_sub',
    ],
)