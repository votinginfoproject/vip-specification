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

+-------------------------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                           | Data Type                        | Required?    | Repeats?     | Description                              | Error Handling                           |
+===============================+==================================+==============+==============+==========================================+==========================================+
| date                          | ``xs:date``                      | **Required** | Single       | Specifies when the election is being     | If the field is invalid, then the        |
|                               |                                  |              |              | held. The `Date` is considered to be in  | implementation is required to ignore the |
|                               |                                  |              |              | the timezone local to the state holding  | ``Election`` element containing it.      |
|                               |                                  |              |              | the election.                            |                                          |
+-------------------------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| election_notice               | :ref:`multi-csv-election-notice` | Optional     | Single       | Allows for the publication of            | If the element is invalid or not         |
|                               |                                  |              |              | information related to election notices, | present, then the implementation is      |
|                               |                                  |              |              | including those attributed to natural    | required to ignore it.                   |
|                               |                                  |              |              | disasters and other unforeseen events.   |                                          |
+-------------------------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| election_type                 | ``xs:string``                    | Optional     | Single       | Specifies the highest controlling        | If the element is invalid or not         |
|                               |                                  |              |              | authority for election (e.g., federal,   | present, then the implementation is      |
|                               |                                  |              |              | state, county, city, town, etc.)         | required to ignore it.                   |
+-------------------------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| state_id                      | ``xs:IDREF``                     | **Required** | Single       | Specifies a link to the `State` element  | If the field is invalid, then the        |
|                               |                                  |              |              | where the election is being held.        | implementation is required to ignore the |
|                               |                                  |              |              |                                          | ``Election`` element containing it.      |
+-------------------------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| is_statewide                  | ``xs:boolean``                   | Optional     | Single       | Indicates whether the election is        | If the field is not present or invalid,  |
|                               |                                  |              |              | statewide.                               | the implementation is required to        |
|                               |                                  |              |              |                                          | default to "yes".                        |
+-------------------------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| name                          | ``xs:string``                    | Optional     | Single       | The name for the election (**NB:** while | If the element is invalid or not         |
|                               |                                  |              |              | optional, this element is highly         | present, then the implementation is      |
|                               |                                  |              |              | recommended).                            | required to ignore it.                   |
+-------------------------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| registration_info             | ``xs:string``                    | Optional     | Single       | Specifies information about registration | If the element is invalid or not         |
|                               |                                  |              |              | for this election either as text or a    | present, then the implementation is      |
|                               |                                  |              |              | URI.                                     | required to ignore it.                   |
+-------------------------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| absentee_ballot_info          | ``xs:string``                    | Optional     | Single       | Specifies information about requesting   | If the element is invalid or not         |
|                               |                                  |              |              | absentee ballots either as text or a URI | present, then the implementation is      |
|                               |                                  |              |              |                                          | required to ignore it.                   |
+-------------------------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| results_uri                   | ``xs:anyURI``                    | Optional     | Single       | Contains a URI where results for the     | If the field is invalid or not present,  |
|                               |                                  |              |              | election may be found                    | then the implementation is required to   |
|                               |                                  |              |              |                                          | ignore it.                               |
+-------------------------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| polling_hours                 | ``xs:string``                    | Optional     | Single       | Contains the hours (in local time) that  | If the element is invalid or not         |
|                               |                                  |              |              | Election Day polling locations are open. | present, then the implementation is      |
|                               |                                  |              |              | If polling hours differ in specific      | required to ignore it.                   |
|                               |                                  |              |              | polling locations, alternative hours may |                                          |
|                               |                                  |              |              | be specified in the                      |                                          |
|                               |                                  |              |              | :ref:`multi-csv-polling-location` object |                                          |
|                               |                                  |              |              | *(NB: this element is deprecated in      |                                          |
|                               |                                  |              |              | favor of the more structured             |                                          |
|                               |                                  |              |              | :ref:`multi-csv-hours-open` element. It  |                                          |
|                               |                                  |              |              | is strongly encouraged that data         |                                          |
|                               |                                  |              |              | providers move toward contributing hours |                                          |
|                               |                                  |              |              | in this format)*.                        |                                          |
+-------------------------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| hours_open_ids                | ``xs:IDREF``                     | Optional     | Single       | References the                           | If the field is invalid or not present,  |
|                               |                                  |              |              | :ref:`multi-csv-hours-open` element,     | then the implementation is required to   |
|                               |                                  |              |              | which lists the hours of operation for   | ignore it.                               |
|                               |                                  |              |              | polling locations.                       |                                          |
+-------------------------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| has_election_day_registration | ``xs:boolean``                   | Optional     | Single       | Specifies if a voter can register on the | If the field is invalid or not present,  |
|                               |                                  |              |              | same day of the election (i.e., the last | then the implementation is required to   |
|                               |                                  |              |              | day of the election). Valid items are    | ignore it.                               |
|                               |                                  |              |              | "yes" and "no".                          |                                          |
+-------------------------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| registration_deadline         | ``xs:date``                      | Optional     | Single       | Specifies the last day to register for   | If the field is invalid or not present,  |
|                               |                                  |              |              | the election with the possible exception | then the implementation is required to   |
|                               |                                  |              |              | of Election Day registration.            | ignore it.                               |
+-------------------------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| absentee_request_deadline     | ``xs:date``                      | Optional     | Single       | Specifies the last day to request an     | If the field is invalid or not present,  |
|                               |                                  |              |              | absentee ballot.                         | then the implementation is required to   |
|                               |                                  |              |              |                                          | ignore it.                               |
+-------------------------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: csv-table
   :linenos:


    id,date,name,election_type,election_notice_text,election_notice_uri,state_id,is_statewide,registration_info,absentee_ballot_info,results_uri,polling_hours,has_election_day_registration,registration_deadline,absentee_request_deadline,hours_open_id
    e001,10-08-2016,Best Hot Dog,State,There are some last minute changes for this election. For additional information see the accompanying URL,https://someelectionnotice.gov,st51,true,www.registrationinfo.com,You can vote absentee,http://hotdogcontest.gov/results,Noon to 3p.m.,true,10/08/2016,,ho002


.. _multi-csv-election-notice:

election_notice
---------------

The ElectionNotice description. 

+----------------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                  | Data Type     | Required?    | Repeats?     | Description                              | Error Handling                           |
+======================+===============+==============+==============+==========================================+==========================================+
| election_notice_text | ``xs:string`` | **Required** | Single       | Text for the Election Notice.            | If the element is invalid, then the      |
|                      |               |              |              |                                          | implementation is required to ignore the |
|                      |               |              |              |                                          | ``ElectionNotice`` element containing    |
|                      |               |              |              |                                          | it.                                      |
+----------------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| election_notice_uri  | ``xs:string`` | Optional     | Single       | Optional URL for additional information  | If the field is invalid or not present,  |
|                      |               |              |              | related to the Election Notice.          | then the implementation is required to   |
|                      |               |              |              |                                          | ignore it.                               |
+----------------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
