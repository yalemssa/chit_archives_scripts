# Parent-child Relationships in ArchivesSpace

## Representation in archival object JSON records

There are several fields in an archival object JSON record which indicate the position of the object in the hierarchy and its relationship to other objects and the top-level resource record:


| Field                    | Data Type | Description                                                                                                                                                                                                   | Example                                                                                                                                                                                                                                                                                                                                                               |
|--------------------------|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ancestors                | array     | An array containing dictionaries which hold the URI of each of the archival objects' ancestors and its record level. Ordered from most immediate ancestor (parent) to most distant (collection-level record)  | "ancestors": [{"level": "file","ref": "/repositories/12/archival_objects/1748121"},{"level": "file","ref": "/repositories/12/archival_objects/1748120"},{"level": "file","ref": "/repositories/12/archival_objects/1748119"},{"level": "series","ref": "/repositories/12/archival_objects/1748118"},{"level": "collection","ref": "/repositories/12/resources/4556"}] |
| has_unpublished_ancestor | bool      | Indicates whether the archival object has an ancestor which is unpublished                                                                                                                                    | "has_unpublished_ancestor": false                                                                                                                                                                                                                                                                                                                                     |
| parent                   | dict      | The URI of the immediate parent                                                                                                                                                                               | "parent": {"ref": "/repositories/12/archival_objects/1748121"}                                                                                                                                                                                                                                                                                                        |
| position                 | int       | The position of the archival object under the immediate parent                                                                                                                                                | "position": 0                                                                                                                                                                                                                                                                                                                                                         |
| repository               | dict      | The URI of the parent repository                                                                                                                                                                              | "repository": {"ref": "/repositories/12"}                                                                                                                                                                                                                                                                                                                             |
| resource                 | dict      | The URI of the parent resource                                                                                                                                                                                | "resource": {"ref": "/repositories/12/resources/4556"}                                                                                                                                                                                                                                                                                                                |
| uri                      | dict      | The URI of the archival object                                                                                                                                                                                | "uri": "/repositories/12/archival_objects/1748122"}                                                                                                                                                                                                                                                                                                                   |

## Representation in MySQL database

Relationships between parent and child records are represented in the archival object table in the ArchivesSpace MySQL database by following fields:

Field | Description | Example
--- | --- | ---
repo_id | The database ID of the parent repository | 12
root_record_id | The database ID of the parent resource record | 4566
parent_id | The database ID of the immediate parent record. The value will be NULL if the only parent is the resource record. | 1748121
parent_name | The database ID or URI, and the record type of the immediate parent | 144@archival_object, root@/repositories/2/resources/2
position | The position of the archival object under the immediate parent | 168000

## API endpoints

There are several ways to access record "trees" which provide additional information about relationships among a collection's component records.

Description | Endpoint | Endpoint Example | Output Example
--- | --- | --- | ---
Get a resource tree | /repositories/:repo_id/resources/:id/tree | /repositories/12/resources/4556/tree | [Example JSON](mssa_ms_0466_tree.json)
Fetch tree information for an Archival Object record within a tree | /repositories/:repo_id/resources/:id/tree/node | /repositories/12/resources/4556/tree/node?node_uri=/repositories/12/archival_objects/1749901 | [Example JSON](mssa_ms_0466_tree_node.json)
Fetch tree paths from the root record to Archival Objects | /repositories/:repo_id/resources/:id/tree/node_from_root | /repositories/12/resources/4556/tree/node_from_root?node_ids[]=1749914 |[Example JSON](mssa_ms_0466_tree_node_from_root.json)
Fetch tree information for the top-level resource record | /repositories/:repo_id/resources/:id/tree/root | /repositories/12/resources/4556/tree/root | [Example JSON](mssa_ms_0466_top_level_tree.json)
Fetch the record slice for a given tree waypoint | /repositories/:repo_id/resources/:id/tree/waypoint | /repositories/12/resources/4556/tree/waypoint?offset=0&parent_node=/repositories/12/archival_objects/1749901 | [Example JSON](mssa_ms_0466_tree_from_waypoint.json)
