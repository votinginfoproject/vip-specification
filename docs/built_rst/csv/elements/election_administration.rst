.. This file is auto-generated.  Do not edit it by hand!

.. _multi-csv-election-administration:

election_administration
=======================

The Election Administration represents an institution for serving a locality's (or state's) election
functions.

+---------------------------------+----------------------------------+--------------+--------------+-------------------------------------------------------------+------------------------------------------+
| Tag                             | Data Type                        | Required?    | Repeats?     | Description                                                 | Error Handling                           |
+=================================+==================================+==============+==============+=============================================================+==========================================+
| absentee_uri                    | ``xs:anyURI``                    | Optional     | Single       | Specifies the web address for information on absentee       |                                          |
|                                 |                                  |              |              | voting.                                                     |                                          |
+---------------------------------+----------------------------------+--------------+--------------+-------------------------------------------------------------+------------------------------------------+
| am_i_registered_uri             | ``xs:anyURI``                    | Optional     | Single       | Specifies the web address for information on whether an     |                                          |
|                                 |                                  |              |              | individual is registered.                                   |                                          |
+---------------------------------+----------------------------------+--------------+--------------+-------------------------------------------------------------+------------------------------------------+
| ballot_tracking_uri             | ``xs:anyURI``                    | Optional     | Single       | Specifies the web address for tracking information for a    |                                          |
|                                 |                                  |              |              | ballot cast by mail                                         |                                          |
+---------------------------------+----------------------------------+--------------+--------------+-------------------------------------------------------------+------------------------------------------+
| ballot_tracking_provisional_uri | ``xs:anyURI``                    | Optional     | Single       | Specifies the web address for tracking information for a    |                                          |
|                                 |                                  |              |              | provisional ballot. To support EAC guidelines for           |                                          |
|                                 |                                  |              |              | "Processing Provisional Ballots"                            |                                          |
|                                 |                                  |              |              | (https://www.eac.gov/research-and-data/provisional-voting/) |                                          |
+---------------------------------+----------------------------------+--------------+--------------+-------------------------------------------------------------+------------------------------------------+
| election_notice                 | :ref:`multi-csv-election-notice` | Optional     | Single       | A place for election administrators to post last minute and |                                          |
|                                 |                                  |              |              | emergency notifications pertaining to the election.         |                                          |
+---------------------------------+----------------------------------+--------------+--------------+-------------------------------------------------------------+------------------------------------------+
| elections_uri                   | ``xs:anyURI``                    | Optional     | Single       | Specifies web address the administration's website.         |                                          |
+---------------------------------+----------------------------------+--------------+--------------+-------------------------------------------------------------+------------------------------------------+
| registration_uri                | ``xs:anyURI``                    | Optional     | Single       | Specifies web address for information on registering to     |                                          |
|                                 |                                  |              |              | vote.                                                       |                                          |
+---------------------------------+----------------------------------+--------------+--------------+-------------------------------------------------------------+------------------------------------------+
| rules_uri                       | ``xs:anyURI``                    | Optional     | Single       | Specifies a URI for the election rules and laws (if any)    |                                          |
|                                 |                                  |              |              | for the jurisdiction of the administration.                 |                                          |
+---------------------------------+----------------------------------+--------------+--------------+-------------------------------------------------------------+------------------------------------------+
| what_is_on_my_ballot_uri        | ``xs:anyURI``                    | Optional     | Single       | Specifies web address for information on what is on an      |                                          |
|                                 |                                  |              |              | individual's ballot.                                        |                                          |
+---------------------------------+----------------------------------+--------------+--------------+-------------------------------------------------------------+------------------------------------------+
| where_do_i_vote_uri             | ``xs:anyURI``                    | Optional     | Single       | The Specifies web address for information on where an       |                                          |
|                                 |                                  |              |              | individual votes based on their address.                    |                                          |
+---------------------------------+----------------------------------+--------------+--------------+-------------------------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:

    id,absentee_uri,am_i_registered_uri,ballot_tracking_uri,ballot_tracking_provisional_uri,election_notice_text,election_notice_uri,elections_uri,registration_uri,rules_uri,what_is_on_my_ballot_uri,where_do_i_vote_uri
    ea123,https://example.com/absentee,https://example.com/am-i-registered,https://www.vote.virginia.gov/,https://www.vote.virginia.gov/,This is an emergency notification for this election.,https://www.yadayada.gov,https://example.com/elections,https://example.com/registration,https://example.com/rules,https://example.com/what-is-on-my-ballot,https://example.com/where-do-i-vote
    ea345,https://example.com/absentee2,https://example.com/am-i-registered2,https://example.com/elections2,https://example.com/registration2,,,https://example.com/rules2,https://example.com/what-is-on-my-ballot2,https://example.com/where-do-i-vote2
    ea625,https://example.com/absentee3,https://example.com/am-i-registered3,https://example.com/elections3,https://example.com/registration3,This is an emergency notification for this election.,,https://example.com/rules3,https://example.com/what-is-on-my-ballot3,https://example.com/where-do-i-vote3
