# France 1939 protective industry

Disposition: implemented source calibration under the accepted historical-start contract; native queue allocation and output remain unverified.
Acceptance basis: the user requested a separately sourced 1939 equipment, industry and personnel setup, approved force-scaled military issue with a 25% reserve, and directed non-British civilian issue to remain zero until country-specific quantities are evidenced.
The parent selected the one-existing-factory allocation below on 2026-10-09 within that mandate.

## Equipment production

`chaosx_startup_grant_fra` in `common/scripted_effects/chaosx_startup_history_effects.txt` requests one existing military factory for `gas_mask_equipment_1` when France exists and the startup date is after 31 December 1938.
The basic-mask technology is granted before the production request, France is the equipment creator, and the existing public startup guard prevents the normal startup path from applying twice.
The file-scoped settings `@fra_1939_respirator_factories = 1` and `@fra_1939_respirator_efficiency = 100` mirror the existing British startup pattern and installed vanilla production syntax.
Both numbers are gameplay calibration for an operating manufacturing program, not a claim about plant counts, productivity, or historical equipment totals.
The line requests an existing factory through the native production queue; it does not create an industrial building or guarantee a free factory.
No equipment stock is granted, no civilian issue flag is set, and the approved military issue and reserve formulas remain intact.
The January 1936 bookmark receives no such production request.

## Historical basis and limits

The [Centre d'Histoire de la Résistance et de la Déportation collection entry](https://www.chrd.lyon.fr/musee/collections/masque-gaz-et-son-etui) describes municipal civilian-mask distribution from spring 1939, multiple manufacturers and demand beyond their available supply.
The [Service historique de la Défense inventory](https://www.servicehistorique.sga.defense.gouv.fr/sites/default/files/notices_files/SHDGR_INV_1N_6N_1920_1940_T1.pdf), record 6 N 340, identifies manufacturing, delivery and private-industry orders covering 31 May 1938 to 3 November 1939.
Together these support active production before the August bookmark.
They do not supply a national mask total or geographic issue profile for that date.
The [January 1939 ICRC review](https://international-review.icrc.org/sites/default/files/S1026881200035029a.pdf), page 24, reports five million as a production forecast rather than completed issue, and the [1951 Senate account](https://www.senat.fr/comptes-rendus-seances/4eme/pdf/1951/02/S19510215_0483_0517.pdf) combines 1938–42 distribution.
Neither total becomes a starting stock grant.
Zero scripted civilian starting coverage records the accepted evidence threshold, not a claim that France had no civilian masks.

The [western country review](../../../plans/chaos_warfare_system_plans/subagent_handoffs/2026-10-09_1939_western_start_entitlements.md) records the France proposal and the reasons for no additional German or Italian grants.
The [eastern country review](../../../plans/chaos_warfare_system_plans/subagent_handoffs/2026-10-09_1939_eastern_start_entitlements.md) retains Japan's and the Soviet Union's approved military profiles and dated staff/institutions without converting procurement plans into delivered civilian inventory.
No unused institutional status flags are added.

## Evidence and interfaces

Run `node docs/testing/2026-10-09_france_1939_protection/source_tests.js` from the mod root.
The bounded projection checks both bookmark dates, the year boundary, absent France, the once-only public grant, prior mask research, unchanged British setup, and exact preservation of every other startup AST node.
`docs/testing/2026-10-09_france_1939_protection/reference_evidence.json` preserves the installed documentation at `documentation/effects_documentation.md:1207–1232`, the offline country-creation wiki at lines 714–743, and installed `history/units/AFG_1939.txt:136–146` as a one-factory, efficiency-100 precedent.
The MCP validator confirmed command kinds and Country scope, with `valid = null` because the production argument block is unchecked; its result is not a native execution pass.
The native equipment name, icon and production consumer already exist, so no new localisation, sprite, CXT grant or event-catalog field is introduced.
The first production request still competes for France's existing factory capacity.

## Further evidence

A civilian starting grant would require dated completed deliveries, issue totals and the recipient locations before the August 1939 bookmark.
The broader historical profile and native production-queue acceptance remain separate from this bounded source correction.
