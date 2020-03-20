import setuptools

setuptools.setup(
    name="stockcacl",
    version="0.1.1",
    author="Antonio Mangiacapra",
    description="Stock Calculator - Percentile Analysis",
    long_description="A simple python module to perform percentile analysis on stock data",
    long_description_content_type="text/markdown",
    url="https://github.com/antonioeatgoat/stockcacl/",
    packages=setuptools.find_packages(),
    install_requires=['python-dotenv', 'pandas', 'requests'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)