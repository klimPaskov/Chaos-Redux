import fs from "node:fs/promises";
import { FileBlob, SpreadsheetFile } from "@oai/artifact-tool";

const modRoot = "C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux";
const stageRoot = modRoot + "/docs/plans/033_acid_rain_plans/catalog_current_2026_10_07";
const visualRoot = stageRoot + "/visual_evidence";
const tempRoot = "C:/Users/klimp/AppData/Local/Temp/chaos_redux_catalog_current_2026_10_07";
const liveWorkbook = modRoot + "/docs/spreadsheets/chaos_redux_events_catalog.xlsx";
const currentOriginal = tempRoot + "/current_original.xlsx";
const headOriginal = tempRoot + "/recorded_head_original.xlsx";
const headVariant = tempRoot + "/head_variant/chaos_redux_events_catalog.xlsx";
const values = {
  Events: {
    C34: "A lethal acid-rain system moves between regions, exposing the inhabited states in its path to corrosion, poisoned runoff, infrastructure damage, and direct civilian loss. Countries can build shelters, protect water and food, expand emergency medicine, harden transport, evacuate states ahead of storm forecasts, and repair the aftermath. The rain ordinarily disperses only after it has crossed every state in its path.",
    D34: "Severe Storm Cells: Concentrated cells form inside the moving front, giving threatened states nine days to prepare for heavier corrosion and lethal exposure.",
    E34: "Multiple Weather Fronts: The atmospheric mass divides into independent fronts with separate routes, warnings, intensity, and severe cells.",
    F34: "Global Acid Rain: The fronts merge into a worldwide layer that exposes every inhabited state in its path and produces regional superstorms with nine-day forecasts.",
    M34: "Needs Testing",
  },
  Clusters: {
    C6: "Natural and environmental catastrophes strike states or regions, with repeated disaster slots allowing the cluster to scale into larger cascades.",
  },
};

async function openWorkbook(filePath) {
  return await SpreadsheetFile.importXlsx(await FileBlob.load(filePath));
}

function displayInspect(response) {
  return response && typeof response.ndjson === "string"
    ? response.ndjson
    : JSON.stringify(response);
}

async function capture(workbook, label, renderPrefix) {
  const queries = [
    ["summary", { kind: "workbook,sheet,table", maxChars: 4500, tableMaxRows: 4, tableMaxCols: 6, tableMaxCellChars: 100 }],
    ["events_region", { kind: "region", sheetId: "Events", range: "A32:M36", maxChars: 3500 }],
    ["clusters_region", { kind: "region", sheetId: "Clusters", range: "A4:H8", maxChars: 2500 }],
    ["events_styles", { kind: "computedStyle", sheetId: "Events", range: "A34:M34", maxChars: 2500 }],
    ["clusters_styles", { kind: "computedStyle", sheetId: "Clusters", range: "A6:H6", maxChars: 1800 }],
    ["events_formulas", { kind: "formula", sheetId: "Events", range: "A34:M34", maxChars: 1200, options: { maxResults: 30 } }],
    ["clusters_formulas", { kind: "formula", sheetId: "Clusters", range: "A6:H6", maxChars: 1000, options: { maxResults: 20 } }],
  ];
  for (const [name, query] of queries) {
    const result = await workbook.inspect(query);
    console.log("INSPECT " + label + " " + name + "\n" + displayInspect(result));
  }
  for (const [sheetName, range, suffix] of [
    ["Events", "A32:M36", "events"],
    ["Clusters", "A4:H8", "clusters"],
  ]) {
    const preview = await workbook.render({ sheetName, range, scale: 1, format: "png" });
    const previewBytes = new Uint8Array(await preview.arrayBuffer());
    const imagePath = visualRoot + "/" + renderPrefix + "_" + suffix + ".png";
    await fs.writeFile(imagePath, previewBytes);
    console.log("RENDER " + label + " " + sheetName + " " + imagePath + " bytes=" + previewBytes.byteLength);
  }
}

async function applyValues(workbook) {
  const events = workbook.worksheets.getItem("Events");
  events.getRange("C34").values = [[values.Events.C34]];
  events.getRange("D34:F34").values = [[values.Events.D34, values.Events.E34, values.Events.F34]];
  events.getRange("M34").values = [[values.Events.M34]];
  workbook.worksheets.getItem("Clusters").getRange("C6").values = [[values.Clusters.C6]];
  workbook.recalculate();
}

const mode = process.argv[2] || "before";
await fs.mkdir(visualRoot, { recursive: true });

if (mode === "before") {
  const workbook = await openWorkbook(liveWorkbook);
  await capture(workbook, "current_before", "before_current");
} else if (mode === "author") {
  const current = await openWorkbook(currentOriginal);
  const head = await openWorkbook(headOriginal);
  await applyValues(current);
  await applyValues(head);
  await capture(current, "current_artifact_authored", "draft_current");
  await capture(head, "head_artifact_authored", "draft_head");
  const draftDir = tempRoot + "/artifact_drafts";
  await fs.mkdir(draftDir, { recursive: true });
  const currentOut = await SpreadsheetFile.exportXlsx(current);
  await currentOut.save(draftDir + "/current_artifact_draft.xlsx");
  const headOut = await SpreadsheetFile.exportXlsx(head);
  await headOut.save(draftDir + "/head_artifact_draft.xlsx");
  console.log("ARTIFACT_DRAFTS " + JSON.stringify([
    draftDir + "/current_artifact_draft.xlsx",
    draftDir + "/head_artifact_draft.xlsx",
  ]));
} else if (mode === "verify") {
  const current = await openWorkbook(liveWorkbook);
  const head = await openWorkbook(headVariant);
  await capture(current, "current_after", "after_current");
  await capture(head, "head_after", "after_head");
} else {
  throw new Error("Unknown mode: " + mode);
}
