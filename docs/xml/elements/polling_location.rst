PollingLocation
===============
The Polling Location object represents a site where voters cast or drop off ballots.

.. todo::

   Add references to other elements

+-----------------------+-----------------------+--------------+------------+--------------------+-----------------------+
| Tag                   | Data Type             | Required?    | Repeats?   | Description        | Error Handling        |
|                       |                       |              |            |                    |                       |
+=======================+=======================+==============+============+====================+=======================+
| AddressLine           | xs:string             | Optional     | Repeats    |**AddressLine**     |If **AddressLine** is  |
|                       |                       |              |            |represents the      |invalid or not present,|
|                       |                       |              |            |various parts of an |the implementation is  |
|                       |                       |              |            |address to a polling|required to ignore the |
|                       |                       |              |            |location.           |PollingLocation element|
|                       |                       |              |            |                    |that contains it.      |
+-----------------------+-----------------------+--------------+------------+--------------------+-----------------------+
| Directions            | InternationalizedText | Optional     | Single     |The **Directions**  |If **Directions** field|
|                       |                       |              |            |specify further     |is invalid or not      |
|                       |                       |              |            |instructions for    |present, the           |
|                       |                       |              |            |locating the polling|implementation is      |
|                       |                       |              |            |location.           |required to ignore it. |
+-----------------------+-----------------------+--------------+------------+--------------------+-----------------------+
| Hours                 | InternationalizedText | Optional     | Single     |The **Hours** field |If **Hours** is invalid|
|                       |                       |              |            |contains the hours  |or not present, the    |
|                       |                       |              |            |(in local time) that|implementation is      |
|                       |                       |              |            |the polling location|required to ignore it. |
|                       |                       |              |            |is open.            |                       |
+-----------------------+-----------------------+--------------+------------+--------------------+-----------------------+
| HoursOpenId           | xs:IDREF              | Optional     | Single     |The **HoursOpenId** |If **HoursOpenId** is  |
|                       |                       |              |            |links to an         |invalid or not present,|
|                       |                       |              |            |:doc:`HoursOpen     |the implementation is  |
|                       |                       |              |            |<hours_open>`       |required to ignore it. |
|                       |                       |              |            |element, which is a |                       |
|                       |                       |              |            |schedule of dates   |                       |
|                       |                       |              |            |and hours during    |                       |
|                       |                       |              |            |which the polling   |                       |
|                       |                       |              |            |location is         |                       |
|                       |                       |              |            |available.          |                       |
+-----------------------+-----------------------+--------------+------------+--------------------+-----------------------+
| IsDropBox             | xs:boolean            | Optional     | Single     |**IsDropBox**       |If **IsDropBox** is    |
|                       |                       |              |            |signifies if this   |invalid or not present,|
|                       |                       |              |            |polling location is |the implementation is  |
|                       |                       |              |            |a drop box.         |required to ignore it. |
+-----------------------+-----------------------+--------------+------------+--------------------+-----------------------+
| IsEarlyVoting         | xs:boolean            | Optional     | Single     |**IsEarlyVoting**   |If **IsEarlyVoting** is|
|                       |                       |              |            |signifies if this   |invalid or not present,|
|                       |                       |              |            |polling location is |the implementation is  |
|                       |                       |              |            |an early vote site. |required to ignore it. |
+-----------------------+-----------------------+--------------+------------+--------------------+-----------------------+
| PhotoUri              | xs:anyURI             | Optional     | Single     |**PhotoUri** links  |If **PhotoUri** is     |
|                       |                       |              |            |to an image of the  |invalid or not present,|
|                       |                       |              |            |polling location.   |the implementation is  |
|                       |                       |              |            |                    |required to ignore it. |
+-----------------------+-----------------------+--------------+------------+--------------------+-----------------------+

.. code-block:: xml
   :linenos:

   <PollingLocation id="pl81274">
      <AddressLine>ALBEMARLE HIGH SCHOOL</AddressLine>
      <AddressLine>2775 Hydraulic Rd</AddressLine>
      <AddressLine>Charlottesville, VA 229018917</AddressLine>
      <HoursOpenId>hours0001</HoursOpenId>
   </PollingLocation>
