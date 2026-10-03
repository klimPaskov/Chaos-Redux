# Prospective Reception Pre-Edit Source Manifest

Date: 2026-10-03.

The directory-local `.gitattributes` disables text conversion and clean filters for these immutable `.txt` archives.
Durable commit acceptance additionally requires reading every committed blob as raw bytes and matching its SHA-256 to the recorded copied-byte hash; filesystem checks alone are not sufficient.

This manifest records byte-equal source snapshots created before the prospective first-host reception edits. The source copies use the original basenames directly under this directory. Frozen bytes were copied from explicit literal source and destination paths, then SHA-256 checked against the original. A preliminary apply_patch copy normalized line endings, so that one snapshot was replaced with a byte-preserving copy before this manifest was written. No runtime source was modified by the auditor.

| Frozen file | Original source | SHA-256 |
| --- | --- | --- |
| migration_decisions.txt | common/decisions/migration_decisions.txt | 5000DD59578763690E391A22C8F09E7BCC0FC16E8AA063CE068B2D6104BAA0D7 |
| migration_decision_category.txt | common/decisions/categories/migration_decision_category.txt | 43E1EE749E97EF952E9B6CBDD66339346970AC4F308E30CA17E9DA6D4A6BF5FB |
| humanitarian_corridor_triggers.txt | common/scripted_triggers/humanitarian_corridor_triggers.txt | 624546039563AE3A75F83C0EEFB3B858ECF3E1C3B20215053F6BF0A51684C27C |
| humanitarian_corridor_effects.txt | common/scripted_effects/humanitarian_corridor_effects.txt | 7FC7A1C0CFB850830D6EA87CDBD45765AE58A1193B7C86263DC8D3D85EAB8568 |
| migration_destination_selection_effects.txt | common/scripted_effects/migration_destination_selection_effects.txt | F20084BF1FE1B12A885710B0A3E081E251F3AEFD3505ACA4C65925421CAEB9FF |
| migration_destination_selection_triggers.txt | common/scripted_triggers/migration_destination_selection_triggers.txt | 3C4AAC5707EC80279477005E22980723CC5846ABA200228395A16C117B06141D |
| migration_decision_owner_effects.txt | common/scripted_effects/migration_decision_owner_effects.txt | 33F1EF4D02143858E6E5C8E1006CC4E99858F756BB0D0454A9FB4CAABD1F618B |
| migration_decision_owner_triggers.txt | common/scripted_triggers/migration_decision_owner_triggers.txt | 5CCADBD726127EC7C9083035F2B09B68AEF0BED5BE2461DC08C12849808C0823 |
| migration_spontaneous_movement_effects.txt | common/scripted_effects/migration_spontaneous_movement_effects.txt | 154A0E413A16A4A57E5872B86EE81FCE5DF5D169EFCF9FDA3CFACD7FFA648A4B |
| migration_spontaneous_movement_triggers.txt | common/scripted_triggers/migration_spontaneous_movement_triggers.txt | 203AB382550841974D83950F2FD841F0299EB75F28C1B811BB4DBC3B6F156CE5 |
| migration_capacity_effects.txt | common/scripted_effects/migration_capacity_effects.txt | 62CE76598B5EE2FCD7517613370C52A8899B23347DF289872C44B31DB1AE607B |
| migration_core_triggers.txt | common/scripted_triggers/migration_core_triggers.txt | 00031F2DBCC7549E0D1FD2EBD40613809EB97332D9CD4B8EC68F8266BC7864FE |
| migration_decision_phase_effects.txt | common/scripted_effects/migration_decision_phase_effects.txt | 1EC09B2A4062AA4338CCF7149B26398382DC99E51BED44B24CF04498E440F2D7 |
| migration_core_effects.txt | common/scripted_effects/migration_core_effects.txt | 7B82BB7ADE8FE9BBE4A988AC4A66B42DC8A7591136F481840757EA94DE2C15CA |
| migration_adapter_effects.txt | common/scripted_effects/migration_adapter_effects.txt | D85735FA71656E37CFE79695D8EF998CEA175F45AFD65DC9CFC41A912D9F8398 |
| famine_adapter_effects.txt | common/scripted_effects/famine_adapter_effects.txt | 9ACC155670EB518D902F5EB750DB5F40E103DF105B68A3D4AFF8960D25828108 |
| famine_core_effects.txt | common/scripted_effects/famine_core_effects.txt | D598B18998B93D9AB1632CBA01B7530B93FD059A907A9D45E48438057233EDBF |
| famine_core_triggers.txt | common/scripted_triggers/famine_core_triggers.txt | 3BE7168A1E1E2CB54E76A1AE6969870113AF5E53FF7DEDC0F2CE0F011EDB44A9 |
| civilian_transfer_effects.txt | common/scripted_effects/civilian_transfer_effects.txt | 77790F99524EDCF110B6B72C22ABE71BA65779B45BB783D5C05386747CD4CFCC |
| civilian_transfer_triggers.txt | common/scripted_triggers/civilian_transfer_triggers.txt | 7A863F33E8377E2F10517E44E80F5813F46BF13ECB3E244FEFB9A343A54EE0B1 |
| migration_forced_movement_effects.txt | common/scripted_effects/migration_forced_movement_effects.txt | 557343903913886DCD0F2A764420DA4F5D1257672C9E8E784A56F983A41E8C49 |
| migration_forced_movement_triggers.txt | common/scripted_triggers/migration_forced_movement_triggers.txt | BD8FF863019FF77502980D0026E53BB1B0A6732C5538501F052314D37EFF465D |
| humanitarian_achievement_effects.txt | common/scripted_effects/humanitarian_achievement_effects.txt | E60304FF30176D1F0AFE36B0AD758EE45BF7BB017AA8E3E096154533B0E179E3 |
| migration_decision_constants.txt | common/script_constants/migration_decision_constants.txt | 48C0CBC35AD6E98E2FAC0A4CB5A499DFA71CB06F5B7ADB484A1D05B47E33F9CE |
| migration_destination_selection_constants.txt | common/script_constants/migration_destination_selection_constants.txt | 2C80A0632B6E14F8B6B855ABE74EE90D5C81EE314C108D49C33C9EEF2623B38E |
| migration_core_constants.txt | common/script_constants/migration_core_constants.txt | 47145391C8A5AA82E333091DD2F7EB424A7B00DAB34C916BFAB2FFABBC66DB9B |
| humanitarian_corridor_constants.txt | common/script_constants/humanitarian_corridor_constants.txt | 12B774D71734564E8D423BFE68B401E37ADFD73C801B1B3FA9EFAAE0E25C0AAB |
| civilian_transfer_constants.txt | common/script_constants/civilian_transfer_constants.txt | 60D551C863AB720FD7F6AC288C5170FFEB569D2AC7024D6344B0D119DB148F33 |
| migration_spontaneous_movement_constants.txt | common/script_constants/migration_spontaneous_movement_constants.txt | C55E19D3E4D4AE91AE616E6DD5B49E83C85437E948EDA0641B135FA321F08DA2 |

All 29 frozen copy hashes were checked against their corresponding source files at capture time. The two decision sources and both decision-category/reception/corridor sources are preserved alongside their exact transfer, tuning, and destination dependencies so subsequent edits can use real before paths rather than current-vs-current comparisons.

The parent additionally authorized a five-read saved-receiver achievement scope correction before automatic corridor terminal cleanup.
`humanitarian_achievement_effects.txt` is the 29th before source: it was byte-copied from `common/scripted_effects/humanitarian_achievement_effects.txt` before editing and both source and copy verified SHA-256 `E60304FF30176D1F0AFE36B0AD758EE45BF7BB017AA8E3E096154533B0E179E3`.
