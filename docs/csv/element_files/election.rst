election.txt
============

The election.txt file represents an Election Day, which usually consists of many individual contests
and/or referenda. A feed must contain **exactly one** Election object. All relationships in the
feed (e.g., street segment to precinct to polling location) are assumed to relate only to
the Election specified by this object. It is permissible, and recommended, to combine unrelated
contests (e.g., a special election and a general election) that occur on the same day into one feed
with one Election object.

.. include:: ../../tables/elements/election.rst

.. literalinclude:: ../../csv/example_files/election.txt
   :linenos:

