# Contributing to the VIP Specification
Thank you for considering a contribution to the Voting Information Project.

The main users of the specification are states and local jurisdictions in the United States. 
To have their data published via VIP, their data must conform to this specification. This 
means that they are structuring exports from existing election management systems (e.g. voter 
registration systems and vote tabulation systems).

This specification's main users are states and local jurisdictions in the United States. 
To have their data published via VIP, their data must conform to this specification. This 
means that they are structuring exports from existing election management systems (e.g. voter 
registration systems and vote tabulation systems).

While the following information shouldn't be considered hard-and-fast rules, they should be
considered more than guidelines. As with anything in this repository, if you'd like to request a
changes to this process, please fill out an issue and file it under the milestone "Up for
Discussion."

## Creating Issues

* Please search through the existing issues before creating a new one.
* Please include as many details as possible.
    * If you can include an example of how you think a new model should work, please do.
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
    3. Please ensure that, when updating the documentation, all reST and HTML files have been re-generated (see below for more details).
3. Once it's done and tested, create a pull request.
4. Some changes might be necessary for a PR to be approved. To get final approval for the PR, you will need approval from two people, including one representative from Democracy Works and one representative from Google. Democracy Works and Google employees still require two approvers and cannot self-approve, but it is not required that either approver on the PR be from the same organization as the PR author. 
5. When it's reviewed and accepted by the team, the PR's author should merge the change
   into the main branch.
6. Finally, delete the feature/bug branch.

At any one point in time ("feature/" and "bug/" temporary branches aside), there should only be a
dev branch (called 'vip5' in the vip-specification's case, but it may change to simply 'dev' in the
future), a stable branch (called 'master' in most cases), and, if necessary, a documentation branch
(called 'gh-pages' if hosted on GitHub).


## Documentation Format

VIP writes its documentation in [YAML][YAML] format
(specifically [YAML version 1.1][YAML_1.1]). The YAML files are stored in the
[`docs/yaml`](docs/yaml) directory. This is then auto-generated into a markup language
called [reStructuredText][reST] (aka reST). Finally, the reST files are used 
to auto-generate the HTML that is viewable by the public.

**Thus to update the documentation, you must edit the YAML files and re-generate the RST and HTML files.**

## Setting up your Environment

Use the command `make install` to create a virtual environment 
with all required packages:

```sh
$ cd /[PATH]/[TO]/[VIP-SPEC]/docs/
$ make install
```

## Updating the Documentation

To update the documentation, edit the YAML files.
Do not edit the reST or HTML files by hand since they are auto-generated
from the YAML files.

Then, by using the `make build` target, the following actions will be performed:

 - The YAML files will be normalized. 
 - The reST files will be re-generated based on the YAML files.
 - The HTML files will be re-generated based on the RST files.

```sh
$ cd /[PATH]/[TO]/[VIP-SPEC]/docs/
$ make build
```

Note: it is essential that you  complete this build process so that 
the reST and HTML reflect your updates.

Once the new HTML has been generated, run `make preview` and open a browser to
[http://127.0.0.1:8000](http://127.0.0.1:8000) to preview the updated documentation.

## Troubleshooting

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
