import crypto from "node:crypto";
import fs from "node:fs";
import path from "node:path";

const [packageRoot, repoRoot] = process.argv.slice(2);
if (!packageRoot || !repoRoot) {
    throw new Error("Usage: patch_meshy_mcp.mjs <package-root> <repo-root>");
}

const tasksPath = path.join(packageRoot, "dist", "tools", "tasks.js");
const schemaPath = path.join(packageRoot, "dist", "schemas", "tasks.js");
const clientPath = path.join(packageRoot, "dist", "services", "meshy-client.js");

function replaceExactly(source, pattern, replacement, label) {
    const matches = source.match(pattern);
    if (!matches || matches.length !== 1) {
        throw new Error(`${label} compatibility anchor count was ${matches?.length ?? 0}, expected 1.`);
    }
    return source.replace(pattern, replacement);
}

let client = fs.readFileSync(clientPath, "utf8");
if (!/export async function getTaskWithAutoInference\s*\(/.test(client)) {
    if (/async function getTaskWithAutoInference\s*\(/.test(client)) {
        client = replaceExactly(
            client,
            /async function getTaskWithAutoInference\s*\(/g,
            "export async function getTaskWithAutoInference(",
            "Meshy task inference export"
        );
    } else {
        const anchor = "/**\n * Create and validate Meshy client\n */";
        if (!client.includes(anchor) || !/export async function fetchTaskByIdFromKnownEndpoints\s*\(/.test(client)) {
            throw new Error("Meshy client no longer exposes the known-endpoint inference anchor.");
        }
        const implementation = `/**
 * Fetch a task, trying the requested endpoint first and then every known task endpoint.
 */
export async function getTaskWithAutoInference(client, taskId, preferredEndpoint) {
    try {
        const task = await client.get(\`${"${preferredEndpoint}"}/${"${taskId}"}\`);
        if (task && task.id) {
            return { task, endpoint: preferredEndpoint };
        }
    }
    catch {
        // Fall through to endpoint inference.
    }
    const result = await fetchTaskByIdFromKnownEndpoints(client, taskId);
    if (result) {
        return result;
    }
    throw new Error(\`Task ${"${taskId}"} not found on any endpoint. Verify the task_id is correct.\`);
}
`;
        client = client.replace(anchor, `${implementation}\n${anchor}`);
    }
    fs.writeFileSync(clientPath, client, "utf8");
}

let schema = fs.readFileSync(schemaPath, "utf8");
if (!schema.includes("compatibility artifact selector")) {
    schema = replaceExactly(
        schema,
        /(\s+format: z\.enum\(\["glb", "fbx", "usdz", "stl", "obj", "blend", "3mf"\]\)[\s\S]*?Do NOT download all formats\.[\s\S]*?\),\n)(\s+include_textures:)/g,
        `$1    // Chaos Redux compatibility artifact selector.\n    artifact: z.enum(["primary", "processed_24fps", "armature", "walking", "walking_armature", "running", "running_armature"])\n        .default("primary")\n        .describe("Official-return artifact to persist. Rigging supports primary/walking/walking_armature/running/running_armature; animation supports primary/processed_24fps/armature."),\n$2`,
        "Meshy download schema"
    );
    fs.writeFileSync(schemaPath, schema, "utf8");
}

let tasks = fs.readFileSync(tasksPath, "utf8");
if (!tasks.includes("CHAOS_REDUX_SECURE_DOWNLOAD_V1")) {
    tasks = replaceExactly(tasks, /import \* as fs from "fs";\n/g, 'import * as fs from "fs";\nimport crypto from "node:crypto";\n', "Meshy crypto import");

    tasks = replaceExactly(
        tasks,
        /async function downloadFileToLocal\(url, saveTo\) \{[\s\S]*?\n\}\nfunction sleep\(ms\) \{/g,
        `// CHAOS_REDUX_SECURE_DOWNLOAD_V1
function containedSavePath(saveTo) {
    if (!path.isAbsolute(saveTo)) {
        throw new Error("save_to must be an absolute path inside the repository.");
    }
    const root = fs.realpathSync(process.cwd());
    const target = path.resolve(saveTo);
    const relative = path.relative(root, target);
    if (relative === "" || relative.startsWith(".." + path.sep) || relative === ".." || path.isAbsolute(relative)) {
        throw new Error("save_to must resolve to a file inside the repository.");
    }
    let existing = path.dirname(target);
    while (!fs.existsSync(existing)) {
        const parent = path.dirname(existing);
        if (parent === existing) {
            throw new Error("save_to has no existing repository ancestor.");
        }
        existing = parent;
    }
    const existingReal = fs.realpathSync(existing);
    const ancestorRelative = path.relative(root, existingReal);
    if (ancestorRelative.startsWith(".." + path.sep) || ancestorRelative === ".." || path.isAbsolute(ancestorRelative)) {
        throw new Error("save_to traverses outside the repository through a link or junction.");
    }
    return target;
}
function fileSha256(filePath) {
    return crypto.createHash("sha256").update(fs.readFileSync(filePath)).digest("hex");
}
function sanitizedDownloadError(error) {
    const message = error instanceof Error ? error.message : String(error);
    return message
        .replace(/https?:\\/\\/[^\\s)\\]}]+/gi, "[signed_url_redacted]")
        .replace(/([?&](?:signature|sig|token|credential|key|expires)=[^&\\s]*)/gi, "[signed_parameter_redacted]");
}
async function downloadFileToLocal(url, saveTo) {
    const target = containedSavePath(saveTo);
    const dir = path.dirname(target);
    fs.mkdirSync(dir, { recursive: true });
    const partial = \`${"${target}"}.partial-${"${process.pid}"}-${"${Date.now()}"}\`;
    try {
        const response = await axios.get(url, { responseType: "stream", timeout: 120000 });
        const writer = fs.createWriteStream(partial, { flags: "wx" });
        response.data.pipe(writer);
        await new Promise((resolve, reject) => {
            response.data.on("error", reject);
            writer.on("finish", resolve);
            writer.on("error", reject);
        });
        const size = fs.statSync(partial).size;
        if (size <= 0) {
            throw new Error("Downloaded artifact was empty.");
        }
        if (fs.existsSync(target)) {
            fs.unlinkSync(target);
        }
        fs.renameSync(partial, target);
        const finalReal = fs.realpathSync(target);
        const finalRelative = path.relative(fs.realpathSync(process.cwd()), finalReal);
        if (finalRelative.startsWith(".." + path.sep) || finalRelative === ".." || path.isAbsolute(finalRelative)) {
            throw new Error("Downloaded artifact resolved outside the repository.");
        }
        return size;
    }
    catch (error) {
        if (fs.existsSync(partial)) {
            fs.unlinkSync(partial);
        }
        throw new Error(sanitizedDownloadError(error));
    }
}
function sleep(ms) {`,
        "Meshy secure downloader"
    );

    tasks = tasks.replace(/\s+image_urls: imageUrls,\n/g, "\n");
    tasks = tasks.replace(/\s+model_urls: task\.model_urls,\n/g, "\n");
    tasks = tasks.replace(
        "  - include_textures (boolean): Include texture files (default: true)\n",
        "  - artifact (enum): Official-return artifact to persist (default: primary). Animation supports processed_24fps and armature; rigging supports walking/running variants.\n  - include_textures (boolean): Include texture files (default: true)\n"
    );
    tasks = tasks.replace(
        '  { "local_path": "/path/to/file.obj", "file_size_bytes": 12345678, "project_dir": "...", "print_fixed": true }',
        '  { "task_id": "abc-123", "local_path": "/path/to/file.obj", "file_size_bytes": 12345678, "sha256": "...", "project_dir": "..." }'
    );
    tasks = tasks.replace(
        "  - If download fails, falls back to returning URLs`",
        "  - Download failures are fail-closed and never expose signed source URLs`"
    );

    tasks = replaceExactly(
        tasks,
        /            \/\/ Rigging tasks: result\.rigged_character_\{format\}_url[\s\S]*?            \/\/ Standard tasks \(text-to-3d, image-to-3d, remesh, retexture\): top-level model_urls/g,
        `            // Rigging and animation tasks return artifacts below result rather than model_urls.
            if ((params.task_type === TaskType.RIGGING || params.task_type === TaskType.ANIMATION) && task.result) {
                const artifact = params.artifact || "primary";
                let downloadUrl;
                if (params.task_type === TaskType.RIGGING) {
                    const rigArtifacts = {
                        primary: task.result[\`rigged_character_${"${fmt}"}_url\`],
                        walking: task.result.basic_animations?.[\`walking_${"${fmt}"}_url\`],
                        walking_armature: fmt === "glb" ? task.result.basic_animations?.walking_armature_glb_url : undefined,
                        running: task.result.basic_animations?.[\`running_${"${fmt}"}_url\`],
                        running_armature: fmt === "glb" ? task.result.basic_animations?.running_armature_glb_url : undefined
                    };
                    downloadUrl = rigArtifacts[artifact];
                }
                else {
                    const animationArtifacts = {
                        primary: fmt === "fbx" ? task.result.animation_fbx_url : fmt === "usdz" ? task.result.processed_usdz_url : task.result.animation_glb_url,
                        processed_24fps: fmt === "fbx" ? task.result.processed_animation_fps_fbx_url : undefined,
                        armature: fmt === "fbx" ? task.result.processed_armature_fbx_url : undefined
                    };
                    downloadUrl = animationArtifacts[artifact];
                }
                if (!downloadUrl) {
                    return {
                        isError: true,
                        content: [{ type: "text", text: \`Error: Artifact ${"${artifact}"} in ${"${fmt}"} is not available for task ${"${params.task_id}"}.\` }]
                    };
                }
                const stage = inferStage(params.task_type, task.type);
                const projectDir = params.save_to ? undefined : resolveProjectDir(params.task_id, params.task_type, task.prompt, params.parent_task_id, task.created_at);
                const savePath = params.save_to || getFilePath(projectDir, artifact === "primary" ? stage : \`${"${stage}"}_${"${artifact}"}\`, fmt);
                try {
                    const fileSize = await downloadFileToLocal(downloadUrl, savePath);
                    const output = {
                        task_id: params.task_id,
                        task_type: params.task_type,
                        artifact,
                        format: fmt,
                        local_path: savePath,
                        project_dir: projectDir,
                        file_size_bytes: fileSize,
                        sha256: fileSha256(savePath)
                    };
                    const textContent = \`# Artifact Downloaded

**Task ID**: ${"${params.task_id}"}
**Task Type**: ${"${params.task_type}"}
**Artifact**: ${"${artifact}"}
**Format**: ${"${fmt.toUpperCase()}"}
**Local File**: ${"${savePath}"}
**SHA-256**: ${"${output.sha256}"}\`;
                    return { content: [{ type: "text", text: textContent }], structuredContent: output };
                }
                catch (downloadError) {
                    return {
                        isError: true,
                        content: [{ type: "text", text: \`Error: MCP artifact persistence failed: ${"${sanitizedDownloadError(downloadError)}"}\` }]
                    };
                }
            }
            // Standard tasks (text-to-3d, image-to-3d, remesh, retexture): top-level model_urls`,
        "Meshy rig and animation download handlers"
    );

    tasks = tasks.replace("                    download_url: downloadUrl,\n", "                    task_id: params.task_id,\n");
    tasks = replaceExactly(
        tasks,
        /                    project_dir: projectDir,\n                    file_size_bytes: fileSize,\n                    format: fmt,/g,
        "                    project_dir: projectDir,\n                    file_size_bytes: fileSize,\n                    sha256: fileSha256(savePath),\n                    format: fmt,",
        "Meshy standard download checksum"
    );
    tasks = tasks.replace(/\s+expires_at: new Date\(Date\.now\(\) \+ 24 \* 60 \* 60 \* 1000\)\.toISOString\(\)\n/g, "\n");
    tasks = tasks.replace("                textContent += `\\n\\n**Note**: Source URL expires after 24 hours. The local file is permanent.`;\n", "                textContent += `\\n**SHA-256**: ${output.sha256}`;\n");
    tasks = replaceExactly(
        tasks,
        /            catch \(downloadError\) \{\n                \/\/ Download failed — fall back to returning URLs[\s\S]*?\n            \}\n        \}\n        catch \(error\) \{/g,
        `            catch (downloadError) {
                return {
                    isError: true,
                    content: [{ type: "text", text: \`Error: MCP artifact persistence failed: ${"${sanitizedDownloadError(downloadError)}"}\` }]
                };
            }
        }
        catch (error) {`,
        "Meshy standard download failure handler"
    );
    fs.writeFileSync(tasksPath, tasks, "utf8");
}

client = fs.readFileSync(clientPath, "utf8");
schema = fs.readFileSync(schemaPath, "utf8");
tasks = fs.readFileSync(tasksPath, "utf8");
if (!/import \{ getTaskWithAutoInference \} from "\.\.\/services\/meshy-client\.js";/.test(tasks) ||
    !/export async function getTaskWithAutoInference\s*\(/.test(client)) {
    throw new Error("Meshy task polling import/export contract is incomplete.");
}
if (!tasks.includes("CHAOS_REDUX_SECURE_DOWNLOAD_V1") || !schema.includes("compatibility artifact selector")) {
    throw new Error("Meshy secure artifact persistence compatibility patch is incomplete.");
}
if (/Download URLs[^\n]*\n[\s\S]{0,200}https?:\/\//.test(tasks)) {
    throw new Error("Meshy download response still contains an embedded signed URL inventory.");
}

for (const filePath of [tasksPath, schemaPath, clientPath]) {
    if (fs.statSync(filePath).size > 5 * 1024 * 1024) {
        throw new Error(`Patched Meshy file exceeds the 5 MiB safety limit: ${filePath}`);
    }
}

const hashes = Object.fromEntries([tasksPath, schemaPath, clientPath].map(filePath => [
    path.relative(packageRoot, filePath).replaceAll(path.sep, "/"),
    crypto.createHash("sha256").update(fs.readFileSync(filePath)).digest("hex")
]));
process.stdout.write(JSON.stringify(hashes));
