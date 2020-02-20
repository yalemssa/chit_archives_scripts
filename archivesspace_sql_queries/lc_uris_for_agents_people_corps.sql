SELECT CONCAT('/agents/people/', np.agent_person_id) as uri
	, np.sort_name
	, nai.authority_id
FROM name_person np
LEFT JOIN name_authority_id nai on nai.name_person_id = np.id
WHERE nai.authority_id like '%id.loc.gov%'
AND np.is_display_name is not null
UNION ALL
SELECT CONCAT('/agents/corporate_entities/', nce.agent_corporate_entity_id) as uri
	, nce.sort_name
	, nai.authority_id
FROM name_corporate_entity nce
LEFT JOIN name_authority_id nai on nai.name_corporate_entity_id = nce.id
WHERE nai.authority_id like '%id.loc.gov%'
AND nce.is_display_name is not null
