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
2. Once it's done and tested, create a pull request to move it into the current working branch.
3. At that point, some discussion might happen and, when it's reviewed and accepted by the team within a reasonable timeframe (TBD), it's merged into the current working branch by the developer who created the pull-request.
4. Delete the feature/bug branch.

At any one point in time ("feature/" and "bug/" temporary branches aside), there should only be a dev branch (called 'vip5' in the vip-specification's case, but it may change to simply 'dev' in the future), a stable branch (called 'master' in most cases), and, if necessary, a documentation branch (called 'gh-pages' if hosted on GitHub).