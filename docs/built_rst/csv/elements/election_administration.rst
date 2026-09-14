.. This file is auto-generated.  Do not edit it by hand!

.. _multi-csv-election-administration:

election_administration
=======================

The ElectionAdministration element represents an administrative body serving a locality's election functions. In VIP 7.0, ElectionAdministration is embedded directly by value inside a :ref:`multi-csv-locality` element rather than referenced by an ID.

In overlay feeds, the entire ElectionAdministration element is replaced as a single unit on the locality, or cleared using ``<ClearElectionAdministration/>``.

+---------------------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                             | Data Type                              | Required?    | Repeats?     | Description                              | Error Handling                           |
+=================================+========================================+==============+==============+==========================================+==========================================+
| absentee_uri                    | :ref:`multi-csv-internationalized-uri` | Optional     | Single       | Web address for absentee voting          | If the element is invalid or not         |
|                                 |                                        |              |              | information.                             | present, then the implementation is      |
|                                 |                                        |              |              |                                          | required to ignore it.                   |
+---------------------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| am_i_registered_uri             | :ref:`multi-csv-internationalized-uri` | Optional     | Single       | Web address for voter registration       | If the element is invalid or not         |
|                                 |                                        |              |              | status verification.                     | present, then the implementation is      |
|                                 |                                        |              |              |                                          | required to ignore it.                   |
+---------------------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ballot_tracking_uri             | :ref:`multi-csv-internationalized-uri` | Optional     | Single       | Web address for tracking mail-in         | If the element is invalid or not         |
|                                 |                                        |              |              | ballots.                                 | present, then the implementation is      |
|                                 |                                        |              |              |                                          | required to ignore it.                   |
+---------------------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ballot_tracking_provisional_uri | :ref:`multi-csv-internationalized-uri` | Optional     | Single       | Web address for provisional ballot       | If the element is invalid or not         |
|                                 |                                        |              |              | tracking.                                | present, then the implementation is      |
|                                 |                                        |              |              |                                          | required to ignore it.                   |
+---------------------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| contact_information             | :ref:`multi-csv-contact-information`   | Optional     | Single       | Primary contact information for the      | If the element is invalid or not         |
|                                 |                                        |              |              | election administration.                 | present, then the implementation is      |
|                                 |                                        |              |              |                                          | required to ignore it.                   |
+---------------------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| elections_uri                   | :ref:`multi-csv-internationalized-uri` | Optional     | Single       | Primary web address for the election     | If the element is invalid or not         |
|                                 |                                        |              |              | administration.                          | present, then the implementation is      |
|                                 |                                        |              |              |                                          | required to ignore it.                   |
+---------------------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| registration_uri                | :ref:`multi-csv-internationalized-uri` | Optional     | Single       | Web address for voter registration.      | If the element is invalid or not         |
|                                 |                                        |              |              |                                          | present, then the implementation is      |
|                                 |                                        |              |              |                                          | required to ignore it.                   |
+---------------------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| rules_uri                       | :ref:`multi-csv-internationalized-uri` | Optional     | Single       | Web address for election rules,          | If the element is invalid or not         |
|                                 |                                        |              |              | regulations, and statutes.               | present, then the implementation is      |
|                                 |                                        |              |              |                                          | required to ignore it.                   |
+---------------------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| voter_service                   | :ref:`multi-csv-voter-service`         | Optional     | Repeats      | Specific voter services provided by the  | If the element is invalid or not         |
|                                 |                                        |              |              | administration (e.g. voter registration, | present, then the implementation is      |
|                                 |                                        |              |              | overseas voting).                        | required to ignore it.                   |
+---------------------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| what_is_on_my_ballot_uri        | :ref:`multi-csv-internationalized-uri` | Optional     | Single       | Web address where voters can see sample  | If the element is invalid or not         |
|                                 |                                        |              |              | ballots.                                 | present, then the implementation is      |
|                                 |                                        |              |              |                                          | required to ignore it.                   |
+---------------------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| where_do_i_vote_uri             | :ref:`multi-csv-internationalized-uri` | Optional     | Single       | Web address for official polling place   | If the element is invalid or not         |
|                                 |                                        |              |              | lookup.                                  | present, then the implementation is      |
|                                 |                                        |              |              |                                          | required to ignore it.                   |
+---------------------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:

    absentee_uri,am_i_registered_uri,ballot_tracking_uri,ballot_tracking_provisional_uri,elections_uri,registration_uri,rules_uri,what_is_on_my_ballot_uri,where_do_i_vote_uri
    https://example.com/absentee,https://example.com/registered,https://vote.virginia.gov/track,https://vote.virginia.gov/provisional,https://example.com/elections,https://example.com/register,https://example.com/rules,https://example.com/ballot,https://example.com/poll
