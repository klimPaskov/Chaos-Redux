# IW-043 / IW-058 portrait prompts

Each of the eight source masters was generated independently with ImageGen as a fictional, all-male institutional group portrait. The prompt template requested a canonical HOI4 country-leader portrait master: a distinct group of several male delegates or officeholders, period-appropriate 1936 civilian or service clothing, subdued painterly photographic finish, quiet readable background, clear identity at 156x210, and no text, flags, maps, UI, real-person likeness, medieval court costume, or generic clergy montage. The institution-specific briefs were:

- `CHU_independence_wave_middle_volga_congress`: Middle Volga civic congress with Russian, Chuvash, Mari, and Tatar delegates.
- `CHU_independence_wave_federal_presidium`: federal presidium in an austere civic chamber, equal male members.
- `CHU_independence_wave_bolgar_civic_presidium`: Bolgar civic presidium in a restrained stone civic setting; no medieval court costume.
- `CHU_independence_wave_river_security_directorate`: river-security directorate with civilian and restrained service roles.
- `ASY_independence_wave_provisional_national_council`: Assyrian provisional council with distinct male civic representatives.
- `ASY_independence_wave_concordat_council`: church-civic concordat council with distinct male institutional roles, not a generic clergy montage.
- `ASY_independence_wave_levies_guardianship`: temporary security guardianship board with male Levies-era service presence and civilian oversight.
- `ASY_independence_wave_civic_national_assembly`: civic national assembly of distinct male representatives, no unattributed sacred symbol.

The retained source masters are not real-person portraits and do not imitate a named individual. They were finished with `advisor_icon_processing.py leader` in collective mode using an explicit full-source crop and the canonical `portraits/leaders` reference family.
