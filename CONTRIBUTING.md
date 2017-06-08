# Contributing to the VIP Specification
Thanks for considering contributing to the Voting Information Project.

While the following information shouldn't be considered hard-and-fast rules, they should be
considered more than guidelines. As with anything in this repository, if you'd like to request a
changes to this process, please fill out an issue and file it under the milestone "Up for
Discussion."

## Creating Issues

* Like many open source projects, we strongly urge you to search through the existing issues before
  creating a new one.
* Please include as many details as possible.
    * Note that this specification's user base are the states and jurisdictions and its primary use
      case is to export structured election data out of the existing election management systems
      (e.g. voter registration systems, vote tabulation systems, et al).
    * If you can include an example of how you think a new model should work, all the better.
* All issues should be filed under the milestone "Up for Discussion" until the team moves it under
  a particular release or other related issue-management action.

## Pull Requests

1. Create a branch to work on a fix/feature (a fix/feature should have a companion bug/enhancement
   issue). Start the branch with either "feature/..." or "bug/...".
    1. If you're not a member of the VIP Spec team, fork the repository and follow the same
       process.
2. Before sending out a pull request, please make sure that:
    1. if working on a schema bug/feature, the resulting XSD and sample feed XML still validate
        1. You can use http://www.utilities-online.info/xsdvalidation/ to do this validation online, or
        2. If you have the [xmllint](http://xmlsoft.org/xmllint.html) tool installed, please run
           `xmllint --nonet --xinclude --noout --schema vip_spec.xsd sample_feed.xml`
        3. If you have the [Jing](http://www.thaiopensource.com/relaxng/jing.html) validator
           installed, please run `jing vip_spec.xsd sample_feed.xml`
    2. if working on a documentation bug/feature, the documentation must build with Sphinx with no
       errors (_**NB:** see [Installing Sphinx](#installing-sphinx) below_).
3. Once it's done and tested, create a pull request to move it into the current working branch.
4. At that point, some discussion might happen. In order to get approval for the pull request, you
   will need approval from two people, including one representative from Pew and one representative
   from Google (Pew and Google employees still need two approvers and cannot self-approve, but it
   is not required that the second approver be from the organization of the PR author). However it
   is important to note that other members have substantial technical and election background as
   well, so please take all feedback to heart, regardless of the source.
    1. Google approvers: @jdmgoogle
    2. Pew approvers: @lbirdpew; @afsmythe
5. When it's reviewed and accepted by the team within a reasonable timeframe (TBD), it's merged
   into the current working branch by the developer who created the pull-request.
6. Delete the feature/bug branch.

At any one point in time ("feature/" and "bug/" temporary branches aside), there should only be a
dev branch (called 'vip5' in the vip-specification's case, but it may change to simply 'dev' in the
future), a stable branch (called 'master' in most cases), and, if necessary, a documentation branch
(called 'gh-pages' if hosted on GitHub).


## Documentation Format

VIP writes its documentation in a format called [reStructuredText][reST]
(aka reST).  reST is a markup language used mainly for documentation.
VIP chose reST because of its enhanced formatting capabilities.
For example, reST supports tables.

The documentation that VIP exposes to the public is in HTML.  VIP generates
its HTML documentation from the reST files automatically using a process
called "building" the documentation.  Instructions for building are below.

One problem with reST is that tables in reST are hard to edit and maintain
by hand.  For this reason, VIP stores the tabular documentation data in
separate files in an open data format called [YAML][YAML]
(specifically [YAML version 1.1][YAML_1.1]). YAML files are human-readable and
easy to edit by hand.  The YAML files are stored in the
[`docs/yaml`](docs/yaml) directory.


## Dev Environment

This section explains how to set up your local development environment for
contributing. First, [install Python][python_download]. **You must use Python
3.4 or higher.**

We also recommend setting up a virtual environment for the repo (e.g. using
[virtualenv][virtualenv]) prior to installing dependencies.

Use [`pip`][pip] to install dependencies, which comes with Python 3.4+
(and is installed automatically when creating a virtual environment).
Open a terminal window and run:

```sh
$ pip install Sphinx PyYAML sphinx_rtd_theme
```

([Sphinx](http://sphinx-doc.org) is for building the documentation.)


## Building the Documentation

To build the documentation:

```sh
$ cd /path/to/vip-specification/docs/
$ make html
```

To see changes to the documentation as the files are edited, use the
following command:

```sh
$ sphinx-autobuild . _build/html
```

Once the above command is executed, open a browser and view
[http://127.0.0.1:8000](http://127.0.0.1:8000) to see the documentation.


## Updating the Documentation

To update the documentation, edit the YAML files by hand as needed.
Do not edit the reST files by hand since they are generated automatically
from the YAML files.

Then, normalize the YAML files and update the reST files:

```sh
$ python scripts/vip.py norm_yaml
$ python scripts/vip.py make_rest
```

After this, you will want to build the documentation as described above.

When submitting a PR, changes to both the YAML files and the updated reST
files should be checked in.  This lets people reviewing your pull request
check to see how the reST files will be affected by your patch.
However, do not check in the generated HTML files.

For help using the Python script above:

```sh
$ python scripts/vip.py -h
```

Or for help with a specific command (for example):

```sh
$ python scripts/vip.py make_rest -h
```


[Markdown]: http://daringfireball.net/projects/markdown/
[pip]: https://pip.pypa.io/en/stable/
[python_download]: https://www.python.org/downloads
[reST]: http://docutils.sourceforge.net/rst.html
[virtualenv]: https://pypi.python.org/pypi/virtualenv/
[YAML]: http://yaml.org/
[YAML_1.1]: http://yaml.org/spec/1.1/
