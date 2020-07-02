#agents without authority IDs created since the Lyrasis ingest
SELECT DISTINCT CONCAT('/agents/people/', ap.id) as agent_uri
	, np.sort_name
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
#WHERE ap.create_time > '2018-07-21 07:59:00:00'
WHERE np.is_display_name is not null
AND nai.authority_id is null
AND (resource.repo_id is null or resource.repo_id != 14)
UNION ALL
SELECT DISTINCT CONCAT('/agents/corporate_entities/', ace.id) as agent_uri
	, nce.sort_name
	, nai.authority_id
	, ace.create_time
	, ace.created_by
	, ev.value as source
FROM agent_corporate_entity ace
LEFT JOIN name_corporate_entity nce on nce.agent_corporate_entity_id = ace.id
LEFT JOIN name_authority_id nai on nai.name_corporate_entity_id = nce.id
LEFT JOIN linked_agents_rlshp lar on lar.agent_corporate_entity_id = ace.id
LEFT JOIN resource on resource.id = lar.resource_id
LEFT JOIN enumeration_value ev on ev.id = nce.source_id
#WHERE ace.create_time > '2018-07-21 07:59:00:00'
WHERE nce.is_display_name is not null
AND nai.authority_id is null
AND (resource.repo_id is null or resource.repo_id != 14)
UNION ALL
SELECT DISTINCT CONCAT('/agents/families/', af.id) as agent_uri
	, nf.sort_name
	, nai.authority_id
	, af.create_time
	, af.created_by
	, ev.value as source
FROM agent_family af
LEFT JOIN name_family nf on nf.agent_family_id = af.id
LEFT JOIN name_authority_id nai on nai.name_family_id = nf.id
LEFT JOIN linked_agents_rlshp lar on lar.agent_family_id = af.id
LEFT JOIN resource on resource.id = lar.resource_id
LEFT JOIN enumeration_value ev on ev.id = nf.source_id
#WHERE af.create_time > '2018-07-21 07:59:00:00'
WHERE nf.is_display_name is not null
AND nai.authority_id is null
AND (resource.repo_id is null or resource.repo_id != 14)