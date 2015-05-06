Street Segment
==============

A Street Segment objection represents a portion of a street and the links to the precinct that this
geography (i.e., segment) is contained within. The start address house number must be less than the
end address house number unless the segment consists of only one address in which case these values
are equal.

.. todo::

   Create file for NonHouseAddress complex type.

.. todo::

   This documentation needs to be thoroughly checked for accuracy.

+-------------------------+------------------+------------------+-----------------------------+----------------------------+
| Tag                     | Data Type        | Optional/Required| Description                 | Error Handling             |
+=========================+==================+==================+=============================+============================+
| StartHouseNumber        | Integer          | **Required**     |The **StartHouseNumber** is  |If the **StartHouseNumber** |
|                         |                  |                  |the house number that street |field is not present or     |
|                         |                  |                  |segment start at. This value |invalid, the implementation |
|                         |                  |                  |is very necessary for the    |is required to ignore the   |
|                         |                  |                  |street segment to make any   |street segment element      |
|                         |                  |                  |sense. It must be less than  |containing it. If the       |
|                         |                  |                  |(or equal to) the            |**StartHouseNumber** is     |
|                         |                  |                  |EndHouseNumber. To specify   |greater than the            |
|                         |                  |                  |any house on the street (or  |**EndHouseNumber** the      |
|                         |                  |                  |when using the "\*" wildcard |implementation **may**      |
|                         |                  |                  |for street name), the best   |reverse the start or or end |
|                         |                  |                  |practice is to put 0 in this |points or it **may** ignore |
|                         |                  |                  |field.                       |the element containing it.  |
|                         |                  |                  |                             |                            |
+-------------------------+------------------+------------------+-----------------------------+----------------------------+
|EndHouseNumber           |Integer           |**Required**      |The **EndHouseNumber** is the|If the **EndHouseNumber**   |
|                         |                  |                  |house number that street     |field is not present or     |
|                         |                  |                  |segment ends at. This value  |invalid, the implementation |
|                         |                  |                  |is very necessary for the    |is required to ignore the   |
|                         |                  |                  |street segment to make any   |street segment element      |
|                         |                  |                  |sense. It must be greater    |containing it. If the       |
|                         |                  |                  |than (or equal to) the       |**EndHouseNumber** is less  |
|                         |                  |                  |StartHouseNumber. To specify |than the                    |
|                         |                  |                  |any house on the street (or  |**StartHouseNumber** the    |
|                         |                  |                  |when using the "\*" wildcard |implementation **may**      |
|                         |                  |                  |for street name), the best   |reverse the start or or end |
|                         |                  |                  |practice is to put a very    |points or it **may** ignore |
|                         |                  |                  |large number such as 999999  |the element containing it.  |
|                         |                  |                  |in this field.               |                            |
|                         |                  |                  |                             |                            |
+-------------------------+------------------+------------------+-----------------------------+----------------------------+
|OddEvenBoth              |OebEnum           |**Required**      |The **OddEvenBoth** field    |If the **OddEvenBoth** field|
|                         |                  |                  |specifies whether the odd    |is not present or invalid,  |
|                         |                  |                  |side of the street (in terms |the implementation is       |
|                         |                  |                  |of house numbers), the even  |required to ignore the      |
|                         |                  |                  |side, or both are in included|StreetSegment containing it.|
|                         |                  |                  |in the street segment. Valid |                            |
|                         |                  |                  |strings are "odd", "even", or|                            |
|                         |                  |                  |"both". It does not apply to |                            |
|                         |                  |                  |**StartApartmentNumber** or  |                            |
|                         |                  |                  |**EndApartmentNumber**.      |                            |
|                         |                  |                  |                             |                            |
+-------------------------+------------------+------------------+-----------------------------+----------------------------+
|UnitNumber               |String            |Optional          |The **UnitNumber** is the    |If the **UnitNumber** field |
|                         |                  |                  |apartment/unit number that   |is not present or invalid,  |
|                         |                  |                  |street segment start at. If  |the implementation is       |
|                         |                  |                  |this value is present then   |required to ignore it and   |
|                         |                  |                  |**StartHouseNumber** must be |assume no distinction is    |
|                         |                  |                  |equal to **EndHouseNumber**. |made between apartments     |
|                         |                  |                  |                             |along the street segment.   |
|                         |                  |                  |                             |                            |
+-------------------------+------------------+------------------+-----------------------------+----------------------------+
| NonHouseAddress         | NonHouseAddress  | **Required**     |The **NonHouseAddress** is   |If the **NonHouseAddress**  |
|                         |                  |                  |the common street address (as|field is not present or     |
|                         |                  |                  |well as city, state, and zip)|invalid, the implementation |
|                         |                  |                  |of the start and end points  |is required to ignore the   |
|                         |                  |                  |of the segment. Specific     |street segment element      |
|                         |                  |                  |information such as street   |containing it.              |
|                         |                  |                  |direction should be included.|                            |
|                         |                  |                  |                             |                            |
|                         |                  |                  |                             |                            |
|                         |                  |                  |                             |                            |
+-------------------------+------------------+------------------+-----------------------------+----------------------------+
| PrecinctId              | IDREF            | **Required**     |The **PrecinctId** references|If the **PrecinctId** field |
|                         |                  |                  |the precinct that contains   |is not present or invalid,  |
|                         |                  |                  |the entire street segment    |the implementation is       |
|                         |                  |                  |                             |required to ignore the      |
|                         |                  |                  |                             |street segment element      |
|                         |                  |                  |                             |containing it.              |
+-------------------------+------------------+------------------+-----------------------------+----------------------------+

.. code-block:: xml
   :linenos:

   <StreetSegment id="1210001">
      <StartHouseNumber>1</StartHouseNumber>
      <EndHouseNumber>10</EndHouseNumber>
      <OddEvenBoth>both</OddEvenBoth>
      <NonHouseAddress>
        <StreetDirection>E</StreetDirection>
	<StreetName>Guinevere</StreetName>
	<StreetSuffix>Dr</StreetSuffix>
	<AddressDirection>SE</AddressDirection>
	<State>VA</State>
	<City>Annandale</City>
	<Zip>22003</Zip>
      </NonHouseAddress>
      <PrecinctId>10101</PrecinctId>
   </StreetSegment>
