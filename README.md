# chit_archives_scripts

Repo to store CHIT-related work on archival and manuscript metadata reconciliation

## Survey

### Metadata schemas and controlled vocabularies for agents and subjects currently in use by YUL special collections and BRBL

#### Metadata schemas

ArchivesSpace metadata schemas for agents and subjects:

* [abstract_agent](https://github.com/archivesspace/archivesspace/blob/master/common/schemas/abstract_agent.rb)
* [agent_person](https://github.com/archivesspace/archivesspace/blob/master/common/schemas/agent_person.rb)
* [agent_family](https://github.com/archivesspace/archivesspace/blob/master/common/schemas/agent_family.rb)
* [agent_corporate_entity](https://github.com/archivesspace/archivesspace/blob/master/common/schemas/agent_corporate_entity.rb)
* [agent_contact](https://github.com/archivesspace/archivesspace/blob/master/common/schemas/agent_contact.rb)
* [name_corporate_entity](https://github.com/archivesspace/archivesspace/blob/master/common/schemas/name_corporate_entity.rb)
* [name_family](https://github.com/archivesspace/archivesspace/blob/master/common/schemas/name_family.rb)
* [name_person](https://github.com/archivesspace/archivesspace/blob/master/common/schemas/name_person.rb)
* [telephone](https://github.com/archivesspace/archivesspace/blob/master/common/schemas/telephone.rb)
* [subject]
* [term]

ArchivesSpace documentation

* [Ruby YARD docs](http://archivesspace.github.io/archivesspace/doc/)
* [tech-docs](https://github.com/archivesspace/tech-docs)
* [API Docs](http://archivesspace.github.io/archivesspace/api/)


XML-based schemas:

* [EAC-CPF](https://eac.staatsbibliothek-berlin.de/schemata-and-tag-library/)
* [EAD 2002](https://www.loc.gov/ead/eadschema.html)
* [EAD 3](https://www.loc.gov/ead/EAD3taglib/index.html)

Example of JSON agent and subject records from ArchivesSpace

agent_person

```
{'agent_contacts': [{'address_1': 'The',
                     'address_2': 'Estate',
                     'address_3': 'Address',
                     'city': 'City',
                     'country': 'Country',
                     'create_time': '2020-02-20T16:42:59Z',
                     'created_by': 'amd243',
                     'email': 'Email',
                     'jsonmodel_type': 'agent_contact',
                     'last_modified_by': 'amd243',
                     'lock_version': 0,
                     'name': 'Estate of Doctor Sir Samuel Jones IV of Wales, '
                             'Esquire',
                     'note': 'Some contact notes',
                     'post_code': 'Code',
                     'region': 'State',
                     'salutation': 'dr',
                     'system_mtime': '2020-02-20T16:42:59Z',
                     'telephones': [{'create_time': '2020-02-20T16:42:59Z',
                                     'created_by': 'amd243',
                                     'ext': 'Here either',
                                     'jsonmodel_type': 'telephone',
                                     'last_modified_by': 'amd243',
                                     'number': 'Nothing says you need to put a '
                                               'number here',
                                     'number_type': 'home',
                                     'system_mtime': '2020-02-20T16:42:59Z',
                                     'uri': '/telephone/929',
                                     'user_mtime': '2020-02-20T16:42:59Z'},
                                    {'create_time': '2020-02-20T16:42:59Z',
                                     'created_by': 'amd243',
                                     'ext': 'but not a number',
                                     'jsonmodel_type': 'telephone',
                                     'last_modified_by': 'amd243',
                                     'number': 'another number',
                                     'number_type': 'fax',
                                     'system_mtime': '2020-02-20T16:42:59Z',
                                     'uri': '/telephone/930',
                                     'user_mtime': '2020-02-20T16:42:59Z'}],
                     'user_mtime': '2020-02-20T16:42:59Z'}],
 'agent_type': 'agent_person',
 'create_time': '2020-02-20T16:42:59Z',
 'created_by': 'amd243',
 'dates_of_existence': [{'begin': '1900',
                         'calendar': 'gregorian',
                         'certainty': 'approximate',
                         'create_time': '2020-02-20T16:42:59Z',
                         'created_by': 'amd243',
                         'date_type': 'range',
                         'end': '2000',
                         'era': 'ce',
                         'expression': '1900-2000',
                         'jsonmodel_type': 'date',
                         'label': 'existence',
                         'last_modified_by': 'amd243',
                         'lock_version': 0,
                         'system_mtime': '2020-02-20T16:42:59Z',
                         'user_mtime': '2020-02-20T16:42:59Z'}],
 'display_name': {'authority_id': 'http://id.loc.gov/authorities/names/testd_name',
                  'authorized': True,
                  'create_time': '2020-02-20T16:42:59Z',
                  'created_by': 'amd243',
                  'dates': '1900-2000',
                  'fuller_form': 'of Wales',
                  'is_display_name': True,
                  'jsonmodel_type': 'name_person',
                  'last_modified_by': 'amd243',
                  'lock_version': 0,
                  'name_order': 'inverted',
                  'number': 'IV',
                  'prefix': 'Doctor',
                  'primary_name': 'Samuel',
                  'qualifier': 'Qualified',
                  'rest_of_name': 'Jones',
                  'rules': 'dacs',
                  'sort_name': 'Samuel, Jones, Doctor, Esquire, Sir, IV (of '
                               'Wales), 1900-2000 (Qualified)',
                  'sort_name_auto_generate': True,
                  'source': 'naf',
                  'suffix': 'Esquire',
                  'system_mtime': '2020-02-20T16:42:59Z',
                  'title': 'Sir',
                  'use_dates': [{'begin': '1999',
                                 'calendar': 'gregorian',
                                 'certainty': 'approximate',
                                 'create_time': '2020-02-20T16:42:59Z',
                                 'created_by': 'amd243',
                                 'date_type': 'range',
                                 'end': '2000',
                                 'era': 'ce',
                                 'expression': '1999-2000',
                                 'jsonmodel_type': 'date',
                                 'label': 'usage',
                                 'last_modified_by': 'amd243',
                                 'lock_version': 0,
                                 'system_mtime': '2020-02-20T16:42:59Z',
                                 'user_mtime': '2020-02-20T16:42:59Z'}],
                  'user_mtime': '2020-02-20T16:42:59Z'},
 'external_documents': [{'create_time': '2020-02-20T16:42:59Z',
                         'created_by': 'amd243',
                         'jsonmodel_type': 'external_document',
                         'last_modified_by': 'amd243',
                         'location': 'This is the link',
                         'lock_version': 0,
                         'publish': True,
                         'system_mtime': '2020-02-20T16:42:59Z',
                         'title': 'Links to some other docs',
                         'user_mtime': '2020-02-20T16:42:59Z'}],
 'is_linked_to_published_record': False,
 'jsonmodel_type': 'agent_person',
 'last_modified_by': 'amd243',
 'linked_agent_roles': [],
 'lock_version': 0,
 'names': [{'authority_id': 'http://id.loc.gov/authorities/names/testd_name',
            'authorized': True,
            'create_time': '2020-02-20T16:42:59Z',
            'created_by': 'amd243',
            'dates': '1900-2000',
            'fuller_form': 'of Wales',
            'is_display_name': True,
            'jsonmodel_type': 'name_person',
            'last_modified_by': 'amd243',
            'lock_version': 0,
            'name_order': 'inverted',
            'number': 'IV',
            'prefix': 'Doctor',
            'primary_name': 'Samuel',
            'qualifier': 'Qualified',
            'rest_of_name': 'Jones',
            'rules': 'dacs',
            'sort_name': 'Samuel, Jones, Doctor, Esquire, Sir, IV (of Wales), '
                         '1900-2000 (Qualified)',
            'sort_name_auto_generate': True,
            'source': 'naf',
            'suffix': 'Esquire',
            'system_mtime': '2020-02-20T16:42:59Z',
            'title': 'Sir',
            'use_dates': [{'begin': '1999',
                           'calendar': 'gregorian',
                           'certainty': 'approximate',
                           'create_time': '2020-02-20T16:42:59Z',
                           'created_by': 'amd243',
                           'date_type': 'range',
                           'end': '2000',
                           'era': 'ce',
                           'expression': '1999-2000',
                           'jsonmodel_type': 'date',
                           'label': 'usage',
                           'last_modified_by': 'amd243',
                           'lock_version': 0,
                           'system_mtime': '2020-02-20T16:42:59Z',
                           'user_mtime': '2020-02-20T16:42:59Z'}],
            'user_mtime': '2020-02-20T16:42:59Z'},
           {'authority_id': 'another_authority_id',
            'authorized': False,
            'create_time': '2020-02-20T16:42:59Z',
            'created_by': 'amd243',
            'is_display_name': False,
            'jsonmodel_type': 'name_person',
            'last_modified_by': 'amd243',
            'lock_version': 0,
            'name_order': 'inverted',
            'primary_name': 'Variant Name',
            'rules': 'dacs',
            'sort_name': 'Variant Name',
            'sort_name_auto_generate': True,
            'source': 'naf',
            'system_mtime': '2020-02-20T16:42:59Z',
            'use_dates': [{'begin': '1940',
                           'create_time': '2020-02-20T16:42:59Z',
                           'created_by': 'amd243',
                           'date_type': 'range',
                           'end': '1941',
                           'expression': '1940-1941',
                           'jsonmodel_type': 'date',
                           'label': 'usage',
                           'last_modified_by': 'amd243',
                           'lock_version': 0,
                           'system_mtime': '2020-02-20T16:42:59Z',
                           'user_mtime': '2020-02-20T16:42:59Z'}],
            'user_mtime': '2020-02-20T16:42:59Z'}],
 'notes': [{'jsonmodel_type': 'note_bioghist',
            'persistent_id': 'e95fb45a253625b249313a9b84bc9742',
            'publish': True,
            'subnotes': [{'content': 'Biographical information',
                          'jsonmodel_type': 'note_text',
                          'publish': True},
                         {'content': 'And some more. THere are other types '
                                     'available too.',
                          'jsonmodel_type': 'note_text',
                          'publish': True}]},
           {'content': ["I guess we're not supposed to use this."],
            'jsonmodel_type': 'note_agent_rights_statement',
            'persistent_id': '75567897965f5fef11d974720119c633',
            'publish': True}],
 'publish': True,
 'related_agents': [{'create_time': '2020-02-20 16:42:59 UTC',
                     'created_by': 'amd243',
                     'dates': {'begin': '1995',
                               'create_time': '2020-02-20T16:42:59Z',
                               'created_by': 'amd243',
                               'date_type': 'inclusive',
                               'end': '2000',
                               'expression': '1995-2000',
                               'jsonmodel_type': 'date',
                               'label': 'agent_relation',
                               'last_modified_by': 'amd243',
                               'lock_version': 1,
                               'system_mtime': '2020-02-20T16:42:59Z',
                               'user_mtime': '2020-02-20T16:42:59Z'},
                     'description': 'Some relationships',
                     'jsonmodel_type': 'agent_relationship_associative',
                     'last_modified_by': 'amd243',
                     'ref': '/agents/people/69480',
                     'relator': 'is_associative_with',
                     'system_mtime': '2020-02-20 16:42:59 UTC',
                     'user_mtime': '2020-02-20 16:42:59 UTC'}],
 'system_mtime': '2020-02-20T16:42:59Z',
 'title': 'Samuel, Jones, Doctor, Esquire, Sir, IV (of Wales), 1900-2000 '
          '(Qualified)',
 'uri': '/agents/people/95065',
 'used_within_published_repositories': [],
 'used_within_repositories': [],
 'user_mtime': '2020-02-20T16:42:59Z'}
```

agent_corporate_entity

```
```

agent_family

```
```

subject

```
```

Example of JSON resource record with linked agent

```
```

Example of bare-bones collection-level EAD file with linked agents (exported from ArchivesSpace)

EAD 2002

```
<?xml version="1.0" encoding="UTF-8"?>
<ead xmlns="urn:isbn:1-931666-22-9"
     xmlns:xlink="http://www.w3.org/1999/xlink"
     xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
     xsi:schemaLocation="urn:isbn:1-931666-22-9 http://www.library.yale.edu/facc/schemas/ead/ead.xsd"
     id="mssa.ms.999999">
   <eadheader countryencoding="iso3166-1"
              dateencoding="iso8601"
              langencoding="iso639-2b"
              repositoryencoding="iso15511"
              audience="internal"
              scriptencoding="iso15924">
      <eadid countrycode="US"
             mainagencycode="US-CtY"
             publicid="-//Yale University::Manuscripts and Archives//TEXT (US::CtY::::[My Papers])//EN"
             url="http://hdl.handle.net/10079/fa/mssa.ms.999999">mssa.ms.999999</eadid>
      <filedesc>
         <titlestmt>
            <titleproper type="formal">My Papers</titleproper>
         </titlestmt>
         <publicationstmt>
            <publisher>Manuscripts and Archives</publisher>
            <address>
               <addressline>Yale University Library</addressline>
               <addressline>P.O. Box 208240</addressline>
               <addressline>New Haven, CT 06520-8240</addressline>
               <addressline>mssa.assist@yale.edu</addressline>
               <addressline>URL: http://www.library.yale.edu/mssa/</addressline>
            </address>
         </publicationstmt>
         <notestmt>
            <note type="bpg">
               <p>This encoded finding aid is compliant with the Yale EAD Best Practice Guidelines, Version 1.0.</p>
            </note>
         </notestmt>
      </filedesc>
      <profiledesc>
         <creation>This finding aid was produced using ArchivesSpace on <date>2020-02-11 22:06:56 UTC</date>.</creation>
         <langusage>Finding aid written in <language langcode="eng" scriptcode="Latn">English</language>
         </langusage>
      </profiledesc>
   </eadheader>
   <archdesc level="collection" relatedencoding="MARC21" type="register">
      <did>
         <head>Overview</head>
         <unitid label="Call Number:" countrycode="US" repositorycode="US-CtY">MS 999999</unitid>
         <origination label="Creator:">
            <persname authfilenumber="https://lccn.loc.gov/n2012059822" source="naf">Alexander, Bobby C.</persname>
         </origination>
         <unittitle label="Title:">My Papers</unittitle>
         <unitdate normal="1900/2000"
                   type="inclusive"
                   label="Dates:"
                   calendar="gregorian"
                   era="ce"
                   datechar="creation">1900–2000</unitdate>
         <physdesc altrender="whole" label="Physical Description:">
            <extent altrender="materialtype spaceoccupied">20 linear feet</extent>
         </physdesc>
         <langmaterial label="Language(s):">The materials are in 
      <language langcode="eng">English</language>
    .</langmaterial>
         <repository label="Repository:">
            <corpname>Manuscripts and Archives</corpname>
            <address>
               <addressline>Sterling Memorial Library</addressline>
               <addressline>128 Wall Street</addressline>
               <addressline>P.O. Box 208240</addressline>
               <addressline>New Haven, CT 06520</addressline>
               <addressline altrender="web">Web: http://web.library.yale.edu/mssa</addressline>
               <addressline altrender="email">Email: mssa.assist@yale.edu</addressline>
               <addressline altrender="phone">Phone: (203) 432-1735</addressline>
               <addressline altrender="fax">Fax: (203) 432-7441</addressline>
            </address>
         </repository>
      </did>
      <controlaccess id="ca">
         <head>Access Terms</head>
         <p>
        This collection is indexed under the following access points in
        <extref xlink:href="http://orbis.library.yale.edu/">Orbis</extref>, the Yale University Library online catalog.
      </p>
         <controlaccess>
            <head>Subjects</head>
            <famname authfilenumber="http://id.loc.gov/authorities/subjects/sh85129229"
                     role="fmo"
                     source="lcsh">Stuart, House of</famname>
            <corpname rules="local" source="local">Robert F. Lucas</corpname>
            <persname rules="local" source="local">Clay, Albert G. (Yale 1921)</persname>
            <persname source="local">Wescott, Barbara Harrison</persname>
            <persname authfilenumber="http://id.loc.gov/authorities/names/no91000799"
                      role="fmo"
                      rules="aacr"
                      source="naf">Aa, Cornelis van der, 1749-1816</persname>
            <persname authfilenumber="http://id.loc.gov/authorities/names/n88128725"
                      role="fmo"
                      rules="aacr"
                      source="naf">Aaboe, Asger</persname>
            <persname authfilenumber="http://id.loc.gov/authorities/names/n50036821"
                      role="fmo"
                      source="naf">Aaron, Daniel, 1912-2016</persname>
            <corpname authfilenumber="http://id.loc.gov/authorities/names/no2006073808"
                      rules="aacr"
                      source="naf">'45 Aid Society</corpname>
            <corpname authfilenumber="http://id.loc.gov/authorities/names/no2002041813"
                      rules="aacr"
                      source="naf">52nd Street Project</corpname>
            <corpname authfilenumber="http://id.loc.gov/authorities/names/no2012154344"
                      source="naf">9999 (Firm)</corpname>
         </controlaccess>
         <controlaccess>
            <head>Added Entries</head>
            <persname authfilenumber="http://id.loc.gov/authorities/names/n79018911"
                      source="naf">Kissinger, Henry, 1923-</persname>
         </controlaccess>
      </controlaccess>
      <dsc type="combined">
         <head>Collection Contents</head>
      </dsc>
   </archdesc>
</ead>
```

EAD 3

```
<?xml version="1.0" encoding="UTF-8"?>
<?xml-model href="https://raw.githubusercontent.com/SAA-SDT/EAD3/master/ead3.rng"
      type="application/xml" schematypens="http://relaxng.org/ns/structure/1.0"?>
<ead xmlns="http://ead3.archivists.org/schema/">
   <control countryencoding="iso3166-1"
            dateencoding="iso8601"
            langencoding="iso639-2b"
            relatedencoding="marc"
            repositoryencoding="iso15511"
            scriptencoding="iso15924">
      <recordid instanceurl="">mssa.ms.999999</recordid>
      <filedesc>
         <titlestmt>
            <titleproper>My Papers</titleproper>
         </titlestmt>
         <publicationstmt>
            <publisher>Manuscripts and Archives</publisher>
            <address>
               <addressline>Yale University Library</addressline>
               <addressline>P.O. Box 208240</addressline>
               <addressline>New Haven, CT 06520-8240</addressline>
               <addressline localtype="email">mssa.assist@yale.edu</addressline>
               <addressline>
                  <ref href="http://www.library.yale.edu/mssa/"
                       linktitle="http://www.library.yale.edu/mssa/"
                       show="new">http://www.library.yale.edu/mssa/</ref>
               </addressline>
            </address>
            <num>MS 999999</num>
         </publicationstmt>
      </filedesc>
      <maintenancestatus value="derived"/>
      <maintenanceagency>
         <agencycode>US-CtY</agencycode>
         <agencyname>Manuscripts and Archives</agencyname>
      </maintenanceagency>
      <rightsdeclaration>
         <abbr>CC0</abbr>
         <citation href="https://creativecommons.org/publicdomain/zero/1.0/"/>
         <descriptivenote>
            <p>CC0 1.0 Universal (CC0 1.0)</p>
         </descriptivenote>
      </rightsdeclaration>
      <maintenancehistory>
         <maintenanceevent>
            <eventtype value="derived"/>
            <eventdatetime>2020-02-11T22:06:53+00:00</eventdatetime>
            <agenttype value="machine"/>
            <agent>ArchivesSpace 2.4.1.yale.20190822</agent>
            <eventdescription>This finding aid was produced using ArchivesSpace on Tuesday February 11, 2020 at 22:06</eventdescription>
         </maintenanceevent>
      </maintenancehistory>
   </control>
   <archdesc level="collection">
      <did>
         <unittitle>My Papers</unittitle>
         <unitid>MS 999999</unitid>
         <repository>
            <corpname>
               <part>Manuscripts and Archives</part>
            </corpname>
         </repository>
         <langmaterial>
            <language langcode="eng">English</language>
         </langmaterial>
         <physdescstructured coverage="whole" physdescstructuredtype="spaceoccupied">
            <quantity>20</quantity>
            <unittype>Linear Feet</unittype>
         </physdescstructured>
         <unitdatestructured unitdatetype="inclusive">
            <daterange>
               <fromdate standarddate="1900">1900</fromdate>
               <todate standarddate="2000">2000</todate>
            </daterange>
         </unitdatestructured>
         <origination label="creator">
            <persname identifier="https://lccn.loc.gov/n2012059822" source="naf">
               <part>Alexander, Bobby C.</part>
            </persname>
         </origination>
    
         <origination label="creator">
            <persname identifier="http://id.loc.gov/authorities/names/n79018911" source="naf">
               <part>Kissinger, Henry, 1923-</part>
            </persname>
         </origination>
      </did>

      <controlaccess>
         <famname identifier="http://id.loc.gov/authorities/subjects/sh85129229"
                  relator="fmo"
                  source="lcsh">
            <part>Stuart, House of</part>
         </famname>
         <corpname rules="local" source="local">
            <part>Robert F. Lucas</part>
         </corpname>
         <persname rules="local" source="local">
            <part>Clay, Albert G. (Yale 1921)</part>
         </persname>
         <persname source="local">
            <part>Wescott, Barbara Harrison</part>
         </persname>
         <persname identifier="http://id.loc.gov/authorities/names/no91000799"
                   relator="fmo"
                   rules="aacr"
                   source="naf">
            <part>Aa, Cornelis van der, 1749-1816</part>
         </persname>
         <persname identifier="http://id.loc.gov/authorities/names/n88128725"
                   relator="fmo"
                   rules="aacr"
                   source="naf">
            <part>Aaboe, Asger</part>
         </persname>
         <persname identifier="http://id.loc.gov/authorities/names/n50036821"
                   relator="fmo"
                   source="naf">
            <part>Aaron, Daniel, 1912-2016</part>
         </persname>
         <corpname identifier="http://id.loc.gov/authorities/names/no2006073808"
                   rules="aacr"
                   source="naf">
            <part>'45 Aid Society</part>
         </corpname>
         <corpname identifier="http://id.loc.gov/authorities/names/no2002041813"
                   rules="aacr"
                   source="naf">
            <part>52nd Street Project</part>
         </corpname>
         <corpname identifier="http://id.loc.gov/authorities/names/no2012154344"
                   source="naf">
            <part>9999 (Firm)</part>
         </corpname>
      </controlaccess>
      <dsc/>
   </archdesc>
</ead>
```

#### Controlled vocabularies

Agents

* Personal names, corporate names: [Library of Congress Name Authority File (LCNAF)](http://id.loc.gov/authorities/names.html)
* Family names: [Library of Congress Subject Headings (LCSH)](http://id.loc.gov/authorities/subjects.html)

Subjects

* [Art and Architecture Thesaurus (AAT)](https://www.getty.edu/research/tools/vocabularies/aat/index.html)

### Overview of previous reconciliation work performed on archival metadata

Deliverables:

* [Task Force Documentation](https://drive.google.com/drive/u/0/folders/0B7qoM_riUwnbMDBtZGpMZEQtbVk)
* [Task Force Final Report](https://docs.google.com/document/d/118o923PDYmTeP_0Xb74wxVUfTOzeLdKGQpdMCjnJf4Y/edit)
* [Task Force Future Recommendations](https://docs.google.com/document/d/1mz8-K8sjCxkx9wf8m6fNkBTQ9pM6F48qyfG9EELq9_I/edit)
* [Ruby app that parsed MARC fields and downloaded authority files](https://github.com/mark-cooper/authorizer)
* [ArchivesSpace authority record importer](https://github.com/lyrasis/aspace-importer)

## Work Plan

* Spring 2020 student [job description](https://docs.google.com/document/d/1C8zBbFWC9V2N3Hs4lHZyrkhrIebDun6eDEtnj39Y8ts/edit)

Preliminary task list:

* Reconcile agents and subjects with existing LCNAF and AAT URIs against Wikidata, SNAC, ULAN, VIAF others?
* Reconcile agents and subjects without existing LCNAF and AAT URIs against Wikidata (pulling LCNAF and other URIs from Wikidata where possible) - includes agents created since last reconciliation and potentially another round on agents which were not found in previous round (using OpenRefine, possibly)
* Edit and upload duplicate detection script to GH repo
* Create reports for use in reconciliation (i.e. will need to have links to finding aids side-by-side with agent records for manual review)
* Create instructions for authority reconciliation in OpenRefine
* Import of authority records into ArchiveSpace following previous processes
* Review of results
* Data audit of agent and subject records in ArchivesSpace (partially Python, partially OpenRefine)
* Cleanup of agent and subject records in ArchivesSpace
* De-duplication - should this happen before or after reconciliation. Or both?
* Planning for storage of additional URIs - no way in ArchivesSpace to store more than one

## Reports from ArchivesSpace

* [Agents - people, all fields](/archivesspace_sql_queries/agent_person_data.sql)
* [Agents - corporate entities, all fields](/archivesspace_sql_queries/agent_corporate_entity_data)
* Agents - families, all fields
* All agent links
* All subjects, all fields
* All subject links
* All agents with URIs
* All agents without URIs
* All agents created since July 21, 2018 with URIs
* All agents created since July 21, 2018 without URIs
* All subjects created since July 21, 2018 with URIs
* All subjects created ince July 21, 2018 without URIs
* Counts?

## Data Sources

* [Wikidata](https://www.wikidata.org/wiki/Wikidata:Data_access)
* [id.loc.gov](http://id.loc.gov/)
* [Getty](https://www.getty.edu/research/tools/vocabularies/lod/)
* [SNAC](https://snaccooperative.org/?command=api_help)
* [VIAF](https://www.oclc.org/developer/develop/web-services/viaf.en.html)
* ArchivesSpace

## Resources to Consult

* [Questioning Authority](https://github.com/samvera/questioning_authority#what-does-this-do)
* [LD4P Lookup Service](https://lookup.ld4l.org/)
* [Metaphactory](https://www.metaphacts.com/product)
* [Wikidata Authority Control](https://www.wikidata.org/wiki/Wikidata:WikiProject_Authority_control)
* [Wikidata Data Access](https://www.wikidata.org/wiki/Wikidata:Data_access#MediaWiki_API)
* [Wikibase Data Model](https://www.mediawiki.org/wiki/Wikibase/DataModel/JSON#Example_)
* [Extracting Data From Wikidata JSON](https://stackoverflow.com/questions/46383784/wikidata-get-all-properties-with-labels-and-values-of-an-item)
* [Example Workflow for Python-based SPARQL Queries](https://towardsdatascience.com/questions-96667b06af5)
* [Linking records back to Wikidata](https://www.research-collection.ethz.ch/bitstream/handle/20.500.11850/393724/Dokumentation_P485_Import.pdf?sequence=1&isAllowed=y)
* [Wikidata Tools for Programmers](https://www.wikidata.org/wiki/Wikidata:Tools/For_programmers)
* [WikidataIntegrator](https://github.com/SuLab/WikidataIntegrator)
* [Extracting info from Wikidata responses, 1](https://stackoverflow.com/questions/38906932/how-to-programmatically-get-all-available-information-from-a-wikidata-entity)
* [Extracting info from Wikidata responses, 2](https://stackoverflow.com/questions/31266398/getting-readable-results-from-wikidata/31290824
)

