help()


# G:\Users\Andrey\PycharmProjects\.venv\Scripts\python.exe G:\Users\Andrey\PycharmProjects\lesson-2\help.py
# Welcome to Python 3.13's help utility! If this is your first time using
# Python, you should definitely check out the tutorial at
# https://docs.python.org/3.13/tutorial/.
#
# Enter the name of any module, keyword, or topic to get help on writing
# Python programs and using Python modules.  To get a list of available
# modules, keywords, symbols, or topics, enter "modules", "keywords",
# "symbols", or "topics".
#
# Each module also comes with a one-line summary of what it does; to list
# the modules whose name or summary contain a given string such as "spam",
# enter "modules spam".
#
# To quit this help utility and return to the interpreter,
# enter "q", "quit" or "exit".
#


# help> keywords
#
# Here is a list of the Python keywords.  Enter any keyword to get more help.
#
# False               class               from                or
# None                continue            global              pass
# True                def                 if                  raise
# and                 del                 import              return
# as                  elif                in                  try
# assert              else                is                  while
# async               except              lambda              with
# await               finally             nonlocal            yield
# break               for                 not
#
# help>


# help> del
# The "del" statement
# *******************
#
#    del_stmt ::= "del" target_list
#
# Deletion is recursively defined very similar to the way assignment is
# defined. Rather than spelling it out in full details, here are some
# hints.
#
# Deletion of a target list recursively deletes each target, from left
# to right.
#
# Deletion of a name removes the binding of that name from the local or
# global namespace, depending on whether the name occurs in a "global"
# statement in the same code block.  If the name is unbound, a
# "NameError" exception will be raised.
#
# Deletion of attribute references, subscriptions and slicings is passed
# to the primary object involved; deletion of a slicing is in general
# equivalent to assignment of an empty slice of the right type (but even
# this is determined by the sliced object).
#
# Changed in version 3.2: Previously it was illegal to delete a name
# from the local namespace if it occurs as a free variable in a nested
# block.
#
# Related help topics: BASICMETHODS
#
# help>


# help> symbols
#
# Here is a list of the punctuation symbols which Python assigns special meaning
# to. Enter any symbol to get more help.
#
# !=                  +                   <<=                 _
# "                   +=                  <=                  __
# """                 ,                   <>                  `
# %                   -                   ==                  b"
# %=                  -=                  >                   b'
# &                   .                   >=                  f"
# &=                  ...                 >>                  f'
# '                   /                   >>=                 j
# '''                 //                  @                   r"
# (                   //=                 J                   r'
# )                   /=                  [                   u"
# *                   :                   \                   u'
# **                  :=                  ]                   |
# **=                 <                   ^                   |=
# *=                  <<                  ^=                  ~
#
# help> **=
# Augmented assignment statements
# *******************************
#
# Augmented assignment is the combination, in a single statement, of a
# binary operation and an assignment statement:
#
#    augmented_assignment_stmt ::= augtarget augop (expression_list | yield_expression)
#    augtarget                 ::= identifier | attributeref | subscription | slicing
#    augop                     ::= "+=" | "-=" | "*=" | "@=" | "/=" | "//=" | "%=" | "**="
#              | ">>=" | "<<=" | "&=" | "^=" | "|="
#
# (See section Primaries for the syntax definitions of the last three
# symbols.)
#
# An augmented assignment evaluates the target (which, unlike normal
# assignment statements, cannot be an unpacking) and the expression
# list, performs the binary operation specific to the type of assignment
# on the two operands, and assigns the result to the original target.
# The target is only evaluated once.
#
# An augmented assignment statement like "x += 1" can be rewritten as "x
# = x + 1" to achieve a similar, but not exactly equal effect. In the
# augmented version, "x" is only evaluated once. Also, when possible,
# the actual operation is performed *in-place*, meaning that rather than
# creating a new object and assigning that to the target, the old object
# is modified instead.
#
# Unlike normal assignments, augmented assignments evaluate the left-
# hand side *before* evaluating the right-hand side.  For example, "a[i]
# += f(x)" first looks-up "a[i]", then it evaluates "f(x)" and performs
# the addition, and lastly, it writes the result back to "a[i]".
#
# With the exception of assigning to tuples and multiple targets in a
# single statement, the assignment done by augmented assignment
# statements is handled the same way as normal assignments. Similarly,
# with the exception of the possible *in-place* behavior, the binary
# operation performed by augmented assignment is the same as the normal
# binary operations.
#
# For targets which are attribute references, the same caveat about
# class and instance attributes applies as for regular assignments.
#
# Related help topics: NUMBERMETHODS
#
# help>
