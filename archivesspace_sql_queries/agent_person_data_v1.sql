SELECT CONCAT('/agents/people/', ap.id) as uri
	, np.sort_name
	, np.title
	, np.prefix
	, np.rest_of_name
	, np.number
	, np.suffix
	, np.fuller_form
	, np.dates
	, np.qualifier
	, ev.value as source
	, ev2.value as rules
	, date.expression
	, date.begin
	, date.end
	, ap.created_by
	, ap.create_time
	, ap.last_modified_by
	, ap.user_mtime
	, JSON_UNQUOTE(JSON_EXTRACT(CAST(CONVERT(note.notes using utf8) as json), '$.subnotes[0].content')) as `note_text`
#need to use the agent record because the name records are deleted and recreated on save,
#so create time info is not accurate
FROM agent_person ap
LEFT JOIN name_person np on np.agent_person_id = ap.id
LEFT JOIN name_authority_id nai on nai.name_person_id = np.id
LEFT JOIN enumeration_value ev on ev.id = np.source_id
LEFT JOIN enumeration_value ev2 on ev2.id = np.rules_id
LEFT JOIN user on user.agent_record_id = ap.id
#taking this out gives ~55 fewer results - so some multiple dates?
LEFT JOIN date on date.agent_person_id = ap.id
LEFT JOIN note on note.agent_person_id = ap.id
#only gets the display name, with the URI; not any alternate name forms
WHERE np.is_display_name IS NOT NULL
#excludes user records
AND user.id IS NULL
AND ap.publish = 0
#any way to just exclude Fortunoff records??