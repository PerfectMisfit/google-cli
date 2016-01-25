#!/usr/bin/env python
import sys
import webbrowser

query = " ".join(sys.argv[1:]).encode('utf-8')
print('Query: "{}"'.format(query))
webbrowser.open_new_tab('http://www.google.com/search?q={}'.format(query))