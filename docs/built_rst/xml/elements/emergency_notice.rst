.. This file is auto-generated.  Do not edit it by hand!

.. _multi-xml-emergency-notice:

EmergencyNotice
===============

A notification for election administrators to post emergency or last-minute updates (e.g. polling place relocations, hours extensions, severe weather alerts).

In VIP 7.0, EmergencyNotice elements are permitted only in feed overlays on :ref:`multi-xml-locality`, :ref:`multi-xml-polling-location`, and :ref:`multi-xml-precinct` elements.

+--------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| Tag          | Data Type                               | Required?    | Repeats?     | Description                              | Error Handling                           |
+==============+=========================================+==============+==============+==========================================+==========================================+
| NoticeText   | :ref:`multi-xml-internationalized-text` | Optional     | Single       | The emergency notification text, which   | If the element is invalid or not         |
|              |                                         |              |              | may be localized in multiple languages.  | present, then the implementation is      |
|              |                                         |              |              |                                          | required to ignore it.                   |
+--------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| NoticeUri    | :ref:`multi-xml-internationalized-uri`  | Optional     | Single       | Web address for additional information   | If the element is invalid or not         |
|              |                                         |              |              | regarding the emergency notice.          | present, then the implementation is      |
|              |                                         |              |              |                                          | required to ignore it.                   |
+--------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+
| AppliesTo    | ``xs:string``                           | Optional     | Repeats      | If specified, the serving contexts in    | If the field is invalid or not present,  |
|              |                                         |              |              | which this emergency notice applies      | then the implementation is required to   |
|              |                                         |              |              | (e.g. "api", "search", "maps"). If       | ignore it.                               |
|              |                                         |              |              | omitted, applies generally across all    |                                          |
|              |                                         |              |              | serving contexts.                        |                                          |
+--------------+-----------------------------------------+--------------+--------------+------------------------------------------+------------------------------------------+

.. code-block:: xml
   :linenos:

   <EmergencyNotice>
      <NoticeText>
         <Text language="i-default">Polling location moved due to water main break.</Text>
         <Text language="es">El centro de votación se ha trasladado debido a una rotura de tubería.</Text>
      </NoticeText>
      <NoticeUri>https://elections.example.gov/notices/precinct-203</NoticeUri>
      <AppliesTo>search</AppliesTo>
      <AppliesTo>maps</AppliesTo>
   </EmergencyNotice>
