# Event 015 Current Localisation, Event Details, and Catalog Re-audit

Date: 2026-07-15

Auditor role: independent current-source cross-surface auditor

Scope: Event 015 English localisation, event identity, Event Details, event log, evolutions, random-event classification, cluster status, and spreadsheet catalog alignment

Mode: read-only audit except for this report

## Verdict

**PASS**

The current Event 015 cross-surface package is aligned. No stale World Tension Subsides or placeholder identity reaches runtime script, English localisation, shared Event Details or event-log selectors, or the workbook. Event 015 is classified as a Minor Fire-Once event, has no cluster membership, and has one complete workbook row whose name, Event Details text, and five evolution entries exactly match current English localisation.

This report fulfills both requested fresh verification surfaces:

- fresh English-localisation verification for Event 015 event, Event Details, event-log, and evolution references
- fresh spreadsheet and catalog verification against the same current runtime and localisation sources

No blocker, simplification, fallback, omission, or unresolved cross-surface finding remains inside this audit scope.

## Disposition

Changed file:

- docs/plans/015_utopia_manifesto_plans/subagent_handoffs/localisation_event_details_catalog_current_reaudit_2026_07_15.md

Files deliberately not changed:

- gameplay script
- English localisation
- scripted localisation
- interface files
- docs/spreadsheets/chaos_redux_events_catalog.xlsx

No gameplay identifier or player-facing value changed. Before this edit, the current PASS existed only as the live audit result. After this edit, the same result and its reproduction commands are preserved in the Event 015 handoff directory.

No commit was created by this auditor.

## Audited source files

Runtime and catalog sources:

- events/015_utopia_manifesto.txt
- common/script_constants/015_utopia_manifesto_constants.txt
- common/script_constants/event_system_constants.txt
- common/scripted_effects/015_utopia_manifesto_effects.txt
- common/scripted_effects/chaosx_logic_effects.txt
- common/scripted_effects/chaosx_settings_effects.txt
- common/scripted_effects/chaosx_events_log_effects.txt
- common/scripted_effects/chaosx_event_cluster_effects.txt
- common/scripted_triggers/chaosx_settings_triggers.txt

Shared display mappings:

- common/scripted_localisation/chaosx_scripted_localisation_events_log.txt
- common/scripted_localisation/chaosx_scripted_localisation_debug.txt
- common/scripted_localisation/chaosx_scripted_localisation_settings.txt

English localisation authorities:

- localisation/english/chaosx_event_names_l_english.yml
- localisation/english/chaosx_gui_l_english.yml
- localisation/english/015_utopia_manifesto_evolutions_l_english.yml
- all English localisation files used by the direct Event 015 reference-parity scan

Catalog authority:

- docs/spreadsheets/chaos_redux_events_catalog.xlsx

Historical-label context:

- docs/events/015_utopia_manifesto.md
- docs/plans/015_utopia_manifesto_plans/015_utopia_manifesto_source_of_truth_and_resume_2026_07_15.md

## Stale identity and ID 15 mapping audit

The exact case-insensitive repository and runtime search produced:

| Search pattern | Repository hits outside wiki, Git, and XLSX | Runtime hits in events, common, localisation, and interface |
| --- | ---: | ---: |
| World Tension Subsides | 27 | 0 |
| world_tension_subsides | 2 | 0 |
| Event 015 Placeholder | 8 | 0 |
| 015_placeholder | 5 | 0 |
| 015_world_tension_falls | 1 | 0 |

Every surviving repository hit is in documentation that preserves migration, recovery, or asset provenance. The canonical event document states at docs/events/015_utopia_manifesto.md:353-355 that these are historical labels and not current names or runtime fallbacks. The source-of-truth resume states at line 189 that World Tension Subsides and placeholder language are historical catalog provenance only.

The workbook XML contains zero instances of all five legacy patterns.

The visible token ID15 has zero runtime occurrences and zero workbook XML occurrences.

A targeted shared-registry search found zero literal assignments of Event ID 15 through event_id, settings_event_id, event_fire_record_id, events_log_selected_event_id, or a bare value assignment. Shared mappings use the symbolic constant.

The symbolic token constant:utopia_manifesto_event.id has 17 relevant references across eight files:

- common/scripted_triggers/chaosx_settings_triggers.txt
- common/scripted_localisation/chaosx_scripted_localisation_debug.txt
- common/scripted_localisation/chaosx_scripted_localisation_events_log.txt
- common/scripted_localisation/chaosx_scripted_localisation_settings.txt
- common/scripted_effects/chaosx_logic_effects.txt
- common/scripted_effects/chaosx_settings_effects.txt
- common/scripted_effects/chaosx_events_log_effects.txt
- common/scripted_effects/015_utopia_manifesto_effects.txt

Result: no stale runtime, workbook, visible ID15, or literal shared-registry mapping exists.

## Event identity, classification, and firing

events/015_utopia_manifesto.txt establishes:

- add_namespace = chaosx.nr15 at line 1
- root ID chaosx.nr15.1 at line 14
- is_triggered_only = yes at line 19
- fire_only_once = yes at line 20

A brace-depth parse found:

| Measure | Count |
| --- | ---: |
| Top-level event definitions | 99 |
| Country events | 96 |
| News events | 3 |
| State events | 0 |
| ID declarations | 99 |
| Unique IDs | 99 |
| Duplicate IDs | 0 |
| Definitions without IDs | 0 |

This exactly matches the 99-definition statement in docs/events/015_utopia_manifesto.md.

common/script_constants/015_utopia_manifesto_constants.txt:16-18 defines:

- id = 15
- event_type = 3
- evolution_type = 15

common/script_constants/event_system_constants.txt:79 defines fire_once = 3.

common/scripted_effects/chaosx_logic_effects.txt:180 registers constant:utopia_manifesto_event.id exactly once in global.fire_once_events. The get_event_type resolver at lines 1104-1140 reads the major, repeatable, and fire-once arrays and resolves this entry to the fire-once type.

Automatic availability and dispatch are wired:

- common/scripted_effects/chaosx_logic_effects.txt:555-557 applies utopia_manifesto_automatic_event_is_available
- common/scripted_effects/chaosx_settings_effects.txt:4658-4668 prepares the random actor context and blocks an invalid context
- common/scripted_effects/chaosx_settings_effects.txt:4733-4741 dispatches chaosx.nr15.1 to the saved actor
- common/scripted_triggers/chaosx_settings_triggers.txt:25 includes Event 015 in event_log_event_is_reworked_default_enabled

Result: Minor Fire-Once and Fully Functional are supported by the live runtime registries.

## Cluster and world-end catalog status

common/scripted_effects/chaosx_event_cluster_effects.txt contains zero Event 015, utopia_manifesto, or symbolic Event 015 membership references. Event 015 is absent from both event_belongs_to_cluster and load_event_cluster_members.

No Event 015 world-end catalog branch was found. The route presentation super events are not world-end scenarios.

Result:

- workbook World-End Scenario is correctly blank
- workbook Cluster ID is correctly blank
- workbook Member Severity is correctly blank

## Workbook verification

The workbook contains these sheets:

- Events
- Clusters
- Scenarios
- Info
- Legend

Event ID 15 occurs exactly once in the Events table at row 16.

| Cell | Header | Current value | Result |
| --- | --- | --- | --- |
| A16 | ID | numeric 15 | PASS |
| B16 | Event Name | Utopia Manifesto | PASS |
| C16 | Details | exact Event Details localisation | PASS |
| D16 | Evo I | evolution 1 title, two newlines, and body | PASS |
| E16 | Evo II | evolution 2 title, two newlines, and body | PASS |
| F16 | Evo III | evolution 3 title, two newlines, and body | PASS |
| G16 | Evo IV | evolution 4 title, two newlines, and body | PASS |
| H16 | Evo V | evolution 5 title, two newlines, and body | PASS |
| I16 | World-End Scenario | blank | PASS |
| J16 | Type | Minor Fire-Once | PASS |
| K16 | Cluster ID | blank | PASS |
| L16 | Member Severity | blank | PASS |
| M16 | Status | Fully Functional | PASS |

The workbook comparison used the current definitions of:

- chaosx.event_name.15
- chaosx.events_log.window.event_details.utopia_manifesto
- utopia_manifesto.evolution.type
- utopia_manifesto.evolution.summary
- utopia_manifesto.evolution.locked_body
- all five utopia_manifesto.evolution.N.title keys
- all five utopia_manifesto.evolution.N.body keys
- all five utopia_manifesto.evolution.N.locked_title keys

All 20 parity keys have exactly one English definition. The workbook name, Event Details cell, and all five public evolution cells match their current localisation values exactly.

## Event log, Event Details, and evolution wiring

The latest actor and default actor path is present:

- common/scripted_effects/chaosx_events_log_effects.txt:253-260 maps Event 015 to utopia_manifesto_latest_actor
- the mapping sets events_log_default_actor and marks the actor as present

The Event Details evolution catalog is complete:

- common/scripted_effects/chaosx_events_log_effects.txt:2170-2191 adds exactly five preview rows
- the order is Glosses in the Margin, Necessary Shores, Cities of One Measure, Nowhere Made Law, and The Perfect Island
- each row uses constant:utopia_manifesto_event.evolution_type and its corresponding stage and tier constant

The live event list handles unavailable state correctly:

- common/scripted_effects/chaosx_events_log_effects.txt:3929-3934 changes the live Event 015 weight to the N/A sentinel when automatic availability is false

Evolution recording is connected to the shared history pipeline:

- common/scripted_effects/015_utopia_manifesto_effects.txt:5084-5088 prepares event ID, evolution type, stage, and tier
- common/scripted_effects/015_utopia_manifesto_effects.txt:5284-5293 validates the selected evolution, saves events_log_evolution_actor, sets the actor marker, and calls record_events_log_evolution_entry

The shared scripted-localisation audit covered the event name, Event Details body, evolution type, five public and locked titles, five bodies, locked body, summary, main evolution list, selected history, history details, and Event Details preview surfaces.

## English localisation parity

### Direct Event 015 popup references

The direct scan of events/015_utopia_manifesto.txt found:

| Measure | Count |
| --- | ---: |
| Direct reference occurrences | 504 |
| Unique referenced keys | 504 |
| Missing English definitions | 0 |
| Keys with duplicate English definitions | 0 |

The scan covered direct title, description, option name, text, tooltip, custom effect tooltip, and custom trigger tooltip values whose keys begin with chaosx.nr15., utopia_manifesto_, or chaosx_nr15_.

### Shared Event Details, log, settings, and evolution references

The three shared scripted-localisation files contain:

| Measure | Count |
| --- | ---: |
| Relevant reference occurrences | 47 |
| Unique parity keys | 20 |
| Unreferenced parity keys | 0 |
| Missing English definitions | 0 |
| Keys with duplicate English definitions | 0 |

The unique definitions are present in:

- localisation/english/chaosx_event_names_l_english.yml:17
- localisation/english/chaosx_gui_l_english.yml:551
- localisation/english/015_utopia_manifesto_evolutions_l_english.yml:2-19

Result: current English localisation and every audited Event Details, log, settings, history, and evolution selector agree.

## Exact command record

All commands were run from the repository root.

### Legacy repository and runtime search

    $patterns=@('World Tension Subsides','world_tension_subsides','Event 015 Placeholder','015_placeholder','015_world_tension_falls')
    foreach($pattern in $patterns){
        $all=@(rg -n -i --hidden -g '!paradox_wiki/**' -g '!.git/**' -g '!*.xlsx' -F -- $pattern . 2>$null)
        $runtime=@(rg -n -i -F -- $pattern events common localisation interface 2>$null)
        '{0}|repo_nonwiki_nonxlsx={1}|runtime={2}' -f $pattern,$all.Count,$runtime.Count
    }

Output:

    World Tension Subsides|repo_nonwiki_nonxlsx=27|runtime=0
    world_tension_subsides|repo_nonwiki_nonxlsx=2|runtime=0
    Event 015 Placeholder|repo_nonwiki_nonxlsx=8|runtime=0
    015_placeholder|repo_nonwiki_nonxlsx=5|runtime=0
    015_world_tension_falls|repo_nonwiki_nonxlsx=1|runtime=0

### Workbook legacy-string search

    python -u -c "import zipfile; p=r'docs/spreadsheets/chaos_redux_events_catalog.xlsx'; z=zipfile.ZipFile(p); x='\n'.join(z.read(n).decode('utf-8','ignore').lower() for n in z.namelist() if n.endswith('.xml')); ps=['world tension subsides','world_tension_subsides','event 015 placeholder','015_placeholder','015_world_tension_falls']; print('\n'.join(f'{q}|{x.count(q)}' for q in ps))"

Output:

    world tension subsides|0
    world_tension_subsides|0
    event 015 placeholder|0
    015_placeholder|0
    015_world_tension_falls|0

### Literal ID 15 shared-mapping search

    $files = @(
        'common/scripted_effects/chaosx_logic_effects.txt',
        'common/scripted_effects/chaosx_events_log_effects.txt',
        'common/scripted_effects/chaosx_settings_effects.txt',
        'common/scripted_effects/chaosx_event_cluster_effects.txt',
        'common/scripted_localisation/chaosx_scripted_localisation_events_log.txt',
        'common/scripted_localisation/chaosx_scripted_localisation_debug.txt',
        'common/scripted_localisation/chaosx_scripted_localisation_settings.txt'
    )
    rg -n --pcre2 '(?:event_id|settings_event_id|event_fire_record_id|events_log_selected_event_id)\s*=\s*15\b|\bvalue\s*=\s*15\b' $files

Output: zero matches.

### Symbolic ID 15 shared-reference count

    $m=@(rg -n -F 'constant:utopia_manifesto_event.id' common/scripted_effects/chaosx_logic_effects.txt common/scripted_effects/chaosx_settings_effects.txt common/scripted_effects/chaosx_events_log_effects.txt common/scripted_effects/015_utopia_manifesto_effects.txt common/scripted_triggers/chaosx_settings_triggers.txt common/scripted_localisation/chaosx_scripted_localisation_events_log.txt common/scripted_localisation/chaosx_scripted_localisation_debug.txt common/scripted_localisation/chaosx_scripted_localisation_settings.txt)
    'CONSTANT_ID_REFERENCES=' + $m.Count

Output:

    CONSTANT_ID_REFERENCES=17

### Cluster membership search

    $m=@(rg -n --pcre2 'utopia_manifesto|constant:utopia_manifesto_event\.id|(?<!\d)event_id\s*=\s*15(?!\d)' common/scripted_effects/chaosx_event_cluster_effects.txt)
    'EVENT15_CLUSTER_REFERENCES=' + $m.Count

Output:

    EVENT15_CLUSTER_REFERENCES=0

### Top-level event-definition parser

    @'
    import re
    from collections import Counter
    from pathlib import Path

    lines = Path('events/015_utopia_manifesto.txt').read_text(encoding='utf-8-sig').splitlines()
    depth = 0
    definitions = []
    current = None

    for line_number, line in enumerate(lines, 1):
        code = line.split('#', 1)[0]
        if depth == 0:
            match = re.match(r'\s*(country_event|news_event|state_event)\s*=\s*\{', code)
            if match:
                current = {'type': match.group(1), 'line': line_number, 'id': None}
                definitions.append(current)
        if current and current['id'] is None:
            match = re.match(r'\s*id\s*=\s*(\S+)', code)
            if match:
                current['id'] = match.group(1)
        depth += code.count('{') - code.count('}')
        if current and depth == 0:
            current = None

    ids = [definition['id'] for definition in definitions]
    duplicates = sorted(key for key, value in Counter(ids).items() if value > 1)
    print(f'TOP_LEVEL_DEFINITIONS={len(definitions)}')
    print(f'COUNTRY_EVENT={sum(d["type"] == "country_event" for d in definitions)}')
    print(f'NEWS_EVENT={sum(d["type"] == "news_event" for d in definitions)}')
    print(f'STATE_EVENT={sum(d["type"] == "state_event" for d in definitions)}')
    print(f'ID_DECLARATIONS={sum(value is not None for value in ids)}')
    print(f'UNIQUE_IDS={len(set(ids))}')
    print('DUPLICATE_IDS=' + repr(duplicates))
    print('MISSING_IDS=' + repr([d['line'] for d in definitions if d['id'] is None]))
    '@ | python -u -

Output:

    TOP_LEVEL_DEFINITIONS=99
    COUNTRY_EVENT=96
    NEWS_EVENT=3
    STATE_EVENT=0
    ID_DECLARATIONS=99
    UNIQUE_IDS=99
    DUPLICATE_IDS=[]
    MISSING_IDS=[]

### Workbook row inspection

    python -u -c "from openpyxl import load_workbook; p=r'docs/spreadsheets/chaos_redux_events_catalog.xlsx'; w=load_workbook(p,read_only=True,data_only=False); s=w['Events']; rows=[(r,[s.cell(r,c).value for c in range(1,14)]) for r in range(2,s.max_row+1) if s.cell(r,1).value==15]; print('SHEETS='+repr(w.sheetnames)); print('ID15_ROWS='+str(len(rows))); print('ROW='+str(rows[0][0])); print('NAME='+repr(rows[0][1][1])); print('TYPE='+repr(rows[0][1][9])); print('CLUSTER_ID='+repr(rows[0][1][10])); print('MEMBER_SEVERITY='+repr(rows[0][1][11])); print('STATUS='+repr(rows[0][1][12]))"

Output:

    SHEETS=['Events', 'Clusters', 'Scenarios', 'Info', 'Legend']
    ID15_ROWS=1
    ROW=16
    NAME='Utopia Manifesto'
    TYPE='Minor Fire-Once'
    CLUSTER_ID=None
    MEMBER_SEVERITY=None
    STATUS='Fully Functional'

### Direct Event 15 localisation-reference parity

    @'
    from pathlib import Path
    import re

    text = Path('events/015_utopia_manifesto.txt').read_text(encoding='utf-8-sig')
    reference_pattern = re.compile(r'^\s*(?:title|desc|name|text|tooltip|custom_effect_tooltip|custom_trigger_tooltip)\s*=\s*"?([A-Za-z0-9_.-]+)"?', re.M)
    references = [
        value for value in reference_pattern.findall(text)
        if value.startswith(('chaosx.nr15.', 'utopia_manifesto_', 'chaosx_nr15_'))
    ]

    definitions = {}
    for path in Path('localisation/english').glob('*.yml'):
        for line_number, line in enumerate(path.read_text(encoding='utf-8-sig').splitlines(), 1):
            match = re.match(r'^([^\s:#][^:]*)\s*:', line)
            if match:
                definitions.setdefault(match.group(1), []).append((str(path), line_number))

    keys = sorted(set(references))
    print(f'EVENT15_DIRECT_LOC_REFERENCE_OCCURRENCES={len(references)}')
    print(f'EVENT15_DIRECT_LOC_REFERENCE_KEYS={len(keys)}')
    print('MISSING_KEYS=' + repr([key for key in keys if key not in definitions]))
    print('DUPLICATE_DEFINITION_KEYS=' + repr({key: definitions[key] for key in keys if len(definitions.get(key, [])) > 1}))
    '@ | python -u -

Output:

    EVENT15_DIRECT_LOC_REFERENCE_OCCURRENCES=504
    EVENT15_DIRECT_LOC_REFERENCE_KEYS=504
    MISSING_KEYS=[]
    DUPLICATE_DEFINITION_KEYS={}

### Shared log, Event Details, settings, and evolution parity

    @'
    from pathlib import Path
    import re

    files = [
        Path('common/scripted_localisation/chaosx_scripted_localisation_events_log.txt'),
        Path('common/scripted_localisation/chaosx_scripted_localisation_debug.txt'),
        Path('common/scripted_localisation/chaosx_scripted_localisation_settings.txt')
    ]
    keys = {
        'chaosx.event_name.15',
        'chaosx.events_log.window.event_details.utopia_manifesto',
        'utopia_manifesto.evolution.type',
        'utopia_manifesto.evolution.summary',
        'utopia_manifesto.evolution.locked_body'
    }
    keys |= {
        f'utopia_manifesto.evolution.{index}.{kind}'
        for index in range(1, 6)
        for kind in ('title', 'body', 'locked_title')
    }

    references = []
    for path in files:
        references += [
            value for value in re.findall(r'\blocalization_key\s*=\s*"?([A-Za-z0-9_.-]+)"?', path.read_text(encoding='utf-8-sig'))
            if value in keys
        ]

    definitions = {}
    for path in Path('localisation/english').glob('*.yml'):
        for line_number, line in enumerate(path.read_text(encoding='utf-8-sig').splitlines(), 1):
            match = re.match(r'^([^\s:#][^:]*)\s*:', line)
            if match:
                definitions.setdefault(match.group(1), []).append((str(path), line_number))

    print(f'SHARED_SCRIPTED_LOC_REFERENCE_OCCURRENCES={len(references)}')
    print(f'SHARED_SCRIPTED_LOC_REFERENCE_KEYS={len(set(references))}')
    print('UNREFERENCED_PARITY_KEYS=' + repr(sorted(keys - set(references))))
    print('MISSING_KEYS=' + repr(sorted(key for key in set(references) if key not in definitions)))
    print('DUPLICATE_DEFINITION_KEYS=' + repr({key: definitions[key] for key in set(references) if len(definitions.get(key, [])) > 1}))
    '@ | python -u -

Output:

    SHARED_SCRIPTED_LOC_REFERENCE_OCCURRENCES=47
    SHARED_SCRIPTED_LOC_REFERENCE_KEYS=20
    UNREFERENCED_PARITY_KEYS=[]
    MISSING_KEYS=[]
    DUPLICATE_DEFINITION_KEYS={}

## Limitations

This is a current static source and workbook audit. It did not render the Event Details interface or launch an in-game event sequence. No limitation found here changes the PASS for reference completeness, identity replacement, classification, workbook parity, or shared mapping coverage.

## Remaining blockers and follow-up

Blockers: none.

Required follow-up from this audit: none.

The parent can use this report as the current evidence record for English-localisation completion and spreadsheet/catalog cross-surface completion.
