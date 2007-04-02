#!/usr/bin/env python
################################################################################
#
#  qooxdoo - the new era of web development
#
#  http://qooxdoo.org
#
#  Copyright:
#    2006-2007 1&1 Internet AG, Germany, http://www.1and1.org
#
#  License:
#    LGPL: http://www.gnu.org/licenses/lgpl.html
#    EPL: http://www.eclipse.org/org/documents/epl-v10.php
#    See the LICENSE file in the project's top-level directory for details.
#
#  Authors:
#    * Sebastian Werner (wpbasti)
#
################################################################################

##
#<h2>Module Description</h2>
#<pre>
# NAME
#  module.py -- module short description
#
# SYNTAX
#  module.py --help
#
#  or
#
#  import module
#  result = module.func()
#
# DESCRIPTION
#  The module module does blah.
#
# CAVEATS
#
# KNOWN ISSUES
#  There are no known issues.
#</pre>
##

import tree, mapper

ignore = []

##                                                                              
# Some nice short description of foo(); this can contain html and 
# {@link #foo Links} to items in the current file.
#                                                                               
# @param     a        Describe a positional parameter
# @keyparam  b        Describe a keyword parameter
# @def       foo(name)    # overwrites auto-generated function signature
# @param     name     Describe aliased parameter
# @return             Description of the things returned
# @defreturn          The return type
# @exception IOError  The error it throws
#
def patch(node, known, prefix, verbose):
    if node.type == "identifier":
        name = node.get("name", False)

        if name != None and name.startswith("__") and not name in ignore:
            if not name in known:
                known[name] = "__%s%s" % (prefix, len(known))

            if verbose:
                print "      - Replace identifier: %s with %s" % (name, known[name])

            node.set("name", known[name])

    elif node.type == "keyvalue":
        name = node.get("key", False)

        if name != None and name.startswith("__") and not name in ignore:
            if not name in known:
                known[name] = "__%s%s" % (prefix, len(known))

            if verbose:
                print "      - Replace key: %s with %s" % (name, known[name])

            node.set("key", known[name])

    if node.hasChildren():
        for child in node.children:
            patch(child, known, prefix, verbose)

    return len(known)
