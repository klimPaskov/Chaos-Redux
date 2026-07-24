# Stage 7 Biological Countermeasure Alpha and DDS Verification

Every processed PNG was checked as RGBA at its exact runtime size.

Every processed PNG has alpha minimum `0`, alpha maximum `255`, and four transparent corners.

Every DDS was checked as a 128-byte-header, one-level, uncompressed BGRA DDS with `DDS_HEADER` size `124`, pixel-format size `32`, pixel-format flags `65`, fourCC `0`, bit count `32`, masks `0x00ff0000`, `0x0000ff00`, `0x000000ff`, and `0xff000000`, and `DDSCAPS_TEXTURE` `0x00001000`.

Every DDS has exact file length `128 + width * height * 4` and pixel-for-pixel BGRA-to-RGBA round-trip equality with its processed PNG.

| Asset | PNG size | DDS size | DDS length | Alpha | Corners | Round-trip | Source SHA-256 | PNG SHA-256 | DDS SHA-256 |
|---|---:|---:|---:|---|---|---|---|---|---|
| `decision_bio_activate_surveillance_network` | 32x32 | 32x32 | 4224 | 0-255 | 0,0,0,0 | true | `513863885faecf3307b429b37da9b29d21627b3b3212b8a10560783b65ee2e62` | `f845652344dcfceb72dda2c419b8e59139d05396fdba783ecf8d6def1372ffde` | `6059c6db47b512ffea42d27d8eba2cce5cce006b92ad5ef1e9d120641699e26c` |
| `decision_bio_quarantine_state` | 32x32 | 32x32 | 4224 | 0-255 | 0,0,0,0 | true | `a8d19c2bb49d4261e2117f71d033caf84e55426d884d182e972e402d9756a125` | `0db7393085b4fc9f4adce35c576585aa3bd763aa506e6eb4268eb664b5f9a68f` | `48e6d43a985bddc67ae63c94e1f5fc8896687095598c9f27d47de98211279237` |
| `decision_bio_border_control` | 32x32 | 32x32 | 4224 | 0-255 | 0,0,0,0 | true | `c399c00d38ccdb35a04982918be35614356bfaa6c429885ab6ff978d7b5d472a` | `9513ebe1264f064a2b14611d372fc18c18dd126d5b50d94333fa2f4bfdf0ccf5` | `35017a8ddc9fd795309f8eb0daa9514b270b42b871a22ae12239cdc1c8fa1e5f` |
| `decision_bio_anthrax_antibiotics` | 32x32 | 32x32 | 4224 | 0-255 | 0,0,0,0 | true | `715843fa0fec503cbb0253c1e3dcc363488e2841c06ab06b02b87feeb25bf9f8` | `fbe200ba4601096483c5dea7448d3124fc4c947d388017da04955c704d675952` | `e4026af02c63946cf149f9f90cd0e3a89cb0665dd549f778abf5ee713f16cc67` |
| `decision_bio_plague_antibiotics` | 32x32 | 32x32 | 4224 | 0-255 | 0,0,0,0 | true | `42c234e5fe4ce75130257c8485aeac9e8f3a615e2dd841c63de8b0b357bd7be9` | `c38f1ddc7d013438dd0c1b1e75dcd0335a4694b11679eefe0f2b628cd3f94bf7` | `08353ef4bf6ccae33f26e1e38b3d93b39275659bcceb61aa4291156ab43e5037` |
| `decision_bio_tularemia_antibiotics` | 32x32 | 32x32 | 4224 | 0-255 | 0,0,0,0 | true | `714bed3d64939ad7566dab3525478bd3fdf4c8c61380d64959b63d13d6be3d25` | `9df4f1f92c4a5834854eb542c1815555149189101776705f06b5154682912c02` | `03519688aa44e2516290b45aa77cc2e38ceabae730473c8955ed06e2ff9d5417` |
| `decision_bio_international_medical_mission` | 32x32 | 32x32 | 4224 | 0-255 | 0,0,0,0 | true | `0a6203f8d4aa3cdc0d5c748ef9dec6e0f18e7ba252caa2cd5add9e84e58aa839` | `9c0a8d1cf671f3407bb1571ac007f881bc2c308321a33e9fd3acd1ee0bf8962a` | `4b6248484bb251f6212c9e1806e2b46fb9e7fc2bdee9953c721b352213167b45` |
| `decision_bio_sustain_containment` | 32x32 | 32x32 | 4224 | 0-255 | 0,0,0,0 | true | `ea9cfa6b4ea8cc7c523eae70b415f86c294269e601d5549667bef2aafeb3ad6e` | `e8d635e07ffb5975fcfd4111546769db6e74592a0071ff26f7870196edb2cdb4` | `3d03124e9c653c4e55a394560c317a4539eb2cff812c4a10312ec672cfdd9c3e` |
| `decision_bio_expand_medical_capacity` | 32x32 | 32x32 | 4224 | 0-255 | 0,0,0,0 | true | `b9524d061be29224362d79db9022aac850b2bce3584510bb08a0e41678f45606` | `bde7793001e72ff64ced903963c824ed08e7ccdb75d0631de125e042d4cc9b90` | `1a10e89e0be110834d7d73ce89cfc732d75b6e064c54f6cf5a650076dc2a326e` |
| `decision_bio_expand_biosecurity_capacity` | 32x32 | 32x32 | 4224 | 0-255 | 0,0,0,0 | true | `e19f997fa498b9391268d0295d3e09acf864c05d19ee7ba6c185fb2b332b1002` | `4f211a4df83f208d3b0dfc135890837f6a0d62216506b8b3daa4c3e921ee477d` | `5d94bdc612f412447d67e03968d3177f814b5e624e254515527f2bd357e700a1` |
| `idea_bio_surveillance_network` | 64x64 | 64x64 | 16512 | 0-255 | 0,0,0,0 | true | `0e73ee46f5ed5fdc858e9d0f17ebb8b1e5a8631cf2849e31aff67dc7ad545c96` | `895e2eee212f19446d4e87bd6f3ca26aecdcb68a143b1eb62842b380b53434c9` | `30f8481003313a9a8208158a0624de6cec340b3da0aee724d2092c01d02d0af5` |
| `idea_smallpox_vaccination` | 64x64 | 64x64 | 16512 | 0-255 | 0,0,0,0 | true | `eb01d77bee40d6a1aff90324ffd2e584407e5a691ed801fe58d997d17e9deddd` | `98d816b3304d72df2aacb2198b58bc1c043757558102dd44e7ab947cdfa5a0e2` | `a5e6d5911df286d483b45fe6602bfca002de7c922d6dcd41b0c4070370c78d7c` |
