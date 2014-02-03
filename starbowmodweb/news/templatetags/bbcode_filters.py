"""
This module defines all of our bbcode capabilities.

To add a new bbcode tag do the following:

    def bbcode_<tag_name>(tag_name, value, options, parent, context):
        return formatted_html

    bbcode_parser.add_formatter("<tag_name>", func_name, **tag_options)

For more information on the different argumnents and options available see the bbcode docs:

    http://bbcode.readthedocs.org/en/latest/
"""
from django import template

import bbcode


def bbcode_img(tag_name, value, options, parent, context):
    if tag_name in options and 'x' in options[tag_name]:
        options['width'], options['height'] = options[tag_name].split('x', 1)
        del options[tag_name]
    attrs = ' '.join([name+'="{}"' for name in options.keys()])
    return ('<img src="{}" '+attrs+' />').format(value, *options.values())


bbcode_parser = bbcode.Parser()
bbcode_parser.add_formatter("img", bbcode_img, replace_links=False)


def bbformat(value):
    return bbcode_parser.format(value)

register = template.Library()
register.filter('bbformat', bbformat)
