SELECT CONCAT('/agents/people/', np.agent_person_id) as uri
	, CONCAT(np.rest_of_name, ' ' , np.primary_name) as name_concat
	, np.sort_name
	, nai.authority_id
    , IF(ev.value, 'naf', 'LCNAF') as source
FROM name_person np
LEFT JOIN name_authority_id nai on nai.name_person_id = np.id
LEFT JOIN enumeration_value ev on ev.id = np.source_id
WHERE nai.authority_id like '%id.loc.gov%'
AND np.is_display_name is not null
UNION ALL
SELECT CONCAT('/agents/corporate_entities/', nce.agent_corporate_entity_id) as uri
	, nce.sort_name as name_concat
	, nce.sort_name
	, nai.authority_id
    , IF(ev.value, 'naf', 'LCNAF') as source
FROM name_corporate_entity nce
LEFT JOIN name_authority_id nai on nai.name_corporate_entity_id = nce.id
LEFT JOIN enumeration_value ev on ev.id = nce.source_id
WHERE nai.authority_id like '%id.loc.gov%'
AND nce.is_display_name is not null