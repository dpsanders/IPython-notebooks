# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=1>

# Proposed general syntax for markup of **references** in the IPython Notebook

# <codecell>

%load_ext nbtoc
%nbtoc

# <markdowncell>

# The use of Markdown corresponds to an idea of *lightweight* markup.
# This document presents two suggestions in this direction:
# 
# 1. Simplifying LaTeX markup
# 
# 2. General cross-references with lightweight markup

# <headingcell level=2>

# Simplifying LaTeX markup

# <markdowncell>

# We use LaTeX for two purposes, for which it is a "killer" application:
# 
# 1. Markup of mathematical equations
# 
# 2. Sophisticated document layout algorithms

# <markdowncell>

# *__All__* other uses of LaTeX are *__obsolete__*, i.e. the great majority of LaTeX packages on CTAN, `.sty` files,
# `.cls` files etc. These all involve *__text processing__*, formatting, etc. which is, to put it mildly, *not* a strong point of
# LaTeX, as anybody who has had the misfortune to look at the LaTeX source code of a LaTeX package will testify!

# <markdowncell>

# From the point of view of the *user*, they see LaTeX only in the form of textual markup  written with `$...$`, `$$...$$` and standard LaTeX and AMSmath environments such as `\begin{equation}...\end{equation}` and `\begin{align}...\end{align}`, written inside Markdown cells. This LaTeX markup can effectively be thought of as
# an extension of the Markdown language.

# <markdowncell>

# However, there is an obvious inconsistency here with respect to the term "lightweight". The original TeX markup
# given by `$...$` and `$$...$$` fits very nicely with lightweight Markdown markup. However, the LaTeX macros grown
# on top of these, starting with `\begin` and ending with `\end`, are big, bloated and uncomfortable to use.

# <markdowncell>

# A simple solution is to recognise that since we are now using LaTeX *only* for mathematics, the `\begin` and `\end` will mark the beginning and end of a LaTeX snippet.
# 
# So let's take advantage of this, and extend the use of `$` to mark the beginning and end of snippets. The `\begin` and `\end` become redundant, so we drop them, leaving the following syntax for an equation, for example:
# 
#     ` \$equation y = x^2 \$ `
#     
# Effectively, the whole string `$equation$` becomes a new LaTeX tag.
# Of course, it would also be sensible, as done in many LaTeX editors, to provide abbreviations, so that we could write
# 
#     ` \$eqn y=x^2 \$`
# 
# Similarly we would have
# 
#     ` \$align y &= x^2 \\ `
#     `         z &= y^3 $ ` 
# 
# This is the proposed new lightweight, agile LaTeX markup. (Of course, the full syntax will still be available via
# the `\` symbol).
# 
# 
#     
# 
# 
#     

# <headingcell level=2>

# References

# <markdowncell>

# A crucial part of any technical writing is the use of cross-references, which for brevity we will refer
# to simply as *references*.

# <headingcell level=3>

# Standard types of references

# <markdowncell>

# Some standard use-cases of references in text or LaTeX documents are:

# <markdowncell>

# - Reference to another labelled hierarchical region (section, sub-section, etc.) in the same document
# 
# - Reference to an equation
# 
# - Reference to a figure
# 
# - Reference to a table
# 
# - Reference to a code block
# 
# - Citation of a bibliographic item

# <markdowncell>

# To this we can add the following from the online world:

# <markdowncell>

# - External link to a webpage or other document (e.g. a YouTube video) given by a URL
# 
# - External link a labelled point inside a webpage, given by the HTML `#` construct
# 
# - Use of Digital Object Identifiers to refer to external digital objects 

# <headingcell level=3>

# Less common reference use-cases

# <markdowncell>

# We could also, for example, think of the following examples. They occur less frequently, but *__only because there has not been, until now, a suitable syntax for them__*!

# <markdowncell>

# - Refer to a particular line of code in a particular code block. This is a common action required in technical
# writing, which has no current good solution: the reference currently would usually be by line number, with the 
# code lines being numbered in the document. However, these line numbers will easily be corrupted when the code is
# edited!
# 
# - Reference *from within* a (comment inside a) code block to the same or another code block, or a line inside it
# 
# - Reference to another IPython notebook document, or to a particular cell or (labelled) line within that document
# 
# - Reference to a certain bar (measure) in a musical score
# 
# - Reference to a time-stamped location in an audio file or video object.

# <headingcell level=3>

# Abstraction to a general reference / label syntax

# <markdowncell>

# There is a clear abstraction of *__all__* of the above use cases, as is obvious from the syntax of, e.g., the
# LaTeX, reST and HTML markup languages: we need a way of *labelling* a position in an *object* (code block,
# equation etc.), and then *referring* to it with a pointer. 

# <markdowncell>

# Thus all we need is a *uniform* syntax for creating a label, and for referring to that label.

# <markdowncell>

# A reference in this sense can be thought of as a uni-directional pointer, or arrow, with a *head* at the *referee*
# (the object referred *to*) and a *tail* at the *referrer* (the object doing the referring). Pictorially, this can
# be denoted as follows:

# <markdowncell>

# referrer |-------------> referee

# <markdowncell>

# It just remains to invent a lightweight, agile syntax for this structure. There is a *very* lightweight syntax for this in reST, as follows. To refer to an object with the label `object` from another position, we use:
# 
# `object_`
# 
# ...
# 
# `_object:`

# <markdowncell>

# The underscores (`_`) thus denote part of the horizontal part of the arrow, and we can think of this syntax as
# labelling the *arrow itself* with the name `object`:

# <markdowncell>

# referrer $\over{\longrightarrow}{\text{object}}$  referee

# <markdowncell>

# However, the underscore is not visually obvious and does not remind us of its function. Instead, we propose the
# following notation:
# 
# `.` :  Current location
# 
# `->` :
#     Reference
# 
# `:` :
#     Label

# <markdowncell>

# A reference from a position in the file to a label `object` is thus written as follows:
# 
# ```
# .->object
# 
# ...
# 
# .:object:
# ``` 

# <markdowncell>

# We may omit the dots and the final colon:
# 
# 
# ```
# ->object
# 
# ...
# 
# :object
# ``` 

# <markdowncell>

# These labels may be included in a LaTeX snippet (`$...$`) or a code block by using the respective comment symbol:
# 
# - LaTeX:
# 
# Trying to solve the equation .->general_quadratic led 16th-century mathematicians to the concept of a *complex number*.
# `$eq ax^2 +bx + c = 0 %:general_quadratic:`
# which will be automatically translated to
# \begin{equation} ax^2 +bx + c = 0 %:general_quadratic: 
# \end{equation}
# Note that using the comment automatically hides the label in this case (but only if we insert a new line after the label).
# 
# - Python code:
# 
# In ->settings_import, we see a useful way of changing the name of an imported variable whose original name we do
# not like.
# ```
# import matplotlib
# from matplotlib import rcParams as settings  #:settings_import:
# ```

# <markdowncell>

# These links will be rendered in the Notebook (upon execution of the cell) as normal HTML-type links.
# In editing mode, syntax highlighting and code completion will be provided: on typing `->`, the color will be
# changed to the link color, and a list of currently-known labels will be provided.

# <markdowncell>

# It may happen that you are writing, say, a text cell and wish to insert a reference to a label of an object which
# is not yet known. In this case, once the label is created later, all the cells with references to this label will
# be *automatically* rerun to include the correct reference. (Of course, this automatic re-running may be turned off by a suitable `%config` parameter.)

# <headingcell level=3>

# Implementation of reference structure

# <markdowncell>

# References and labels can naturally be thought of in terms of *graphs* (or *networks*), consisting of *vertices* 
# and *edges*. The vertices of the graph represent the objects in the notebook, such as code cells, lines in code
# cells, LaTeX snippets, etc., and the edges represent the references between them.
# 
# Such graphs are standard objects in computer science and mathematics, and it is well understood how to implement
# them efficiently, for example as a list of lists. Note that various tails may link to the same head, i.e. the
# structure is many-to-one. It need not be either *surjective* (every label is referred to), nor *injective* (one
# label cannot be referred to by more than one reference).

# <headingcell level=3>

# Conversion of notebook references to output formats

# <markdowncell>

# When the notebook is exported, the references in the notebook must be converted into suitable code to implement
# the reference in each output type (HTML, LaTeX) etc.
# 
# The *context* of the reference should (usually, at least) be sufficient to determine how it is exported. For
# example, if the reference is inside a LaTeX snippet, it should be translated as being an equation reference,
# and given the appropriate syntax. If it is a reference 

# <headingcell level=2>

# Figures

# <markdowncell>

# There needs to be a way to add a *caption* to a *plot output* in order to produce a new object, called (as in
# LaTeX), a *figure*. Such a figure must then also be able to be *labelled*, as above.
# 
# A solution for this is to put the reference and the caption in the *metadata*. The caption must be displayed.

# <headingcell level=2>

# External references

# <markdowncell>

# An *external reference* is a reference to an external document, i.e. to any object which is not inside the current notebook. To specify an external reference, it is thus necessary to specify at least the file name / URL / DOI /
# etc. of the external object. For example, to refer to a webpage, we can do:
# 
#     One of the most famous websites in the world is .->url:wikipedia.org 

# <markdowncell>

# If we want to refer to a point labelled using `<a>`, we must make a reference to an object *inside* the page.
# To do so, we use either `.` or `:` to dereference:
# 
#     At .->url:wikipedia.org:"Today's news"

# <markdowncell>

# But this can now be extended as the completely *general* syntax for references to sub-objects of external objects. For example, to refer to the `.:sec_quadratics:` label inside the IPython notebook document `polynomials.ipynb`
# located in the `../book` directory, 
# we write:
# 
#     The well-known solution of quadratic equations is described in .->../my_book/polynomials.ipynb:sec_quadratics:
#     
# To refer to an equation in that section would use exactly the *same* syntax!

# <markdowncell>

# Of course, we will often need several different references pointing to the *same* external resource. As in reST,
# we can then provide a *resource table* as a dictionary object, represented as key-value pairs:
# 
#     .book: ../my_book
#     .booksite: github.io/book_site
#     
# Then the links become simple!:
# 
#     Quadratics are discussed in our textbook ->.book:chap_quadratics. 
#     For additional examples, see the book's website ->.booksite:examples

# <headingcell level=2>

# Bibliographic references

# <markdowncell>

# Bibliographic references are a key part of any scientific document. Current tools are, as usual, lacking in this
# area!
# 
# A bibliographic reference is just a reference to an external resource, and so should be treated in *exactly* the
# same way. Let's start by considering papers published recently (say, within the last 10 years), which exist on the web. Then the reference can just be a reference to the website, and external scraping tools, or the relevant
# database API, can be used to extract the correct citation for HTML or PDF export:
# 
#     .giuggioli_paper: http://prl.aps.org/abstract/PRL/v110/i5/e058103
# 
#      In ->.giuggioli_paper, we showed how to calculate first-passage times of two confined random walkers 
#      with overlapping habitats.

# <markdowncell>

# Of course, we do *not* want to have a list of all the bibliographic references chosen by hand and stuck at the end of our `.ipynb` notebook. For this purpose, BibTeX was invented. However, BibTeX, being a text formatting tool
# written in LaTeX or similar, is a functional but clumsy solution to the problem of formatting bibliography in 
# the correct style for a certain journal. What is the correct solution? Python, of course!
# 
# Indeed, a BibTeX file is basically a database, expressed in something like JSON format using key-value pairs. So
# let's really *make* it a proper JSON file and store it in a proper database. This is the goal of ->bibjson.
# 
#     bibjson: http://bibjson.org
#     
# The ->bibserver site implements a server for bibJSON files.
# 
#     bibserver: http://bibserver.org
#     
#  
#   
# 

# <markdowncell>

# So, we will have some external resource consisting of a bibliographic database with some access protocol. The
# items in the bibliographic database are named objectos, so we can do:
# 
#     .bib: url:bib-database-server-url
#     .giuggioli: .bib:giuggioli_sanders_prl_2013
# 
# Note that here we have introduced an abbreviation, `.giuggioli`. Of course, these are nothing more than Python
# variables with mangled names, for example `.giuggioli -> giuggioli_`, so that the above lines are 
# implemented as the following Python statements:

# <codecell>

refs = {}  # collection of all current references

refs["bib_"] = "http://bib-database-server-url"
refs["giuggioli_"] = refs["bib_"] + "/giuggioli_sanders_prl_2013"

# <markdowncell>

#     In ->.bib.giuggioli_paper, we showed how to calculate first-passage times of two confined random walkers with overlapping habitats.
#     
# And, naturally, we can refer to individual sections and equations etc. within the reference:
# 
#     In ->.giuggioli:sec_2, we showed how to calculate first-passage times of two confined random walkers with
#     overlapping habitats. Equation ->.giuggioli:sec_2:eq_first_passage is the main result, giving an exact result
#     for first-passage times in an approximate circular geometry, as shown in ->.giuggioli:sec_2:fig_circular

# <codecell>


