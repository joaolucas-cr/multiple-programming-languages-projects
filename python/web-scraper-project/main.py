from bs4 import BeautifulSoup
from requests import request
import sys


"""
- Title
- Price
- Availability
- Product URL
- Rating
"""
from objects.cli import processArguments
def main():
    processArguments(sys.argv)

if __name__ == "__main__":
    main()