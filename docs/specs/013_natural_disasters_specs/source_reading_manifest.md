# Source Reading Manifest

I processed the uploaded project source bundle before writing this package. The bundle included project skills, subagent TOML files, mechanics documentation, and the CSV exports for the current event, cluster, and scenario catalogs.

## Files processed

| File | Bytes | SHA-256 |
| --- | ---: | --- |
| `AGENTS.md` | 33825 | `07c0a22711699c6ebb7add72613f8594bc49d45ed64942fbded1b7e419dd1f71` |
| `CHAOS_REDUX_MECHANICS.md` | 44359 | `fb4ed4ab5894c5c93c319c4a144f2f6f95c7593f22286de449681e94675d4715` |
| `chaos-redux-event-assets.md` | 54245 | `059ba78e37912742e22a050b9dcd6927d394a3c1860b242649e69cefb52f93e0` |
| `chaos-redux-event-planning.md` | 131350 | `fa145bb0d3c9a97f8b50610533785163c3e1181734f4047f36140b44e7cb48de` |
| `chaos-redux-events.md` | 53008 | `3544341fa09d7a8053e66d498261e77843c711566f992ea1c91b6eef6beb5da5` |
| `chaos-redux-frame-animation.md` | 23669 | `6a4e68dc4e5a89f0b7b8fc8984c0b9cb64665046eaefd728bd41056375cb0d98` |
| `chaos-redux-improvement-loop.md` | 24080 | `7e137b6135c335e4e92c61768b8231ab433028e8a17d264531d94c3d7c17d4bd` |
| `chaos-redux-subagents.md` | 19124 | `1d155c650f16f6c4bd0934f8b9e93a063ce79a65b895f45c0aaa860cc713c50e` |
| `chaos-redux-super-events.md` | 30134 | `1fabb5d93da377039606f148b5d6a829643f39568b75bdff8353172d9f33eaaa` |
| `chaos_redux_clusters_catalog.csv` | 1721 | `6d21ad63a942c17e0a2a5fa0f836ffa2045b91596c8f6afa8b103bb8bd9fc60e` |
| `chaos_redux_events_catalog.csv` | 56282 | `8c669b51f762ec299555bcb79da022221861dea12d80c46fc1770475144a6cfd` |
| `chaos_redux_scenarios_catalog.csv` | 3660 | `e972443ca43849b3a877ceb2bc4f7171a309c03eaa79cb0df0c630732f496a6a` |
| `chaosx_asset_source_researcher.toml` | 3847 | `421793129a5a846cd00cce9ad21c4d9a53a30c4ee1909044cb13b7c63b105065` |
| `chaosx_country_package_auditor.toml` | 6614 | `78b510c8425f08835ec14d4f4376ef3106aee28285ab7a93d211285e0d9d6bec` |
| `chaosx_decision_mission_auditor.toml` | 4608 | `48fa04a9100b85f1cfea3f0f27dfa8ffb48de461bfca48eb0afc132cbf123126` |
| `chaosx_documentation_curator.toml` | 8395 | `86145139edca0e585b6da1237c887feb50d5f8f6ff7f242772407d9945e7819a` |
| `chaosx_event_completion_auditor.toml` | 2956 | `57668b3c570692689320de4e242fa667d47db3ebdb078af0f7f57bf7802483ba` |
| `chaosx_focus_tree_auditor.toml` | 3646 | `36afd9e6d67b98be82049ba1c45b129eb0d961f1696fdf2d4fd6db4286b3a4f6` |
| `chaosx_generated_event_art.toml` | 5856 | `61bdcfac345f3bb7b2408d481c91c763cdcac7c75fb40109b2dff99a843c50b2` |
| `chaosx_icon_artist.toml` | 7170 | `b75b6f1e18e8469c1cc0fccd6d3d38c8b52ac6c2efd64b0998d43249dcafd375` |
| `chaosx_improvement_loop_planner.toml` | 6345 | `f438da1473185ad804e875c3825422c8ed2770099b4ad492f1d4f60452629738` |
| `chaosx_localisation_auditor.toml` | 4163 | `79ffbeddb6683c8361bcce4d7167f94d5b05f59cd9a1a7474003644c42560d61` |
| `chaosx_repo_explorer.toml` | 11817 | `9bde006e5add9c9f3287a2b15d83a1bce460c3e7ce296b8c7c0d4084581cfd86` |
| `chaosx_scripted_system_architect.toml` | 4565 | `62406e456ed972e9c8d58f9670318a0548d70419e955fbed14cb80bb29ba2085` |
| `chaosx_skill_maintainer.toml` | 3236 | `13d693a536b5225c7cf3547ddd665a34b0cd525ffc6a186cb26b5e8525167e30` |
| `chaosx_spreadsheet_doc_worker.toml` | 3947 | `712d05bf76de9b49c2adec1092db90d45ca7e9f9d31429418e5cd7bf1fbd08af` |
| `chaosx_super_event_audio_researcher.toml` | 3314 | `ea374f776aabaa3e0448f59bfc2442c24a5a57d443f8910691013c6d879d77f2` |
| `chaosx_super_event_text_researcher.toml` | 3902 | `5d466a4d0e7a217c311e08c0f5555ae9dba2604549b4cb878ee47e3995425665` |
| `hoi4-decisions-missions.md` | 40087 | `369db0c2785ec2f0d681fef904df50d82fb82f21da08dd9e94847fcc113bfff0` |
| `hoi4-focus-trees.md` | 38682 | `6b8dfb504b3eec14b1e6b0bc93c66af4aa5ce7a682f145540e66afc2ac61e37d` |

## Catalog facts used

Event 013 row read from `chaos_redux_events_catalog.csv`:

```json
{
  "ID": "13",
  "Event Name": "Natural Disasters",
  "Details": "Reserved",
  "Evo I": "",
  "Evo II": "",
  "Evo III": "",
  "Evo IV": "Meteor shower and more intense natural disasters.",
  "Evo V": "",
  "World-End Scenario": "",
  "Type": "Minor Repeatable",
  "Cluster ID": "",
  "Member Severity": "",
  "Status": "To Be Reworked"
}
```

Related row 46:

```json
{
  "ID": "46",
  "Event Name": "Earth Earthquake",
  "Details": "All buildings in the world gain slight damage.",
  "Evo I": "",
  "Evo II": "",
  "Evo III": "",
  "Evo IV": "",
  "Evo V": "",
  "World-End Scenario": "",
  "Type": "Minor Repeatable",
  "Cluster ID": "",
  "Member Severity": "",
  "Status": "To Be Reworked"
}
```

Related row 51:

```json
{
  "ID": "51",
  "Event Name": "Heat Wave",
  "Details": "Hot everywhere. Add idea heat wave to every country.",
  "Evo I": "",
  "Evo II": "",
  "Evo III": "",
  "Evo IV": "",
  "Evo V": "",
  "World-End Scenario": "",
  "Type": "Minor Fire-Once",
  "Cluster ID": "",
  "Member Severity": "",
  "Status": "To Be Reworked"
}
```

Related row 99:

```json
{
  "ID": "99",
  "Event Name": "Sandstorm",
  "Details": "Everything will be covered with sand fog for states affected, similar to acid rain. Will make it difficult for divisions in combat and division intel.",
  "Evo I": "",
  "Evo II": "",
  "Evo III": "",
  "Evo IV": "",
  "Evo V": "",
  "World-End Scenario": "",
  "Type": "Minor Fire-Once",
  "Cluster ID": "",
  "Member Severity": "",
  "Status": "To Be Reworked"
}
```

Natural Disaster cluster rows found in `chaos_redux_clusters_catalog.csv`:

```json
[
  {
    "Cluster ID": "",
    "Cluster Name": "Natural Disasters",
    "Details": "A random selection of natural disasters will happen",
    "Members (ID)": "",
    "Type": "Minor Fire-Once",
    "Chaos level": "2",
    "Status": "New"
  },
  {
    "Cluster ID": "",
    "Cluster Name": "Natural Disasters 2",
    "Details": "A random selection of natural disasters will happen (more global)",
    "Members (ID)": "",
    "Type": "Minor Fire-Once",
    "Chaos level": "3",
    "Status": "New"
  }
]
```

Disaster Barrage scenario row found in `chaos_redux_scenarios_catalog.csv`:

```json
[
  {
    "Scenario ID": "SCN-007",
    "Scenario Name": "Disaster Barrage",
    "Details": "The Disaster Barrage scenario launches Event 013 directly from the selected country. It bypasses ordinary chaos and evolution prerequisites for the manual scenario only, then uses the same Natural Disasters sequence controller, warning logic, dynamic population-loss math, family categories, recovery missions, aftermath cleanup, and throttled family news as a live Event 13 firing.",
    "Type Options": "Random Barrage draws from the full eligible pool.\nGeological Crisis favors earthquake, rupture, landslide, volcanic, tsunami, and meteor families.\nWeather Crisis favors flood, cyclone, severe storm, corridor storm, wildfire, drought, heat, winter, and dust families.\nSkyfall Crisis pushes meteor and skyfall families.\nFull Catalogue keeps the broad pool open.",
    "Intensity Scaling": "Intensity controls sequence size, delay compression, and abnormal access.\nLow intensity starts a varied local season.\nMedium starts regional disaster systems.\nHigh opens severe chained behavior and abnormal access.\nMaximum can combine meteor showers, rupture waves, massive eruption pressure, delayed tsunami, and storm corridor movement in one season.\nDisaster Barrage never creates an Event 13 world-end branch.",
    "Status": "Needs Testing"
  }
]
```

## Limitation note

The environment exposed the subagent instruction files, not a separate tool for actually spawning independent project subagents. I incorporated their role rules into the package and wrote a subagent routing plan for implementation, asset production, audits, and spreadsheet alignment.
