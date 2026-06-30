# Achievement prompt for Event 011 Secret Alliance

Use the event spec files as source design. Implement achievements only after the gameplay mechanics, decisions, reveal routes, public faction state, and member tracking flags exist. Do not make any achievement unlock just because Event 011 fired.

The list below gives achievement directions. Write polished title and description text from each direction.

## Achievement list

| Working key | Visibility | Eligible country | Unlock conditions | Disqualifiers | Difficulty | Icon direction |
| --- | --- | --- | --- | --- | --- | --- |
| `secret_alliance_open_file` | Visible | Target country | Reveal at least one founding member through evidence before Evolution II sabotage succeeds | Reveal caused by war or ultimatum first | Medium | Open dossier with three blurred seals |
| `secret_alliance_empty_chairs` | Hidden | Target country | Make all founding members leave or become neutral before public reveal | Any founding member joins public war | Hard | Three empty chairs under lamp |
| `secret_alliance_no_one_came` | Visible | Target country | Public reveal happens, but fewer than three members join the opening war because of preparation and diplomacy | Target joins a larger faction after reveal starts | Hard | Empty faction table and broken call bell |
| `secret_alliance_border_knife` | Visible | Target country | Win a limited border operation against a neighboring pact member before public reveal | Full war starts before operation success | Medium | Border post with small knife and sealed pouch |
| `secret_alliance_patron_exposed` | Hidden | Target country | Identify and neutralize or isolate a major patron before Evolution III public reveal | Major patron leads public pact | Hard | Great-power seal under magnifying glass |
| `secret_alliance_counter_pact` | Visible | Target country | Rally at least two friendly governments or guarantees before the pact goes public, then survive the reveal crisis | Player already in a major faction at root event | Medium | Friendly hands around a defensive shield |
| `secret_alliance_alone_against_room` | Hidden | Target country, must be minor at root | Defeat a public pact that includes a major patron while never joining a faction during the crisis | Target becomes major through tag switch exploit route | Very hard | Small flag facing a ring of seals |
| `secret_alliance_last_signature` | Visible | Target country | Capitulate or force exit of every founding member within a defined post-reveal deadline | Pact disbands only through member invalid cleanup | Hard | Pen scratching out three signatures |
| `secret_alliance_clean_reveal` | Visible | Target country | Publicly reveal the pact through evidence and avoid any sabotage deaths before reveal | Any fatal sabotage event fires | Hard | Clean dossier and unbroken factory window |
| `secret_alliance_war_case` | Hidden | Target country | Use prepared public war case to start the war with high preparedness and win without losing a core state | Target loses a core state before peace | Very hard | Court file over mobilization map |

## Tracking requirements

Implementation needs flags or variables for:

- Founding member IDs.
- Member exit cause.
- Reveal route.
- Whether reveal was caused by war, evidence, leak, patron, or ultimatum.
- Whether a major patron joined or led.
- Number of public members joining opening war.
- Fatal sabotage before reveal.
- Target faction status during crisis.
- Target core-state loss during public crisis.
- Border operation success before reveal.
- Friendly governments rallied before reveal.
- Deadlines after reveal.

## Asset handoff

Achievement icon production belongs to the asset prompt. Completed icons should be generated first at 64x64, then grey and not-eligible variants can be created according to the project achievement workflow.
