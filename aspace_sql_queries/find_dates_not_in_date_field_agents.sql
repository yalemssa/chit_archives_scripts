SELECT *
FROM (SELECT CONCAT('/agents/people/', np.agent_person_id) as agent_uri
	, np.sort_name
    , np.dates
    , date.begin
    , date.end
	, CONCAT(	IF(np.primary_name is not null, np.primary_name, 'NULL')
									, ' '
									, IF(np.title is not null, np.title, 'NULL')
                                    , ' '
                                    , IF(np.prefix is not null, np.prefix, 'NULL')
                                    , ' '
                                    , IF(np.rest_of_name is not null, np.rest_of_name, 'NULL')
                                    , ' '
                                    , IF(np.suffix is not null, np.suffix, 'NULL')
                                    , ' '
                                    , IF(np.fuller_form is not null, np.fuller_form, 'NULL')
                                    , ' '
                                    , IF(np.number is not null, np.number, 'NULL')
                                    , ' '
                                    , IF(np.qualifier is not null, np.qualifier, 'NULL')
                                    ) as full_name_concat
FROM name_person np
JOIN agent_person ap on ap.id = np.agent_person_id
LEFT JOIN date on date.agent_person_id = ap.id
WHERE np.is_display_name is not null) as concated_agents
WHERE (full_name_concat regexp '.*[0-9]{4}$' or full_name_concat regexp '.*[0-9]{4}[-]$')