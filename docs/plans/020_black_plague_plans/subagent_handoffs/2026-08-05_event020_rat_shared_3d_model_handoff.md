# Event 020 shared rat 3D model handoff

## Result

The one approved native ImageGen reference was submitted once to a legacy Meshy provider task `019fd39c-3f8e-7f96-bd04-214ccbb7d64f` in response group `d60d46ca-ef2d-43f4-ab50-84b883e9e946`. The provider consumed 30 credits. The GLB and FBX outputs, request/response evidence, hashes, Blender checkpoints, previews, DDS packs, exports, and reimport proof are retained under `docs/assets/020_black_plague/models_3d/rat_ground_unit_shared/`. Meshy 7 is required for future generation.

## Production evidence

- Adapter route: `chaosx_blender_hoi4` `1.2.0`, Blender `5.1.2`, io_pdx_mesh `0.91.0`.
- Working geometry: 29,999 triangles, 15,012 vertices, zero degenerate faces, zero non-manifold edges, 101 loose boundary edges recorded as a QA risk.
- Rig: `black_plague_rat_armature`, 17 semantic bones, one full influence per working vertex, no zero-weight working vertices.
- Actions: `black_plague_rat_idle`, `black_plague_rat_move`, `black_plague_rat_attack`, `black_plague_rat_retreat`, `black_plague_rat_death`, all at 24 FPS.
- Material: PdxMeshAdvanced, 1024px diffuse/specular/normal DDS, packed specular and PDX normal channels recorded in `blender/reports/pdx_generation_specular_pack.json` and `blender/reports/pdx_normal_pack.json`.
- Reimport: `validation/reimport_black_plague_rat_attack.json` imports the exported mesh, attack animation, and all three runtime DDS files.

## Runtime consumers

The parent installed `gfx/models/units/020_black_plague_rat/`, registered `black_plague_rat_mesh` and `black_plague_rat_entity`, applies entity scale `1.35` exactly once, maps all five states, and sets `override_model = black_plague_rat_entity` on all five locked rat templates. The same entity covers the six rat subtypes and only `RTA`/`RTX`; no Rat King or subtype model exists.

Runtime mesh SHA-256 is `52C4C6B5E4EB41D6726DDD5EA7271E8FD486C1136B5F4CF7E496E3FED639EBA4`. The five animation hashes are recorded by filename in the production handoff; the three active texture maps are 1024x1024 DDS. The large counter SHA-256 is `2D1DAC7276B58964D1D4656F1474B326C6DAA65BAB0194A4546F8225F5AB8E71`, and the map counter SHA-256 is `FD14144EF07115B26BAE3434BAB03817228B586383D506BA154F5FD0152329E3`.

## Remaining risks and handoffs

The sound companion remains `needs_user_review` for the four CC BY 4.0 vocal candidates and has no accepted impact/contact source. The bespoke vanilla-green counter package is installed at the parent-owned large/map counter paths and registered through the shared rat sprite aliases; it remains review-gated for visual/live consumer validation. Parent-owned sound definitions and live in-game validation remain open. The model package itself is production-complete and ready for those consumers.
