# Event 020 GUI acceptance evidence

Status: partial acceptance; no Event 020 source file was changed.

This folder contains the selected accepted reference record, exact MCP request and response records, the recovered Git GUI source baseline, and the checksum-verified production pixels reviewed during the task.

The accepted reference PNG and SVG remain at docs/plans/020_black_plague_plans/subagent_handoffs/references/020_black_plague_gui_visibility_capacity_intended.png and docs/plans/020_black_plague_plans/subagent_handoffs/references/020_black_plague_gui_visibility_capacity_intended.svg.

Reviewed production images are active_zero_1920_full.png, active_zero_1920_crop.png, active_zero_2560_full.png, active_zero_2560_crop.png, active_organized_1920_full.png, active_organized_1920_crop.png, exhausted_1920_full.png, exhausted_1920_crop_from_full.png, exhausted_2560_full.png, and completed_maximum_1920_full.png.

The active-zero and active-organized crops are derived from checksum-verified production full pixels at 536×298, matching the render gallery crop dimensions; the exhausted 1920 crop is also derived from its checksum-verified full production PNG.

The active-zero and active-organized production SVGs were assembled from verified MCP byte ranges and rasterized with the installed sharp package; their local PNG hashes are recorded separately from the source SVG hashes.
The exhausted and maximum-progress full PNGs were recovered directly in byte ranges and verified against their MCP artifact byte counts and SHA-256 values before pixel review.

The active-zero 1920 and 2560 local full PNG hashes are CDFCE3BE62BBD190FA992D42DFA6101FDB0774B0D3A767B019D180E6F4AE85A1 and 4708C27196ED8A63F860316B0E364771B828D64EB786C13B58BEE56E5730D4EA.
The active-organized 1920 local full PNG hash is DDE9DB6AC6720577233969010C3C95FE304F16E8AB5697ADD66CCDB8B830B9A6; its source SVG artifact SHA-256 is e3f285a5ad8b331b78660a9050bd1d22e181d59c3cafa1311ac3741fcf97bee7.
The exhausted 1920 and 2560 full PNG hashes are 5fcf426764a11331e0ecac7f70ba795ed98b2e9d5e7a1595fd8dbffe5a1d50e7 and 336ba1e7b70a98771c2cac10a2e674fc6cfa2c5e81c229739c2410e586f2e293.
The completed maximum-progress 1920 full PNG hash is 20543f4ea1b0565ec62d274a837512cb66d7c85fe73eb28174d85f1e8e5fa698.

The accepted board is 520×282 and uses one category picture outside the attached GUI, an empty meter at 0%, a neutral unorganized capacity label for 0/0, and an exhaustion warning only for positive total capacity with zero remaining.

The active-zero state rendered and visually passed at both requested resolutions; the active-organized state rendered and visually passed at 1920×1080; exhausted capacity rendered and visually passed at both sizes; the extra 100% preview verified all five fill segments at 1920×1080.

The pre-outbreak and recovered-hidden category gates remain unresolved because the live GUI scenario schema rejects the required global active-state array and the GUI condition evaluator does not resolve the source any_state_in trigger; fixtures declared two direct facts used inside black_plague_country_is_human_host but did not inject the category helper result or force element visibility.

The active-organized 2560×1440 view remains unverified after two bounded render attempts; its request files and exact outcome are recorded in the handoff.

The exact accepted reference mapping, source identities, artifact URIs, scenario matrix, route errors, visual findings, and omissions are recorded in docs/plans/020_black_plague_plans/subagent_handoffs/2026-10-07_event020_gui_acceptance.md.

The incomplete one-shot exhausted full-image base64 payload was discarded after the full image was recovered correctly with byte ranges; all temporary transfer files were removed after verifying the retained PNGs.
