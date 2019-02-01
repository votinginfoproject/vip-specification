.. This file is auto-generated.  Do not edit it by hand!

.. _multi-xml-source:

Source
======

The Source object represents the organization that is publishing the information. This object is
the only required object in the feed file, and only one source object is allowed to be present.

+-----------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag             | Data Type                               | Required?    | Repeats?     | Description                              | Error Handling                           |
+=================+=========================================+==============+==============+==========================================+==========================================+
| Name            | ``xs:string``                           | **Required** | Single       | Specifies the name of the organization   | If the field is invalid, then the        |
|                 |                                         |              |              | that is providing the information.       | implementation is required to ignore the |
|                 |                                         |              |              |                                          | ``Source`` element containing it.        |
+-----------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| VipId           | ``xs:string``                           | **Required** | Single       | Specifies the ID of the organization.    | If the field is invalid, then the        |
|                 |                                         |              |              | VIP uses FIPS_ codes for this ID.        | implementation is required to ignore the |
|                 |                                         |              |              |                                          | ``Source`` element containing it.        |
+-----------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| DateTime        | ``xs:dateTime``                         | **Required** | Single       | Specifies the date and time of the feed  | If the field is invalid, then the        |
|                 |                                         |              |              | production. The date/time is considered  | implementation is required to ignore it. |
|                 |                                         |              |              | to be in the timezone local to the       |                                          |
|                 |                                         |              |              | organization.                            |                                          |
+-----------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Description     | :ref:`multi-xml-internationalized-text` | Optional     | Single       | Specifies both the nature of the         | If the element is invalid or not         |
|                 |                                         |              |              | organization providing the data and what | present, then the implementation is      |
|                 |                                         |              |              | data is in the feed.                     | required to ignore it.                   |
+-----------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OrganizationUri | ``xs:string``                           | Optional     | Single       | Specifies a URI to the home page of the  | If the field is invalid or not present,  |
|                 |                                         |              |              | organization publishing the data.        | then the implementation is required to   |
|                 |                                         |              |              |                                          | ignore it.                               |
+-----------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| FeedContactId   | ``xs:IDREF``                            | Optional     | Single       | Reference to the :ref:`multi-xml-person` | If the field is invalid or not present,  |
|                 |                                         |              |              | who will respond to inquiries about the  | then the implementation is required to   |
|                 |                                         |              |              | information contained within the file.   | ignore it.                               |
+-----------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| TouUri          | ``xs:anyURI``                           | Optional     | Single       | Specifies the website where the Terms of | If the field is invalid or not present,  |
|                 |                                         |              |              | Use for the information in this file can | then the implementation is required to   |
|                 |                                         |              |              | be found.                                | ignore it.                               |
+-----------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Version         | ``xs:string``                           | **Required** | Single       | Specifies the version of the data        | If the field is invalid, then the        |
|                 |                                         |              |              |                                          | implementation is required to ignore it. |
+-----------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. _FIPS: https://www.census.gov/geo/reference/codes/cou.html

.. code-block:: xml
   :linenos:

   <Source id="src1">
      <DateTime>2013-10-24T14:25:28</DateTime>
      <Description>
         <Text language="en">SBE is the official source for Virginia data</Text>
      </Description>
      <Name>State Board of Elections, Commonwealth of Virginia</Name>
      <OrganizationUri>http://www.sbe.virginia.gov/</OrganizationUri>
      <VipId>51</VipId>
      <Version>5.0</Version>
   </Source>


.. _multi-xml-internationalized-text:

InternationalizedText
---------------------

``InternationalizedText`` allows for support of multiple languages for a string.
``InternationalizedText`` has an optional attribute ``label``, which allows the feed to refer
back to the original label for the information (e.g. if the contact information came from a
CSV, ``label`` may refer to a row ID). Examples of ``InternationalizedText`` can be seen in:

* Any element that extends :ref:`multi-xml-contest-base`

* Any element that extends :ref:`multi-xml-ballot-selection-base`

* :ref:`multi-xml-candidate`

* :ref:`multi-xml-contact-information`

* :ref:`multi-xml-election`

* :ref:`multi-xml-election-administration`

* :ref:`multi-xml-office`

* :ref:`multi-xml-party`

* :ref:`multi-xml-person`

* :ref:`multi-xml-polling-location`

* :ref:`multi-xml-source`

+--------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type                        | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+==================================+==============+==============+==========================================+==========================================+
| Text         | :ref:`multi-xml-language-string` | **Required** | Repeats      | Contains the translations of a           | At least one valid ``Text`` must be      |
|              |                                  |              |              | particular string of text.               | present for ``InternationalizedText`` to |
|              |                                  |              |              |                                          | be valid. If no valid ``Text`` is        |
|              |                                  |              |              |                                          | present, the implementation is required  |
|              |                                  |              |              |                                          | to ignore the ``InternationalizedText``  |
|              |                                  |              |              |                                          | element.                                 |
+--------------+----------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
