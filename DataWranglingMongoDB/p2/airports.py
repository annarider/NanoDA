#!/usr/bin/env python
# -*- coding: utf-8 -*-
# All your changes should be in the 'extract_airports' function
# It should return a list of airport codes, excluding any combinations like "All"

from bs4 import BeautifulSoup
html_page = "options.html"


def extract_airports(page):
    data = []
    with open(page, "r") as html:
        # convert html to beautiful soup object
        soup = BeautifulSoup(html)

        # find all option tags for codes
        codes = soup.find_all('option')

        for code in codes: 
            airp_value = code['value']
        # filter out codes more than 3 char (airport codes all 3 chars long)
            if len(airp_value) == 3:
                if 'all' not in airp_value.lower():
                # also remove any combination airports
                    data.append(airp_value)
    return data


def test():
    data = extract_airports(html_page)
    assert len(data) == 15
    assert "ATL" in data
    assert "ABR" in data

test()