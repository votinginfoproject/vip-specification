Polling Location
================

The Polling Location object represents a site where voters cast ballots.

.. todo::
   Work on preamble.
.. todo::
   Figure out Description and Error Handling for AddressLine.

+-------------+---------------------+-----------------+-----------------+-----------------+
|Tag          |Data                 |Optional/Required|Description      |Error            |
|             |Type                 |                 |                 |Handling         |
+-------------+---------------------+-----------------+-----------------+-----------------+
|AddressLine  |String               |**Required**;    |                 |If               |
|             |                     |multiple allowed |                 |**AddressLine**  |
|             |                     |                 |                 |is invalid or    |
|             |                     |                 |                 |not present,     |
|             |                     |                 |                 |the              |
|             |                     |                 |                 |implementation   |
|             |                     |                 |                 |is required to   |
|             |                     |                 |                 |ignore the       |
|             |                     |                 |                 |PollingLocation  |
|             |                     |                 |                 |element that     |
|             |                     |                 |                 |contains it.     |
+-------------+---------------------+-----------------+-----------------+-----------------+
|Directions   |InternationalizedText|Optional         |The              |If               |
|             |                     |                 |**Directions**   |**Directions**   |
|             |                     |                 |specify          |field is invalid |
|             |                     |                 |further          |or not present,  |
|             |                     |                 |instructions     |the              |
|             |                     |                 |for locating     |implementation   |
|             |                     |                 |the polling      |is required to   |
|             |                     |                 |location.        |ignore it.       |
+-------------+---------------------+-----------------+-----------------+-----------------+
|Hours        |InternationalizedText|Optional;        |The **Hours**    |If **Hours** is  |
|             |                     |multiple allowed |field contains   |invalid or not   |
|             |                     |                 |the hours (in    |present, the     |
|             |                     |                 |local time) that |implementation   |
|             |                     |                 |the polling      |is required to   |
|             |                     |                 |location is open.|ignore it.       |
|             |                     |                 |                 |                 |
|             |                     |                 |                 |                 |
|             |                     |                 |                 |                 |
|             |                     |                 |                 |                 |
|             |                     |                 |                 |                 |
|             |                     |                 |                 |                 |
|             |                     |                 |                 |                 |
+-------------+---------------------+-----------------+-----------------+-----------------+
|HoursOpenId  |IDREF                |Optional;        |The              |If               |
|             |                     |multiple allowed |**HoursOpenId**  |**HoursOpenId**  |
|             |                     |                 |links to a       |is invalid or    |
|             |                     |                 |schedule of dates|not present, the |
|             |                     |                 |and hours during |implementation   |
|             |                     |                 |which the polling|is required to   |
|             |                     |                 |location is      |ignore it.       |
|             |                     |                 |available.       |                 |
+-------------+---------------------+-----------------+-----------------+-----------------+
|IsDropBox    |Boolean              |Optional         |**IsDropBox**    |If **IsDropBox** |
|             |                     |                 |signifies if this|is invalid or    |
|             |                     |                 |polling location |not present, the |
|             |                     |                 |is a drop box.   |implementation   |
|             |                     |                 |                 |is required to   |
|             |                     |                 |                 |ignore it.       |
+-------------+---------------------+-----------------+-----------------+-----------------+
|IsEarlyVoting|Boolean              |Optional         |**IsEarlyVoting**|If               |
|             |                     |                 |signifies if this|**IsEarlyVoting**|
|             |                     |                 |polling location |is invalid or not|
|             |                     |                 |is an early vote |present, the     |
|             |                     |                 |site.            |implementation is|
|             |                     |                 |                 |required to      |
|             |                     |                 |                 |ignore it.       |
+-------------+---------------------+-----------------+-----------------+-----------------+
|PhotoUri     |anyURI               |Optional         |**PhotoUri**     |If **PhotoUri**  |
|             |                     |                 |links to an image|is invalid or not|
|             |                     |                 |of the polling   |present, the     |
|             |                     |                 |location.        |implementation is|
|             |                     |                 |                 |required to      |
|             |                     |                 |                 |ignore it.       |
+-------------+---------------------+-----------------+-----------------+-----------------+

.. code-block:: xml
   :linenos:

   <PollingLocation id="pl81191">
      <AddressLine>ST ANNE'S-BELFIELD LWR SCHOOL - Convocation Ctr.</AddressLine>
      <AddressLine>799 Faulconer Drive</AddressLine>
      <AddressLine>Charlottesville, VA 22903</AddressLine>
      <HoursOpenId>hours0001</HoursOpenId>
   </PollingLocation>
