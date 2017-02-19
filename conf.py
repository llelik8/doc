# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf8')

import os

sys.path.insert(0, os.path.abspath('..'))

# -- General configuration ------------------------------------------------

master_doc = 'doc/index'
# master_doc = 'index'

extensions = [
    'sphinx.ext.todo',
    'sphinx.ext.ifconfig',
    'sphinx.ext.intersphinx',
    'ext.custom',
    'ext.LuaDomain',
    'ext.LuaLexer',
    'ext.TapLexer',
    'ext.TarantoolSessionLexer',
    'ext.DropdownList',
    'ext.WebPageSection',
    'ext.WebPageButtons',
    'ext.WebPageRocks',
    'ext.WebPageMaps'
]
primary_domain = 'lua'
source_suffix = '.rst'

project = u'Tarantool'

# |release| The full version, including alpha/beta/rc tags.
release = "1.7.3"
# |version| The short X.Y version.
version = '.'.join(release.split('.')[0:2])

exclude_patterns = [
    '_build',
    'doc/book/connectors/__*',
    'doc/book/replication/*_1.rst',
    'doc/book/replication/*_2.rst',
    'doc/book/admin.rst',
    'doc/book/box/box_introspection.rst',
    'doc/book/cookbook.rst',
    'doc/book/box/vinyl.rst',
    'doc/dev_guide/box_protocol.rst',
    'doc/dev_guide/internals.rst',
    'doc/reference/configuration/cfg_*',
    'doc/reference/reference_lua/jit.rst',
    'doc/reference/reference_lua/os.rst',
    'doc/reference/reference_lua/net_box_1.6.rst',
    'CNAME',
    'robots.txt',
    '_downloads/license.docx',
    '_downloads/license_eng.docx',
    '_downloads/terms.docx',
    '_downloads/terms_eng.docx',
    'images'
#     'doc'
]

# -- Options for HTML output ----------------------------------------------
html_theme           = 'tarantool'
html_theme_path      = ['../_theme']
html_theme_options   = {
    'base_url': "https://tarantool.org/"
}
html_static_path     = ['../_static']
html_show_sphinx     = False
html_show_copyright  = False
html_domain_indices  = False
html_use_modindex    = False
html_use_index       = True
html_use_smartypants = True
html_compact_lists   = True
html_copy_source     = False

html_context = {
    'website': {
        'index'       : True,
        'download'    : True,
        'download_16' : True,
        'careers'     : True,
        'benchmark'   : True,
        'doc'         : True,
        'try'         : True,
        'rocks'       : True,
        # Helper webpages
        '404'            : True,
        # Internal webpages
        'genindex'       : True,
        'lua-modindex'   : True,
        'search'         : True,
    },
    'wp_local': True
}

# Tarantool has extended Sphinx so that there are four new roles:
# * :codenormal:`text`     displays text as monospace
# * :codebold:`text`       displays text as monospace bold
# * :codeitalic:`text`     displays text as monospace italic
# * :codebolditalic:`text` displays text as monospace italic bold
#
# The effect on HTML output is defined in _static/sphinx_design.css
# (which is the css file designated in _templates/layout.html).
rst_prolog = """
.. role:: codenormal
   :class: ccode

.. role:: codebold
   :class: ccodeb

.. role:: codeitalic
   :class: ccodei

.. role:: codebolditalic
   :class: ccodebi

.. role:: codegreen
   :class: ccodegreen

.. role:: codered
   :class: ccodered

.. role:: codeblue
   :class: ccodeblue

.. |nbsp| unicode:: 0xA0

.. |br| raw:: html

    <br />
"""

# Intersphinx configuration
intersphinx_mapping = {
    'tarantoolc': ('http://tarantool.github.io/tarantool-c/', None)
}

latex_elements = {
    'fontenc': r'\usepackage[T1,T2A]{fontenc}'
}

intersphinx_cache_limit = 0

# Localization options
language = 'en'
locale_dirs = ['./locale']
gettext_additional_targets = ['literal-block']
