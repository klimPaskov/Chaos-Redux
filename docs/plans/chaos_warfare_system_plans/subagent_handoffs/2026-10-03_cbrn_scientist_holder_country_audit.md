# CBRN Scientist Holder Country Package Audit

Disposition: The bounded country-holder implementation is reviewed at source under the parent’s active CBRN task. This report records implementation evidence and does not claim fresh native runtime acceptance.

## Scope and evidence

This was a read-only source audit. The only file written by this audit is this handoff.

The before-state comparison used `docs\testing\2026-10-03_cbrn_dated_holder_before\chaosx_startup_character_recruitment.txt` and `docs\testing\2026-10-03_cbrn_dated_holder_before\chaosx_startup_history_effects.txt`.

The authorized QA file is `docs\testing\live_qa\20261003_full_playtest\logs\cycle1\error.log`, SHA-256 `EDB523793E8C7EA1C79FF53546B1CFE5789C498217160191C9B022F09A85BAB3`. It has 553 lines and 58 `recruit_character should only happen in game/history files` warnings. The same 29 warning sites repeat at lines 250–278 and 513–541. This is evidence for the old runtime-recruit source, not validation of the current holder source. The file contains no `Unknown character` entry.

The user separately reported that a fresh January 1, 1936 USA start showed `Unknown character` for Haldane, Fishman, and Velikanov under the prior runtime-recruit implementation. That report is not present in the authorized log file. Fresh native validation of the current CSH implementation remains pending.

## Country package coverage

- Tag registration is present once at `common\country_tags\cbrn_scientist_holder.txt:2`, and the corresponding definition is `common\countries\CBRN Scientist Holder.txt`. The installed vanilla country-tag and country-definition folders contain no CSH collision.
- Parent follow-up scanned every `common/country_tags/*.txt` under `C:\Program Files (x86)\Steam\steamapps\workshop\content\394360` and the local `Hearts of Iron IV\mod` root with `rg --no-ignore` and the anchored `CSH =` declaration pattern. The scan completed with only this package's registration as a match; no other installed Workshop or local-mod tag collision was found.
- The history roster has 38 direct home-country recruits and 29 CSH recruits, for 67 unique identities. All 67 IDs have static definitions in `common\characters\`; none are missing or duplicated in the history roster.
- The 29 CSH identities each have one matching `set_nationality` transfer. Every transfer checks that the home country does not already have the character and that CSH still has it. The parent’s contract rerun independently confirmed the 67/38/29 counts, all 29 guarded transfers, and exact executable reconstruction.
- The CSH history block at `history\general\chaosx_startup_character_recruitment.txt:89` is tag-scoped and has no date or DLC gate. The three reported IDs are declared as ordinary top-level character definitions: Haldane at `common\characters\cbrn_historical_scientists.txt:124`, Fishman at `common\characters\cbrn_historical_scientists.txt:533`, and Velikanov at `common\characters\cbrn_historical_specialists.txt:400`. None of these three definitions is hidden behind a DLC or definition-date gate. Velikanov’s advisor role has a doctrine availability condition, which does not gate his character definition or scientist role.
- The dated helper blocks in `common\scripted_effects\chaosx_startup_history_effects.txt:393` through `:952` preserve the prior date conditions, retirement handling, traits, and identity flags while replacing runtime `recruit_character` calls with guarded CSH-origin `set_nationality` calls. Haldane keeps the pre-1936-03-14 transfer gate and post-1936-03-13 retirement check. Fishman and Velikanov keep their existing 1937-06-05 and 1938-04-08 cutoffs. The parent’s scoped diff review confirmed the unchanged executable portions.
- `common\on_actions\cbrn_historical_startup_on_actions.txt:9` calls only the eight fixed home-tag helpers through `on_daily_AST`, `on_daily_CAN`, `on_daily_ENG`, `on_daily_GER`, `on_daily_JAP`, `on_daily_POL`, `on_daily_SOV`, and `on_daily_USA`. There is no CSH daily hook or new world-wide iteration.
- The history setup at `history\countries\CSH - Scientist Registry.txt:1` assigns no states, cores, or claims. The mod has no state-history reference to CSH and no CSH focus tree, decision, event, formable, or AI-strategy route was found in the inspected script surfaces. The OOB at `history\units\cbrn_scientist_holder.txt:1` is empty. Research slots, stability, and war support are set to zero, and the tag is politically neutral with elections disabled.
- CSH has no flag files under `gfx\flags`. Since the holder has no states or in-scope player-facing route, this is a latent visibility gap rather than a confirmed playability defect. Its English country name, definition, and adjective are localized in `localisation\english\cbrn_scientist_holder_l_english.yml:2`.
- The character definitions and their portrait, scientist, and advisor data are not modified by the holder change. Installed effect documentation describes `set_nationality` as transferring the existing character from one country to another, and character documentation says character roles remain on transfer. The sampled definitions show the expected scientist records and portraits. Velikanov’s source definition also retains its advisor role and `original_tag = SOV` eligibility.
- No CSH-owned CXT setup, unit, equipment, technology, or starting production surface was found. The holder adds no military formation, stockpile, production line, or research package.

## Map and MCP limits

CSH declares `capital = 1` in `history\countries\CSH - Scientist Registry.txt:2`. Installed vanilla identifies state 1 as Corsica and assigns it to FRA in `history\states\1-France.txt:3` and `:10`. This capital reference does not itself assign ownership, cores, or claims, and its source comment labels it an engine bootstrap. Its runtime effect on a stateless tag remains unverified and is the main map-state risk to retain for review.

The HOI4 MCP reference calls and the bounded map inspection exposed in the connected tool list did not return during this audit and were cancelled. The service health and workspace negotiation therefore remain unverified. MCP map inspection and rendering evidence is absent, so the source review above is not a substitute for that evidence.

Relevant offline syntax evidence was read locally because the reference route did not return. `paradox_wiki\Effects - Hearts of Iron 4 Wiki.md:2735` and `:2742` describe the country-scoped `set_nationality` transfer shape. `paradox_wiki\Effects - Hearts of Iron 4 Wiki.md:3246` and `:3252` state that `recruit_character` is history-only. Installed `documentation\effects_documentation.md:5696` describes country-scoped character attachment, while `:7397` describes the nationality-transfer scope contract; the history-only restriction is stated by the offline wiki and the user-supplied engine warning. Vanilla `common\scripted_effects\INS_scripted_effects.txt:974` uses the target-country and character-parameter form of `set_nationality`.

## Findings and next validation

No blocking source defect was confirmed in the CSH registration, roster counts, character definitions, guarded transfer structure, or retained date and retirement logic. The original 58 startup warnings correspond to the old `recruit_character` calls in scripted effects and the current source removes that runtime-recruit pattern.

The reported January 1 USA `Unknown character` symptom is not explained by missing or gated source definitions. It remains a runtime question about whether history-time recruitment into CSH is visible to the startup transfer helpers on the current source state. Keep fresh native confirmation pending before claiming that this symptom is resolved.

The review did not launch HOI4, modify gameplay, stage files, or commit. The parent owns final source integration and commit. No balance or weighted-logic change is in this bounded country-holder scope.
