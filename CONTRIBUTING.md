# Contributing to the VIP Specification
Thanks for considering contributing to the Voting Information Project.

While the following information shouldn't be considered hard-and-fast rules, they should be considered more than guidelines. As with anything in this repository, if you'd like to request a changes to this process, please fill out an issue and file it under the milestone "Up for Discussion."

## Creating Issues

* Like many open source projects, we strongly urge you to search through the existing issues before creating a new one.
* Please include as many details as possible.
    * Note that this specification's user base are the states and jurisdictions and its primary use case is to export structured election data out of the existing election management systems (e.g. voter registration systems, vote tabulation systems, et al).
    * If you can include an example of how you think a new model should work, all the better.
* All issues should be filed under the milestone "Up for Discussion" until the team moves it under a particular release or other related issue-management action.

## Pull Requests

1. Create a branch to work on a fix/feature (a fix/feature should have a companion bug/enhancement issue). Start the branch with either "feature/..." or "bug/...".
    1. If you're not a member of the VIP Spec team, fork the repository and follow the same process.
2. Before sending out a pull request, please make sure that:
    1. if working on a schema bug/feature, the resulting XSD and sample feed XML still validate
        1. You can use http://www.utilities-online.info/xsdvalidation/ to do this validation online, or
        2. If you have the `xmllint` tool on your system, please run `xmllint --postvalid --nonet --xinclude --noout --schema vip_spec.xsd sample_feed.xml`
    2. if working on a documentation bug/feature, the documentation must build with Sphinx with no errors (_**NB:** see [Installing Sphinx](#installing-sphinx) below_).
3. Once it's done and tested, create a pull request to move it into the current working branch.
4. At that point, some discussion might happen. In order to get approval for the pull request, you will need approval from two people, including one representative from Pew and one representative from Google (Pew and Google employees still need two approvers and cannot self-approve, but it is not required that the second approver be from the organization of the PR author). However it is important to note that other members have substantial technical and election background as well, so please take all feedback to heart, regardless of the source.
    1. Google approvers: @jdmgoogle @jktomer
    2. Pew approvers: @jungshadow @jen-tolentino (Pew employees) @pstenbjorn (official Pew proxy)
5. When it's reviewed and accepted by the team within a reasonable timeframe (TBD), it's merged into the current working branch by the developer who created the pull-request.
6. Delete the feature/bug branch.

At any one point in time ("feature/" and "bug/" temporary branches aside), there should only be a dev branch (called 'vip5' in the vip-specification's case, but it may change to simply 'dev' in the future), a stable branch (called 'master' in most cases), and, if necessary, a documentation branch (called 'gh-pages' if hosted on GitHub).

## Dev Environment

This section explains how to set up your local development environment for
contributing.  First, [install Python][python_download].  We recommend
installing the latest stable version of Python 3 (Python 3.4.3 as of June 2015).

We also recommend setting up a virtual environment for the repo (e.g. using
[virtualenv][virtualenv]) prior to installing dependencies.

Use [`pip`][pip] to install dependencies, which comes with Python 3.4+
(and is installed automatically when creating a virtual environment).
Open a terminal window and run:

```sh
$ pip install Sphinx PyYAML
```

([Sphinx](http://sphinx-doc.org) is for building the documentation.)


## Building the Documentation

To build the documentation:

```sh
$ python scripts/vip.py update_tables
$ cd /path/to/vip-specification/docs/
$ make html
```

To see changes to the documentation as the files are edited, use the following command:

```sh
$ sphinx-autobuild . _build/html
```

Once the above command is executed, open a browser and enter http://127.0.0.1:8000 to see the documentation.


[pip]: https://pip.pypa.io/en/stable/
[python_download]: https://www.python.org/downloads
[virtualenv]: https://pypi.python.org/pypi/virtualenv/
