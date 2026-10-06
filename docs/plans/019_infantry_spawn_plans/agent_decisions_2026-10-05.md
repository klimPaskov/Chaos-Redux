# 019 Soldiers from Nowhere release review, 2026-10-05

Status: source repairs implemented; release sign-off remains incomplete because required current-source MCP and live evidence is unavailable.

## Accepted decisions and implementation

- Accepted under the user's G3, G5-G7 authority: plain military reports, accurate admission/refusal language and a clear result for excluded human requesters.
- Implemented: the base report is Unidentified Troops Assemble, with the acknowledgement explaining the Muster decisions.
- Implemented: Evolution III and IV opening text describes admitting or refusing arriving troops instead of bookkeeping.
- Implemented: .905 tells an excluded human requester that troops cannot arrive in territory available to its command.
- Implemented: four focus navigation shortcuts provide Command, Supply, Army and Expansion anchors.
- Implemented: claimant-demand cost getters show only the selected demand, using the eight existing fee branches.
- Player-facing localisation cleanup preserves backend keys, macros and paid quantities; its full handoff lists changed keys and unused legacy-string dispositions.
- Existing formation generation, country/family packages, equipment obligations, claimant outcomes, cleanup and the two documented engine-constrained transfer/combat arrangements were retained.
- No formation, country route, unit model or runtime portrait was replaced.

## Owned files and surfaces

- `events/019_infantry_spawn.txt`
- `common/national_focus/019_infantry_spawn_derivative_focus.txt`
- `localisation/english/019_infrantry_spawn_l_english.yml`
- `common/scripted_localisation/019_infantry_spawn_claimant_cost_localisation.txt`
- `docs/events/019_infantry_spawn/overview.md`

## Evidence and limits

- Live baseline: evt019_pop00.png and the contact sheet show one manifestation report plus unrelated vanilla popups.
- Localisation handoff: subagent_handoffs/localisation_cleanup_2026-10-05.md records consumer checks and zero parchment colour findings.
- The country/asset audit resolves the 104 flag identities and 45 derivative focus icons; the latter retain their existing 100x88 consumer family.
- The 45-node derivative route map and mutually exclusive branches were reviewed in source.
- Current MCP event/focus/probability evidence remains unavailable after route timeouts, and native long-text/cost display still requires the orchestrator's checks.

## Exact orchestrator checks

- Load qa_001_fresh_head as USA and force Event 019: expect one next-day country report, formations in the army, and no report for every state.
- Use the existing Evolution III/IV setup and open the first arrival: expect short admission/refusal choices and no bookkeeping terms in their prose.
- Open a claimant with each of the eight demand types: the Accept Demand row and tooltip must show only the selected demand's payment, and the debit must match it.
- Exercise a formation request, failed materialisation refund, prototype-preservation timeout and demobilisation: confirm one debit/refund and no repeat free draw.
- Use an existing derivative scenario to inspect Command/Supply/Army/Expansion navigation, family routes, unit models, portraits, counters and the relevant Event Log entries.
- Force the global manifestation while the human requester is in an excluded scenario/cleanup state: expect one No Troops Arrive Here explanation.

## Catalog and assets

The catalog workbook and exports were not edited.
Catalog alignment notes are in catalog_changes_pending.md.
Existing runtime art, sound, flags, portraits and models were reused.
No live HOI4 session or desktop window was opened by this task.

## Required reference evidence

- `paradox_wiki/Event modding - Hearts of Iron 4 Wiki.md:117-150`, local source SHA-256 `96327b896298420d84058394a44ed08be7eb518726b8f207b392fea71f05d43d`.
- `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md:303-328`, local source SHA-256 `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md:2943-2967`, local source SHA-256 `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md:5053-5074`, local source SHA-256 `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/triggers_documentation.md:3624-3640`, local source SHA-256 `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`.
- `paradox_wiki/National focus modding - Hearts of Iron 4 Wiki.md:146-167`, local source SHA-256 `bd989a13237c464f140a0aa671cc42c30a48e84a27dae791b8914654fb9c6203`.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/national_focus/germany.txt:42-80`, local source SHA-256 `4cfd72972e19bcc560684dfc2f170e62ce786153ee01cf06ee7acc9609996095`.

Reference context/search/read routes returned some citations; failed and omitted sections were read locally.
Context inventories do not establish rule or engine coverage.
The connected service version and standalone viewer availability were not independently confirmed.
No repository-wide state-flow or helper-expansion query was used.


## Graphics decisions accepted on 2026-10-06

The current graphics brief authorizes solid badge interiors and removal of detached export fragments while retaining the existing artwork.
Both zombie focus badges and the prototype-cannibalization icon preserve their main silhouettes and stable names.
Independent native-size review accepted all three repaired textures.
Evidence is docs/plans/gfx_fix_2026-10/019_report.md and alpha_independent_review.md.
