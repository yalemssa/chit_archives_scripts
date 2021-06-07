SELECT DISTINCT agent_uri
    , agent_aay_url
    , name_concat
    , sort_name
    , dates
    , begin
    , end
    , authority_id
    , GROUP_CONCAT(resource_ids) as resource_ids
    , GROUP_CONCAT(archival_object_ids) as archival_object_ids
    , GROUP_CONCAT(accession_ids) as accesssion_ids
    , publish
FROM (SELECT DISTINCT CONCAT('/agents/people/', ap.id) as agent_uri
    , CONCAT('https://archives.yale.edu/agents/people/', ap.id) as agent_aay_url
    , replace(CONCAT(np.rest_of_name, ' ' , np.primary_name), '&', 'and') as name_concat
    , np.sort_name as sort_name
    , np.dates as dates
    , date.begin as begin
    , date.end as end
    , nai.authority_id as authority_id
    #resources and archival_objects are usually published
    , CONCAT(replace(resource.title, '"', "'"), ': ', 'https://archives.yale.edu/repositories/', resource.repo_id, '/resources/', lar.resource_id) as resource_ids
    , CONCAT(replace(ao.display_string, '"', "'"), ': ', 'https://archives.yale.edu/repositories/', ao.repo_id, '/archival_objects/', lar.archival_object_id) as archival_object_ids
    #these are not - what to do?
    , CONCAT(replace(accession.title, '"', "'"), ': ' , 'https://archivesspace.library.yale.edu/accessions/', lar.accession_id, ' (', accession.repo_id, ')') as accession_ids
    , ap.publish as publish
FROM linked_agents_rlshp lar
#this will only retrieve agent_person links to resources
LEFT JOIN resource on resource.id = lar.resource_id
LEFT JOIN accession on accession.id = lar.accession_id
LEFT JOIN archival_object ao on ao.id = lar.archival_object_id
JOIN agent_person ap on ap.id = lar.agent_person_id
LEFT JOIN name_person np on np.agent_person_id = ap.id
LEFT JOIN name_authority_id nai on nai.name_person_id = np.id
LEFT JOIN enumeration_value ev on ev.id = np.source_id
LEFT JOIN date on date.agent_person_id = ap.id
LEFT JOIN user on user.agent_record_id = ap.id
WHERE np.is_display_name is not null
AND user.id is NULL
AND (resource.repo_id is null or resource.repo_id != 14)) as aglinks
WHERE name_concat is NOT NULL
GROUP BY aglinks.agent_uri
