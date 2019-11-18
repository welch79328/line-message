import logging
import re
import sys

LOGGER = logging.getLogger('linebot')

def to_snake_case(text):
 
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def to_camel_case(text):
   
    split = text.split('_')
    return split[0] + "".join(x.title() for x in split[1:])
