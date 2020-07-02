SELECT * FROM
(SELECT DISTINCT CONCAT('/agents/people/', ap.id) as agent_uri
	, replace(CONCAT(np.rest_of_name, ' ' , np.primary_name), '&', 'and') as name_concat
	, np.sort_name
    , np.dates
    , date.begin
    , date.end
	, nai.authority_id
	, ap.create_time
	, ap.created_by
	, ev.value as source
FROM agent_person ap
LEFT JOIN name_person np on np.agent_person_id = ap.id
LEFT JOIN name_authority_id nai on nai.name_person_id = np.id
LEFT JOIN linked_agents_rlshp lar on lar.agent_person_id = ap.id
LEFT JOIN resource on resource.id = lar.resource_id
LEFT JOIN enumeration_value ev on ev.id = np.source_id
LEFT JOIN date on date.agent_person_id = ap.id
WHERE np.is_display_name is not null
AND nai.authority_id is null
AND (resource.repo_id is null or resource.repo_id != 14)) as agents
WHERE name_concat is not NULL