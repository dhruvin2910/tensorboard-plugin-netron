from setuptools import setup, find_packages

with open('README.md', 'r') as readme:
    long_description = readme.read()

setup(
    name='tensorboard-plugin-netron',
    version='0.1.1',
    packages=find_packages(),
    url='https://github.com/dhruvin2910/tensorboard-plugin-netron',
    license='MIT',
    author='Dhruvin Gandhi',
    author_email='contact@dhruvin.dev',
    description='Netron TensorBoard Plugin',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=[
        'netron~=4.3.2',
        'tensorboard~=2.2.2',
        'werkzeug~=1.0.1'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    entry_points={
        'tensorboard_plugins': [
            'netron = tensorboard_plugin_netron:Netron'
        ]
    }
)
