# ArchivesSpace Duplicate Name Game

A simple Terminal-based text game for identifying duplicate names in ArchivesSpace.

## Requirements

* Mac OS
* iTerm2: this enables users to click on links within the game. The default Mac Terminal does not allow this.

## Tutorial

1. Clone or download this repository
2. Unpack the .zip file and move the resulting folder out of Downloads folder (if applicable)
3. Navigate to the `authority_reconciliation/name_game` directory
4. Download your data source and save it to the `name_game` directory
5. Right-click on the Unix executable file, and select Open With --> iTerm
6. When prompted to enter your data source, drag and drop the input CSV file into the game window. This will copy the full path of the data source. Press return.
7. Review each entry and determine whether the two names refer to the same person. If they do refer to the same person, enter `Y` and press return. If they do not refer the same person, enter `N` and press return. If there is not enough information to determine whether they refer to the same person, enter `M` and press return. See the section below for criteria for determining matches.
8. To end your session, enter `Q` into the prompt. When you restart the game you will start where you left off in your previous session.

## Guidelines for Identifying Duplicate Names

While it is sometimes very obvious that two records refer to the same person - for instance, if the names are an exact match and the life dates are exactly the same - this is not always the case. Some general criteria for determining matches when there is ambiguity include:

* The names are very similar or the same __AND__:
	* Life dates are similar or the same
	* The context clues provided by the listed links indicate that the two individuals are the same person (i.e. they are linked to the same collection or collections which are related to similar subject areas)
* For women, one record might include just the maiden name, while a duplicate record will also include the married name. If there are no other context clues indicating they are the same person (life dates, collection links, etc.), mark these entries as `M`.
* If there is a match on the name, but no other information about the individuals, there is not enough information to definitively determine a match, since many people can have the same name. Mark these entries as `M`.
* When in doubt, mark entries as `M`.

### Examples of Matches (`Y`)

In the following entry, the matched names differ somewhat, but the full name is quite similar. The life dates are also not exactly the same, but the end date is the same. This is sufficent to conclude that it is a match.

```
│                                                                                        │
│     Entry number: 202/2275                                                             │
│     Similarity score: 0.811634366966268/1                                              │
│                                                                                        │
│     Name #1:                                                                           │
│                                                                                        │
│     Matched name: Anne Fitzpatrick Upper Ossory                                        │
│     Full name: Upper Ossory, Anne Fitzpatrick, Countess of, 1737 or 8-1804             │
│     Life dates: 1737 or 8-1804                                                         │
│     Library of Congress ID:                                                            │
│     Archives at Yale URL: https://archives.yale.edu/agents/people/83893                │
│     Collection links:                                                                  │
│         Joshua Reynolds Archive                                                        │
│     Component links:                                                                   │
│         <emph render='bold'>Letter to the Countess of Ossory</emph>, 1791 January 1    │
│     Accession titles (no links):                                                       │
│                                                                                        │
│                                                                                        │
│                                                                                        │
│     Name #2:                                                                           │
│                                                                                        │
│     Matched name: Anne Liddell Fitzpatrick Upper Ossory                                │
│     Full name: Upper Ossory, Anne Liddell Fitzpatrick, Countess of, -1804              │
│     Life dates: -1804                                                                  │
│     Library of Congress ID:                                                            │
│     Archives at Yale URL: https://archives.yale.edu/agents/people/85983                │
│     Collection links:                                                                  │
│         Horace Walpole collection                                                      │
│     Component links:                                                                   │
│                                                                                        │
│     Accession titles (no links):
```

In the following entry, the name is very similar except for one letter. The life dates are the same and the linked collections are related. This is sufficient to determine a match.

```
│     Entry number: 154/2275                                                             │
│     Similarity score: 0.809054795342396/1                                              │
│                                                                                        │
│     Name #1:                                                                           │
│                                                                                        │
│     Matched name: Carl Sternhelm                                                       │
│     Full name: Sternhelm, Carl, 1878-1942                                              │
│     Life dates: 1878-1942                                                              │
│     Library of Congress ID:                                                            │
│     Archives at Yale URL: https://archives.yale.edu/agents/people/88408                │
│     Collection links:                                                                  │
│         Kurt Wolff archive                                                             │
│     Component links:                                                                   │
│                                                                                        │
│     Accession titles (no links):                                                       │
│                                                                                        │
│                                                                                        │
│                                                                                        │
│     Name #2:                                                                           │
│                                                                                        │
│     Matched name: Carl Sternheim                                                       │
│     Full name: Sternheim, Carl, 1878-1942                                              │
│     Life dates: 1878-1942                                                              │
│     Library of Congress ID: http://id.loc.gov/authorities/names/n50023975              │
│     Archives at Yale URL: https://archives.yale.edu/agents/people/92878                │
│     Collection links:                                                                  │
│         Helen and Kurt Wolff papers                                                    │
│     Component links:                                                                   │
│                                                                                        │
│     Accession titles (no links):
```

In the following entry, the names are the same except for a middle intial. There are no life dates, but both of the links are related to music. This is enough to indicate a match.

```
│                                                                                        │
│     Entry number: 62/2275                                                              │
│     Similarity score: 0.802929174845616/1                                              │
│                                                                                        │
│     Name #1:                                                                           │
│                                                                                        │
│     Matched name: Gottfried Wagner                                                     │
│     Full name: Wagner, Gottfried                                                       │
│     Life dates:                                                                        │
│     Library of Congress ID:                                                            │
│     Archives at Yale URL: https://archives.yale.edu/agents/people/54102                │
│     Collection links:                                                                  │
│                                                                                        │
│     Component links:                                                                   │
│         Kurt Weill and the music of the Weimar Republic, 1980 Aug.                     │
│     Accession titles (no links):                                                       │
│                                                                                        │
│                                                                                        │
│                                                                                        │
│     Name #2:                                                                           │
│                                                                                        │
│     Matched name: Gottfried H. Wagner                                                  │
│     Full name: Wagner, Gottfried H.                                                    │
│     Life dates:                                                                        │
│     Library of Congress ID:                                                            │
│     Archives at Yale URL: https://archives.yale.edu/agents/people/54103                │
│     Collection links:                                                                  │
│                                                                                        │
│     Component links:                                                                   │
│         Zu Lotte Lenyas achtzigstem Geburtstag, .                                      │
│     Accession titles (no links):
```

### Examples of No-Matches (`N`)

In the following entry, the names are somewhat similar, but the records refer to two males with different surnames. The life dates are also different. Many entries will include individuals who are named after a famous person.

```
│     Entry number: 63/2275                                                              │
│     Similarity score: 0.80303033439022/1                                               │
│                                                                                        │
│     Name #1:                                                                           │
│                                                                                        │
│     Matched name: Isaac Newton                                                         │
│     Full name: Newton, Isaac, 1837-1884                                                │
│     Life dates: 1837-1884                                                              │
│     Library of Congress ID: http://id.loc.gov/authorities/names/nb2008018780           │
│     Archives at Yale URL: https://archives.yale.edu/agents/people/60384                │
│     Collection links:                                                                  │
│         Boardman family papers                                                         │
│     Component links:                                                                   │
│                                                                                        │
│     Accession titles (no links):                                                       │
│                                                                                        │
│                                                                                        │
│                                                                                        │
│     Name #2:                                                                           │
│                                                                                        │
│     Matched name: Isaac Newton Ritner                                                  │
│     Full name: Ritner, Isaac Newton                                                    │
│     Life dates:                                                                        │
│     Library of Congress ID:                                                            │
│     Archives at Yale URL: https://archives.yale.edu/agents/people/65940                │
│     Collection links:                                                                  │
│         Photograph album and photographs of Montana, New Mexico, and Colorado          │
│     Component links:                                                                   │
│                                                                                        │
│     Accession titles (no links):
```

In the following entry, two family members with similar middle and last names are indicated as a possible match. They are linked to similar collections, but it is possible to tell by the first name and life dates that they are not the same.

```
│     Entry number: 70/2275                                                              │
│     Similarity score: 0.803554065862655/1                                              │
│                                                                                        │
│     Name #1:                                                                           │
│                                                                                        │
│     Matched name: Anne Morrow Lindbergh                                                │
│     Full name: Lindbergh, Anne Morrow, 1906-2001                                       │
│     Life dates: 1906-2001                                                              │
│     Library of Congress ID: http://id.loc.gov/authorities/names/n79108313              │
│     Archives at Yale URL: https://archives.yale.edu/agents/people/58367                │
│     Collection links:                                                                  │
│         Warren L. Duffield papers                                                      │
│         Paul Palmer papers                                                             │
│         Alfred Mitchell Bingham and the Common Sense collection                        │
│         Lindbergh picture collection                                                   │
│         Anne Morrow Lindbergh papers                                                   │
│         Samuel F. Pryor papers                                                         │
│         Insignia Films Lindbergh documentary collection                                │
│         Helen and Kurt Wolff papers                                                    │
│         Blanche Matthias papers                                                        │
│         Charles Augustus Lindbergh papers                                              │
│     Component links:                                                                   │
│                                                                                        │
│     Accession titles (no links):                                                       │
│         Lindbergh, Anne Morrow, Papers                                                 │
│         Lindbergh, Anne Morrow, Papers                                                 │
│         Lindbergh, Charles A., Papers                                                  │
│         Lindbergh, Anne Morrow, Papers                                                 │
│                                                                                        │
│                                                                                        │
│     Name #2:                                                                           │
│                                                                                        │
│     Matched name: Jon Morrow Lindbergh                                                 │
│     Full name: Lindbergh, Jon Morrow, 1932-                                            │
│     Life dates: 1932-                                                                  │
│     Library of Congress ID:                                                            │
│     Archives at Yale URL: https://archives.yale.edu/agents/people/85274                │
│     Collection links:                                                                  │
│         Anne Morrow Lindbergh papers                                                   │
│     Component links:                                                                   │
│                                                                                        │
│     Accession titles (no links):
```

In the following entry, the names are almost an exact match. However, the life dates are different.

```
│     Entry number: 92/2275                                                              │
│     Similarity score: 0.804662726109594/1                                              │
│                                                                                        │
│     Name #1:                                                                           │
│                                                                                        │
│     Matched name: Cadwallader Colden                                                   │
│     Full name: Colden, Cadwallader, 1688-1776                                          │
│     Life dates: 1688-1776                                                              │
│     Library of Congress ID: http://id.loc.gov/authorities/names/n50029086              │
│     Archives at Yale URL: https://archives.yale.edu/agents/people/57496                │
│     Collection links:                                                                  │
│         William Inglis Morse collection                                                │
│     Component links:                                                                   │
│                                                                                        │
│     Accession titles (no links):                                                       │
│                                                                                        │
│                                                                                        │
│                                                                                        │
│     Name #2:                                                                           │
│                                                                                        │
│     Matched name: Cadwallader D. Colden                                                │
│     Full name: Colden, Cadwallader D. (Cadwallader David), 1769-1834                   │
│     Life dates: 1769-1834                                                              │
│     Library of Congress ID: http://id.loc.gov/authorities/names/n84216304              │
│     Archives at Yale URL: https://archives.yale.edu/agents/people/61129                │
│     Collection links:                                                                  │
│         Annie Burr Jennings collection                                                 │
│         Woolsey family papers                                                          │
│     Component links:                                                                   │
│                                                                                        │
│     Accession titles (no links):                                                       │
│
```

### Examples of Possible Matches (`M`)

In the following entry, the names are very similar except for a possible married name. There is also not enough information in the life dates or collections to make a definitive match.

```
│     Entry number: 192/2275                                                             │
│     Similarity score: 0.81055132056568/1                                               │
│                                                                                        │
│     Name #1:                                                                           │
│                                                                                        │
│     Matched name: Danielle Di Bianco                                                   │
│     Full name: Di Bianco, Danielle                                                     │
│     Life dates:                                                                        │
│     Library of Congress ID:                                                            │
│     Archives at Yale URL: https://archives.yale.edu/agents/people/37541                │
│     Collection links:                                                                  │
│                                                                                        │
│     Component links:                                                                   │
│                                                                                        │
│     Accession titles (no links):                                                       │
│         Records                                                                        │
│                                                                                        │
│                                                                                        │
│     Name #2:                                                                           │
│                                                                                        │
│     Matched name: Danielle Di Bianco Caracas                                           │
│     Full name: Di Bianco Caracas, Danielle                                             │
│     Life dates:                                                                        │
│     Library of Congress ID:                                                            │
│     Archives at Yale URL: https://archives.yale.edu/agents/people/54667                │
│     Collection links:                                                                  │
│                                                                                        │
│     Component links:                                                                   │
│                                                                                        │
│     Accession titles (no links):                                                       │
│         Cultural and Civilization of China project records
```

In the following entry, the names are similar, but there is not enough information to conclude whether they are the same person.

```
│     Entry number: 151/2275                                                             │
│     Similarity score: 0.808807271749431/1                                              │
│                                                                                        │
│     Name #1:                                                                           │
│                                                                                        │
│     Matched name: E. Fowler                                                            │
│     Full name: Fowler, E.                                                              │
│     Life dates:                                                                        │
│     Library of Congress ID:                                                            │
│     Archives at Yale URL: https://archives.yale.edu/agents/people/21302                │
│     Collection links:                                                                  │
│                                                                                        │
│     Component links:                                                                   │
│         Letter : Liverpool, New York, to Roger S. Skinner, New Haven, Connecticut,     │
│ 1824 Nov 4                                                                             │
│     Accession titles (no links):                                                       │
│                                                                                        │
│                                                                                        │
│                                                                                        │
│     Name #2:                                                                           │
│                                                                                        │
│     Matched name: Eve Fowler                                                           │
│     Full name: Fowler, Eve                                                             │
│     Life dates:                                                                        │
│     Library of Congress ID:                                                            │
│     Archives at Yale URL: https://archives.yale.edu/agents/people/4098                 │
│     Collection links:                                                                  │
│                                                                                        │
│     Component links:                                                                   │
│         [Untitled], 1992                                                               │
│     Accession titles (no links):
```

In the following entry, the names appear to be transposed. The life dates are the same, as are the linked collections. This is a likely match, but would require review by an archivist to confirm.

```
│     Entry number: 112/2275                                                             │
│     Similarity score: 0.805642989558441/1                                              │
│                                                                                        │
│     Name #1:                                                                           │
│                                                                                        │
│     Matched name: Douglas Conrad                                                       │
│     Full name: Conrad, Douglas, 1958-                                                  │
│     Life dates: 1958-                                                                  │
│     Library of Congress ID:                                                            │
│     Archives at Yale URL: https://archives.yale.edu/agents/people/36838                │
│     Collection links:                                                                  │
│                                                                                        │
│     Component links:                                                                   │
│                                                                                        │
│     Accession titles (no links):                                                       │
│         Douglas Conrad Eastern European LGBT interviews and supporting materials       │
│                                                                                        │
│                                                                                        │
│     Name #2:                                                                           │
│                                                                                        │
│     Matched name: Conrad Douglas                                                       │
│     Full name: Douglas, Conrad, 1958-                                                  │
│     Life dates: 1958-                                                                  │
│     Library of Congress ID:                                                            │
│     Archives at Yale URL: https://archives.yale.edu/agents/people/77305                │
│     Collection links:                                                                  │
│         Douglas Conrad Eastern and Central European LGBT interviews and supporting     │
│ materials                                                                              │
│     Component links:                                                                   │
│                                                                                        │
│     Accession titles (no links):
```

## Tips

* Be sure to quit (by entering `Q` into the prompt) when you wish to end your game session. This will ensure that all of your data is saved to the output file
* Keep the data source in the `name_game` directory. Do not move it or the output file.
* There are multiple (blue) links that can be clicked to view additional information about the possible matches. To follow the link hold the `command` key and click the link. The titles in the `Accession titles (no links)` section are __NOT__ clickable, as the records require additional permissions to access. However, the titles often provide enough context to determine matches.

## Resources

* YouTube setup [video](https://www.youtube.com/watch?v=dF3oXSa03wA)
* YUL archives and manuscripts [data source](https://drive.google.com/file/d/1FVmis_lzvZyf_kHxvQNYXsx1xTiUlEw-/view?usp=sharing)
