# coding: utf-8

"""
    EOD STOCK API

     <h2>Intelligent EOD Stocks API</h2>
     <p>
        Intelligent Stock Market API provides end-of-day stock data worldwide, financial news, and financial social
        media trends for web application developers, researchers and service providers.
        The API covers over 150,000 tickers, stocks, mutual funds, and more from around the world.
        It offers information for any period, including daily, weekly.
     </p>
     <ul>
        <li>Exchange Information</li>
        <li>Stock Tickers Data</li>
        <li>End of Day (EOD) Stock Data</li>
        <li>Fundamental Data</li>
        <li>Stock Options And Splits Data</li>
        <li>Financial News API</li>
        <li>Social Media Trend Data For Stocks</li>
        <li>Sentiment Analysis for News & Social Media</li>
    </ul>
    <p>
        The information provided covers more than 150 000 tickers, stocks, mutual funds and more around the world.
        we provide information for any period, including daily, weekly.
    </p>

    Contact: support@eod-stock-api.site
"""
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "PROJECT_README.md").read_text()


from setuptools import setup, find_packages  # noqa: H301

NAME = "Intelligent-Stock-Market-API"
VERSION = "0.0.6"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]
PYTHON_REQUIRES = '>=3.7'
setup(
    name=NAME,
    version=VERSION,
    description="An Intelligent EOD Stock Market, Financial News & Financial Social Media Trends API",
    author="MJ API Development",
    author_email="support@eod-stock-api.site",
    url="https://eod-stock-api.site",
    project_urls={
        'Documentation': 'https://github.com/MJ-API-Development/stock-api-pythonsdk',
        'Source': 'https://github.com/MJ-API-Development/stock-api-pythonsdk',
        'Tracker': 'https://github.com/MJ-API-Development/stock-api-pythonsdk/issues',
        'Subscribe - API Keys': 'https://eod-stock-api.site/login#signup',
        'Intelligent Stock Market API': 'https://eod-stock-api.site',
        'API Gateway': 'https://gateway.eod-stock-api.site'
    },
    keywords=["OpenAPI", "Intelligent EOD Stock Market API", "EOD STOCK API", "Financial News API", "Financial Social Media Trends"],
    install_requires=REQUIRES,
    python_requires=PYTHON_REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="Apache 2.0",
    long_description=long_description,
    long_description_content_type='text/markdown'
)
