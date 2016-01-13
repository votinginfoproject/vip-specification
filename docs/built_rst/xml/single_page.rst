.. This file is auto-generated.  Do not edit it by hand!

.. _single-xml:

XML Elements & Enumerations (Single Page)
=========================================


.. _single-xml-elements:

Elements
--------


.. _single-xml-ballot-measure-contest:

BallotMeasureContest
~~~~~~~~~~~~~~~~~~~~

The BallotMeasureContest provides information about a ballot measure before the voters, including
summary statements on each side. Extends :doc:`ContestBase <contest_base>`.

+------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag              | Data Type                              | Required?    | Repeats?     | Description                              | Error Handling                           |
+==================+========================================+==============+==============+==========================================+==========================================+
| ConStatement     | :doc:`InternationalizedText            | Optional     | Single       | Specifies a statement in opposition to   | If the element is invalid or not         |
|                  | <internationalized_text>`              |              |              | the referendum. It does not necessarily  | present, then the implementation is      |
|                  |                                        |              |              | appear on the ballot.                    | required to ignore it.                   |
+------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| EffectOfAbstain  | :doc:`InternationalizedText            | Optional     | Single       | Specifies what effect abstaining (i.e.   | If the element is invalid or not         |
|                  | <internationalized_text>`              |              |              | not voting) on this proposition will     | present, then the implementation is      |
|                  |                                        |              |              | have (i.e. whether abstaining is         | required to ignore it.                   |
|                  |                                        |              |              | considered a vote against it).           |                                          |
+------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| FullText         | :doc:`InternationalizedText            | Optional     | Single       | Specifies the full text of the           | If the element is invalid or not         |
|                  | <internationalized_text>`              |              |              | referendum as it appears on the ballot.  | present, then the implementation is      |
|                  |                                        |              |              |                                          | required to ignore it.                   |
+------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| InfoUri          | xs:anyURI                              | Optional     | Single       | Specifies a URI that links to additional | If the field is invalid or not present,  |
|                  |                                        |              |              | information about the referendum.        | then the implementation is required to   |
|                  |                                        |              |              |                                          | ignore it.                               |
+------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PassageThreshold | :doc:`InternationalizedText            | Optional     | Single       | Specifies the threshold of votes that    | If the element is invalid or not         |
|                  | <internationalized_text>`              |              |              | the referendum needs in order to pass.   | present, then the implementation is      |
|                  |                                        |              |              | The default is a simple majority (i.e.   | required to ignore it.                   |
|                  |                                        |              |              | 50% plus one vote). Other common         |                                          |
|                  |                                        |              |              | thresholds are "three-fifths" and        |                                          |
|                  |                                        |              |              | "two-thirds". If there are `competing    |                                          |
|                  |                                        |              |              | initiatives`_, information about their   |                                          |
|                  |                                        |              |              | effect on the passage of the             |                                          |
|                  |                                        |              |              | BallotMeasureContest would go here.      |                                          |
+------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ProStatement     | :doc:`InternationalizedText            | Optional     | Single       | Specifies a statement in favor of the    | If the element is invalid or not         |
|                  | <internationalized_text>`              |              |              | referendum. It does not necessarily      | present, then the implementation is      |
|                  |                                        |              |              | appear on the ballot.                    | required to ignore it.                   |
+------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| SummaryText      | :doc:`InternationalizedText            | Optional     | Single       | Specifies a short summary of the         | If the element is invalid or not         |
|                  | <internationalized_text>`              |              |              | referendum that is on the ballot, below  | present, then the implementation is      |
|                  |                                        |              |              | the title, but above the text.           | required to ignore it.                   |
+------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Type             | :doc:`BallotMeasureType                | Optional     | Single       | Specifies the particular type of ballot  | If the field is invalid or not present,  |
|                  | <../enumerations/ballot_measure_type>` |              |              | measure. Must be one of the valid        | then the implementation is required to   |
|                  |                                        |              |              | :doc:`BallotMeasureType                  | ignore it.                               |
|                  |                                        |              |              | <../enumerations/ballot_measure_type>`   |                                          |
|                  |                                        |              |              | options.                                 |                                          |
+------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OtherType        | xs:string                              | Optional     | Single       | Allows for cataloging a new              | If the field is invalid or not present,  |
|                  |                                        |              |              | :doc:`BallotMeasureType                  | then the implementation is required to   |
|                  |                                        |              |              | <../enumerations/ballot_measure_type>`   | ignore it.                               |
|                  |                                        |              |              | option, when Type is specified as        |                                          |
|                  |                                        |              |              | "other."                                 |                                          |
+------------------+----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

   <BallotMeasureContest id="bmc30001">
      <BallotSelectionId>bms30001a</BallotSelectionId>
      <BallotSelectionId>bms30001b</BallotSelectionId>
      <BallotTitle>
         <Text language="en">State of the State</Text>
         <Text language="es">Estado del Estado.</Text>
      </BallotTitle>
      <ElectoralDistrictId>ed60129</ElectoralDistrictId>
      <Name>Referendum on Virginia</Name>
      <ConStatement label="bmc30001con">
         <Text language="en">This is no good.</Text>
         <Text language="es">Esto no es bueno.</Text>
      </ConStatement>
      <EffectOfAbstain label="bmc30001abs">
         <Text language="en">Nothing will happen.</Text>
         <Text language="es">Nada pasará.</Text>
      </EffectOfAbstain>
      <ProStatement label="bmc30001pro">
         <Text language="en">Everything will be great.</Text>
         <Text language="es">Todo va a estar bien.</Text>
      </ProStatement>
      <Type>referendum</Type>
   </BallotMeasureContest>

.. _competing initiatives: http://ballotpedia.org/Laws_governing_the_initiative_process_in_California#Competing_initiatives


.. _single-xml-ballot-measure-selection:

BallotMeasureSelection
~~~~~~~~~~~~~~~~~~~~~~

Represents the possible selection (e.g. yes/no, recall/do not recall, et al) for a
:doc:`BallotMeasureContest <ballot_measure_contest>` that would appear on the ballot.
BallotMeasureSelection extends :doc:`BallotSelectionBase <ballot_selection_base>`.

+--------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type                   | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+=============================+==============+==============+==========================================+==========================================+
| Selection    | :doc:`InternationalizedText | **Required** | Single       | Selection text for a                     | If the element is invalid or not         |
|              | <internationalized_text>`   |              |              | :doc:`BallotMeasureContest               | present, the implementation is required  |
|              |                             |              |              | <ballot_measure_contest>`                | to ignore the BallotMeasureSelection     |
|              |                             |              |              |                                          | containing it.                           |
+--------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

   <BallotMeasureSelection id="bms30001a">
      <Selection label="bms30001at">
         <Text language="en">Yes</Text>
         <Text language="es">Sí</Text>
      </Selection>
   </BallotMeasureSelection>
   <BallotMeasureSelection id="bms30001b">
      <Selection label="bms30001bt">
         <Text language="en">No</Text>
         <Text language="es">No</Text>
      </Selection>
   </BallotMeasureSelection>


.. _single-xml-ballot-selection-base:

BallotSelectionBase
~~~~~~~~~~~~~~~~~~~

A base model for all ballot selection types:
:doc:`BallotMeasureSelection <ballot_measure_selection>`,
:doc:`CandidateSelection <candidate_selection>`, and :doc:`PartySelection <party_selection>`.
Besides an id attribute, it has no additional fields.


.. _single-xml-ballot-style:

BallotStyle
~~~~~~~~~~~

A container for the contests/measures on the ballot.

+------------------+--------------+--------------+--------------+--------------------------------------------+------------------------------------------+
| Tag              | Data Type    | Required?    | Repeats?     | Description                                | Error Handling                           |
+==================+==============+==============+==============+============================================+==========================================+
| ImageUri         | xs:anyURI    | Optional     | Single       | Specifies a URI that returns an image of   | If the field is invalid or not present,  |
|                  |              |              |              | the sample ballot.                         | then the implementation is required to   |
|                  |              |              |              |                                            | ignore it.                               |
+------------------+--------------+--------------+--------------+--------------------------------------------+------------------------------------------+
| OrderedContestId | xs:IDREF     | Optional     | Repeats      | Reference to an :doc:`OrderedContest       | If the field is invalid or not present,  |
|                  |              |              |              | </built_rst/xml/elements/ordered_contest>` | then the implementation is required to   |
|                  |              |              |              |                                            | ignore it.                               |
+------------------+--------------+--------------+--------------+--------------------------------------------+------------------------------------------+
| PartyId          | xs:IDREF     | Optional     | Repeats      | Reference to a :doc:`Party <party>`.       | If the field is invalid or not present,  |
|                  |              |              |              |                                            | then the implementation is required to   |
|                  |              |              |              |                                            | ignore it.                               |
+------------------+--------------+--------------+--------------+--------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

   <BallotStyle id="bs00000">
      <OrderedContestId>oc20003</OrderedContestId>
      <OrderedContestId>oc20004</OrderedContestId>
      <OrderedContestId>oc20005</OrderedContestId>
      <OrderedContestId>oc20025</OrderedContestId>
      <OrderedContestId>oc20355</OrderedContestId>
      <OrderedContestId>oc20449</OrderedContestId>
   </BallotStyle>


.. _single-xml-candidate:

Candidate
~~~~~~~~~

The Candidate object represents a candidate in a contest. If a candidate is running in multiple contests, the same
Candidate object may be used.

+---------------------+---------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                 | Data Type                                         | Required?    | Repeats?     | Description                              | Error Handling                           |
+=====================+===================================================+==============+==============+==========================================+==========================================+
| BallotName          | :doc:`InternationalizedText                       | **Required** | Single       | The candidate's name as it will be       | If the element is invalid or not         |
|                     | <internationalized_text>`                         |              |              | displayed on the official ballot (e.g.   | present, then the implementation is      |
|                     |                                                   |              |              | "Ken T. Cuccinelli II").                 | required to ignore the Candidate element |
|                     |                                                   |              |              |                                          | containing it.                           |
+---------------------+---------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ExternalIdentifiers | :doc:`ExternalIdentifiers                         | Optional     | Single       | Another identifier for a candidate that  | If the element is invalid or not         |
|                     | </built_rst/xml/elements/external_identifiers>`   |              |              | links to another source of information   | present, then the implementation is      |
|                     |                                                   |              |              | (e.g. a campaign committee ID that links | required to ignore it.                   |
|                     |                                                   |              |              | to a campaign finance system).           |                                          |
+---------------------+---------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| FileDate            | xs:date                                           | Optional     | Single       | Date when the candidate filed for the    | If the field is invalid or not present,  |
|                     |                                                   |              |              | contest.                                 | then the implementation is required to   |
|                     |                                                   |              |              |                                          | ignore it.                               |
+---------------------+---------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IsIncumbent         | xs:boolean                                        | Optional     | Single       | Indicates whether the candidate is the   | If the field is invalid or not present,  |
|                     |                                                   |              |              | incumbent for the office associated with | then the implementation is required to   |
|                     |                                                   |              |              | the contest.                             | ignore it.                               |
+---------------------+---------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IsTopTicket         | xs:boolean                                        | Optional     | Single       | Indicates whether the candidate is the   | If the field is invalid or not present,  |
|                     |                                                   |              |              | top of a ticket that includes multiple   | then the implementation is required to   |
|                     |                                                   |              |              | candidates.                              | ignore it.                               |
+---------------------+---------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PartyId             | xs:IDREF                                          | Optional     | Single       | Reference to a :doc:`Party <party>`      | If the field is invalid or not present,  |
|                     |                                                   |              |              | element with additional information      | then the implementation is required to   |
|                     |                                                   |              |              | about the candidate's affiliated party.  | ignore it.                               |
+---------------------+---------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PersonId            | xs:IDREF                                          | Optional     | Single       | Reference to a :doc:`Person <person>`    | If the field is invalid or not present,  |
|                     |                                                   |              |              | element with additional information      | then the implementation is required to   |
|                     |                                                   |              |              | about the candidate.                     | ignore it.                               |
+---------------------+---------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PostElectionStatus  | :doc:`CandidatePostElectionStatus                 | Optional     | Single       | Final status of the candidate (e.g.      | If the field is invalid or not present,  |
|                     | <../enumerations/candidate_post_election_status>` |              |              | winner, withdrawn, etc...).              | then the implementation is required to   |
|                     |                                                   |              |              |                                          | ignore it.                               |
+---------------------+---------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PreElectionStatus   | :doc:`CandidatePreElectionStatus                  | Optional     | Single       | Registration status of the candidate     | If the field is invalid or not present,  |
|                     | <../enumerations/candidate_pre_election_status>`  |              |              | (e.g. filed, qualified, etc...).         | then the implementation is required to   |
|                     |                                                   |              |              |                                          | ignore it.                               |
+---------------------+---------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| SequenceOrder       | xs:integer                                        | Optional     | Single       | The order in which the candidate can be  | If the field is invalid or not present,  |
|                     |                                                   |              |              | listed on the ballot or in results.      | then the implementation is required to   |
|                     |                                                   |              |              |                                          | ignore it.                               |
+---------------------+---------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

   <Candidate id="can10961">
      <BallotName>
        <Text language="en">Ken T. Cuccinelli II</Text>
      </BallotName>
      <PartyId>par0001</PartyId>
      <PersonId>per10961</PersonId>
   </Candidate>


.. _single-xml-candidate-contest:

CandidateContest
~~~~~~~~~~~~~~~~

CandidateContest extends :doc:`ContestBase <contest_base>` and represents a contest among
candidates.

+----------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag            | Data Type    | Required?    | Repeats?     | Description                              | Error Handling                           |
+================+==============+==============+==============+==========================================+==========================================+
| NumberElected  | xs:integer   | Optional     | Single       | Number of candidates that are elected in | If the field is invalid or not present,  |
|                |              |              |              | the contest (i.e. "N" of N-of-M).        | then the implementation is required to   |
|                |              |              |              |                                          | ignore it.                               |
+----------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OfficeId       | xs:IDREF     | Optional     | Repeats      | References an :doc:`Office <office>`     | If the field is invalid or not present,  |
|                |              |              |              | element, if available, which gives       | then the implementation is required to   |
|                |              |              |              | additional information about the office. | ignore it.                               |
+----------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PrimaryPartyId | xs:IDREF     | Optional     | Single       | References a :doc:`Party <party>`        | If the field is invalid or not present,  |
|                |              |              |              | element, if the contest is related to a  | then the implementation is required to   |
|                |              |              |              | particular party.                        | ignore it.                               |
+----------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| VotesAllowed   | xs:integer   | Optional     | Single       | Maximum number of votes/write-ins per    | If the field is invalid or not present,  |
|                |              |              |              | voter in this contest.                   | then the implementation is required to   |
|                |              |              |              |                                          | ignore it.                               |
+----------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

   <CandidateContest id="cc20003">
      <BallotSelectionId>cs10961</BallotSelectionId>
      <BallotSelectionId>cs10962</BallotSelectionId>
      <BallotSelectionId>cs10963</BallotSelectionId>
      <BallotTitle>
        <Text language="en">Governor of Virginia</Text>
      </BallotTitle>
      <ElectoralDistrictId>ed60129</ElectoralDistrictId>
      <Name>Governor</Name>
      <NumberElected>1</NumberElected>
      <OfficeId>off0000</OfficeId>
      <VotesAllowed>1</VotesAllowed>
   </CandidateContest>


.. _single-xml-candidate-selection:

CandidateSelection
~~~~~~~~~~~~~~~~~~

CandidateSelection extends :doc:`BallotSelectionBase <ballot_selection_base>` and represents a
ballot selection for a candidate contest.

+--------------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                | Data Type    | Required?    | Repeats?     | Description                              | Error Handling                           |
+====================+==============+==============+==============+==========================================+==========================================+
| CandidateId        | xs:IDREF     | Optional     | Repeats      | References a :doc:`Candidate             | If the field is invalid or not present,  |
|                    |              |              |              | <candidate>` element. The number of      | then the implementation is required to   |
|                    |              |              |              | candidates that can be references is     | ignore it.                               |
|                    |              |              |              | unbounded in cases where the ballot      |                                          |
|                    |              |              |              | selection is for a ticket (e.g.          |                                          |
|                    |              |              |              | "President/Vice President", "Governor/Lt |                                          |
|                    |              |              |              | Governor").                              |                                          |
+--------------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| EndorsementPartyId | xs:IDREF     | Optional     | Repeats      | References a :doc:`Party <party>`        | If the field is invalid or not present,  |
|                    |              |              |              | element, which signifies one or more     | then the implementation is required to   |
|                    |              |              |              | endorsing parties for the candidate(s).  | ignore it.                               |
+--------------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IsWriteIn          | xs:boolean   | Optional     | Single       | Signifies if the particular ballot       | If the field is invalid or not present,  |
|                    |              |              |              | selection allows for write-in            | then the implementation is required to   |
|                    |              |              |              | candidates. If true, one or more         | ignore it.                               |
|                    |              |              |              | write-in candidates are allowed for this |                                          |
|                    |              |              |              | contest.                                 |                                          |
+--------------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

   <CandidateSelection id="cs10861">
      <CandidateId>can10861a</CandidateId>
      <CandidateId>can10861b</CandidateId>
      <EndorsementPartyId>par0001</EndorsementPartyId>
   </CandidateSelection>


.. _single-xml-contact-information:

ContactInformation
~~~~~~~~~~~~~~~~~~

For defining contact information about objects such as persons, boards of authorities,
organizations, etc. ContactInformation is always a sub-element of another object (e.g.
:doc:`ElectionAdministration <election_administration>`, :doc:`Office <office>`,
:doc:`Person <person>`, :doc:`Source <source>`). ContactInformation has an optional attribute
``label``, which allows the feed to refer back to the original label for the information
(e.g. if the contact information came from a CSV, ``label`` may refer to a row ID).

+------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag              | Data Type                   | Required?    | Repeats?     | Description                              | Error Handling                           |
+==================+=============================+==============+==============+==========================================+==========================================+
| AddressLine      | xs:string                   | Optional     | Repeats      | The "location" portion of a mailing      | If the field is invalid or not present,  |
|                  |                             |              |              | address. `See usage note.`_              | then the implementation is required to   |
|                  |                             |              |              |                                          | ignore it.                               |
+------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Email            | xs:string                   | Optional     | Repeats      | An email address for the contact.        | If the field is invalid or not present,  |
|                  |                             |              |              |                                          | then the implementation is required to   |
|                  |                             |              |              |                                          | ignore it.                               |
+------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Fax              | xs:string                   | Optional     | Repeats      | A fax line for the contact.              | If the field is invalid or not present,  |
|                  |                             |              |              |                                          | then the implementation is required to   |
|                  |                             |              |              |                                          | ignore it.                               |
+------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Hours            | :doc:`InternationalizedText | Optional     | Single       | Contains the hours (in local time) that  | If the element is invalid or not         |
| **[deprecated]** | <internationalized_text>`   |              |              | the location is open *(NB: this element  | present, then the implementation is      |
|                  |                             |              |              | is deprecated in favor of the more       | required to ignore it.                   |
|                  |                             |              |              | structured :doc:`HoursOpen <hours_open>` |                                          |
|                  |                             |              |              | element. It is strongly encouraged that  |                                          |
|                  |                             |              |              | data providers move toward contributing  |                                          |
|                  |                             |              |              | hours in this format)*.                  |                                          |
+------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| HoursOpenId      | xs:IDREF                    | Optional     | Single       | References an :doc:`HoursOpen            | If the field is invalid or not present,  |
|                  |                             |              |              | <hours_open>` element, which lists the   | then the implementation is required to   |
|                  |                             |              |              | hours of operation for a location.       | ignore it.                               |
+------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Name             | xs:string                   | Optional     | Single       | The name of the location or contact.     | If the field is invalid or not present,  |
|                  |                             |              |              | `See usage note.`_                       | then the implementation is required to   |
|                  |                             |              |              |                                          | ignore it.                               |
+------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Phone            | xs:string                   | Optional     | Repeats      | A phone number for the contact.          | If the field is invalid or not present,  |
|                  |                             |              |              |                                          | then the implementation is required to   |
|                  |                             |              |              |                                          | ignore it.                               |
+------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Uri              | xs:anyURI                   | Optional     | Repeats      | An informational URI for the contact or  | If the field is invalid or not present,  |
|                  |                             |              |              | location.                                | then the implementation is required to   |
|                  |                             |              |              |                                          | ignore it.                               |
+------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. _See usage note.:

``Name`` and ``AddressLine`` Usage Note
---------------------------------------

The ``Name`` and ``AddressLine`` fields should be chosen so that a display
or mailing address can be constructed programmatically by joining the
``Name`` and ``AddressLine`` fields together.  For example, for the
following address::

    Department of Elections
    1 Dr. Carlton B. Goodlett Place, Room 48
    San Francisco, CA 94102

The name could be "Department of Elections" and the first address line
could be "1 Dr. Carlton B. Goodlett Place, Room 48."

However, VIP does not yet support the representation of mailing addresses
whose "name" portion spans more than one line, for example::

    California Secretary of State
    Elections Division
    1500 11th Street
    Sacramento, CA 95814

For addresses like the above, we recommend choosing a name like, "California
Secretary of State, Elections Division" with "1500 11th Street" as the
first address line. This would result in a programmatically constructed
address like the following::

    California Secretary of State, Elections Division
    1500 11th Street
    Sacramento, CA 95814

.. code-block:: xml
   :linenos:

   <ContactInformation label="ci10861a">
      <AddressLine>1600 Pennsylvania Ave</AddressLine>
      <AddressLine>Washington, DC 20006</AddressLine>
      <Email>president@whitehouse.gov</Email>
      <Phone>202-456-1111</Phone>
      <Phone annotation="TDD">202-456-6213</Phone>
      <Uri>http://www.whitehouse.gov</Uri>
   </ContactInformation>


.. _single-xml-contest-base:

ContestBase
~~~~~~~~~~~

A base model for all Contest types: :doc:`BallotMeasureContest <ballot_measure_contest>`,
:doc:`CandidateContest <candidate_contest>`, :doc:`PartyContest <party_contest>`,
and :doc:`RetentionContest <retention_contest>` (NB: the latter because it extends
:doc:`BallotMeasureContest <ballot_measure_contest>`).

+-------------------------+-------------------------------------------------+--------------+--------------+---------------------------------------------------+------------------------------------------+
| Tag                     | Data Type                                       | Required?    | Repeats?     | Description                                       | Error Handling                           |
+=========================+=================================================+==============+==============+===================================================+==========================================+
| Abbreviation            | xs:string                                       | Optional     | Single       | An abbreviation for the contest.                  | If the field is invalid or not present,  |
|                         |                                                 |              |              |                                                   | then the implementation should ignore    |
|                         |                                                 |              |              |                                                   | it.                                      |
+-------------------------+-------------------------------------------------+--------------+--------------+---------------------------------------------------+------------------------------------------+
| BallotSelectionId       | xs:IDREF                                        | Optional     | Repeats      | References a particular BallotSelection, which    | If the field is invalid or not present,  |
|                         |                                                 |              |              | could be of any selection type that extends       | then the implementation should ignore    |
|                         |                                                 |              |              | :doc:`BallotSelectionBase                         | it.                                      |
|                         |                                                 |              |              | </built_rst/xml/elements/ballot_selection_base>`. |                                          |
+-------------------------+-------------------------------------------------+--------------+--------------+---------------------------------------------------+------------------------------------------+
| BallotSubTitle          | :doc:`InternationalizedText                     | Optional     | Single       | Subtitle of the contest as it appears on the      | If the element is invalid or not         |
|                         | <internationalized_text>`                       |              |              | ballot.                                           | present, then the implementation should  |
|                         |                                                 |              |              |                                                   | ignore it.                               |
+-------------------------+-------------------------------------------------+--------------+--------------+---------------------------------------------------+------------------------------------------+
| BallotTitle             | :doc:`InternationalizedText                     | Optional     | Single       | Title of the contest as it appears on the ballot. | If the element is invalid or not         |
|                         | <internationalized_text>`                       |              |              |                                                   | present, then the implementation should  |
|                         |                                                 |              |              |                                                   | ignore it.                               |
+-------------------------+-------------------------------------------------+--------------+--------------+---------------------------------------------------+------------------------------------------+
| ElectoralDistrictId     | xs:IDREF                                        | Optional     | Single       | References an :doc:`ElectoralDistrict             | If the field is invalid or not present,  |
|                         |                                                 |              |              | <electoral_district>` element that represents the | then the implementation should ignore    |
|                         |                                                 |              |              | geographical scope of the contest.                | it.                                      |
+-------------------------+-------------------------------------------------+--------------+--------------+---------------------------------------------------+------------------------------------------+
| ElectorateSpecification | :doc:`InternationalizedText                     | Optional     | Single       | Specifies any changes to the eligible electorate  | If the element is invalid or not         |
|                         | <internationalized_text>`                       |              |              | for this contest past the usual, "all registered  | present, then the implementation should  |
|                         |                                                 |              |              | voters" electorate. This subtag will most often   | ignore it.                               |
|                         |                                                 |              |              | be used for primaries and local elections. In     |                                          |
|                         |                                                 |              |              | primaries, voters may have to be registered as a  |                                          |
|                         |                                                 |              |              | specific party to vote, or there may be special   |                                          |
|                         |                                                 |              |              | rules for which ballot a voter can pull. In some  |                                          |
|                         |                                                 |              |              | local elections, non-citizens can vote.           |                                          |
+-------------------------+-------------------------------------------------+--------------+--------------+---------------------------------------------------+------------------------------------------+
| ExternalIdentifiers     | :doc:`ExternalIdentifiers                       | Optional     | Single       | Other identifiers for a contest that links to     | If the element is invalid or not         |
|                         | </built_rst/xml/elements/external_identifiers>` |              |              | another source of information.                    | present, then the implementation should  |
|                         |                                                 |              |              |                                                   | ignore it.                               |
+-------------------------+-------------------------------------------------+--------------+--------------+---------------------------------------------------+------------------------------------------+
| HasRotation             | xs:boolean                                      | Optional     | Single       | Indicates whether the selections in the contest   | If the field is invalid or not present,  |
|                         |                                                 |              |              | are rotated.                                      | then the implementation should ignore    |
|                         |                                                 |              |              |                                                   | it.                                      |
+-------------------------+-------------------------------------------------+--------------+--------------+---------------------------------------------------+------------------------------------------+
| Name                    | xs:string                                       | Optional     | Single       | Name of the contest, not necessarily how it       | If the field is invalid or not present,  |
|                         |                                                 |              |              | appears on the ballot (NB: BallotTitle should be  | then the implementation should ignore    |
|                         |                                                 |              |              | used for this purpose).                           | it.                                      |
+-------------------------+-------------------------------------------------+--------------+--------------+---------------------------------------------------+------------------------------------------+
| SequenceOrder           | xs:integer                                      | Optional     | Single       | Order in which the candidates are listed on the   | If the field is invalid or not present,  |
|                         |                                                 |              |              | ballot.                                           | then the implementation should ignore    |
|                         |                                                 |              |              |                                                   | it.                                      |
+-------------------------+-------------------------------------------------+--------------+--------------+---------------------------------------------------+------------------------------------------+
| VoteVariation           | :doc:`VoteVariation                             | Optional     | Single       | Vote variation associated with the contest (e.g.  | If the field is invalid or not present,  |
|                         | <../enumerations/vote_variation>`               |              |              | n-of-m, majority, et al).                         | then the implementation should ignore    |
|                         |                                                 |              |              |                                                   | it.                                      |
+-------------------------+-------------------------------------------------+--------------+--------------+---------------------------------------------------+------------------------------------------+
| OtherVoteVariation      | xs:string                                       | Optional     | Single       | If "other" is selected as the **VoteVariation**,  | If the field is invalid or not present,  |
|                         |                                                 |              |              | the name of the variation can be specified here.  | then the implementation should ignore    |
|                         |                                                 |              |              |                                                   | it.                                      |
+-------------------------+-------------------------------------------------+--------------+--------------+---------------------------------------------------+------------------------------------------+


.. _single-xml-department:

Department
~~~~~~~~~~

+--------------------------+--------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                      | Data Type                | Required?    | Repeats?     | Description                              | Error Handling                           |
+==========================+==========================+==============+==============+==========================================+==========================================+
| ContactInformation       | :doc:`ContactInformation | Optional     | Single       | Contact and physical address information | If the element is invalid or not         |
|                          | <contact_information>`   |              |              | for the election administration body     | present, then the implementation is      |
|                          |                          |              |              | (see :doc:`ContactInformation            | required to ignore it.                   |
|                          |                          |              |              | <contact_information>`).                 |                                          |
+--------------------------+--------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ElectionOfficialPersonId | xs:IDREF                 | Optional     | Single       | The individual to contact at the         | If the field is invalid or not present,  |
|                          |                          |              |              | election administration office. The      | then the implementation is required to   |
|                          |                          |              |              | specified person should be the           | ignore it.                               |
|                          |                          |              |              | :doc:`election official <person>`.       |                                          |
+--------------------------+--------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| VoterService             | :ref:`VoterService       | Optional     | Repeats      | The types of services and appropriate    | If the element is invalid or not         |
|                          | <ea-dep-voter-service>`  |              |              | contact individual available to voters.  | present, then the implementation is      |
|                          |                          |              |              |                                          | required to ignore it.                   |
+--------------------------+--------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. _ea-dep-voter-service:


.. _single-xml-election:

Election
~~~~~~~~

The Election object represents an Election Day, which usually consists of many individual contests
and/or referenda. A feed must contain **exactly one** Election object. All relationships in the
feed (e.g., street segment to precinct to polling location) are assumed to relate only to
the Election specified by this object. It is permissible, and recommended, to combine unrelated
contests (e.g., a special election and a general election) that occur on the same day into one feed
with one Election object.

+----------------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                        | Data Type                   | Required?    | Repeats?     | Description                              | Error Handling                           |
+============================+=============================+==============+==============+==========================================+==========================================+
| Date                       | xs:date                     | **Required** | Single       | Specifies when the election is being     | If the field is invalid, then the        |
|                            |                             |              |              | held. The `Date` is considered to be in  | implementation is required to ignore the |
|                            |                             |              |              | the timezone local to the state holding  | ``Election`` element containing it.      |
|                            |                             |              |              | the election.                            |                                          |
+----------------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ElectionType               | :doc:`InternationalizedText | Optional     | Single       | Specifies the highest controlling        | If the element is invalid or not         |
|                            | <internationalized_text>`   |              |              | authority for election (e.g., federal,   | present, then the implementation is      |
|                            |                             |              |              | state, county, city, town, etc.)         | required to ignore it.                   |
+----------------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| StateId                    | xs:IDREF                    | **Required** | Single       | Specifies a link to the `State` element  | If the field is invalid, then the        |
|                            |                             |              |              | where the election is being held.        | implementation is required to ignore the |
|                            |                             |              |              |                                          | ``Election`` element containing it.      |
+----------------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IsStatewide                | xs:boolean                  | Optional     | Single       | Indicates whether the election is        | If the field is not present or invalid,  |
|                            |                             |              |              | statewide.                               | the implementation is required to        |
|                            |                             |              |              |                                          | default to "yes".                        |
+----------------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Name                       | :doc:`InternationalizedText | Optional     | Single       | The name for the election (**NB:** while | If the element is invalid or not         |
|                            | <internationalized_text>`   |              |              | optional, this element is highly         | present, then the implementation is      |
|                            |                             |              |              | recommended).                            | required to ignore it.                   |
+----------------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| RegistrationInfo           | :doc:`InternationalizedText | Optional     | Single       | Specifies information about registration | If the element is invalid or not         |
|                            | <internationalized_text>`   |              |              | for this election either as text or a    | present, then the implementation is      |
|                            |                             |              |              | URI.                                     | required to ignore it.                   |
+----------------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| AbsenteeBallotInfo         | :doc:`InternationalizedText | Optional     | Single       | Specifies information about requesting   | If the element is invalid or not         |
|                            | <internationalized_text>`   |              |              | absentee ballots either as text or a URI | present, then the implementation is      |
|                            |                             |              |              |                                          | required to ignore it.                   |
+----------------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ResultsUri                 | xs:anyURI                   | Optional     | Single       | Contains a URI where results for the     | If the field is invalid or not present,  |
|                            |                             |              |              | election may be found                    | then the implementation is required to   |
|                            |                             |              |              |                                          | ignore it.                               |
+----------------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PollingHours               | :doc:`InternationalizedText | Optional     | Single       | Contains the hours (in local time) that  | If the element is invalid or not         |
| **[deprecated]**           | <internationalized_text>`   |              |              | Election Day polling locations are open. | present, then the implementation is      |
|                            |                             |              |              | If polling hours differ in specific      | required to ignore it.                   |
|                            |                             |              |              | polling locations, alternative hours may |                                          |
|                            |                             |              |              | be specified in the                      |                                          |
|                            |                             |              |              | :doc:`PollingLocation                    |                                          |
|                            |                             |              |              | <polling_location>` object *(NB: this    |                                          |
|                            |                             |              |              | element is deprecated in favor of the    |                                          |
|                            |                             |              |              | more structured :doc:`HoursOpen          |                                          |
|                            |                             |              |              | <hours_open>` element. It is strongly    |                                          |
|                            |                             |              |              | encouraged that data providers move      |                                          |
|                            |                             |              |              | toward contributing hours in this        |                                          |
|                            |                             |              |              | format)*.                                |                                          |
+----------------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| HoursOpenId                | xs:IDREF                    | Optional     | Single       | References the :doc:`HoursOpen           | If the field is invalid or not present,  |
|                            |                             |              |              | <hours_open>` element, which lists the   | then the implementation is required to   |
|                            |                             |              |              | hours of operation for polling           | ignore it.                               |
|                            |                             |              |              | locations.                               |                                          |
+----------------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| HasElectionDayRegistration | xs:boolean                  | Optional     | Single       | Specifies if a voter can register on the | If the field is invalid or not present,  |
|                            |                             |              |              | same day of the election (i.e., the last | then the implementation is required to   |
|                            |                             |              |              | day of the election). Valid items are    | ignore it.                               |
|                            |                             |              |              | "yes" and "no".                          |                                          |
+----------------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| RegistrationDeadline       | xs:date                     | Optional     | Single       | Specifies the last day to register for   | If the field is invalid or not present,  |
|                            |                             |              |              | the election with the possible exception | then the implementation is required to   |
|                            |                             |              |              | of Election Day registration.            | ignore it.                               |
+----------------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| AbsenteeRequestDeadline    | xs:date                     | Optional     | Single       | Specifies the last day to request an     | If the field is invalid or not present,  |
|                            |                             |              |              | absentee ballot.                         | then the implementation is required to   |
|                            |                             |              |              |                                          | ignore it.                               |
+----------------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

   <Election id="ele30000">
     <AbsenteeRequestDeadline>2013-10-30</AbsenteeRequestDeadline>
     <Date>2013-11-05</Date>
     <ElectionType>
       <Text language="en">General</Text>
       <Text language="es">Generales</Text>
     </ElectionType>
     <HasElectionDayRegistration>false</HasElectionDayRegistration>
     <HoursOpenId>hours0001</HoursOpenId>
     <IsStatewide>true</IsStatewide>
     <Name>
       <Text language="en">2013 Statewide General</Text>
     </Name>
     <RegistrationDeadline>2013-10-15</RegistrationDeadline>
     <ResultsUri>http://www.sbe.virginia.gov/ElectionResults.html</ResultsUri>
     <StateId>st51</StateId>
   </Election>


.. _single-xml-election-administration:

ElectionAdministration
~~~~~~~~~~~~~~~~~~~~~~

The Election Administration represents an institution for serving a locality's (or state's) election
functions.

+---------------------+------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                 | Data Type        | Required?    | Repeats?     | Description                              | Error Handling                           |
+=====================+==================+==============+==============+==========================================+==========================================+
| AbsenteeUri         | xs:anyURI        | Optional     | Single       | Specifies the web address for            | If the field is invalid or not present,  |
|                     |                  |              |              | information on absentee voting.          | then the implementation is required to   |
|                     |                  |              |              |                                          | ignore it.                               |
+---------------------+------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| AmIRegisteredUri    | xs:anyURI        | Optional     | Single       | Specifies the web address for            | If the field is invalid or not present,  |
|                     |                  |              |              | information on whether an individual is  | then the implementation is required to   |
|                     |                  |              |              | registered.                              | ignore it.                               |
+---------------------+------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Department          | :ref:`Department | **Required** | Repeats      | Describes the administrative body for a  | There must be at least one valid         |
|                     | <ea-dep>`        |              |              | particular voter service.                | `Department` in each                     |
|                     |                  |              |              |                                          | `ElectionAdministration` element. If no  |
|                     |                  |              |              |                                          | valid `Department` objects are present,  |
|                     |                  |              |              |                                          | the implementation is required to ignore |
|                     |                  |              |              |                                          | the `ElectionAdministration` object that |
|                     |                  |              |              |                                          | contains it/them.                        |
+---------------------+------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ElectionsUri        | xs:anyURI        | Optional     | Single       | Specifies web address the                | If the field is invalid or not present,  |
|                     |                  |              |              | administration's website.                | then the implementation is required to   |
|                     |                  |              |              |                                          | ignore it.                               |
+---------------------+------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| RegistrationUri     | xs:anyURI        | Optional     | Single       | Specifies web address for information on | If the field is invalid or not present,  |
|                     |                  |              |              | registering to vote.                     | then the implementation is required to   |
|                     |                  |              |              |                                          | ignore it.                               |
+---------------------+------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| RulesUri            | xs:anyURI        | Optional     | Single       | Specifies a URI for the election rules   | If the field is invalid or not present,  |
|                     |                  |              |              | and laws (if any) for the jurisdiction   | then the implementation is required to   |
|                     |                  |              |              | of the administration.                   | ignore it.                               |
+---------------------+------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| WhatIsOnMyBallotUri | xs:anyURI        | Optional     | Single       | Specifies web address for information on | If the field is invalid or not present,  |
|                     |                  |              |              | what is on an individual's ballot.       | then the implementation is required to   |
|                     |                  |              |              |                                          | ignore it.                               |
+---------------------+------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| WhereDoIVoteUri     | xs:anyURI        | Optional     | Single       | The Specifies web address for            | If the field is invalid or not present,  |
|                     |                  |              |              | information on where an individual votes | then the implementation is required to   |
|                     |                  |              |              | based on their address.                  | ignore it.                               |
+---------------------+------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. _ea-dep:


.. _single-xml-department:

Department
^^^^^^^^^^

+--------------------------+--------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                      | Data Type                | Required?    | Repeats?     | Description                              | Error Handling                           |
+==========================+==========================+==============+==============+==========================================+==========================================+
| ContactInformation       | :doc:`ContactInformation | Optional     | Single       | Contact and physical address information | If the element is invalid or not         |
|                          | <contact_information>`   |              |              | for the election administration body     | present, then the implementation is      |
|                          |                          |              |              | (see :doc:`ContactInformation            | required to ignore it.                   |
|                          |                          |              |              | <contact_information>`).                 |                                          |
+--------------------------+--------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ElectionOfficialPersonId | xs:IDREF                 | Optional     | Single       | The individual to contact at the         | If the field is invalid or not present,  |
|                          |                          |              |              | election administration office. The      | then the implementation is required to   |
|                          |                          |              |              | specified person should be the           | ignore it.                               |
|                          |                          |              |              | :doc:`election official <person>`.       |                                          |
+--------------------------+--------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| VoterService             | :ref:`VoterService       | Optional     | Repeats      | The types of services and appropriate    | If the element is invalid or not         |
|                          | <ea-dep-voter-service>`  |              |              | contact individual available to voters.  | present, then the implementation is      |
|                          |                          |              |              |                                          | required to ignore it.                   |
+--------------------------+--------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. _ea-dep-voter-service:


.. _single-xml-voter-service:

VoterService
^^^^^^^^^^^^

+--------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                      | Data Type                             | Required?    | Repeats?     | Description                              | Error Handling                           |
+==========================+=======================================+==============+==============+==========================================+==========================================+
| ContactInformation       | :doc:`ContactInformation              | Optional     | Single       | The contact for a particular voter       | If the element is invalid or not         |
|                          | <contact_information>`                |              |              | service.                                 | present, then the implementation is      |
|                          |                                       |              |              |                                          | required to ignore it.                   |
+--------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Description              | :doc:`InternationalizedText           | Optional     | Single       | Long description of the services         | If the element is invalid or not         |
|                          | <internationalized_text>`             |              |              | available.                               | present, then the implementation is      |
|                          |                                       |              |              |                                          | required to ignore it.                   |
+--------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ElectionOfficialPersonId | xs:IDREF                              | Optional     | Single       | The :doc:`authority <person>` for a      | If the field is invalid or not present,  |
|                          |                                       |              |              | particular voter service.                | then the implementation is required to   |
|                          |                                       |              |              |                                          | ignore it.                               |
+--------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Type                     | :doc:`VoterServiceType                | Optional     | Single       | The type of :doc:`voter service          | If the field is invalid or not present,  |
|                          | <../enumerations/voter_service_type>` |              |              | <../enumerations/voter_service_type>`.   | then the implementation is required to   |
|                          |                                       |              |              |                                          | ignore it.                               |
+--------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OtherType                | xs:string                             | Optional     | Single       | If Type is "other", OtherType allows for | If the field is invalid or not present,  |
|                          |                                       |              |              | cataloging another type of voter         | then the implementation is required to   |
|                          |                                       |              |              | service.                                 | ignore it.                               |
+--------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

   <ElectionAdministration id="ea40133">
      <AbsenteeUri>http://www.sbe.virginia.gov/absenteevoting.html</AbsenteeUri>
      <AmIRegisteredUri>https://www.vote.virginia.gov/</AmIRegisteredUri>
      <Department>
        <ContactInformation label="ci60000">
          <AddressLine>Washington Building First Floor</AddressLine>
          <AddressLine>1100 Bank Street</AddressLine>
          <AddressLine>Richmond, VA 23219</AddressLine>
          <Name>State Board of Elections</Name>
        </ContactInformation>
      </Department>
      <ElectionsUri>http://www.sbe.virginia.gov/</ElectionsUri>
      <RegistrationUri>https://www.vote.virginia.gov/</RegistrationUri>
      <RulesUri>http://www.sbe.virginia.gov/</RulesUri>
      <WhatIsOnMyBallotUri>https://www.vote.virginia.gov/</WhatIsOnMyBallotUri>
      <WhereDoIVoteUri>https://www.vote.virginia.gov/</WhereDoIVoteUri>
   </ElectionAdministration>


.. _single-xml-electoral-district:

ElectoralDistrict
~~~~~~~~~~~~~~~~~

The ``ElectoralDistrict`` object represents the geographic area in which contests are held. Examples
of ``ElectoralDistrict`` include: "the state of Maryland", "Virginia's 5th Congressional District",
or "Union School District". The geographic area that comprises a ``ElectoralDistrict`` is defined by
which precincts link to the ``ElectoralDistrict``.

+---------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                 | Data Type                                       | Required?    | Repeats?     | Description                              | Error Handling                           |
+=====================+=================================================+==============+==============+==========================================+==========================================+
| ExternalIdentifiers | :doc:`ExternalIdentifiers                       | Optional     | Single       | Other identifiers that link to external  | If the element is invalid or not         |
|                     | </built_rst/xml/elements/external_identifiers>` |              |              | datasets (e.g. `OCD-IDs`_)               | present, then the implementation is      |
|                     |                                                 |              |              |                                          | required to ignore it.                   |
+---------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Name                | xs:string                                       | **Required** | Single       | Specifies the electoral area's name.     | If the field is invalid or not present,  |
|                     |                                                 |              |              |                                          | then the implementation is required to   |
|                     |                                                 |              |              |                                          | ignore the ``ElectoralDistrict`` object  |
|                     |                                                 |              |              |                                          | containing it.                           |
+---------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Number              | xs:integer                                      | Optional     | Single       | Specifies the district number of the     | If the field is invalid or not present,  |
|                     |                                                 |              |              | district (e.g. 34, in the case of the    | then the implementation is required to   |
|                     |                                                 |              |              | 34th State Senate District). If a number | ignore it.                               |
|                     |                                                 |              |              | is not applicable, instead of leaving    |                                          |
|                     |                                                 |              |              | the field blank, leave this field out of |                                          |
|                     |                                                 |              |              | the object; empty strings are not valid  |                                          |
|                     |                                                 |              |              | for xs:integer fields.                   |                                          |
+---------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Type                | :doc:`DistrictType                              | **Required** | Single       | Specifies the type of electoral area.    | If the field is invalid or not present,  |
|                     | <../enumerations/district_type>`                |              |              |                                          | then the implementation is required to   |
|                     |                                                 |              |              |                                          | ignore the ``ElectoralDistrict`` object  |
|                     |                                                 |              |              |                                          | containing it.                           |
+---------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OtherType           | xs:string                                       | Optional     | Single       | Allows for cataloging a new              | If the field is invalid or not present,  |
|                     |                                                 |              |              | :doc:`DistrictType                       | then the implementation is required to   |
|                     |                                                 |              |              | <../enumerations/district_type>` option  | ignore it.                               |
|                     |                                                 |              |              | when ``Type`` is specified as "other".   |                                          |
+---------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. _OCD-IDs: http://opencivicdata.readthedocs.org/en/latest/ocdids.html

.. code-block:: xml
   :linenos:

   <ElectoralDistrict id="ed60129">
      <ExternalIdentifiers>
        <ExternalIdentifier>
          <Type>ocd-id</Type>
          <Value>ocd-division/country:us/state:va</Value>
        </ExternalIdentifier>
        <ExternalIdentifier>
          <Type>fips</Type>
          <Value>51</Value>
        </ExternalIdentifier>
      </ExternalIdentifiers>
      <Name>Commonwealth of Virginia</Name>
      <Type>state</Type>
   </ElectoralDistrict>


.. _single-xml-external-identifier:

ExternalIdentifier
~~~~~~~~~~~~~~~~~~

+--------------+------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type                          | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+====================================+==============+==============+==========================================+==========================================+
| Type         | :doc:`IdentifierType               | **Required** | Single       | Specifies the type of identifier. Must   | If the field is invalid or not present,  |
|              | <../enumerations/identifier_type>` |              |              | be one of the valid types as defined by  | the implementation is required to ignore |
|              |                                    |              |              | :doc:`IdentifierType                     | the ``ElectionIdentifier`` containing    |
|              |                                    |              |              | <../enumerations/identifier_type>`.      | it.                                      |
+--------------+------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OtherType    | xs:string                          | Optional     | Single       | Allows for cataloging an                 | If the field is invalid or not present,  |
|              |                                    |              |              | ``ExternalIdentifier`` type that falls   | then the implementation is required to   |
|              |                                    |              |              | outside the options listed in            | ignore it.                               |
|              |                                    |              |              | :doc:`IdentifierType                     |                                          |
|              |                                    |              |              | <../enumerations/identifier_type>`.      |                                          |
|              |                                    |              |              | ``Type`` should be set to "other" when   |                                          |
|              |                                    |              |              | using this field.                        |                                          |
+--------------+------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Value        | xs:string                          | **Required** | Single       | Specifies the identifier.                | If the field is invalid or not present,  |
|              |                                    |              |              |                                          | the implementation is required to ignore |
|              |                                    |              |              |                                          | the ``ElectionIdentifier`` containing    |
|              |                                    |              |              |                                          | it.                                      |
+--------------+------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

   <ExternalIdentifiers>
      <ExternalIdentifier>
         <Type>ocd-id</Type>
         <Value>ocd-division/country:us/state:nc/county:durham</Value>
      </ExternalIdentifier>
      <ExternalIdentifier>
         <Type>FIPS</Type>
         <Value>37063</Value>
      </ExternalIdentifier>
      <ExternalIdentifier>
         <Type>OTHER</Type>
         <OtherType>GNIS</OtherType>
         <Value>1008550</Value>
      </ExternalIdentifier>
      <external_identifer>
         <Type>OTHER</Type>
         <OtherType>census</OtherType>
         <Value>99063</Value>
      </ExternalIdentifier>
   </ExternalIdentifiers>


.. _single-xml-external-identifiers:

ExternalIdentifiers
~~~~~~~~~~~~~~~~~~~

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

+--------------------+-----------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                | Data Type             | Required?    | Repeats?     | Description                              | Error Handling                           |
+====================+=======================+==============+==============+==========================================+==========================================+
| ExternalIdentifier | `ExternalIdentifier`_ | **Required** | Repeats      | Defines the identifier and the type of   | At least one valid `ExternalIdentifier`_ |
|                    |                       |              |              | identifier it is (see                    | must be present for                      |
|                    |                       |              |              | `ExternalIdentifier`_ for complete       | ``ExternalIdentifiers`` to be valid. If  |
|                    |                       |              |              | information).                            | no valid `ExternalIdentifier`_ is        |
|                    |                       |              |              |                                          | present, the implementation is required  |
|                    |                       |              |              |                                          | to ignore the ``ExternalIdentifiers``    |
|                    |                       |              |              |                                          | element.                                 |
+--------------------+-----------------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _single-xml-external-identifier:

ExternalIdentifier
^^^^^^^^^^^^^^^^^^

+--------------+------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type                          | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+====================================+==============+==============+==========================================+==========================================+
| Type         | :doc:`IdentifierType               | **Required** | Single       | Specifies the type of identifier. Must   | If the field is invalid or not present,  |
|              | <../enumerations/identifier_type>` |              |              | be one of the valid types as defined by  | the implementation is required to ignore |
|              |                                    |              |              | :doc:`IdentifierType                     | the ``ElectionIdentifier`` containing    |
|              |                                    |              |              | <../enumerations/identifier_type>`.      | it.                                      |
+--------------+------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OtherType    | xs:string                          | Optional     | Single       | Allows for cataloging an                 | If the field is invalid or not present,  |
|              |                                    |              |              | ``ExternalIdentifier`` type that falls   | then the implementation is required to   |
|              |                                    |              |              | outside the options listed in            | ignore it.                               |
|              |                                    |              |              | :doc:`IdentifierType                     |                                          |
|              |                                    |              |              | <../enumerations/identifier_type>`.      |                                          |
|              |                                    |              |              | ``Type`` should be set to "other" when   |                                          |
|              |                                    |              |              | using this field.                        |                                          |
+--------------+------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Value        | xs:string                          | **Required** | Single       | Specifies the identifier.                | If the field is invalid or not present,  |
|              |                                    |              |              |                                          | the implementation is required to ignore |
|              |                                    |              |              |                                          | the ``ElectionIdentifier`` containing    |
|              |                                    |              |              |                                          | it.                                      |
+--------------+------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

   <ExternalIdentifiers>
      <ExternalIdentifier>
         <Type>ocd-id</Type>
         <Value>ocd-division/country:us/state:nc/county:durham</Value>
      </ExternalIdentifier>
      <ExternalIdentifier>
         <Type>FIPS</Type>
         <Value>37063</Value>
      </ExternalIdentifier>
      <ExternalIdentifier>
         <Type>OTHER</Type>
         <OtherType>GNIS</OtherType>
         <Value>1008550</Value>
      </ExternalIdentifier>
      <external_identifer>
         <Type>OTHER</Type>
         <OtherType>census</OtherType>
         <Value>99063</Value>
      </ExternalIdentifier>
   </ExternalIdentifiers>


.. _single-xml-hours:

Hours
~~~~~

The open and close time for this place. All times must be fully specified,
including a timezone offset from UTC.

+--------------+-----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type       | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+=================+==============+==============+==========================================+==========================================+
| StartTime    | `TimeWithZone`_ | Optional     | Single       | The time at which this place opens.      | If the element is invalid or not         |
|              |                 |              |              |                                          | present, then the implementation is      |
|              |                 |              |              |                                          | required to ignore it.                   |
+--------------+-----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| EndTime      | `TimeWithZone`_ | Optional     | Single       | The time at which this place closes.     | If the element is invalid or not         |
|              |                 |              |              |                                          | present, then the implementation is      |
|              |                 |              |              |                                          | required to ignore it.                   |
+--------------+-----------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _single-xml-hours-open:

HoursOpen
~~~~~~~~~

A structured way of describing the days and hours that a place such as a
:doc:`Office <office>` or :doc:`PollingLocation <polling_location>` is open, or
that an event such as an :doc:`Election <election>` is happening.

+--------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type    | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+==============+==============+==============+==========================================+==========================================+
| Schedule     | `Schedule`_  | **Required** | Repeats      | Defines a block of days and hours that a | At least one valid `Schedule`_ must be   |
|              |              |              |              | place will be open.                      | present for ``HoursOpen`` to be valid.   |
|              |              |              |              |                                          | If no valid `Schedule`_ is present, the  |
|              |              |              |              |                                          | implementation is required to ignore the |
|              |              |              |              |                                          | ``HoursOpen`` element.                   |
+--------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _single-xml-schedule:

Schedule
^^^^^^^^

A sub-portion of the schedule. This describes a range of days, along with one or
more set of open and close times for those days, as well as the options
describing whether or not appointments are necessary or possible.

+---------------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                 | Data Type    | Required?    | Repeats?     | Description                              | Error Handling                           |
+=====================+==============+==============+==============+==========================================+==========================================+
| Hours               | `Hours`_     | Optional     | Repeats      | Blocks of hours in the date range in     | If the element is invalid or not         |
|                     |              |              |              | which the place is open.                 | present, then the implementation is      |
|                     |              |              |              |                                          | required to ignore it.                   |
+---------------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IsOnlyByAppointment | xs:boolean   | Optional     | Single       | If true, the place is only open during   | If the field is invalid or not present,  |
|                     |              |              |              | the specified time window with an        | then the implementation is required to   |
|                     |              |              |              | appointment.                             | ignore it.                               |
+---------------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IsOrByAppointment   | xs:boolean   | Optional     | Single       | If true, the place is open during the    | If the field is invalid or not present,  |
|                     |              |              |              | hours specified time window and may also | then the implementation is required to   |
|                     |              |              |              | be open with an appointment.             | ignore it.                               |
+---------------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IsSubjectToChange   | xs:boolean   | Optional     | Single       | If true, the place should be open during | If the field is invalid or not present,  |
|                     |              |              |              | the specified time window, but may be    | then the implementation is required to   |
|                     |              |              |              | subject to change. People should contact | ignore it.                               |
|                     |              |              |              | prior to arrival to confirm hours are    |                                          |
|                     |              |              |              | still accurate.                          |                                          |
+---------------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| StartDate           | xs:date      | Optional     | Single       | The date at which this collection of     | If the field is invalid or not present,  |
|                     |              |              |              | start and end times and options begin.   | then the implementation is required to   |
|                     |              |              |              |                                          | ignore it.                               |
+---------------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| EndDate             | xs:date      | Optional     | Single       | The date at which this collection of     | If the field is invalid or not present,  |
|                     |              |              |              | start and end times and options end.     | then the implementation is required to   |
|                     |              |              |              |                                          | ignore it.                               |
+---------------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _single-xml-hours:

Hours
^^^^^

The open and close time for this place. All times must be fully specified,
including a timezone offset from UTC.

+--------------+-----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type       | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+=================+==============+==============+==========================================+==========================================+
| StartTime    | `TimeWithZone`_ | Optional     | Single       | The time at which this place opens.      | If the element is invalid or not         |
|              |                 |              |              |                                          | present, then the implementation is      |
|              |                 |              |              |                                          | required to ignore it.                   |
+--------------+-----------------+--------------+--------------+------------------------------------------+------------------------------------------+
| EndTime      | `TimeWithZone`_ | Optional     | Single       | The time at which this place closes.     | If the element is invalid or not         |
|              |                 |              |              |                                          | present, then the implementation is      |
|              |                 |              |              |                                          | required to ignore it.                   |
+--------------+-----------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _single-xml-time-with-zone:

TimeWithZone
^^^^^^^^^^^^

A string pattern restricting the value to a time with an included offset from
UTC. The pattern is

``(([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]|(24:00:00))(Z|[+-]((0[0-9]|1[0-3]):[0-5][0-9]|14:00))``

.. code-block:: xml
   :linenos:

   <HoursOpen id="hours0001">
     <Schedule>
       <Hours>
         <StartTime>06:00:00-05:00</StartTime>
         <EndTime>12:00:00-05:00</EndTime>
       </Hours>
       <Hours>
         <StartTime>13:00:00-05:00</StartTime>
         <EndTime>19:00:00-05:00</EndTime>
       </Hours>
       <StartDate>2013-11-05</StartDate>
       <EndDate>2013-11-05</EndDate>
     </Schedule>
   </HoursOpen>


.. _single-xml-html-color-string:

HtmlColorString
~~~~~~~~~~~~~~~

A restricted string pattern for a six-character hex code representing an HTML
color string. The pattern is:

``[0-9a-f]{6}``

.. code-block:: xml
   :linenos:

   <Party id="par0001">
     <Abbreviation>REP</Abbreviation>
     <Color>e91d0e</Color>
     <Name>
       <Text language="en">Republican</Text>
     </Name>
   </Party>


.. _single-xml-internationalized-text:

InternationalizedText
~~~~~~~~~~~~~~~~~~~~~

``InternationalizedText`` allows for support of multiple languages for a string.
``InternationalizedText`` has an optional attribute ``label``, which allows the feed to refer
back to the original label for the information (e.g. if the contact information came from a
CSV, ``label`` may refer to a row ID). Examples of ``InternationalizedText`` can be seen in:

* Any element that extends :doc:`ContestBase <contest_base>`

* Any element that extends :doc:`BallotSelectionBase <ballot_selection_base>`

* :doc:`Candidate <candidate>`

* :doc:`ContactInformation <contact_information>`

* :doc:`Election <election>`

* :doc:`ElectionAdministration <election_administration>`

* :doc:`Office <office>`

* :doc:`Party <party>`

* :doc:`Person <person>`

* :doc:`PollingLocation <polling_location>`

* :doc:`Source <source>`

+--------------+-------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type         | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+===================+==============+==============+==========================================+==========================================+
| Text         | `LanguageString`_ | **Required** | Repeats      | Contains the translations of a           | At least one valid ``Text`` must be      |
|              |                   |              |              | particular string of text.               | present for ``InternationalizedText`` to |
|              |                   |              |              |                                          | be valid. If no valid ``Text`` is        |
|              |                   |              |              |                                          | present, the implementation is required  |
|              |                   |              |              |                                          | to ignore the ``InternationalizedText``  |
|              |                   |              |              |                                          | element.                                 |
+--------------+-------------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _single-xml-language-string:

LanguageString
^^^^^^^^^^^^^^

``LanguageString`` extends xs:string and can contain text from any language. ``LanguageString``
has one required attribute, ``language``, that must contain the 2-character `language code`_ for the
type of language ``LanguageString`` contains.

.. _`language code`: http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes

.. code-block:: xml
   :linenos:

   <BallotTitle>
      <Text language="en">Retention of Supreme Court Justice</Text>
      <Text language="es">La retención de juez de la Corte Suprema</Text>
   </BallotTitle>


.. _single-xml-language-string:

LanguageString
~~~~~~~~~~~~~~

``LanguageString`` extends xs:string and can contain text from any language. ``LanguageString``
has one required attribute, ``language``, that must contain the 2-character `language code`_ for the
type of language ``LanguageString`` contains.

.. _`language code`: http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes

.. code-block:: xml
   :linenos:

   <BallotTitle>
      <Text language="en">Retention of Supreme Court Justice</Text>
      <Text language="es">La retención de juez de la Corte Suprema</Text>
   </BallotTitle>


.. _single-xml-lat-lng:

LatLng
~~~~~~

The latitude and longitude of a polling location in `WGS 84`_ format. Both
latitude and longitude values are measured in decimal degrees.

+--------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type    | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+==============+==============+==============+==========================================+==========================================+
| Latitude     | xs:float     | **Required** | Single       | The latitude of the polling location.    | If the field is invalid, then the        |
|              |              |              |              |                                          | implementation is required to ignore it. |
+--------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Longitude    | xs:float     | **Required** | Single       | The longitude of the polling location.   | If the field is invalid, then the        |
|              |              |              |              |                                          | implementation is required to ignore it. |
+--------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Source       | xs:string    | Optional     | Single       | The system used to perform the lookup    | If the field is invalid or not present,  |
|              |              |              |              | from location name to lat/lng. For       | then the implementation is required to   |
|              |              |              |              | example, this could be the name of a     | ignore it.                               |
|              |              |              |              | geocoding service.                       |                                          |
+--------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. _`WGS 84`: http://en.wikipedia.org/wiki/World_Geodetic_System#A_new_World_Geodetic_System:_WGS_84

.. code-block:: xml
   :linenos:

   <PollingLocation id="pl81274">
      <AddressLine>ALBEMARLE HIGH SCHOOL</AddressLine>
      <AddressLine>2775 Hydraulic Rd</AddressLine>
      <AddressLine>Charlottesville, VA 229018917</AddressLine>
      <HoursOpenId>hours0001</HoursOpenId>
      <LatLng>
        <Latitude>38.0754627</Latitude>
        <Longitude>-78.5014875</Longitude>
        <Source>Google Maps</Source>
      </LatLng>
   </PollingLocation>


.. _single-xml-locality:

Locality
~~~~~~~~

The Locality object represents the jurisdiction below the :doc:`state <state>` (e.g. county).

+--------------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                      | Data Type                                       | Required?    | Repeats?     | Description                              | Error Handling                           |
+==========================+=================================================+==============+==============+==========================================+==========================================+
| ElectionAdministrationId | xs:IDREF                                        | Optional     | Single       | Links to the locality's :doc:`election   | If the field is invalid or not present,  |
|                          |                                                 |              |              | administration                           | then the implementation is required to   |
|                          |                                                 |              |              | <election_administration>` object.       | ignore it.                               |
+--------------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ExternalIdentifiers      | :doc:`ExternalIdentifiers                       | Optional     | Single       | Another identifier for a locality that   | If the element is invalid or not         |
|                          | </built_rst/xml/elements/external_identifiers>` |              |              | links to another dataset (e.g.           | present, then the implementation is      |
|                          |                                                 |              |              | `OCD-ID`_)                               | required to ignore it.                   |
+--------------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Name                     | xs:string                                       | **Required** | Single       | Specifies the name of a locality.        | If the field is not present or invalid,  |
|                          |                                                 |              |              |                                          | the implementation is required to ignore |
|                          |                                                 |              |              |                                          | the Locality element containing it.      |
+--------------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PollingLocationId        | xs:IDREF                                        | Optional     | Repeats      | Specifies a link to the locality's       | If the field is invalid or not present,  |
|                          |                                                 |              |              | :doc:`polling locations                  | the implementation is required to ignore |
|                          |                                                 |              |              | <polling_location>`. If early vote       | it. However, the implementation should   |
|                          |                                                 |              |              | centers or ballot drop locations are     | still check to see if there are any      |
|                          |                                                 |              |              | locality-wide, they should be specified  | polling locations associated with this   |
|                          |                                                 |              |              | here.                                    | locality's state.                        |
+--------------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| StateId                  | xs:IDREF                                        | **Required** | Single       | References the locality's :doc:`state    | If the field is invalid or not present,  |
|                          |                                                 |              |              | <state>`.                                | the implementation is required to ignore |
|                          |                                                 |              |              |                                          | the Locality element containing.         |
+--------------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Type                     | :doc:`DistrictType                              | Optional     | Single       | Defines the kind of locality (e.g.       | If the field is invalid or not present,  |
|                          | <../enumerations/district_type>`                |              |              | county, town, et al.), which is one of   | then the implementation is required to   |
|                          |                                                 |              |              | the various :doc:`DistrictType           | ignore it.                               |
|                          |                                                 |              |              | enumerations                             |                                          |
|                          |                                                 |              |              | <../enumerations/district_type>`.        |                                          |
+--------------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OtherType                | xs:string                                       | Optional     | Single       | Allows for defining a type of locality   | If the field is invalid or not present,  |
|                          |                                                 |              |              | that falls outside the options listed in | then the implementation is required to   |
|                          |                                                 |              |              | :doc:`DistrictType                       | ignore it.                               |
|                          |                                                 |              |              | <../enumerations/district_type>`.        |                                          |
+--------------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. _OCD-ID: http://opencivicdata.readthedocs.org/en/latest/ocdids.html

.. code-block:: xml
   :linenos:

   <Locality id="loc70001">
     <ElectionAdministrationId>ea40001</ElectionAdministrationId>
     <ExternalIdentifiers>
       <ExternalIdentifier>
         <Type>ocd-id</Type>
         <Value>ocd-division/country:us/state:va/county:albemarle</Value>
       </ExternalIdentifier>
     </ExternalIdentifiers>
     <Name>ALBEMARLE COUNTY</Name>
     <StateId>st51</StateId>
     <Type>county</Type>
   </Locality>


.. _single-xml-office:

Office
~~~~~~

``Office`` represents the office associated with a contest or district (e.g. Alderman, Mayor,
School Board, et al).

+----------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                  | Data Type                                       | Required?    | Repeats?     | Description                              | Error Handling                           |
+======================+=================================================+==============+==============+==========================================+==========================================+
| ContactInformation   | :doc:`ContactInformation <contact_information>` | Optional     | Repeats      | Specifies the contact information for    | If the element is invalid or not         |
|                      |                                                 |              |              | the office and/or individual holding the | present, then the implementation is      |
|                      |                                                 |              |              | office.                                  | required to ignore it.                   |
+----------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ElectoralDistrictId  | xs:IDREF                                        | **Required** | Single       | Links to the :doc:`ElectoralDistrict     | If the field is invalid or not present,  |
|                      |                                                 |              |              | <electoral_district>` element associated | the implementation is required to ignore |
|                      |                                                 |              |              | with the office.                         | the ``Office`` element containing it.    |
+----------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ExternalIdentifiers  | :doc:`ExternalIdentifiers                       | Optional     | Single       | Other identifiers that link this office  | If the element is invalid or not         |
|                      | </built_rst/xml/elements/external_identifiers>` |              |              | to other related datasets (e.g. campaign | present, then the implementation is      |
|                      |                                                 |              |              | finance systems, OCD IDs, et al.).       | required to ignore it.                   |
+----------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| FilingDeadline       | xs:date                                         | Optional     | Single       | Specifies the date and time when a       | If the field is invalid or not present,  |
|                      |                                                 |              |              | candidate must have filed for the        | then the implementation is required to   |
|                      |                                                 |              |              | contest for the office.                  | ignore it.                               |
+----------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IsPartisan           | xs:boolean                                      | Optional     | Single       | Indicates whether the office is          | If the field is invalid or not present,  |
|                      |                                                 |              |              | partisan.                                | then the implementation is required to   |
|                      |                                                 |              |              |                                          | ignore it.                               |
+----------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Name                 | :doc:`InternationalizedText                     | **Required** | Single       | The name of the office.                  | If the field is invalid or not present,  |
|                      | <internationalized_text>`                       |              |              |                                          | the implementation is required to ignore |
|                      |                                                 |              |              |                                          | the ``Office`` element containing it.    |
+----------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OfficeHolderPersonId | xs:IDREF                                        | Optional     | Repeats      | Links to the :doc:`Person <person>`      | If the field is invalid or not present,  |
|                      |                                                 |              |              | element(s) that hold additional          | then the implementation is required to   |
|                      |                                                 |              |              | information about the current office     | ignore it.                               |
|                      |                                                 |              |              | holder(s).                               |                                          |
+----------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Term                 | `Term`_                                         | Optional     | Single       | Defines the term the office can be held. | If the element is invalid or not         |
|                      |                                                 |              |              |                                          | present, then the implementation is      |
|                      |                                                 |              |              |                                          | required to ignore it.                   |
+----------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _single-xml-term:

Term
^^^^

+--------------+-------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type                           | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+=====================================+==============+==============+==========================================+==========================================+
| Type         | :doc:`OfficeTermType                | **Required** | Single       | Specifies the type of office term (see   | If the field is invalid or not present,  |
|              | <../enumerations/office_term_type>` |              |              | :doc:`OfficeTermType                     | the implementation is required to ignore |
|              |                                     |              |              | <../enumerations/office_term_type>` for  | the ``Office`` element containing it.    |
|              |                                     |              |              | valid values).                           |                                          |
+--------------+-------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| StartDate    | xs:date                             | Optional     | Single       | Specifies the start date for the current | If the field is invalid or not present,  |
|              |                                     |              |              | term of the office.                      | then the implementation is required to   |
|              |                                     |              |              |                                          | ignore it.                               |
+--------------+-------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| EndDate      | xs:date                             | Optional     | Single       | Specifies the end date for the current   | If the field is invalid or not present,  |
|              |                                     |              |              | term of the office.                      | then the implementation is required to   |
|              |                                     |              |              |                                          | ignore it.                               |
+--------------+-------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

   <Office id="off0000">
     <ElectoralDistrictId>ed60129</ElectoralDistrictId>
     <FilingDeadline>2013-01-01</FilingDeadline>
     <IsPartisan>false</IsPartisan>
     <Name>
       <Text language="en">Governor</Text>
     </Name>
     <Term>
       <Type>full-term</Type>
     </Term>
   </Office>


.. _single-xml-ordered-contest:

OrderedContest
~~~~~~~~~~~~~~

``OrderedContest`` encapsulates links to the information that comprises a contest and potential
ballot selections. ``OrderedContest`` elements can be collected within a
:doc:`BallotStyle <ballot_style>` to accurate depict exactly what will show up on a particular
ballot in the proper order.

+--------------------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                      | Data Type    | Required?    | Repeats?     | Description                              | Error Handling                           |
+==========================+==============+==============+==============+==========================================+==========================================+
| ContestId                | xs:IDREF     | **Required** | Single       | Links to elements that extend            | If the field is invalid or not present,  |
|                          |              |              |              | :doc:`ContestBase <contest_base>`.       | the implementation is required to ignore |
|                          |              |              |              |                                          | the ``OrderedContest`` element           |
|                          |              |              |              |                                          | containing it.                           |
+--------------------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OrderedBallotSelectionId | xs:IDREF     | Optional     | Repeats      | Links to elements that extend            | If the field is invalid or not present,  |
|                          |              |              |              | :doc:`BallotSelectionBase                | the implementation is required to ignore |
|                          |              |              |              | <ballot_selection_base>`.                | it. If no ``OrderedBallotSelectionId``   |
|                          |              |              |              |                                          | elements are present, the presumed order |
|                          |              |              |              |                                          | of the selection will be the order of    |
|                          |              |              |              |                                          | :doc:`BallotSelectionBase                |
|                          |              |              |              |                                          | <ballot_selection_base>`-extended        |
|                          |              |              |              |                                          | elements referenced by the underlying    |
|                          |              |              |              |                                          | :doc:`ContestBase                        |
|                          |              |              |              |                                          | <contest_base>`-extended elements.       |
+--------------------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

   <OrderedContest id="oc20003abc">
      <ContestId>cc20003</ContestId>
      <OrderedBallotSelectionId>cs10961</OrderedBallotSelectionId>
      <OrderedBallotSelectionId>cs10962</OrderedBallotSelectionId>
      <OrderedBallotSelectionId>cs10963</OrderedBallotSelectionId>
   </OrderedContest>


.. _single-xml-party:

Party
~~~~~

This element describes a political party and the metadata associated with them.

+---------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                 | Data Type                                       | Required?    | Repeats?     | Description                              | Error Handling                           |
+=====================+=================================================+==============+==============+==========================================+==========================================+
| Abbreviation        | xs:string                                       | Optional     | Single       | An abbreviation for the party name.      | If the field is invalid or not present,  |
|                     |                                                 |              |              |                                          | then the implementation is required to   |
|                     |                                                 |              |              |                                          | ignore it.                               |
+---------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Color               | `HtmlColorString`_                              | Optional     | Single       | The preferred display color for the      | If the element is invalid or not         |
|                     |                                                 |              |              | party, for use in maps and other         | present, then the implementation is      |
|                     |                                                 |              |              | displays.                                | required to ignore it.                   |
+---------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ExternalIdentifiers | :doc:`ExternalIdentifiers                       | Optional     | Single       | Other identifiers that link this party   | If the element is invalid or not         |
|                     | </built_rst/xml/elements/external_identifiers>` |              |              | to other related data sets (e.g. a       | present, then the implementation is      |
|                     |                                                 |              |              | campaign finance system, etc).           | required to ignore it.                   |
+---------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| LogoUri             | xs:anyURI                                       | Optional     | Single       | Web address of a logo to use in          | If the field is invalid or not present,  |
|                     |                                                 |              |              | displays.                                | then the implementation is required to   |
|                     |                                                 |              |              |                                          | ignore it.                               |
+---------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Name                | :doc:`InternationalizedText                     | Optional     | Single       | The name of the party.                   | If the element is invalid or not         |
|                     | <internationalized_text>`                       |              |              |                                          | present, then the implementation is      |
|                     |                                                 |              |              |                                          | required to ignore it.                   |
+---------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _single-xml-html-color-string:

HtmlColorString
^^^^^^^^^^^^^^^

A restricted string pattern for a six-character hex code representing an HTML
color string. The pattern is:

``[0-9a-f]{6}``

.. code-block:: xml
   :linenos:

   <Party id="par0001">
     <Abbreviation>REP</Abbreviation>
     <Color>e91d0e</Color>
     <Name>
       <Text language="en">Republican</Text>
     </Name>
   </Party>


.. _single-xml-party-contest:

PartyContest
~~~~~~~~~~~~

An extension of :doc:`ContestBase <contest_base>` which describes a contest in
which the possible ballot selections are of type :doc:`PartySelection
<party_selection>`. These could include contests in which straight-party
selections are allowed, or party-list contests (although these are more common
outside of the United States).


.. _single-xml-party-selection:

PartySelection
~~~~~~~~~~~~~~

This element extends :doc:`BallotSelectionBase <ballot_selection_base>` to
support contests in which the selections can be groups of one or more parties.

+--------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type    | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+==============+==============+==============+==========================================+==========================================+
| PartyId      | xs:IDREF     | **Required** | Repeats      | One or more :doc:`Party <party>` IDs     | If one or more parties referenced are    |
|              |              |              |              | which collectively represent a ballot    | invalid or not present, the              |
|              |              |              |              | selection.                               | implementation is required to ignore the |
|              |              |              |              |                                          | PartySelection containing it.            |
+--------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _single-xml-person:

Person
~~~~~~

``Person`` defines information about a person. The person may be a candidate, election administrator,
or elected official. These elements reference ``Person``:

* :doc:`Candidate <candidate>`

* :doc:`ElectionAdministration <election_administration>`

* :doc:`Office <office>`

+--------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                | Data Type                   | Required?    | Repeats?     | Description                              | Error Handling                           |
+====================+=============================+==============+==============+==========================================+==========================================+
| ContactInformation | :doc:`ContactInformation    | Optional     | Repeats      | Specifies contact information for the    | If the element is invalid or not         |
|                    | <contact_information>`      |              |              | person.                                  | present, then the implementation is      |
|                    |                             |              |              |                                          | required to ignore it.                   |
+--------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| DateOfBirth        | xs:date                     | Optional     | Single       | Represents the individual's date of      | If the field is invalid or not present,  |
|                    |                             |              |              | birth.                                   | then the implementation is required to   |
|                    |                             |              |              |                                          | ignore it.                               |
+--------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| FirstName          | xs:string                   | Optional     | Single       | Represents an individual's first name.   | If the field is invalid or not present,  |
|                    |                             |              |              |                                          | then the implementation is required to   |
|                    |                             |              |              |                                          | ignore it.                               |
+--------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| FullName           | :doc:`InternationalizedText | Optional     | Single       | Specifies a person's full name (**NB:**  | If the element is invalid or not         |
|                    | <internationalized_text>`   |              |              | this information is                      | present, then the implementation is      |
|                    |                             |              |              | :doc:`InternationalizedText              | required to ignore it.                   |
|                    |                             |              |              | <internationalized_text>` because it     |                                          |
|                    |                             |              |              | sometimes appears on ballots in multiple |                                          |
|                    |                             |              |              | languages).                              |                                          |
+--------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| LastName           | xs:string                   | Optional     | Single       | Represents an individual's last name.    | If the field is invalid or not present,  |
|                    |                             |              |              |                                          | then the implementation is required to   |
|                    |                             |              |              |                                          | ignore it.                               |
+--------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| MiddleName         | xs:string                   | Optional     | Repeats      | Represents any number of names between   | If the field is invalid or not present,  |
|                    |                             |              |              | an individual's first and last names     | then the implementation is required to   |
|                    |                             |              |              | (e.g. John **Ronald Reuel** Tolkien).    | ignore it.                               |
+--------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Nickname           | xs:string                   | Optional     | Single       | Represents an individual's nickname.     | If the field is invalid or not present,  |
|                    |                             |              |              |                                          | then the implementation is required to   |
|                    |                             |              |              |                                          | ignore it.                               |
+--------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PartyId            | xs:IDREF                    | Optional     | Single       | Refers to the associated :doc:`Party     | If the field is invalid or not present,  |
|                    |                             |              |              | <party>`.                                | then the implementation is required to   |
|                    |                             |              |              |                                          | ignore it.                               |
+--------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Prefix             | xs:string                   | Optional     | Single       | Specifies a prefix associated with a     | If the field is invalid or not present,  |
|                    |                             |              |              | person (e.g. Dr.).                       | then the implementation is required to   |
|                    |                             |              |              |                                          | ignore it.                               |
+--------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Profession         | :doc:`InternationalizedText | Optional     | Single       | Specifies a person's profession (**NB:** | If the element is invalid or not         |
|                    | <internationalized_text>`   |              |              | this information is                      | present, then the implementation is      |
|                    |                             |              |              | :doc:`InternationalizedText              | required to ignore it.                   |
|                    |                             |              |              | <internationalized_text>` because it     |                                          |
|                    |                             |              |              | sometimes appears on ballots in multiple |                                          |
|                    |                             |              |              | languages).                              |                                          |
+--------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Suffix             | xs:string                   | Optional     | Single       | Specifies a suffix associated with a     | If the field is invalid or not present,  |
|                    |                             |              |              | person (e.g. Jr.).                       | then the implementation is required to   |
|                    |                             |              |              |                                          | ignore it.                               |
+--------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Title              | :doc:`InternationalizedText | Optional     | Single       | A title associated with a person         | If the element is invalid or not         |
|                    | <internationalized_text>`   |              |              | (**NB:** this information is             | present, then the implementation is      |
|                    |                             |              |              | :doc:`InternationalizedText              | required to ignore it.                   |
|                    |                             |              |              | <internationalized_text>` because it     |                                          |
|                    |                             |              |              | sometimes appears on ballots in multiple |                                          |
|                    |                             |              |              | languages).                              |                                          |
+--------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

   <Person id="per50001">
      <ContactInformation label="ci60002">
        <Email>rwashburne@albemarle.org</Email>
        <Phone>4349724173</Phone>
      </ContactInformation>
      <FirstName>RICHARD</FirstName>
      <LastName>WASHBURNE</LastName>
      <MiddleName>J.</MiddleName>
      <Nickname>JAKE</Nickname>
      <Title>
        <Text language="en">General Registrar Physical</Text>
      </Title>
   </Person>


.. _single-xml-polling-location:

PollingLocation
~~~~~~~~~~~~~~~

The PollingLocation object represents a site where voters cast or drop off ballots.

+------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag              | Data Type                   | Required?    | Repeats?     | Description                              | Error Handling                           |
+==================+=============================+==============+==============+==========================================+==========================================+
| AddressLine      | xs:string                   | **Required** | Repeats      | Represents the various parts of an       | At least one valid ``AddressLine`` must  |
|                  |                             |              |              | address to a polling location.           | be present for ``PollingLocation`` to be |
|                  |                             |              |              |                                          | valid. If no valid ``AddressLine`` is    |
|                  |                             |              |              |                                          | present, the implementation is required  |
|                  |                             |              |              |                                          | to ignore the ``PollingLocation``        |
|                  |                             |              |              |                                          | element containing it.                   |
+------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Directions       | :doc:`InternationalizedText | Optional     | Single       | Specifies further instructions for       | If the element is invalid or not         |
|                  | <internationalized_text>`   |              |              | locating the polling location.           | present, then the implementation is      |
|                  |                             |              |              |                                          | required to ignore it.                   |
+------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Hours            | :doc:`InternationalizedText | Optional     | Single       | Contains the hours (in local time) that  | If the element is invalid or not         |
| **[deprecated]** | <internationalized_text>`   |              |              | the polling location is open (**NB:**    | present, then the implementation is      |
|                  |                             |              |              | this element is deprecated in favor of   | required to ignore it.                   |
|                  |                             |              |              | the more structured :doc:`HoursOpen      |                                          |
|                  |                             |              |              | <hours_open>` element. It is strongly    |                                          |
|                  |                             |              |              | encouraged that data providers move      |                                          |
|                  |                             |              |              | toward contributing hours in this        |                                          |
|                  |                             |              |              | format).                                 |                                          |
+------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| HoursOpenId      | xs:IDREF                    | Optional     | Single       | Links to an :doc:`HoursOpen              | If the field is invalid or not present,  |
|                  |                             |              |              | <hours_open>` element, which is a        | then the implementation is required to   |
|                  |                             |              |              | schedule of dates and hours during which | ignore it.                               |
|                  |                             |              |              | the polling location is available.       |                                          |
+------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IsDropBox        | xs:boolean                  | Optional     | Single       | Indicates if this polling location is a  | If the field is invalid or not present,  |
|                  |                             |              |              | drop box.                                | then the implementation is required to   |
|                  |                             |              |              |                                          | ignore it.                               |
+------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IsEarlyVoting    | xs:boolean                  | Optional     | Single       | Indicates if this polling location is an | If the field is invalid or not present,  |
|                  |                             |              |              | early vote site.                         | then the implementation is required to   |
|                  |                             |              |              |                                          | ignore it.                               |
+------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| LatLng           | `LatLng`_                   | Optional     | Single       | Specifies the latitude and longitude of  | If the element is invalid or not         |
|                  |                             |              |              | this polling location.                   | present, then the implementation is      |
|                  |                             |              |              |                                          | required to ignore it.                   |
+------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PhotoUri         | xs:anyURI                   | Optional     | Single       | Contains a link to an image of the       | If the field is invalid or not present,  |
|                  |                             |              |              | polling location.                        | then the implementation is required to   |
|                  |                             |              |              |                                          | ignore it.                               |
+------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _single-xml-lat-lng:

LatLng
^^^^^^

The latitude and longitude of a polling location in `WGS 84`_ format. Both
latitude and longitude values are measured in decimal degrees.

+--------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type    | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+==============+==============+==============+==========================================+==========================================+
| Latitude     | xs:float     | **Required** | Single       | The latitude of the polling location.    | If the field is invalid, then the        |
|              |              |              |              |                                          | implementation is required to ignore it. |
+--------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Longitude    | xs:float     | **Required** | Single       | The longitude of the polling location.   | If the field is invalid, then the        |
|              |              |              |              |                                          | implementation is required to ignore it. |
+--------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Source       | xs:string    | Optional     | Single       | The system used to perform the lookup    | If the field is invalid or not present,  |
|              |              |              |              | from location name to lat/lng. For       | then the implementation is required to   |
|              |              |              |              | example, this could be the name of a     | ignore it.                               |
|              |              |              |              | geocoding service.                       |                                          |
+--------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. _`WGS 84`: http://en.wikipedia.org/wiki/World_Geodetic_System#A_new_World_Geodetic_System:_WGS_84

.. code-block:: xml
   :linenos:

   <PollingLocation id="pl81274">
      <AddressLine>ALBEMARLE HIGH SCHOOL</AddressLine>
      <AddressLine>2775 Hydraulic Rd</AddressLine>
      <AddressLine>Charlottesville, VA 229018917</AddressLine>
      <HoursOpenId>hours0001</HoursOpenId>
      <LatLng>
        <Latitude>38.0754627</Latitude>
        <Longitude>-78.5014875</Longitude>
        <Source>Google Maps</Source>
      </LatLng>
   </PollingLocation>


.. _single-xml-precinct:

Precinct
~~~~~~~~

The Precinct object represents a precinct, which is contained within a Locality. While the id
attribute does not have to be static across feeds for one election, the combination of
:doc:`Source.VipId <source>`, :doc:`Locality.Name <locality>`, :doc:`Precinct.Ward <precinct>`,
:doc:`Precinct.Name <precinct>`, and :doc:`Precinct.Number <precinct>` should remain constant across
feeds for one election (NB: not all of the fields just mentioned are required -- omitting those
non-required fields is fine).

+---------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                 | Data Type                                       | Required?    | Repeats?     | Description                              | Error Handling                           |
+=====================+=================================================+==============+==============+==========================================+==========================================+
| BallotStyleId       | xs:IDREF                                        | Optional     | Single       | Links to the :doc:`ballot style          | If the field is invalid or not present,  |
|                     |                                                 |              |              | <ballot_style>`, which a person who      | then the implementation is required to   |
|                     |                                                 |              |              | lives in this precinct will vote.        | ignore it.                               |
+---------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ElectoralDistrictId | xs:IDREF                                        | Optional     | Repeats      | Links to an :doc:`electoral district     | If the field is invalid or not present,  |
|                     |                                                 |              |              | <electoral_district>` (e.g.,             | then the implementation is required to   |
|                     |                                                 |              |              | congressional district, state house      | ignore it.                               |
|                     |                                                 |              |              | district, school board district) to      |                                          |
|                     |                                                 |              |              | which the precinct belongs. **Highly     |                                          |
|                     |                                                 |              |              | Recommended** if candidate information   |                                          |
|                     |                                                 |              |              | is to be provided. Multiple allowed and  |                                          |
|                     |                                                 |              |              | recommended to specify the geography of  |                                          |
|                     |                                                 |              |              | multiple electoral districts. If an      |                                          |
|                     |                                                 |              |              | electoral district splits a precinct,    |                                          |
|                     |                                                 |              |              | use the `PrecinctSplitName` object and   |                                          |
|                     |                                                 |              |              | do not specify that particular electoral |                                          |
|                     |                                                 |              |              | district in this object.                 |                                          |
+---------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ExternalIdentifiers | :doc:`ExternalIdentifiers                       | Optional     | Single       | Other identifier for the precinct that   | If the element is invalid or not         |
|                     | </built_rst/xml/elements/external_identifiers>` |              |              | relates to another dataset (e.g.         | present, then the implementation is      |
|                     |                                                 |              |              | `OCD-ID`_).                              | required to ignore it.                   |
+---------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IsMailOnly          | xs:boolean                                      | Optional     | Single       | Determines if the precinct runs          | If the field is missing or invalid, the  |
|                     |                                                 |              |              | mail-only elections.                     | implementation is required to assume     |
|                     |                                                 |              |              |                                          | `IsMailOnly` is false.                   |
+---------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| LocalityId          | xs:IDREF                                        | **Required** | Single       | Links to the :doc:`locality <locality>`  | If the field is invalid or not present,  |
|                     |                                                 |              |              | that comprises the precinct.             | the implementation is required to ignore |
|                     |                                                 |              |              |                                          | the precinct element containing it.      |
+---------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Name                | xs:string                                       | **Required** | Single       | Specifies the precinct's name (or number | If the field is invalid or not present,  |
|                     |                                                 |              |              | if no name exists).                      | the implementation is required to ignore |
|                     |                                                 |              |              |                                          | the precinct element containing it.      |
+---------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Number              | xs:string                                       | Optional     | Single       | Specifies the precinct's number (e.g.,   | If the field is invalid or not present,  |
|                     |                                                 |              |              | 32 or 32A -- alpha characters are        | then the implementation is required to   |
|                     |                                                 |              |              | legal). Should be used if the `Name`     | ignore it.                               |
|                     |                                                 |              |              | field is populated by a name and not a   |                                          |
|                     |                                                 |              |              | number.                                  |                                          |
+---------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PollingLocationId   | xs:IDREF                                        | Optional     | Repeats      | Specifies a link to the precinct's       | If the field is invalid or not present,  |
|                     |                                                 |              |              | :doc:`polling location                   | then the implementation is required to   |
|                     |                                                 |              |              | <polling_location>` object(s). Multiple  | ignore it.                               |
|                     |                                                 |              |              | `PollingLocationId` tags may be          |                                          |
|                     |                                                 |              |              | specified.                               |                                          |
+---------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PrecinctSplitName   | xs:string                                       | Optional     | Single       | Refers to name of the associated         | If the field is invalid or not present,  |
|                     |                                                 |              |              | precinct split.                          | then the implementation is required to   |
|                     |                                                 |              |              |                                          | ignore it.                               |
+---------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Ward                | xs:string                                       | Optional     | Single       | Specifies the ward the precinct is       | If the field is invalid or not present,  |
|                     |                                                 |              |              | contained within.                        | then the implementation is required to   |
|                     |                                                 |              |              |                                          | ignore it.                               |
+---------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. _OCD-ID: http://opencivicdata.readthedocs.org/en/latest/ocdids.html

.. code-block:: xml
   :linenos:

   <Precinct id="pre90111">
      <BallotStyleId>bs00010</BallotStyleId>
      <ElectoralDistrictId>ed60129</ElectoralDistrictId>
      <ElectoralDistrictId>ed60311</ElectoralDistrictId>
      <ElectoralDistrictId>ed60054</ElectoralDistrictId>
      <IsMailOnly>false</IsMailOnly>
      <LocalityId>loc70001</LocalityId>
      <Name>203 - GEORGETOWN</Name>
      <Number>0203</Number>
      <PollingLocationId>pl81274</PollingLocationId>
   </Precinct>


.. _single-xml-retention-contest:

RetentionContest
~~~~~~~~~~~~~~~~

``RetentionContest`` extends :doc:`BallotMeasureContest <ballot_measure_contest>` and represents a
contest where a candidate is retained in a position (e.g. a judge).

+--------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type    | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+==============+==============+==============+==========================================+==========================================+
| CandidateId  | xs:IDREF     | **Required** | Single       | Links to the :doc:`Candidate             | If the field is invalid or not present,  |
|              |              |              |              | <candidate>` being retained.             | the implementation is required to ignore |
|              |              |              |              |                                          | the ``RetentionContest`` element         |
|              |              |              |              |                                          | containing it.                           |
+--------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OfficeId     | xs:IDREF     | Optional     | Single       | Links to the information about the       | If the field is invalid or not present,  |
|              |              |              |              | office.                                  | then the implementation is required to   |
|              |              |              |              |                                          | ignore it.                               |
+--------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

   <RetentionContest id="rc40001">
      <BallotSelectionId>rc40001a</BallotSelectionId>
      <BallotSelectionId>rc40001b</BallotSelectionId>
      <BallotTitle>
         <Text language="en">Retention of Supreme Court Justice</Text>
         <Text language="es">La retención de juez de la Corte Suprema</Text>
      </BallotTitle>
      <ElectoralDistrictId>ed60129</ElectoralDistrictId>
      <Name>Judicial Retention, Supreme Court</Name>
      <CandidateId>can14444</CandidateId>
      <OfficeId>off20006</OfficeId>
   </RetentionContest>


.. _single-xml-schedule:

Schedule
~~~~~~~~

A sub-portion of the schedule. This describes a range of days, along with one or
more set of open and close times for those days, as well as the options
describing whether or not appointments are necessary or possible.

+---------------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                 | Data Type    | Required?    | Repeats?     | Description                              | Error Handling                           |
+=====================+==============+==============+==============+==========================================+==========================================+
| Hours               | `Hours`_     | Optional     | Repeats      | Blocks of hours in the date range in     | If the element is invalid or not         |
|                     |              |              |              | which the place is open.                 | present, then the implementation is      |
|                     |              |              |              |                                          | required to ignore it.                   |
+---------------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IsOnlyByAppointment | xs:boolean   | Optional     | Single       | If true, the place is only open during   | If the field is invalid or not present,  |
|                     |              |              |              | the specified time window with an        | then the implementation is required to   |
|                     |              |              |              | appointment.                             | ignore it.                               |
+---------------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IsOrByAppointment   | xs:boolean   | Optional     | Single       | If true, the place is open during the    | If the field is invalid or not present,  |
|                     |              |              |              | hours specified time window and may also | then the implementation is required to   |
|                     |              |              |              | be open with an appointment.             | ignore it.                               |
+---------------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IsSubjectToChange   | xs:boolean   | Optional     | Single       | If true, the place should be open during | If the field is invalid or not present,  |
|                     |              |              |              | the specified time window, but may be    | then the implementation is required to   |
|                     |              |              |              | subject to change. People should contact | ignore it.                               |
|                     |              |              |              | prior to arrival to confirm hours are    |                                          |
|                     |              |              |              | still accurate.                          |                                          |
+---------------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| StartDate           | xs:date      | Optional     | Single       | The date at which this collection of     | If the field is invalid or not present,  |
|                     |              |              |              | start and end times and options begin.   | then the implementation is required to   |
|                     |              |              |              |                                          | ignore it.                               |
+---------------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+
| EndDate             | xs:date      | Optional     | Single       | The date at which this collection of     | If the field is invalid or not present,  |
|                     |              |              |              | start and end times and options end.     | then the implementation is required to   |
|                     |              |              |              |                                          | ignore it.                               |
+---------------------+--------------+--------------+--------------+------------------------------------------+------------------------------------------+


.. _single-xml-source:

Source
~~~~~~

The Source object represents the organization that is publishing the information. This object is
the only required object in the feed file, and only one source object is allowed to be present.

+-----------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag             | Data Type                   | Required?    | Repeats?     | Description                              | Error Handling                           |
+=================+=============================+==============+==============+==========================================+==========================================+
| Name            | xs:string                   | **Required** | Single       | Specifies the name of the organization   | If the field is invalid, then the        |
|                 |                             |              |              | that is providing the information.       | implementation is required to ignore the |
|                 |                             |              |              |                                          | ``Source`` element containing it.        |
+-----------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| VipId           | xs:string                   | **Required** | Single       | Specifies the ID of the organization.    | If the field is invalid, then the        |
|                 |                             |              |              | VIP uses FIPS_ codes for this ID.        | implementation is required to ignore the |
|                 |                             |              |              |                                          | ``Source`` element containing it.        |
+-----------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| DateTime        | xs:dateTime                 | **Required** | Single       | Specifies the date and time of the feed  | If the field is invalid, then the        |
|                 |                             |              |              | production. The date/time is considered  | implementation is required to ignore it. |
|                 |                             |              |              | to be in the timezone local to the       |                                          |
|                 |                             |              |              | organization.                            |                                          |
+-----------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Description     | :doc:`InternationalizedText | Optional     | Single       | Specifies both the nature of the         | If the element is invalid or not         |
|                 | <internationalized_text>`   |              |              | organization providing the data and what | present, then the implementation is      |
|                 |                             |              |              | data is in the feed.                     | required to ignore it.                   |
+-----------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OrganizationUri | xs:string                   | Optional     | Single       | Specifies a URI to the home page of the  | If the field is invalid or not present,  |
|                 |                             |              |              | organization publishing the data.        | then the implementation is required to   |
|                 |                             |              |              |                                          | ignore it.                               |
+-----------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| FeedContactId   | xs:IDREF                    | Optional     | Single       | Reference to the :doc:`person <person>`  | If the field is invalid or not present,  |
|                 |                             |              |              | who will respond to inquiries about the  | then the implementation is required to   |
|                 |                             |              |              | information contained within the file.   | ignore it.                               |
+-----------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| TouUri          | xs:anyURI                   | Optional     | Single       | Specifies the website where the Terms of | If the field is invalid or not present,  |
|                 |                             |              |              | Use for the information in this file can | then the implementation is required to   |
|                 |                             |              |              | be found.                                | ignore it.                               |
+-----------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Version         | xs:string                   | **Required** | Single       | Specifies the version of the data        | If the field is invalid, then the        |
|                 |                             |              |              |                                          | implementation is required to ignore it. |
+-----------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

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


.. _single-xml-state:

State
~~~~~

The State object includes state-wide election information. The ID attribute is
recommended to be the state's FIPS code, along with the prefix "st".

+--------------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                      | Data Type                                       | Required?    | Repeats?     | Description                              | Error Handling                           |
+==========================+=================================================+==============+==============+==========================================+==========================================+
| ElectionAdministrationId | xs:IDREF                                        | Optional     | Single       | Links to the state's election            | If the field is invalid or not present,  |
|                          |                                                 |              |              | administration object.                   | then the implementation is required to   |
|                          |                                                 |              |              |                                          | ignore it.                               |
+--------------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ExternalIdentifiers      | :doc:`ExternalIdentifiers                       | Optional     | Single       | Other identifier for the state that      | If the element is invalid or not         |
|                          | </built_rst/xml/elements/external_identifiers>` |              |              | relates to another dataset (e.g.         | present, then the implementation is      |
|                          |                                                 |              |              | `OCD-ID`_).                              | required to ignore it.                   |
+--------------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Name                     | xs:string                                       | **Required** | Single       | Specifiers the name of a state, such as  | If the field is invalid, then the        |
|                          |                                                 |              |              | Alabama.                                 | implementation is required to ignore it. |
+--------------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PollingLocationId        | xs:IDREF                                        | Optional     | Repeats      | Specifies a link to the state's          | If the field is invalid or not present,  |
|                          |                                                 |              |              | :doc:`polling locations                  | then the implementation is required to   |
|                          |                                                 |              |              | <polling_location>`. If early vote       | ignore it.                               |
|                          |                                                 |              |              | centers or ballot drop locations are     |                                          |
|                          |                                                 |              |              | state-wide (e.g., anyone in the state    |                                          |
|                          |                                                 |              |              | can use them), they can be specified     |                                          |
|                          |                                                 |              |              | here, but you are encouraged to only use |                                          |
|                          |                                                 |              |              | the :doc:`Precinct <precinct>` element.  |                                          |
+--------------------------+-------------------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. _OCD-ID: http://opencivicdata.readthedocs.org/en/latest/ocdids.html

.. code-block:: xml
   :linenos:

   <State id="st51">
      <ElectionAdministrationId>ea40133</ElectionAdministrationId>
      <ExternalIdentifiers>
        <ExternalIdentifier>
          <Type>ocd-id</Type>
          <Value>ocd-division/country:us/state:va</Value>
        </ExternalIdentifier>
      </ExternalIdentifiers>
      <Name>Virginia</Name>
   </State>


.. _single-xml-street-segment:

StreetSegment
~~~~~~~~~~~~~

A Street Segment objection represents a portion of a street and the links to the precinct that this
geography (i.e., segment) is contained within. The start address house number must be less than the
end address house number unless the segment consists of only one address, in which case these values
are equal.

+----------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                  | Data Type                   | Required?    | Repeats?     | Description                              | Error Handling                           |
+======================+=============================+==============+==============+==========================================+==========================================+
| AddressDirection     | xs:string                   | Optional     | Single       | Specifies the (inter-)cardinal direction | If the field is invalid or not present,  |
|                      |                             |              |              | of the entire address. An example is     | then the implementation is required to   |
|                      |                             |              |              | "NE" for the address "100 E Capitol St   | ignore it.                               |
|                      |                             |              |              | NE."                                     |                                          |
+----------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| City                 | xs:string                   | **Required** | Single       | The city specifies the city or town of   | If the field is invalid, then the        |
|                      |                             |              |              | the address.                             | implementation is required to ignore it. |
+----------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| IncludesAllAddresses | xs:boolean                  | Optional     | Single       | Specifies if the segment covers every    | If the field is invalid or not present,  |
|                      |                             |              |              | address on this street. If this is       | then the implementation is required to   |
|                      |                             |              |              | *true*, then the values of               | ignore it.                               |
|                      |                             |              |              | **StartHouseNumber** and                 |                                          |
|                      |                             |              |              | **EndHouseNumber** should be ignored.    |                                          |
|                      |                             |              |              | The value of **OddEvenBoth** must be     |                                          |
|                      |                             |              |              | *both*.                                  |                                          |
+----------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OddEvenBoth          | :doc:`OebEnum               | **Required** | Single       | Specifies whether the odd side of the    | If the field is not present or invalid,  |
|                      | <../enumerations/oeb_enum>` |              |              | street (in terms of house numbers), the  | the implementation is required to ignore |
|                      |                             |              |              | even side, or both are in included in    | the StreetSegment containing it.         |
|                      |                             |              |              | the street segment.                      |                                          |
+----------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| PrecinctId           | xs:IDREF                    | Optional     | Single       | References the :doc:`precinct            | If the field is not present or invalid,  |
|                      |                             |              |              | <precinct>` that contains the entire     | the implementation is required to ignore |
|                      |                             |              |              | street segment.                          | the StreetSegment element containing it. |
+----------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| StartHouseNumber     | xs:integer                  | Optional     | Single       | The house number at which the street     | Unless **IncludesAllAddresses** is true, |
|                      |                             |              |              | segment starts. This value is necessary  | if the field is not present or invalid,  |
|                      |                             |              |              | for the street segment to make any       | the implementation is required to ignore |
|                      |                             |              |              | sense. Unless **IncludesAllAddresses**   | the StreetSegment element containing it. |
|                      |                             |              |              | is true, this value must be less than or | If the **StartHouseNumber** is greater   |
|                      |                             |              |              | equal to **EndHouseNumber**. If          | than the **EndHouseNumber**, the         |
|                      |                             |              |              | **IncludesAllAddresses** is true, this   | implementation should ignore the element |
|                      |                             |              |              | value is ignored.                        | containing them.                         |
+----------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| EndHouseNumber       | xs:integer                  | Optional     | Single       | The house number at which the street     | Unless **IncludesAllAddresses** is true, |
|                      |                             |              |              | segment ends. This value is necessary    | if the field is not present or invalid,  |
|                      |                             |              |              | for the street segment to make any       | the implementation is required to ignore |
|                      |                             |              |              | sense. Unless **IncludesAllAddresses**   | the StreetSegment element containing it. |
|                      |                             |              |              | is true, it must be greater than or      | If the **EndHouseNumber** is less than   |
|                      |                             |              |              | equal to **StartHouseNumber**. If        | the **StartHouseNumber**, the            |
|                      |                             |              |              | **IncludesAllAddresses** is true, this   | implementation should ignore the element |
|                      |                             |              |              | value is ignored.                        | containing it.                           |
+----------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| State                | xs:string                   | **Required** | Single       | Specifies the two-letter state           | If the field is invalid, then the        |
|                      |                             |              |              | abbreviation of the address.             | implementation is required to ignore it. |
+----------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| StreetDirection      | xs:string                   | Optional     | Single       | Specifies the (inter-)cardinal direction | If the field is invalid or not present,  |
|                      |                             |              |              | of the street address (e.g., the "E" in  | then the implementation is required to   |
|                      |                             |              |              | "100 E Capitol St NE").                  | ignore it.                               |
+----------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| StreetName           | xs:string                   | **Required** | Single       | Represents the name of the street for    | If the field is invalid, then the        |
|                      |                             |              |              | the address. A special wildcard, "*",    | implementation is required to ignore it. |
|                      |                             |              |              | denotes every street in the given        |                                          |
|                      |                             |              |              | city/town. It optionally may contain     |                                          |
|                      |                             |              |              | street direction, street suffix or       |                                          |
|                      |                             |              |              | address direction (e.g., both "Capitol"  |                                          |
|                      |                             |              |              | and "E Capitol St NE" are acceptable for |                                          |
|                      |                             |              |              | the address "100 E Capitol St NE"),      |                                          |
|                      |                             |              |              | however this is not preferred. Preferred |                                          |
|                      |                             |              |              | is street name alone (e.g. "Capitol").   |                                          |
+----------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| StreetSuffix         | xs:string                   | Optional     | Single       | Represents the abbreviated,              | If the field is invalid or not present,  |
|                      |                             |              |              | non-directional suffix to the street     | then the implementation is required to   |
|                      |                             |              |              | name. An example is "St" for the address | ignore it.                               |
|                      |                             |              |              | "100 E Capitol St NE."                   |                                          |
+----------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| UnitNumber           | xs:string                   | Optional     | Repeats      | The apartment/unit number for a street   | If the field is invalid or not present,  |
|                      |                             |              |              | segment. If this value is present then   | then the implementation is required to   |
|                      |                             |              |              | **StartHouseNumber** must be equal to    | ignore it.                               |
|                      |                             |              |              | **EndHouseNumber**. This field cannot be |                                          |
|                      |                             |              |              | used if **IncludesAllAddresses** is      |                                          |
|                      |                             |              |              | true.                                    |                                          |
+----------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Zip                  | xs:string                   | **Required** | Single       | Specifies the zip code of the address.   | If the field is invalid, then the        |
|                      |                             |              |              | It may be 5 or 9 digits, and it may      | implementation is required to ignore it. |
|                      |                             |              |              | include a hyphen ('-'). It is required   |                                          |
|                      |                             |              |              | as it helps with geocoding, which is     |                                          |
|                      |                             |              |              | crucial for distributors.                |                                          |
+----------------------+-----------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

   <StreetSegment id="ss999999">
      <City>Charlottesville</City>
      <IncludesAllAddresses>true</IncludesAllAddresses>
      <OddEvenBoth>both</OddEvenBoth>
      <PrecinctId>pre99999</PrecinctId>
      <State>VA</State>
      <StreetName>CHAPEL HILL</StreetName>
      <StreetSuffix>RD</StreetSuffix>
      <Zip>22901</Zip>
   </StreetSegment>
   <StreetSegment id="ss309904">
      <City>GREENWOOD</City>
      <OddEvenBoth>both</OddEvenBoth>
      <PrecinctId>pre92145</PrecinctId>
      <StartHouseNumber>1</StartHouseNumber>
      <EndHouseNumber>201</EndHouseNumber>
      <State>VA</State>
      <StreetName>MISTY MOUNTAIN</StreetName>
      <StreetSuffix>RD</StreetSuffix>
      <Zip>22943</Zip>
   </StreetSegment>


.. _single-xml-term:

Term
~~~~

+--------------+-------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type                           | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+=====================================+==============+==============+==========================================+==========================================+
| Type         | :doc:`OfficeTermType                | **Required** | Single       | Specifies the type of office term (see   | If the field is invalid or not present,  |
|              | <../enumerations/office_term_type>` |              |              | :doc:`OfficeTermType                     | the implementation is required to ignore |
|              |                                     |              |              | <../enumerations/office_term_type>` for  | the ``Office`` element containing it.    |
|              |                                     |              |              | valid values).                           |                                          |
+--------------+-------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| StartDate    | xs:date                             | Optional     | Single       | Specifies the start date for the current | If the field is invalid or not present,  |
|              |                                     |              |              | term of the office.                      | then the implementation is required to   |
|              |                                     |              |              |                                          | ignore it.                               |
+--------------+-------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| EndDate      | xs:date                             | Optional     | Single       | Specifies the end date for the current   | If the field is invalid or not present,  |
|              |                                     |              |              | term of the office.                      | then the implementation is required to   |
|              |                                     |              |              |                                          | ignore it.                               |
+--------------+-------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

   <Office id="off0000">
     <ElectoralDistrictId>ed60129</ElectoralDistrictId>
     <FilingDeadline>2013-01-01</FilingDeadline>
     <IsPartisan>false</IsPartisan>
     <Name>
       <Text language="en">Governor</Text>
     </Name>
     <Term>
       <Type>full-term</Type>
     </Term>
   </Office>


.. _single-xml-time-with-zone:

TimeWithZone
~~~~~~~~~~~~

A string pattern restricting the value to a time with an included offset from
UTC. The pattern is

``(([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]|(24:00:00))(Z|[+-]((0[0-9]|1[0-3]):[0-5][0-9]|14:00))``

.. code-block:: xml
   :linenos:

   <HoursOpen id="hours0001">
     <Schedule>
       <Hours>
         <StartTime>06:00:00-05:00</StartTime>
         <EndTime>12:00:00-05:00</EndTime>
       </Hours>
       <Hours>
         <StartTime>13:00:00-05:00</StartTime>
         <EndTime>19:00:00-05:00</EndTime>
       </Hours>
       <StartDate>2013-11-05</StartDate>
       <EndDate>2013-11-05</EndDate>
     </Schedule>
   </HoursOpen>


.. _single-xml-voter-service:

VoterService
~~~~~~~~~~~~

+--------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag                      | Data Type                             | Required?    | Repeats?     | Description                              | Error Handling                           |
+==========================+=======================================+==============+==============+==========================================+==========================================+
| ContactInformation       | :doc:`ContactInformation              | Optional     | Single       | The contact for a particular voter       | If the element is invalid or not         |
|                          | <contact_information>`                |              |              | service.                                 | present, then the implementation is      |
|                          |                                       |              |              |                                          | required to ignore it.                   |
+--------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Description              | :doc:`InternationalizedText           | Optional     | Single       | Long description of the services         | If the element is invalid or not         |
|                          | <internationalized_text>`             |              |              | available.                               | present, then the implementation is      |
|                          |                                       |              |              |                                          | required to ignore it.                   |
+--------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| ElectionOfficialPersonId | xs:IDREF                              | Optional     | Single       | The :doc:`authority <person>` for a      | If the field is invalid or not present,  |
|                          |                                       |              |              | particular voter service.                | then the implementation is required to   |
|                          |                                       |              |              |                                          | ignore it.                               |
+--------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Type                     | :doc:`VoterServiceType                | Optional     | Single       | The type of :doc:`voter service          | If the field is invalid or not present,  |
|                          | <../enumerations/voter_service_type>` |              |              | <../enumerations/voter_service_type>`.   | then the implementation is required to   |
|                          |                                       |              |              |                                          | ignore it.                               |
+--------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| OtherType                | xs:string                             | Optional     | Single       | If Type is "other", OtherType allows for | If the field is invalid or not present,  |
|                          |                                       |              |              | cataloging another type of voter         | then the implementation is required to   |
|                          |                                       |              |              | service.                                 | ignore it.                               |
+--------------------------+---------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

   <ElectionAdministration id="ea40133">
      <AbsenteeUri>http://www.sbe.virginia.gov/absenteevoting.html</AbsenteeUri>
      <AmIRegisteredUri>https://www.vote.virginia.gov/</AmIRegisteredUri>
      <Department>
        <ContactInformation label="ci60000">
          <AddressLine>Washington Building First Floor</AddressLine>
          <AddressLine>1100 Bank Street</AddressLine>
          <AddressLine>Richmond, VA 23219</AddressLine>
          <Name>State Board of Elections</Name>
        </ContactInformation>
      </Department>
      <ElectionsUri>http://www.sbe.virginia.gov/</ElectionsUri>
      <RegistrationUri>https://www.vote.virginia.gov/</RegistrationUri>
      <RulesUri>http://www.sbe.virginia.gov/</RulesUri>
      <WhatIsOnMyBallotUri>https://www.vote.virginia.gov/</WhatIsOnMyBallotUri>
      <WhereDoIVoteUri>https://www.vote.virginia.gov/</WhereDoIVoteUri>
   </ElectionAdministration>


.. _single-xml-enumerations:

Enumerations
------------


.. _single-xml-ballot-measure-type:

BallotMeasureType
~~~~~~~~~~~~~~~~~

A list of the various types of ballot measures. States may have different legal
definitions of each type; Wikipedia_ has more details about each type.  These
values are to help states with multiple types of non-candidate-based contests
distinguish between each type; as such, the definitions in this table are simple
guidelines. Ultimately it is up to the state or local election official to
choose the value which best describes the ballot measure(s) in their
jurisdiction.

+----------------+----------------------------------------------------+
| Tag            | Description                                        |
+================+====================================================+
| ballot-measure | A catch-all for generic types of                   |
|                | non-candidate-based contests.                      |
+----------------+----------------------------------------------------+
| initiative     | These are usually citizen-driven measures to be    |
|                | placed on the ballot. These could include both     |
|                | statutory changes and constitutional amendments.   |
+----------------+----------------------------------------------------+
| referendum     | These could include measures to repeal existing    |
|                | acts of legislation, legislative referrals, and    |
|                | legislatively-referred state constitutional        |
|                | amendments.                                        |
+----------------+----------------------------------------------------+
| other          | Anything that does not fall into the above         |
|                | categories.                                        |
+----------------+----------------------------------------------------+

.. _Wikipedia: http://en.wikipedia.org/wiki/Initiatives_and_referendums_in_the_United_States


.. _single-xml-candidate-post-election-status:

CandidatePostElectionStatus
~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------+----------------------------------------------------+
| Tag                | Description                                        |
+====================+====================================================+
| advanced-to-runoff | For contests in which the top *N* candidates       |
|                    | advance to the next round.                         |
+--------------------+----------------------------------------------------+
| projected-winner   | A candidate is expected to win, but official       |
|                    | results are not yet complete.                      |
+--------------------+----------------------------------------------------+
| winner             | The candidate has officially won.                  |
+--------------------+----------------------------------------------------+
| withdrawn          | The candidate has withdrawn from the contest.      |
+--------------------+----------------------------------------------------+


.. _single-xml-candidate-pre-election-status:

CandidatePreElectionStatus
~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------+----------------------------------------------------+
| Tag          | Description                                        |
+==============+====================================================+
| filed        | The candidate has filed for office but not yet     |
|              | been qualified.                                    |
+--------------+----------------------------------------------------+
| qualified    | The candidate has qualified for the contest.       |
+--------------+----------------------------------------------------+
| withdrawn    | The candidate has withdrawn from the contest (but  |
|              | may still be on the ballot).                       |
+--------------+----------------------------------------------------+
| write-in     |                                                    |
+--------------+----------------------------------------------------+


.. _single-xml-district-type:

DistrictType
~~~~~~~~~~~~

Enumeration describing the set of possible jurisdiction and district types.
Please use the enumeration value which most accurately reflects the type of
district or jurisdiction in your state or county. For example, "town" and
"township" may mean different things -- or not be defined at all -- in your
state, so please use the definition which best matches your local meaning.

+----------------+----------------------------------------------------+
| Tag            | Description                                        |
+================+====================================================+
| city           | A city.                                            |
+----------------+----------------------------------------------------+
| city-council   | A specific seat/jurisdiction for a city, town, or  |
|                | village council.                                   |
+----------------+----------------------------------------------------+
| congressional  | A United States congressional district.            |
+----------------+----------------------------------------------------+
| county         | A county.                                          |
+----------------+----------------------------------------------------+
| county-council | A county council district, either in its entirety  |
|                | or for a specific seat.                            |
+----------------+----------------------------------------------------+
| judicial       | A judicial district.                               |
+----------------+----------------------------------------------------+
| municipality   | A civil division which is not a town, city,        |
|                | village, or county.                                |
+----------------+----------------------------------------------------+
| national       | The United States.                                 |
+----------------+----------------------------------------------------+
| school         | A school district.                                 |
+----------------+----------------------------------------------------+
| special        | A `special-purpose district`_ that exist separate  |
|                | from general-purpose districts.                    |
+----------------+----------------------------------------------------+
| state          | A state, district, commonwealth, or U.S.           |
|                | territory.                                         |
+----------------+----------------------------------------------------+
| state-house    | The lower house of a state legislature.            |
+----------------+----------------------------------------------------+
| state-senate   | The upper house of a state legislature.            |
+----------------+----------------------------------------------------+
| town           | A town_.                                           |
+----------------+----------------------------------------------------+
| township       | A township, which may be different than a town.    |
|                | See the `Wikipedia article`_.                      |
+----------------+----------------------------------------------------+
| utility        | A non-water public or municipal utility district.  |
+----------------+----------------------------------------------------+
| village        | A village district.                                |
+----------------+----------------------------------------------------+
| ward           | A ward.                                            |
+----------------+----------------------------------------------------+
| water          | A water district.                                  |
+----------------+----------------------------------------------------+
| other          | Any district not described above. Use the          |
|                | *OtherType* field to describe it.                  |
+----------------+----------------------------------------------------+

.. _`special-purpose district`: http://en.wikipedia.org/wiki/Special-purpose_district
.. _town: http://en.wikipedia.org/wiki/Town#United_States
.. _`Wikipedia article`: http://en.wikipedia.org/wiki/Town#United_States


.. _single-xml-identifier-type:

IdentifierType
~~~~~~~~~~~~~~

+----------------+----------------------------------------------------+
| Tag            | Description                                        |
+================+====================================================+
| fips           | Federal Information Processing Standards codes for |
|                | states_, counties_, and cities_.                   |
+----------------+----------------------------------------------------+
| local-level    | An identifier generated or used by local           |
|                | governments or organizations.                      |
+----------------+----------------------------------------------------+
| national-level | An identifier generated or used by national        |
|                | organizations.                                     |
+----------------+----------------------------------------------------+
| ocd-id         | An `Open Civic Data Division Identifier`_.         |
+----------------+----------------------------------------------------+
| state-level    | An identifier generated or used by state           |
|                | governments or organizations.                      |
+----------------+----------------------------------------------------+
| other          | Any identifier which doesn't fall into any of the  |
|                | above categories.                                  |
+----------------+----------------------------------------------------+

.. _states: http://en.wikipedia.org/wiki/Federal_Information_Processing_Standard_state_code
.. _counties: http://en.wikipedia.org/wiki/FIPS_county_code
.. _cities: http://geonames.usgs.gov/domestic/fips55codedef.html
.. _`Open Civic Data Division Identifier`: http://docs.opencivicdata.org/en/latest/proposals/0002.html


.. _single-xml-oeb-enum:

OebEnum
~~~~~~~

+--------------+----------------------------------------------------+
| Tag          | Description                                        |
+==============+====================================================+
| both         | Both even and odd addresses within the range.      |
+--------------+----------------------------------------------------+
| even         | Only even-numbered addresses within the range.     |
+--------------+----------------------------------------------------+
| odd          | Only odd-numbered addresses within the range.      |
+--------------+----------------------------------------------------+


.. _single-xml-office-term-type:

OfficeTermType
~~~~~~~~~~~~~~

+----------------+----------------------------------------------------+
| Tag            | Description                                        |
+================+====================================================+
| full-term      | This election is for an office for which the       |
|                | existing term has been completed.                  |
+----------------+----------------------------------------------------+
| unexpired-term | This election is for an office for which the       |
|                | original term is not yet complete.                 |
+----------------+----------------------------------------------------+


.. _single-xml-vote-variation:

VoteVariation
~~~~~~~~~~~~~

Note that the descriptions below describe what the enumeration names
stand for in the context of the VIP spec, rather than provide general
definitions of the election terms that the names correspond to.  For example,
even though there are majority voting methods that are not "1-of-m" (e.g.
ranked choice voting), we constrain "majority" to 1-of-m.  We do this to
eliminate any source of ambiguity when a single enumeration value needs
to be assigned to a contest.

+----------------+----------------------------------------------------+
| Tag            | Description                                        |
+================+====================================================+
| 1-of-m         | A method where each voter can select up to one     |
|                | option.                                            |
+----------------+----------------------------------------------------+
| approval       | `Approval voting`_, where each voter can select as |
|                | many options as desired.                           |
+----------------+----------------------------------------------------+
| borda          | `Borda count`_, where each voter can rank the      |
|                | options, and the rankings are assigned point       |
|                | values.                                            |
+----------------+----------------------------------------------------+
| cumulative     | `Cumulative voting`_, where each voter can         |
|                | distribute their vote to up to *N* options.        |
+----------------+----------------------------------------------------+
| majority       | A 1-of-m method where the winner needs more than   |
|                | 50% of the vote to be elected.                     |
+----------------+----------------------------------------------------+
| n-of-m         | A method where each voter can select up to *N*     |
|                | options.                                           |
+----------------+----------------------------------------------------+
| plurality      | A 1-of-m method where the option with the most     |
|                | votes is elected, regardless of whether the option |
|                | has more than 50% of the vote.                     |
+----------------+----------------------------------------------------+
| proportional   | A `proportional representation`_ method (other     |
|                | than STV), which is any system that elects winners |
|                | in proportion to the total vote.                   |
+----------------+----------------------------------------------------+
| range          | `Range voting`_, where each voter can select a     |
|                | score for each option.                             |
+----------------+----------------------------------------------------+
| rcv            | `Ranked choice voting`_ (RCV), where each voter    |
|                | can rank the options, and the ballots are counted  |
|                | in rounds.  Also known as instant-runoff voting    |
|                | (IRV) and the single transferable vote (STV).      |
+----------------+----------------------------------------------------+
| super-majority | A 1-of-m method where the winner needs more than   |
|                | some predetermined fraction of the vote to be      |
|                | elected, where the fraction is more than 50% (e.g. |
|                | three-fifths or two-thirds).                       |
+----------------+----------------------------------------------------+
| other          | Used when the vote variation type is not included  |
|                | in this enumeration.                               |
+----------------+----------------------------------------------------+

.. _`Approval voting`: http://en.wikipedia.org/wiki/Approval_voting
.. _`Borda count`: http://en.wikipedia.org/wiki/Borda_count
.. _`Cumulative voting`: http://en.wikipedia.org/wiki/Cumulative_voting
.. _`proportional representation`: https://en.wikipedia.org/wiki/Proportional_representation
.. _`Range voting`: http://en.wikipedia.org/wiki/Range_voting
.. _`Ranked choice voting`: http://http://en.wikipedia.org/wiki/Ranked_Choice_Voting


.. _single-xml-voter-service-type:

VoterServiceType
~~~~~~~~~~~~~~~~

+--------------------+----------------------------------------------------+
| Tag                | Description                                        |
+====================+====================================================+
| absentee-ballots   | This department handles the dispatch, tracking,    |
|                    | and return of absentee ballots.                    |
+--------------------+----------------------------------------------------+
| overseas-voting    | The department for overseas, military, and other   |
|                    | outside-the-U.S. voters.                           |
+--------------------+----------------------------------------------------+
| polling-places     | This deparment handles the selection and           |
|                    | management of polling places.                      |
+--------------------+----------------------------------------------------+
| voter-registration | The deparment that manages voter registration.     |
+--------------------+----------------------------------------------------+
| other              | Any other service not covered by the above         |
|                    | descriptions.                                      |
+--------------------+----------------------------------------------------+
