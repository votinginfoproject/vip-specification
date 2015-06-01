ExternalIdentifiers
===================

The ``ExternalIdentifiers`` element allows VIP data to connect with external datasets (e.g.
candidates with campaign finance datasets, electoral geographies with `OCD-IDs`_ that allow for
greater connectivity with additional datasets, etc...). Examples for ``ExternalIdentifiers`` can be
found on the objects that support them:

* :doc:`Candidate <candidate>`

* Any element that extends :doc:`ContestBase <contest_base>`

* :doc:`ElectoralDistrict <electoral_district>`

* :doc:`Locality <locality>`

* :doc:`Office <office>`

* :doc:`Party <party>`

* :doc:`Precinct <precinct>`

* :doc:`State <state>`

.. _OCD-IDs: http://opencivicdata.readthedocs.org/en/latest/ocdids.html

+--------------------+-------------------------+------------+----------+------------------------------+----------------------------+
| Tag                | Data Type               | Required?  | Repeats? |Description                   |Error Handling              |
|                    |                         |            |          |                              |                            |
+====================+=========================+============+==========+==============================+============================+
| ExternalIdentifier |`ExternalIdentifier`_    |**Required**| Repeats  |Defines the identifier and the|At least one valid          |
|                    |                         |            |          |type of identifier it is (see |`ExternalIdentifier`_ must  |
|                    |                         |            |          |`ExternalIdentifier`_ for     |be present for              |
|                    |                         |            |          |complete information).        |``ExternalIdentifiers`` to  |
|                    |                         |            |          |                              |be valid. If no valid       |
|                    |                         |            |          |                              |`ExternalIdentifier`_ is    |
|                    |                         |            |          |                              |present, the implementation |
|                    |                         |            |          |                              |is required to ignore the   |
|                    |                         |            |          |                              |``ExternalIdentifiers``     |
|                    |                         |            |          |                              |element.                    |
|                    |                         |            |          |                              |                            |
|                    |                         |            |          |                              |                            |
+--------------------+-------------------------+------------+----------+------------------------------+----------------------------+

ExternalIdentifier
------------------

+------------+----------------------------------+------------+----------+-----------------------------------+----------------------------+
| Tag        | Data Type                        | Required?  | Repeats? |Description                        |Error Handling              |
|            |                                  |            |          |                                   |                            |
+============+==================================+============+==========+===================================+============================+
| Type       |:doc:`IdentifierType              |**Required**| Single   |Specifies the type of              |If the field is invalid or  |
|            |<../enumerations/identifier_type>`|            |          |identifier. Must be one of the     |not present, the            |
|            |                                  |            |          |valid types as defined by          |implementation is required  |
|            |                                  |            |          |:doc:`IdentifierType               |to ignore the               |
|            |                                  |            |          |<../enumerations/identifier_type>`.|``ElectionIdentifier``      |
|            |                                  |            |          |                                   |containing it.              |
+------------+----------------------------------+------------+----------+-----------------------------------+----------------------------+
| OtherType  | xs:string                        | Optional   | Single   |Allows for cataloging an           |If the field is invalid or  |
|            |                                  |            |          |``ExternalIdentifier`` type that   |not present, the            |
|            |                                  |            |          |falls outside the options listed in|implementation is required  |
|            |                                  |            |          |:doc:`IdentifierType               |to ignore it.               |
|            |                                  |            |          |<../enumerations/identifier_type>`.|                            |
|            |                                  |            |          |``Type`` should be set to "other"  |                            |
|            |                                  |            |          |when using this field.             |                            |
+------------+----------------------------------+------------+----------+-----------------------------------+----------------------------+
| Value      | xs:string                        |**Required**| Single   |Specifies the identifier.          |If the field is invalid or  |
|            |                                  |            |          |                                   |not present, the            |
|            |                                  |            |          |                                   |implementation is required  |
|            |                                  |            |          |                                   |to ignore the               |
|            |                                  |            |          |                                   |``ElectionIdentifier``      |
|            |                                  |            |          |                                   |containing it.              |
+------------+----------------------------------+------------+----------+-----------------------------------+----------------------------+
