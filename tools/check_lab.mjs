// Syntax-check the module scripts of a lab page: node tools/check_lab.mjs web/labs/<slug>.html
import { readFileSync, writeFileSync, mkdtempSync } from "node:fs";
import { execFileSync } from "node:child_process";
import { tmpdir } from "node:os";
import { join } from "node:path";

const file = process.argv[2];
if (!file) { console.error("usage: node tools/check_lab.mjs <page.html>"); process.exit(2); }
const html = readFileSync(file, "utf8");
const scripts = [...html.matchAll(/<script type="module">([\s\S]*?)<\/script>/g)].map((m) => m[1]);
if (!scripts.length) { console.error(`${file}: no module script found`); process.exit(1); }
if (!html.includes('href="../kit/lab.css"') || !html.includes("createLab(")) {
  console.error(`${file}: must load ../kit/lab.css and call createLab()`); process.exit(1);
}
const dir = mkdtempSync(join(tmpdir(), "foundry-check-"));
let failed = false;
scripts.forEach((src, i) => {
  const path = join(dir, `script${i}.mjs`);
  writeFileSync(path, src);
  try { execFileSync(process.execPath, ["--check", path], { stdio: "pipe" }); }
  catch (e) { failed = true; console.error(`${file}: module script ${i + 1}:\n${e.stderr.toString()}`); }
});
console.log(failed ? "FAILED" : `OK: ${file}`);
process.exit(failed ? 1 : 0);
