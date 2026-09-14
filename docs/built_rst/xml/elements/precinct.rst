.. This file is auto-generated.  Do not edit it by hand!

.. _multi-xml-precinct:

Precinct
========

The Precinct object represents a voting precinct or precinct split within a Locality.

In overlay feeds, clearable fields can be cleared using ``<Clear{FieldName}/>`` (e.g. ``<ClearBallotStyleId/>``, ``<ClearPollingLocationIds/>``, ``<ClearIsInactive/>``). LocalityId and Name are optional in overlays. EmergencyNotice is permitted only in overlays.

+----------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                  | Data Type                            | Required?    | Repeats?     | Description                              | Error Handling                           |
+======================+======================================+==============+==============+==========================================+==========================================+
| BallotStyleId        | ``xs:IDREF``                         | Optional     | Single       | Links to the                             | If the field is invalid or not present,  |
|                      |                                      |              |              | :ref:`multi-xml-ballot-style` voted by   | then the implementation is required to   |
|                      |                                      |              |              | electors in this precinct. Clearable in  | ignore it.                               |
|                      |                                      |              |              | overlays.                                |                                          |
+----------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ElectoralDistrictIds | ``xs:IDREFS``                        | Optional     | Single       | Links to the                             | If the field is invalid or not present,  |
|                      |                                      |              |              | :ref:`multi-xml-electoral-district`      | then the implementation is required to   |
|                      |                                      |              |              | elements containing this precinct.       | ignore it.                               |
|                      |                                      |              |              | Clearable in overlays.                   |                                          |
+----------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ExternalIdentifier   | :ref:`multi-xml-external-identifier` | Optional     | Repeats      | External identifier(s) linking this      | If the element is invalid or not         |
|                      |                                      |              |              | precinct to other datasets (e.g.         | present, then the implementation is      |
|                      |                                      |              |              | OCD-ID). Clearable in overlays.          | required to ignore it.                   |
+----------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IsMailOnly           | ``xs:boolean``                       | Optional     | Single       | Specifies if this precinct conducts      | If the field is missing or invalid, the  |
|                      |                                      |              |              | mail-only elections. Clearable in        | implementation is required to assume     |
|                      |                                      |              |              | overlays.                                | IsMailOnly is false.                     |
+----------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| LocalityId           | ``xs:IDREF``                         | **Required** | Single       | References the containing                | If LocalityId is invalid or not present, |
|                      |                                      |              |              | :ref:`multi-xml-locality`. Required in   | the implementation is required to ignore |
|                      |                                      |              |              | main feed; optional in overlays.         | the Precinct containing it.              |
+----------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Name                 | ``xs:string``                        | **Required** | Single       | Name of the precinct. Required in main   | If Name is invalid or not present, the   |
|                      |                                      |              |              | feed; optional in overlays.              | implementation is required to ignore the |
|                      |                                      |              |              |                                          | Precinct containing it.                  |
+----------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Number               | ``xs:string``                        | Optional     | Single       | Precinct number or code. Clearable in    | If the field is invalid or not present,  |
|                      |                                      |              |              | overlays.                                | then the implementation is required to   |
|                      |                                      |              |              |                                          | ignore it.                               |
+----------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PollingLocationIds   | ``xs:IDREFS``                        | Optional     | Single       | Links to polling locations serving this  | If the field is invalid or not present,  |
|                      |                                      |              |              | precinct. Clearable in overlays.         | then the implementation is required to   |
|                      |                                      |              |              |                                          | ignore it.                               |
+----------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PrecinctSplitName    | ``xs:string``                        | Optional     | Single       | Sub-identifier for precinct splits.      | If the field is invalid or not present,  |
|                      |                                      |              |              | Clearable in overlays.                   | then the implementation is required to   |
|                      |                                      |              |              |                                          | ignore it.                               |
+----------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| SpatialBoundary      | :ref:`multi-xml-spatial-boundary`    | Optional     | Single       | Geospatial boundary defining the         | If the element is invalid or not         |
|                      |                                      |              |              | precinct polygon. Clearable in overlays. | present, then the implementation is      |
|                      |                                      |              |              |                                          | required to ignore it.                   |
+----------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Ward                 | ``xs:string``                        | Optional     | Single       | Ward identifier if applicable. Clearable | If the field is invalid or not present,  |
|                      |                                      |              |              | in overlays.                             | then the implementation is required to   |
|                      |                                      |              |              |                                          | ignore it.                               |
+----------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| EmergencyNotice      | :ref:`multi-xml-emergency-notice`    | Optional     | Repeats      | Emergency notice specific to this        | If the element is invalid or not         |
|                      |                                      |              |              | precinct. Permitted only in feed         | present, then the implementation is      |
|                      |                                      |              |              | overlays.                                | required to ignore it.                   |
+----------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IsInactive           | ``xs:string``                        | Optional     | Single       | If specified, marks the precinct as      | If the field is invalid or not present,  |
|                      |                                      |              |              | inactive, stating the reason why.        | then the implementation is required to   |
|                      |                                      |              |              | Clearable in overlays.                   | ignore it.                               |
+----------------------+--------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

   <Precinct id="pre90111">
      <BallotStyleId>bs00010</BallotStyleId>
      <ElectoralDistrictIds>ed60129 ed60311</ElectoralDistrictIds>
      <IsMailOnly>false</IsMailOnly>
      <LocalityId>loc70001</LocalityId>
      <Name>203 - GEORGETOWN</Name>
      <Number>0203</Number>
      <PollingLocationIds>pl00001</PollingLocationIds>
   </Precinct>


.. _multi-xml-spatial-boundary:

SpatialBoundary
---------------

The ``SpatialBoundary`` object defines a boundary in space. This boundary is usually defined by one or more discrete, closed polygonal shapes.

+---------------------------+----------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                       | Data Type                                    | Required?    | Repeats?     | Description                              | Error Handling                           |
+===========================+==============================================+==============+==============+==========================================+==========================================+
| ExternalGeospatialFeature | :ref:`multi-xml-external-geospatial-feature` | **Required** | Single       | The spatial boundary defined by a        | If the element is invalid, then the      |
|                           |                                              |              |              | geospatial feature that is external to   | implementation is required to ignore the |
|                           |                                              |              |              | the VIP feed.                            | ``SpatialBoundary`` element containing   |
|                           |                                              |              |              |                                          | it.                                      |
+---------------------------+----------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

    <SpatialBoundary>
      <ExternalGeospatialFeature>
        <ExternalFileId>ef1</ExternalFileId>
        <FileFormat>shp</FileFormat>
        <FeatureIdentifier>
          <Index>3</Index>
        </FeatureIdentifier>
      </ExternalGeospatialFeature>
    </SpatialBoundary>


.. _multi-xml-external-geospatial-feature:

ExternalGeospatialFeature
~~~~~~~~~~~~~~~~~~~~~~~~~

The ``ExternalGeospatialFeature`` object contains a reference to a geospatial feature (one or more shapes) contained in a separate file external to the VIP feed.

+-------------------+-------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag               | Data Type                           | Required?    | Repeats?     | Description                              | Error Handling                           |
+===================+=====================================+==============+==============+==========================================+==========================================+
| ExternalFileId    | ``xs:IDREF``                        | **Required** | Single       | Links to the                             | If the field is invalid, then the        |
|                   |                                     |              |              | :ref:`multi-xml-external-file`           | implementation is required to ignore the |
|                   |                                     |              |              | containing the geospatial shape(s) that  | ``ExternalGeospatialFeature`` element    |
|                   |                                     |              |              | define the feature's boundary.           | containing it.                           |
+-------------------+-------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| FileFormat        | :ref:`multi-xml-geospatial-format`  | **Required** | Single       | The format of the geospatial file.       | If the field is invalid, then the        |
|                   |                                     |              |              |                                          | implementation is required to ignore the |
|                   |                                     |              |              |                                          | ``ExternalGeospatialFeature`` element    |
|                   |                                     |              |              |                                          | containing it.                           |
+-------------------+-------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| FeatureIdentifier | :ref:`multi-xml-feature-identifier` | **Required** | Repeats      | Identifiers indicating which specific    | If the element is invalid, then the      |
|                   |                                     |              |              | shape(s) to use from the geospatial      | implementation is required to ignore the |
|                   |                                     |              |              | file. These refer to identifiers within  | ``ExternalGeospatialFeature`` element    |
|                   |                                     |              |              | the referenced external file. This is a  | containing it.                           |
|                   |                                     |              |              | repeated field in the XML specification, |                                          |
|                   |                                     |              |              | but a scalar field in the CSV            |                                          |
|                   |                                     |              |              | specification. If more than one          |                                          |
|                   |                                     |              |              | identifier is required with the CSV      |                                          |
|                   |                                     |              |              | specifiation, multiple values can be     |                                          |
|                   |                                     |              |              | provided by delimited by space.          |                                          |
+-------------------+-------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _multi-xml-feature-identifier:

FeatureIdentifier
^^^^^^^^^^^^^^^^^

+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type     | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+===============+==============+==============+==========================================+==========================================+
| Index        | ``xs:string`` | **Required** | Single       | The index value for the shapefile        | If the Index field is invalid or not     |
|              |               |              |              | feature.                                 | present, the implementation is required  |
|              |               |              |              |                                          | to ignore the FeatureIdentifier          |
|              |               |              |              |                                          | containing it.                           |
+--------------+---------------+--------------+--------------+------------------------------------------+------------------------------------------+
