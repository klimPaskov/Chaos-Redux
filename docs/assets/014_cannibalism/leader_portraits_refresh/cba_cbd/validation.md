# Event 014 CBA-CBD Warlord Portrait Validation

Validation date: 2026-07-15; reduction amendment: 2026-07-16.

## 2026-07-16 reduction audit

- 21 attachment-listed CBA-CBD DDS files were removed from `gfx/leaders/014_cannibalism/`.
- 7 unique CBA-CBD DDS files remain live: CBA Middle East/South America, CBB Middle East, CBC base/South America, and CBD North America/South America.
- The 32 CBA-CBD sprite names remain registered; retired names alias the retained texture documented in `gfx_handoff.md`.
- The 28-row source/processed/hash ledger below is retained as a historical pre-reduction record, not as a claim that those DDS files remain installed.

## Historical pre-reduction package checks

- Historical exact selected asset count: 28 source PNGs, 28 processed PNGs, 28 metadata JSON records, 28 per-portrait review sheets, and 28 pre-reduction DDS files.
- Historical uniqueness: 28 unique source SHA-256 hashes, 28 unique processed-PNG SHA-256 hashes, and 28 unique pre-reduction DDS SHA-256 hashes.
- Processed dimensions: 156x210 for all 28.
- DDS decoded dimensions and mode: 156x210 RGBA for all 28.
- DDS byte length: 131,168 bytes for all 28.
- Processor metadata: version 2.0, fictional source mode, explicit source-sized crop, canonical vanilla leader reference directory, and 156x210 output for all 28.
- Review-sheet dimensions: 1344x464 for all 28.
- Final visual review: all 28 disturbing actions survive the 156x210 crop; every scalp reads bald; faces, clothes, props, environments, and silhouettes remain distinct; matte oil/gouache handling, simplified planes, muted period values, and quiet painted backgrounds keep the set in classic vanilla-HOI4 style; no photographic-modern or prison imagery appears.

Source SHA-256 values and their built-in generated-output filenames are recorded in prompts/warlord_prompts.md.

## Historical pre-reduction processed and DDS hashes

| Asset | Processed PNG SHA-256 | DDS SHA-256 |
| --- | --- | --- |
| leader_CBA_warlord | 78b9350fec3f935cd96a167be0d3c786a746786548fda081b75be6898ad376b0 | b3174db630503a06ffceb2588b8b505de291cf775718fb119829803b6e73cfac |
| leader_CBA_warlord_africa | d6070c9b57757b54713558d0ba23f20fd3f8f8e737f509778aa959dd20925471 | 27f728faf5b8ab7a35df2ee3d23f8ea9728996c67bd8c5623f359cc4cd5dfe2b |
| leader_CBA_warlord_asia | 9bde2324493bafb698a7c6f0244c2679b2350b61d07f6d55c3466524b0c3af63 | 251ba6dbd1fc9cdc1955a2a300f744ef6d7df87c176967638ae0c47eaa70f417 |
| leader_CBA_warlord_middle_east | 32c01b6118f1a68751a505a3f123d2d94b929829b19813659139ee3fdf29a127 | 7a3f2da952de19a2ec484969123913373172a7a529f7ef3bfc4b407147cecc1f |
| leader_CBA_warlord_north_america | aa63c0158450caace42914eff5c1fcfa3399e837d5aa93d297a3296b5db9ff9e | 03ccbafef0ffc5b4f707acb131977d8769456352176dba77b5ccd1b6c2055bfe |
| leader_CBA_warlord_oceania | d50be1a92fae955ea576b7706becad17e15acbd701a5a8141323adef4a12e423 | 5b98e3c633b4949bedb09396d53e5d8984a14bbd27c19edf5a8183397aac2c5c |
| leader_CBA_warlord_south_america | 75f7a4cec593d4259b0fcce58f666de74541bf8b516f8ddcc11bbb4eb8934906 | 36b48c100e0d4bb9efa001bfa360ffd2147c6492886d5c0e14894946e66fa27b |
| leader_CBB_warlord | 1fe0a1fe54d510ee4bd7622d3bf9a58443012108efdba0a568b6fede9f2fd7c1 | ead9fbadc481826e51c3c8176f18c14a2f5377ea82dec4ffd1480b570e596202 |
| leader_CBB_warlord_africa | 0be693140afa603500062e09d5a63d3570edea8f55ce5dbae1fa855aa6ca83b3 | da05f34379aea60d72265acb8fddc4c341cc4b79a0d11425d7a48972e42a0d62 |
| leader_CBB_warlord_asia | fe589bd9d72384c83595555bc2bc3d1f28da60cf739c20691b51dbb98e35d34e | c7767b503274648c635fe995e7f2b24ed4a8eecb58481667dd29098f158d2bc7 |
| leader_CBB_warlord_middle_east | 6520342a1bf97ba1134f56fee4bf3e14b3162b5c3610ae7bf55208a5fd23278c | 6855d90880155748a825ed4876cba83c692c5d638a836fe70546bb1954d36d05 |
| leader_CBB_warlord_north_america | bb6681b859ab154cafe8050034f9bd1adcbf6a49930f4c1fbfec22a0e19d6acb | ec798e5f6abce7f7174d4563ab3563b8129f5ccdcc55cbfa25b4db01d55982d6 |
| leader_CBB_warlord_oceania | c8a83fa662341732bbe869f63c2e0a29d261b91084f6748c870b5b72bcac4c9b | 8ddf4e4d9b00862176fb6dbd9a70f7d85687e09ebe9adf4c23d1ce11fb7b95a7 |
| leader_CBB_warlord_south_america | abe284ca69f09057c28a3fb2c8ddf881e956ee3a5c7f20ba9421b357fed2d89b | d80f73302e81c98df4da9b61a4d1a1fdf73298749193d7cdd2a5348651d27803 |
| leader_CBC_warlord | ff9d9ae5d154b3a5dd37c30bd73adbc8c1f73b59463767b35de58eda96639d5a | b151550391a301d6436458bce5eb2362adfd06e2874976c001e0e7aa6bc9c026 |
| leader_CBC_warlord_africa | ea7b39ee1d304ef4aeb352889ba0f9c05d221f3a8e41a58eec95707362cbaf68 | 800813271f7afd940359977dee374e8bb9cbc9012a9ad4ea8872c3ee018fdf00 |
| leader_CBC_warlord_asia | 2d9360615396578e96c20ce659a2971d315613d7312ef1c4284fbb34946b4cc8 | be1b11992822e5bc88d4a2d9be47360daa103bcdccf822d541041f4bd4518fea |
| leader_CBC_warlord_middle_east | 1f867c29f3303729d616ce726eb788fee015bc9c85a284831065c9690949ca78 | ad4db2a83e3d23e29d323e78cbea8954278747474a00cc124bf724dc9d9d9d4a |
| leader_CBC_warlord_north_america | cfc81882439c99176dd96d3d66bbc3c15369fe8dedd50da7d789fca607d5ca5f | ccf29a61c66c9ca0213e80e2f796b4305e0fea59854e69ef9befc0db54f139cb |
| leader_CBC_warlord_oceania | c5e30dcfd73e83984a45336bdf142b6d2aba52ff328912d578bdd45333e1bd3a | 40cb12cca4389eeaf14427b8f4e401e61cb822de41a9428750f518022fa4b8d5 |
| leader_CBC_warlord_south_america | aa4d2a370e45b87e34707b1487130e13e003a366737d5e1b5c78e0723aad6414 | cad343f0cf528e3d7276094a93bf396bffee5a826d6a5e6a6886b42141b07b7e |
| leader_CBD_warlord | b41ee1e7516ecaba5f54aebdd531cd87132f922c23c3a10a3441640135fc26ba | 3e7cda046d6c76fa10949a3954a4e703018f5448366bdb7e5a21286f48444d06 |
| leader_CBD_warlord_africa | f8989df90ab0e27e76e3e09ffe3e3ef1904c5dd14494e4d342c45b8e5ffc0d30 | 8db25662864a103d5b28af873f032ae61b170d654281e9fceed5ecc804ff27d3 |
| leader_CBD_warlord_asia | 4ab9bb3fce0196fe0b1627a8b449fdd969dbb55d5c19c2838ba2c4f04815fbc3 | 28d539f088abf846188f9ce9cfc39d3ecf68c316ab3941263f1bc5fa9014429f |
| leader_CBD_warlord_middle_east | cb4e9849f66820e8514f0833bbad24ee1be02ec83488db2ba3fbf28f9ab9dfc3 | b16462eb4a66e36bce05f82b79dfb131c563573ef88261e318d32d0bf7ea6d05 |
| leader_CBD_warlord_north_america | 2795b70042879d303f3800de5b524c8120fbaed0a155ef421bff337f6d818d03 | 21f19b026da7eb765eb5e0128d0aff66de20476cdbe8f881c24f3df25bce729b |
| leader_CBD_warlord_oceania | cba2baee4af291b99e07a1da8d20e5ef4b1b367c7d8019df8f6ffe9c2c051ac4 | 993deeab0bb55acc37809b7ddb4f01d028001fe91359c635f82602b571624bb1 |
| leader_CBD_warlord_south_america | 9a50284b54a529132048e69c9d2eef81b568aac6e542ae5fda9c7d7015d4c1c7 | d7f72fd48a426f1c4fd0f9c6a8e4f653f508ae01a55d98175f05d8a3d15f505c |

## Scope boundary

The historical portrait refresh did not edit gameplay, localisation, script, spreadsheet, flag, or unrelated texture files. The current sprite registrations target 7 live CBA-CBD DDS paths plus the documented retained-texture aliases.

The independent read-only style audit compared the historical native-size repaint sheets and individual review sheets against the three canonical vanilla references and passed all 28 pre-reduction portraits without a borderline finding. It also verified that `hannibal.dds` and `hannibal_wendigo.dds` remain byte-identical to `HEAD`.
