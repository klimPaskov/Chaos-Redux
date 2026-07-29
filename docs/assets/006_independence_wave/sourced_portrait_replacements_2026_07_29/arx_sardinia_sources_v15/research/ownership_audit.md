# ARX Event 006 portrait ownership audit v15

Date: 2026-07-29.

Search roots: current Chaos Redux `common/characters`, `history/countries`, `interface`, and `localisation`; installed vanilla HOI4 equivalents; and approved workshop references `1521695605`, `2265420196`, and `1458561226`.

## Results

| Identity | Current Chaos Redux | Vanilla | Workshop references |
|---|---|---|---|
| Emilio Lussu | Exact current owner is `ARX_emilio_lussu` in `common/characters/006_independence_wave_mediterranean_characters.txt:92-94`, with `GFX_portrait_ARX_independence_wave_emilio_lussu` in `interface/006_independence_wave_mediterranean_portraits.gfx:20-21` and localisation `ARX_emilio_lussu`. | No exact Emilio Lussu character, portrait, GFX, recruitment, or localisation owner found. | Kaiserreich `1521695605` owns `SRI_emilio_lussu` in `common/characters/SRI characters.txt:181-203`, recruits it in `history/countries/SRI - Socialist Republic of Italy.txt:256`, and registers large/small portraits in `interface/kaiserreich/portraits/SRI_portraits.gfx:67-72`; this is a cross-mod disclosure collision, not a reason to clone the face into another subject. No exact owner found in `2265420196` or `1458561226`. |
| Luigi Arborio Mella di Sant'Elia | No exact character, portrait, GFX, recruitment, or localisation owner found. | No exact owner found; vanilla `Vázquez de Mella` focus text is unrelated. | No exact owner found. Kaiserreich `Julio Mella McPartland` is an unrelated Cuban subject and was excluded. |
| Giuseppe Valle | No exact current owner found. | No exact owner found. | Kaiserreich `1521695605` owns `SRD_giuseppe_valle` in `common/characters/SRD characters.txt:129-148`, recruits it in `history/countries/SRD - Sardinia.txt:173`, localises it in `localisation/english/KR_country_specific/SRD - Sardinia l_english.yml:598-599`, and registers large/small portrait sprites in `interface/kaiserreich/portraits/SRD_portraits.gfx:27-32`; direct transfer is blocked. No exact owner found in `2265420196` or `1458561226`. |
| Vittorio Vernè | No exact current owner found; only the preserved source package is present. | No exact character, portrait, GFX, recruitment, or localisation owner found. | No exact owner found in any approved reference. |
| Giuseppe Pizzorno | No exact current owner found. | No exact owner found. | No exact owner found in any approved reference. |

Search variants included accented and unaccented forms (`Vernè`/`Verne`, `Sant'Elia`/`Sant_Elia`, `Arborio Mella`, `Mella di Sant'Elia`, `Giuseppe Valle`, `giuseppe_valle`, `Giuseppe Pizzorno`, and script-id forms).

The only owner collisions that affect this package are the existing ARX Lussu consumer (allowed because it is the target being replaced) and Kaiserreich's `SRI_emilio_lussu` and `SRD_giuseppe_valle` consumers (disclosure only for Lussu, hard transfer blocker for Valle).

