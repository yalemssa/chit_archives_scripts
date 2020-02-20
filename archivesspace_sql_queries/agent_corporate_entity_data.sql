SELECT CONCAT('/agents/corporate_entities/', ace.id) as uri
	, nce.sort_name
	, nce.primary_name
	, nce.subordinate_name_1
	, nce.subordinate_name_2
	, number
	, dates
	, qualifier
	, ev.value as source
	, ev2.value as rules
	, date.expression
	, date.begin
	, date.end
	, ace.created_by
	, ace.create_time
	, ace.last_modified_by
	, ace.user_mtime
	, JSON_UNQUOTE(JSON_EXTRACT(CAST(CONVERT(note.notes using utf8) as json), '$.subnotes[0].content')) as `note_text`
FROM agent_corporate_entity ace
LEFT JOIN name_corporate_entity nce on nce.agent_corporate_entity_id = ace.id
LEFT JOIN name_authority_id nai on nai.name_corporate_entity_id = nce.id
LEFT JOIN enumeration_value ev on ev.id = nce.source_id
LEFT JOIN enumeration_value ev2 on ev2.id = nce.rules_id
LEFT JOIN date on date.agent_corporate_entity_id = ace.id
LEFT JOIN note on note.agent_corporate_entity_id = ace.id
WHERE nce.is_display_name IS NOT NULL