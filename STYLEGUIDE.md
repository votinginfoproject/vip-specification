# Coding Styles


## Text Files

This section applies to all text files in the repository (XML, HTML,
Markdown, etc).

* The file encoding should be UTF-8.

* Line endings should be LF (as opposed to CRLF).  Git should handle this
  automatically for you via the project [`.gitattributes`](.gitattributes) file.

* Trailing white space should be removed from the end of lines.

* Spaces should be used instead of tabs.  See the file-type specific
  section for how many spaces should be used for indentations.


## XSD Styles

### Indentation

* Two-space indents should be used (e.g. in place of tabs).


### Casing

+ Attributes should be camelCased - The first letter of the second and subsequent words are capitalized.
+ Elements should be TitleCased (PascalCased) - The first letter of every word is capitalized.
+ Enumerations should be spinal-case - all lower case with spaces replaced with hyphens.


### Type Names

* Type names should only end in "Type" if _instances_ of the type correspond
  to types.  For example, instances of the "Candidate" type represent
  candidates rather than types of candidates.  In contrast, "OfficeTermType"
  instances correspond to the different types of office terms:

  ```xml
  <xs:simpleType name="OfficeTermType">
    <xs:restriction base="xs:string">
      <xs:enumeration value="full-term" />
      <xs:enumeration value="unexpired-term" />
    </xs:restriction>
  </xs:simpleType>
  ```

* The names of abstract "base class" types should end in "Base" as a
  reminder that the types should not be instantiated directly.


### IDs

* A primary key ID should be an attribute with type "xs:ID" and name "id".
  For example,

    ```xml
    <xs:attribute name="id" type="xs:ID" use="required" />
    ````
  Note that this departs from the style used by [VSSC 1622.2][vssc_1622],
  where the name is "object_id".

* A reference to a primary key should have type "xs:IDREF".  The name
  of the element or attribute should normally end with the name of the type
  of the object being referenced, followed by "Id" (and made TitleCased or
  camelCased as appropriate).  For example,

    ```xml
    <xs:element name="ElectoralDistrictId" type="xs:IDREF" />
    ````


### Attributes

Attributes should appear in the following order:

1. name
2. type
3. minOccurs
4. maxOccurs

Any attributes not listed above should appear after those listed.  Also,
a single space should separate the final attribute from the closing "`/>`".
For example--

```xml
<xs:attribute name="id" type="xs:ID" use="required" />
```


### Type Definitions: Global vs. Local

This subsection describes when a type definition should be "global"
(i.e. named and an immediate child of "xs:schema") versus
"local" (i.e. anonymous and nested within another component, aka in-lined).

Global might look like--

```xml
<xs:schema>
  <xs:complexType name="Person">
    <xs:element name="Name" type="xs:string" />
  </xs:complexType>
  ...
```

Local might look like--

```xml
<xs:element name="Person">
  <xs:complexType>
    <xs:element name="Name" type="xs:string" />
  </xs:complexType>
</xs:element>
```

Our approach is in the spirit of "Venetian Blind."  Define a type globally
if any of the following are true:

1. elements of the type are referenced by ID via `type="xs:IDREF"`.
   For example--

   ```xml
   <xs:element name="PrecinctId" type="xs:IDREF" />
   ```

2. elements of the type occur in more than one location within the
   root element.  For example--

   ```xml
   <xs:element name="Title" type="InternationalizedText" />
   <xs:element name="Subtitle" type="InternationalizedText" />
   ```

3. the type is an "enum".  For example--

   ```xml
   <xs:simpleType name="OebEnum">
     <xs:restriction base="xs:string">
       <xs:enumeration value="odd" />
       <xs:enumeration value="even" />
       <xs:enumeration value="both" />
     </xs:restriction>
   </xs:simpleType>
   ```


### Global Type Definition Ordering

Global type definitions should be ordered as follows:

1. Put global type definitions before the root element.

2. Group them in the following order: enumerations, other simple types,
   then complex types.

3. Within each of the groups in (2) above, order them alphabetically by name.


## CSV Styles
To be determined


[vssc_1622]: http://grouper.ieee.org/groups/1622/groups/2/index.html
