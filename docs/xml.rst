XML Specification
=================

.. contents::
   :local:


.. _xml-getting-started:

Getting Started
---------------

The election data specification describes a collection of interconnected entities encapsulated in a root object named ``<VipObject>`` with attribute ``schemaVersion="7.0"``. See the `sample xml file`_ and `xsd file`_ for more details.

Each top-level tag is a container for other fields, described in its own section below. The only required
top-level tags are the :doc:`Source object <built_rst/xml/elements/source>` and the
:doc:`Election object <built_rst/xml/elements/election>`, each of which must be present exactly once. All other
top-level tags can be repeated an unlimited number of times, or not included at all; order of
top-level tags does not matter. Each top-level entity is required to have a unique "id" attribute.

In VIP 7.0, political geography is represented hierarchically using the :doc:`Locality object <built_rst/xml/elements/locality>` (which replaces the former ``State`` element). The state-level jurisdiction is represented as a root ``<Locality>`` element with ``Type="state"`` (and typically has an ID based on the state's FIPS code, e.g. ``loc51``). Sub-jurisdictions (such as counties, cities, and towns) point to their enclosing jurisdiction using ``ParentLocalityId``. The :doc:`Election <built_rst/xml/elements/election>` element connects to the state via ``TopLevelLocalityId``.

In addition to full base feeds, VIP 7.0 introduces :doc:`Feed Overlays <overlay>` (defined in ``vip_overlay.xsd``) to distribute targeted delta updates, emergency notifications, and hours overrides.

In general, subtag data can appear a maximum of one time within each top-level tag object and in any
order, unless designated as repeating.

For character data, the XML special characters &, <, and > must be encoded as &amp;, &lt;, and &gt;,
respectively.

.. _sample xml file: https://github.com/votinginfoproject/vip-specification/blob/master/sample_feed.xml
.. _xsd file: https://github.com/votinginfoproject/vip-specification/blob/master/vip_spec.xsd


Elements & Enumerations
-----------------------


Single-page Format
~~~~~~~~~~~~~~~~~~

.. toctree::
   :maxdepth: 2
   :glob:

   built_rst/xml/single_page


Elements (Separate Pages)
~~~~~~~~~~~~~~~~~~~~~~~~~

.. toctree::
   :maxdepth: 2
   :glob:

   built_rst/xml/elements/*


Enumerations (Separate Pages)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. toctree::
   :maxdepth: 2
   :glob:

   built_rst/xml/enumerations/*
