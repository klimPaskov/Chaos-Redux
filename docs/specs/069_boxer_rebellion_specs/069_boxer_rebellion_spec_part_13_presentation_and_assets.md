# Presentation, artwork, and super-events

The visual and writing direction follows a revived movement operating in the campaign's actual twentieth-century world.
Ordinary scenes should use period-compatible clothing, weapons, transport, architecture, and photographic treatment.
High-Chaos material can show a clearly fictional anomaly while keeping the surrounding military world consistent.

All labels in this package are working design descriptions.
No finished localisation, selected quotation, licensed audio file, portrait, flag, or game-ready image is supplied here.
The asset and research prompts define that later work.

## The normal decision surface

The actor sees one principal Event 069 category for its current role and phase.
It contains Boxer Strength, Intervention Pressure, a short current-situation description, a small set of useful actions, and the active missions.
Show the important causes through concise status text and tooltips.
Do not expose a table of every hidden regional score.

The design uses ordinary decisions and formatted numeric text.
It does not require a new scripted-GUI window, a custom graphical meter, or extra category controls.
A static category picture is therefore appropriate under the project's presentation rules.
The normal scenario settings window is reused for manual setups.

Prepare role-specific category-picture directions for a Chinese government, the organized movement, a foreign expedition, and a settlement.
Only the appropriate picture is shown for the current primary category.
The actual category consumer, size, and supported switching behavior need inspection before production.
The reference family's 114 by 101 canvas is a starting reference, not proof of the runtime dimensions.

## News and personal reports

| Presentation ID | Moment | Audience and content direction |
| --- | --- | --- |
| N01 Opening | Several Boxer centers become a national issue | One major news event. Identify the actual affected regions and governments, without assuming Qing rule |
| N02 Foreign district threatened | A significant siege or attack creates an international crisis | News only for a major public incident. Personal reports go to actual responsible and affected actors |
| N03 Chinese government endorses the movement | An important government accepts a public compact | Explain the government's choice, its stated limits, and the actual foreign response |
| N04 Coalition formed | At least two independent powers accept a common mandate | Name the real coalition and mandate, with the actual member count |
| N05 Major relief or siege result | A major objective is resolved | Distinguish evacuation, protection, capture, and civilian losses |
| N06 Boxer authority established | A durable independent government emerges | Describe its founding territory, institutions, and unresolved claims |
| N07 Foreign withdrawal or defeat | A substantial intervention ends | Identify who withdrew, what was recovered, and which disputes remain |
| N08 Protocol imposed or amended | An important settlement becomes effective | Describe the actual terms and their recipients, not a stock historical treaty |
| N09 Postwar Chinese dispute | A major pact faces a real territorial or command dispute | Explain the competing governments and the agreement at issue |

Routine arrests, deliveries, and minor route repairs do not need global news.
Use the event log and targeted reports for ordinary progress.
Aggregate repeated regional incidents where possible without hiding an urgent actionable warning.

Personal report families cover the opening policy, a threatened site, a society's compact, a command dispute, an ultimatum, a mandate revision, an evacuation result, a ritual investigation, a treaty term, and a postwar integration.
Every report names the current actor and location through correct dynamic localisation.
It must not show an extinct government as the active issuer.

## Writing direction

Chinese government text should distinguish sovereignty, civilian security, local authority, and the military usefulness of the societies.
Foreign text should distinguish rescue, protection, suppression, coercion, and territorial ambition.
Boxer text should reflect disagreements over command, traditional authority, modern weapons, and the limits of government cooperation.

Do not make every Chinese actor sound like the same monarchist government.
Do not assume that every foreign country is a Western colonial power.
Do not equate Chinese Christians with foreign nationals or imply that all local supporters endorse attacks on civilians.

Options should state the public action and its visible consequences.
Tone can be dry, ironic, skeptical, or bureaucratic where it fits, but civilian suffering should not become a disposable joke.
Keep hidden outcomes, internal variable names, source history, and tuning explanations out of player-facing text.

## Asset families and placement

Use `069_boxer_rebellion` as the event folder below the relevant asset category.
Keep root-only engine exceptions for flags and achievements.
Every produced asset needs its source, exact consumer, runtime path, sprite or lookup, state binding, and review evidence.

| Family | Required coverage | Target or verification rule | Proposed runtime location |
| --- | --- | --- | --- |
| Report images | The ten report families described above, with intentional reuse only when the same scene fits | 210 by 176 processed documentary card, black and white with sepia and transparent card edges | `gfx/event_pictures/069_boxer_rebellion/` |
| News images | N01 through N09 | 397 by 153 black-and-white period documentary or press composition | `gfx/event_pictures/069_boxer_rebellion/` |
| Super-event scenes | SE01 through SE03 below | 457 by 328 real scene composition, not a title card or icon | `gfx/super_events/069_boxer_rebellion/` |
| Category icons | Current role and phase category identity | Inspect the exact category-icon consumer and reference family | `gfx/interface/decisions/069_boxer_rebellion/` |
| Category pictures | Chinese response, Boxer organization, foreign intervention, settlement | Inspect the actual consumer, with 114 by 101 as the reference-family canvas | `gfx/interface/decisions/069_boxer_rebellion/` |
| Decision icons | The thirty semantic icon requirements below | 32 by 32, independent decision-family source art | `gfx/interface/decisions/069_boxer_rebellion/` |
| Mission icons | One reviewed semantic requirement for each M01 through M18 | Use the mission reference family and actual consumer, normally 32 by 32 | `gfx/interface/decisions/069_boxer_rebellion/` |
| Idea icons | The three institutional slots and their actual lifecycle variants | 64 by 64, compact independent idea artwork | `gfx/interface/ideas/069_boxer_rebellion/` |
| Focus icons | Every final focus node derived from B01 through B09 | Normally 94 by 86, with an explicit node-to-icon crosswalk | `gfx/interface/goals/069_boxer_rebellion/` |
| Institutional portraits | Founding council and the three changed governing institutions when a distinct portrait is needed | 156 by 210, source-mode and identity gate required | `gfx/leaders/069_boxer_rebellion/` |
| Commander portraits | Every explicitly selected new or transferred commander requiring a portrait | 156 by 210, no fabricated small full-portrait texture | `gfx/leaders/069_boxer_rebellion/` |
| Advisor cards | Only the explicitly adopted civil, command, arsenal, and diplomatic role cards | Native 65 by 67 card workflow, independent crop and approved template | Verified advisor consumer under the event-scoped leader asset path |
| Boxer flags | Founding identity and three political-route identities | Flat masters with 82 by 52, 41 by 26, and 10 by 7 TGA exports | Normal, medium, and small engine flag roots |
| Coalition emblem | One event-owned coordination symbol, if the approved consumer displays it | Exact faction or emblem family inspection, no generic resized focus art | Appropriate event-scoped interface asset folder |
| Division-template emblem | The planned Boxer militia identity | Separate 76 by 42 and 30 by 12 outputs, subject to exact consumer review | Verified event-scoped unit-interface folder |
| Achievements | A01 through A12, each with completed, grey, and not-eligible states | 64 by 64, supplied templates and deterministic state pipeline | `gfx/achievements/` root |

The focus architecture deliberately leaves the final node graph to implementation.
Before art production begins, expand each focus-family requirement into a row for every actual node.
A family-level row is not enough to claim complete asset coverage.
The same rule applies if a planned report family becomes several materially different scenes.

## Decision icon crosswalk

Intentional reuse is confined to the same semantic decision family.
No decision icon is a resized focus, idea, or achievement icon.

| Icon requirement | Consumers | Main visual subject |
| --- | --- | --- |
| DI01 | D01 | A restrained security order and local authority symbol |
| DI02 | D02 | A guarded local accommodation |
| DI03 | D03 | Public recognition of an organized society |
| DI04 | D04, D12, D17, D38, D39 | Protection of a civilian district |
| DI05 | D05, D21 | A command or network under control |
| DI06 | D06, D19 | A local compact with surrendered or regulated arms |
| DI07 | D07, D42 | Evidence and inspection |
| DI08 | D09, D34 | A supplied military or transport commitment |
| DI09 | D10 | Civilian relief |
| DI10 | D08 | A repaired railway connection |
| DI11 | D11, D31, D37 | An orderly ending of an armed commitment |
| DI12 | D13 | Local civil administration |
| DI13 | D14 | A locally raised rifle formation |
| DI14 | D15 | A contested finite depot |
| DI15 | D16 | Training and regularization |
| DI16 | D18, D29, D32, D33 | A council or conference deciding a mandate |
| DI17 | D20 | A specific regulated ritual practice |
| DI18 | D22 | A controlled workshop or arsenal |
| DI19 | D23, D30 | A limited military compact |
| DI20 | D24 | A government established by the societies |
| DI21 | D25 | Safe evacuation |
| DI22 | D26, D28, D35 | A real expeditionary commitment |
| DI23 | D27 | A formal, specific ultimatum |
| DI24 | D36 | A documented compensation claim |
| DI25 | D40 | A scheduled treaty payment |
| DI26 | D41 | A negotiated payment pause |
| DI27 | D43 | Reconstruction of a damaged district |
| DI28 | D44 | Revision of an imposed protocol |
| DI29 | D45 | Administrative integration by an actual agreement |
| DI30 | D46 | Closure of a completed intervention conference |

## Portrait and flag boundaries

Grounded portraits need attributed sources and an independent identity, framing, and provenance review.
Existing people require ownership checks before recruitment or reuse.
An authentic historical object used for an institutional portrait must be identified as an object, not presented as a photograph of a fictional council meeting.
A missing source cannot be replaced with an invented realistic face.

Every new flag begins with research into appropriate symbols and a clear distinction between an attested design and an alternate-history synthesis.
The final flat design follows the required ImageGen route and is checked against the accepted reference or motif plan.
Do not use a Qing flag merely because the event is named Boxer Rebellion.
Do not replace the existing base flags of Chinese or foreign participants that merely take part in the crisis.

Each political-route identity needs a deliberate visual design.
A recolored founding flag or a small added shape is not sufficient for three materially different governments.
The three flag sizes must remain readable and use the engine's correct orientation convention.

## Super-event candidates

Super-events mark earned campaign-level moments.
They do not replace the normal opening news and do not fire for every coalition, siege, or local victory.
The design IDs below are semantic references, not reserved numeric framework slots.

### SE01 A common Chinese anti-intervention front

The moment is the effective formation of a broad Chinese pact against a credible intervention, not the first conference invitation.
The participants must control a substantial share of the active Chinese theater, accept useful contributions, and face an actual foreign campaign.
In a unified China, the national regional-institution variant can qualify without creating extra governments.

The proposed threshold includes at least 60% of the reviewed theater's relevant population under participating authority, functioning regional participation, and a verified intervention threat.
The exact threshold must be tested against the installed map.
The image direction is a period-compatible public or military assembly with visibly distinct participating institutions, without unreadable generated banners.
The quote research concerns cooperation, common danger, and the conditions of political unity.
The audio direction is a structured musical recording appropriate to collective mobilization, with verified composition and recording rights.

### SE02 A substantial intervention withdraws

The moment requires a credible campaign, not the departure of a token observer.
The intervention must have established real military commitments and remained consequential for roughly 180 days or produced an equivalently reviewed major campaign outcome.
At least two independent participating powers and a substantial actual foreign deployment are the normal qualifying pattern.

The image direction is an actual departure, abandoned foreign position, or Chinese reoccupation of a named site, with period equipment and a clear human subject.
The quote research concerns withdrawal, limited power, sovereignty, or the cost of intervention.
The audio should fit the actual victor and outcome without treating civilian loss as a simple celebration.
A separate defeat-aftermath treatment is not required for a merely local expedition.

### SE03 Boxer authority becomes a durable national government

The moment follows a completed political route, functioning institutions, a sustained independent military core, and broad actual authority.
A newly created two-state enclave does not qualify immediately.
The proposed threshold includes at least 60% of the reviewed theater population, several functioning regional institutions, and a completed 90-day consolidation hold after the relevant route commitment.

The image direction follows the actual governing route: a civilian assembly, a national military institution, or a religious governing council.
It must not depict a named real person whose identity has not been sourced.
The quote research concerns government, authority, independence, or the responsibility that follows victory.
The musical recording must be unique to this super-event unless a specific reuse is explicitly approved.

## Super-event production contract

For each candidate, select the actual framework slot only after inspecting the current registry.
Research several relevant quote and short cultural-reference candidates, verify wording and attribution, and record any translation or rights uncertainty.
Do not invent a quote or label a modern recording public domain because its composition is old.

Use a real, properly licensed musical recording, normally one to two minutes and no more than two minutes without an explicit exception.
Do not substitute generated tones, a noise bed, or a generic sound effect.
Each completed super-event needs its own accepted track, audio ID, sound definition, settings-volume wrappers, image getter, localisation, event trigger, and canonical music-catalog row.

No quote, musical recording, or numeric slot has been selected in this planning run.
The super-event research prompt owns that unresolved work.
The moments can be designed here without pretending that their final presentation package already exists.

## Production and evidence

Generated icons and other alpha-backed assets begin with native transparency.
Report and news scenes use their proper photographic treatment.
Keep source images, processed previews, runtime files, and candidate history separate.
Use the skill-local report and DDS processors and the exact supplied achievement templates.

The asset manifest must start from the accepted requirements, then trace every row to an actual runtime consumer.
A folder full of attractive images is not complete coverage.
No final art has been generated or converted in this planning package, and no asset references have been wired into the repository.
