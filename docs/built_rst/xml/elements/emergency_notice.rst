.. This file is auto-generated.  Do not edit it by hand!

.. _multi-xml-emergency-notice:

EmergencyNotice
===============

A notification for election administrators to post emergency or last-minute updates (e.g. polling place relocations, hours extensions, severe weather alerts).

In VIP 7.0, EmergencyNotice elements are permitted only in feed overlays on :ref:`multi-xml-locality`, :ref:`multi-xml-polling-location`, and :ref:`multi-xml-precinct` elements.

+--------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type                               | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+=========================================+==============+==============+==========================================+==========================================+
| NoticeText   | :ref:`multi-xml-internationalized-text` | Optional     | Repeats      | The emergency notification text, which   | If the element is invalid or not         |
|              |                                         |              |              | may be localized in multiple languages.  | present, then the implementation is      |
|              |                                         |              |              |                                          | required to ignore it.                   |
+--------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| NoticeUri    | :ref:`multi-xml-internationalized-uri`  | Optional     | Single       | Web address for additional information   | If the element is invalid or not         |
|              |                                         |              |              | regarding the emergency notice.          | present, then the implementation is      |
|              |                                         |              |              |                                          | required to ignore it.                   |
+--------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| AppliesTo    | ``xs:string``                           | Optional     | Repeats      | If specified, the contexts in which this | If the field is invalid or not present,  |
|              |                                         |              |              | emergency notice applies (e.g.           | then the implementation is required to   |
|              |                                         |              |              | "polling_place", "vote_center",          | ignore it.                               |
|              |                                         |              |              | "ballot_drop_box", "jurisdiction"). If   |                                          |
|              |                                         |              |              | omitted, applies generally.              |                                          |
+--------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

   <EmergencyNotice>
      <NoticeText>
         <Text language="en">Polling location moved due to water main break.</Text>
         <Text language="es">El centro de votación se ha trasladado debido a una rotura de tubería.</Text>
      </NoticeText>
      <NoticeUri>https://elections.example.gov/notices/precinct-203</NoticeUri>
      <AppliesTo>polling_place</AppliesTo>
   </EmergencyNotice>
