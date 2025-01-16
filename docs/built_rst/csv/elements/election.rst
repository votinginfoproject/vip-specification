.. This file is auto-generated.  Do not edit it by hand!

.. _multi-csv-election:

election
========

The Election object represents an Election Day, which usually consists of many individual contests
and/or referenda. A feed must contain **exactly one** Election object. All relationships in the
feed (e.g., street segment to precinct to polling location) are assumed to relate only to
the Election specified by this object. It is permissible, and recommended, to combine unrelated
contests (e.g., a special election and a general election) that occur on the same day into one feed
with one Election object.

+-------------------------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                           | Data Type      | Required?    | Repeats?     | Description                              | Error Handling                           |
+===============================+================+==============+==============+==========================================+==========================================+
| date                          | ``xs:date``    | **Required** | Single       | Specifies when the election is being     |                                          |
|                               |                |              |              | held. The `Date` is considered to be in  |                                          |
|                               |                |              |              | the timezone local to the state holding  |                                          |
|                               |                |              |              | the election.                            |                                          |
+-------------------------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| election_type                 | ``xs:string``  | Optional     | Single       | Specifies the highest controlling        |                                          |
|                               |                |              |              | authority for election (e.g., federal,   |                                          |
|                               |                |              |              | state, county, city, town, etc.)         |                                          |
+-------------------------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| state_id                      | ``xs:IDREF``   | **Required** | Single       | Specifies a link to the `State` element  |                                          |
|                               |                |              |              | where the election is being held.        |                                          |
+-------------------------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| is_statewide                  | ``xs:boolean`` | Optional     | Single       | Indicates whether the election is        | If the field is not present or invalid,  |
|                               |                |              |              | statewide.                               | the implementation is required to        |
|                               |                |              |              |                                          | default to "yes".                        |
+-------------------------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| name                          | ``xs:string``  | Optional     | Single       | The name for the election (**NB:** while |                                          |
|                               |                |              |              | optional, this element is highly         |                                          |
|                               |                |              |              | recommended).                            |                                          |
+-------------------------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| registration_info             | ``xs:string``  | Optional     | Single       | Specifies information about registration |                                          |
|                               |                |              |              | for this election either as text or a    |                                          |
|                               |                |              |              | URI.                                     |                                          |
+-------------------------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| absentee_ballot_info          | ``xs:string``  | Optional     | Single       | Specifies information about requesting   |                                          |
|                               |                |              |              | absentee ballots either as text or a URI |                                          |
+-------------------------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| results_uri                   | ``xs:anyURI``  | Optional     | Single       | Contains a URI where results for the     |                                          |
|                               |                |              |              | election may be found                    |                                          |
+-------------------------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| polling_hours                 | ``xs:string``  | Optional     | Single       | Contains the hours (in local time) that  |                                          |
|                               |                |              |              | Election Day polling locations are open. |                                          |
|                               |                |              |              | If polling hours differ in specific      |                                          |
|                               |                |              |              | polling locations, alternative hours may |                                          |
|                               |                |              |              | be specified in the                      |                                          |
|                               |                |              |              | :ref:`multi-csv-polling-location` object |                                          |
|                               |                |              |              | *(NB: this element is deprecated in      |                                          |
|                               |                |              |              | favor of the more structured             |                                          |
|                               |                |              |              | :ref:`multi-csv-hours-open` element. It  |                                          |
|                               |                |              |              | is strongly encouraged that data         |                                          |
|                               |                |              |              | providers move toward contributing hours |                                          |
|                               |                |              |              | in this format)*.                        |                                          |
+-------------------------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| hours_open_ids                | ``xs:IDREF``   | Optional     | Single       | References the                           |                                          |
|                               |                |              |              | :ref:`multi-csv-hours-open` element,     |                                          |
|                               |                |              |              | which lists the hours of operation for   |                                          |
|                               |                |              |              | polling locations.                       |                                          |
+-------------------------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| has_election_day_registration | ``xs:boolean`` | Optional     | Single       | Specifies if a voter can register on the |                                          |
|                               |                |              |              | same day of the election (i.e., the last |                                          |
|                               |                |              |              | day of the election). Valid items are    |                                          |
|                               |                |              |              | "yes" and "no".                          |                                          |
+-------------------------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| registration_deadline         | ``xs:date``    | Optional     | Single       | Specifies the last day to register for   |                                          |
|                               |                |              |              | the election with the possible exception |                                          |
|                               |                |              |              | of Election Day registration.            |                                          |
+-------------------------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| absentee_request_deadline     | ``xs:date``    | Optional     | Single       | Specifies the last day to request an     |                                          |
|                               |                |              |              | absentee ballot.                         |                                          |
+-------------------------------+----------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:


    id,date,name,election_type,state_id,is_statewide,registration_info,absentee_ballot_info,results_uri,polling_hours,has_election_day_registration,registration_deadline,absentee_request_deadline,hours_open_id
    e001,10-08-2016,Best Hot Dog,State,st51,true,www.registrationinfo.com,You can vote absentee,http://hotdogcontest.gov/results,Noon to 3p.m.,true,10/08/2016,,ho002
