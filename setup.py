from setuptools import setup

VERSION          = '2.0.3' 
DESCRIPTION      = '3D and 2D Truss structural analysis'


setup(
        name="slientruss3", 
        version=VERSION,
        license="MIT",
        author="Rohit-K-Gaikwad",
        author_email="rgaikwad1998@gmail.com",
        description=DESCRIPTION,
        url="https://github.com/Rohit-K-Gaikwad/3D-Truss-analysis-by-using-python",
        packages=['slientruss3d'],
        install_requires=['numpy', 'matplotlib>=3.5.1'], 
        keywords=['python', 'truss', 'civil engineering', 'structural analysis'],
        classifiers= [
            "Development Status :: 5 - Production/Stable",
            "Intended Audience :: Education",
            "Intended Audience :: Developers",
            "Intended Audience :: Manufacturing",
            "Intended Audience :: Science/Research",
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python :: 3.9"
        ]
)
