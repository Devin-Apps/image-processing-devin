from setuptools import setup, find_packages

setup(
    name='image_processing_dev',
    version='0.1.0',
    author='Devin',
    author_email='devin@devin-ai.com',
    description='A simple image processing package to crop images and convert them to black and white or sepia.',
    packages=find_packages(),
    install_requires=[
        'Pillow>=8.0.0',
    ],
    python_requires='>=3.6',
)
