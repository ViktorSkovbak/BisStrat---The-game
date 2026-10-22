// The Foundry lab kit. A lab page imports createLab() and hands it a plain config:
// goal, story, parameters, a fast model, an optional chart and scene, decision tests and takeaways.
// The kit builds the page, runs the tests (call first, then the reveal) and drives the scene.
// Contract for lab authors: see web/kit/README.md.

import * as THREE from "three";
import { EffectComposer } from "three/addons/postprocessing/EffectComposer.js";
import { RenderPass } from "three/addons/postprocessing/RenderPass.js";
import { UnrealBloomPass } from "three/addons/postprocessing/UnrealBloomPass.js";
import { OutputPass } from "three/addons/postprocessing/OutputPass.js";
import { RoomEnvironment } from "three/addons/environments/RoomEnvironment.js";

export { THREE };

export const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));

/** Compact number: 18.2, 3.5, 0.62, 140, 12,400. Infinity reads as "∞". */
export function fmt(x, digits) {
  if (x === Infinity) return "∞";
  if (x === -Infinity) return "−∞";
  if (!Number.isFinite(x)) return "–";
  if (digits !== undefined) return x.toFixed(digits);
  const a = Math.abs(x);
  if (a >= 10000) return Math.round(x).toLocaleString("en-US");
  if (a >= 100) return x.toFixed(0);
  if (a >= 10) return x.toFixed(1);
  return x.toFixed(2);
}

const SIZES = [
  { id: "small", label: "Small (under 1.5×)", lo: 0, hi: 1.5 },
  { id: "double", label: "About 2× (1.5-3×)", lo: 1.5, hi: 3 },
  { id: "big", label: "Big (3× or more)", lo: 3, hi: Infinity },
];

function el(tag, cls, html) {
  const e = document.createElement(tag);
  if (cls) e.className = cls;
  if (html !== undefined) e.innerHTML = html;
  return e;
}

function store(key, value) {
  try {
    if (value === undefined) return JSON.parse(localStorage.getItem(key) || "null");
    localStorage.setItem(key, JSON.stringify(value));
  } catch { return null; }
  return null;
}

export function createLab(cfg) {
  const defaults = Object.fromEntries(cfg.params.map((p) => [p.key, p.value]));
  const metricByKey = Object.fromEntries(cfg.metrics.map((m) => [m.key, m]));
  const wrap = el("div", "wrap");
  document.body.append(wrap);

  // --- Header, goal and story ---
  wrap.append(el("div", "top", `<h1><small>Lab ${esc(cfg.id)} · ${esc(cfg.area)}</small>${esc(cfg.title)}</h1>
    <a class="back" href="../" id="back">← Back to the machine</a>`));
  wrap.querySelector("#back").addEventListener("click", (e) => { if (history.length > 1) { e.preventDefault(); history.back(); } });
  wrap.append(el("div", "intro", `<div class="goal"><span class="label">Your goal</span>${cfg.goal}</div>
    <div class="story"><span class="label">The setting</span>${cfg.story}</div>`));
  wrap.append(el("p", "how", `<b>How this works:</b> each test gives you a real decision. Make your call and guess how big the effect is, then lock it. Only then does the floor show what happens. Your calls are the practice; the reveal is the lesson.`));

  // --- Scene, caption, metrics ---
  const sceneBox = el("section", "", "");
  sceneBox.setAttribute("aria-label", "Simulation");
  const sceneHost = el("div", "scene", `<div class="hud"></div><div class="showing"></div>`);
  if (cfg.scene) sceneBox.append(sceneHost);
  const caption = el("p", "caption", "");
  sceneBox.append(caption);
  wrap.append(sceneBox);
  const metricsBox = el("section", "metrics", "");
  metricsBox.setAttribute("aria-label", "Key numbers");
  wrap.append(metricsBox);

  // --- Tests and chart ---
  const cols = el("div", "cols", "");
  const testsPanel = el("section", "panel", `<h2>Tests</h2><div class="tabs" role="tablist"></div><div class="test-body"></div>
    <div class="summary"><span class="score"></span><button type="button" class="copy">Copy my results</button></div>`);
  const chartPanel = el("section", "panel", `<h2>${esc(cfg.chart?.title || "The curve")}</h2><div class="chart-wrap"></div><div class="legend"></div>${cfg.chart?.note ? `<p class="how" style="margin-top:8px">${cfg.chart.note}</p>` : ""}`);
  cols.append(testsPanel);
  if (cfg.chart) cols.append(chartPanel);
  wrap.append(cols);

  // --- Free play ---
  const explore = el("details", "panel explore", `<summary>Free play</summary>
    <p class="note">Every lever, unlocked. Use it after your test calls: it shows the answers.</p><div class="params"></div>`);
  wrap.append(explore);
  const paramsBox = explore.querySelector(".params");

  if (cfg.takeaways?.length) {
    wrap.append(el("section", "panel takeaways", `<h2>Keep these</h2><ol>${cfg.takeaways.map((t) => `<li>${t}</li>`).join("")}</ol>`));
  }

  // --- State ---
  let current = { ...defaults };
  let result = null;
  const controls = {};

  for (const p of cfg.params) {
    const box = el("div", "ctl");
    if (p.options) {
      box.innerHTML = `<span class="lab"><span>${esc(p.label)}</span></span><div class="seg" role="group" aria-label="${esc(p.label)}"></div>${p.hint ? `<span class="hint">${esc(p.hint)}</span>` : ""}`;
      const seg = box.querySelector(".seg");
      for (const o of p.options) {
        const b = el("button", "", esc(o.label));
        b.type = "button";
        b.addEventListener("click", () => show({ ...current, [p.key]: o.value }, "Free play"));
        b.dataset.value = String(o.value);
        seg.append(b);
      }
      controls[p.key] = () => seg.querySelectorAll("button").forEach((b) => b.setAttribute("aria-pressed", String(b.dataset.value === String(current[p.key]))));
    } else {
      const id = `p-${p.key}`;
      box.innerHTML = `<label for="${id}"><span>${esc(p.label)}</span><output></output></label>
        <input type="range" id="${id}" min="${p.min}" max="${p.max}" step="${p.step}" value="${p.value}">${p.hint ? `<span class="hint">${esc(p.hint)}</span>` : ""}`;
      const input = box.querySelector("input"), out = box.querySelector("output");
      input.addEventListener("input", () => show({ ...current, [p.key]: Number(input.value) }, "Free play"));
      controls[p.key] = () => { input.value = current[p.key]; out.textContent = p.format ? p.format(current[p.key]) : fmt(current[p.key]); };
    }
    paramsBox.append(box);
  }

  // --- Scene runtime ---
  let sceneApi = null;
  let kit = null;
  if (cfg.scene) {
    kit = makeStage(sceneHost, cfg.stage || {});
    try { sceneApi = cfg.scene(kit); } catch (e) { console.error(e); }
  }

  function renderMetrics() {
    metricsBox.innerHTML = cfg.metrics.map((m) => {
      const v = result.values[m.key];
      return `<div class="metric"><div class="k">${esc(m.label)}</div><div class="v">${m.format ? m.format(v, result.values) : fmt(v)}${m.unit ? `<small>${esc(m.unit)}</small>` : ""}</div></div>`;
    }).join("");
  }

  function show(params, label) {
    current = { ...current, ...params };
    result = cfg.model(current);
    caption.textContent = result.caption || "";
    renderMetrics();
    Object.values(controls).forEach((f) => f());
    sceneHost.querySelector(".showing").textContent = label ? `Showing: ${label}` : "";
    if (sceneApi?.update) sceneApi.update(current, result);
    drawChart();
  }

  // --- Chart ---
  function drawChart() {
    if (!cfg.chart) return;
    const c = cfg.chart;
    const series = c.series(current, result);
    const W = 600, H = 320, L = 56, R = 14, T = 12, B = 42;
    const xs = series.flatMap((s) => s.points.map((p) => p[0]));
    const ys = series.flatMap((s) => s.points.map((p) => p[1])).filter(Number.isFinite);
    const xMin = c.xMin ?? Math.min(...xs), xMax = c.xMax ?? Math.max(...xs);
    const marker = c.marker ? c.marker(current, result) : null;
    const yMaxRaw = c.yMax ?? Math.max(1e-9, ...ys, ...(marker && Number.isFinite(marker[1]) ? [marker[1]] : []));
    const yMin = c.yMin ?? 0;
    const ticks = niceTicks(yMin, yMaxRaw);
    const yMax = ticks[ticks.length - 1];
    const x = (v) => L + ((v - xMin) / (xMax - xMin || 1)) * (W - L - R);
    const y = (v) => H - B - ((Math.min(Math.max(v, yMin), yMax) - yMin) / (yMax - yMin || 1)) * (H - T - B);
    const tick = (v) => Number(v.toPrecision(6)).toLocaleString("en-US");
    const xf = c.xFormat || tick, yf = c.yFormat || tick;
    let s = "";
    for (const t of ticks) s += `<line x1="${L}" y1="${y(t)}" x2="${W - R}" y2="${y(t)}" stroke="var(--line)"/><text x="${L - 8}" y="${y(t) + 4}" text-anchor="end">${yf(t)}</text>`;
    for (const t of niceTicks(xMin, xMax, 6)) if (t >= xMin && t <= xMax) s += `<line x1="${x(t)}" y1="${T}" x2="${x(t)}" y2="${H - B}" stroke="var(--line)"/><text x="${x(t)}" y="${H - B + 16}" text-anchor="middle">${xf(t)}</text>`;
    s += `<text x="${(L + W - R) / 2}" y="${H - 4}" text-anchor="middle">${esc(c.xLabel)}</text>`;
    s += `<text transform="translate(14 ${(T + H - B) / 2}) rotate(-90)" text-anchor="middle">${esc(c.yLabel)}</text>`;
    const colors = { brass: "var(--brass)", glow: "var(--glow)", cool: "var(--cool)", ok: "var(--ok)", jam: "var(--jam)", dim: "var(--ink-dim)" };
    for (const se of series) {
      const col = colors[se.color] || colors.brass;
      const pts = se.points.filter((p) => Number.isFinite(p[1]));
      if (se.dots) pts.forEach((p) => (s += `<circle cx="${x(p[0])}" cy="${y(p[1])}" r="4.5" fill="${col}"/>`));
      else if (pts.length) s += `<path d="${pts.map((p, i) => `${i ? "L" : "M"}${x(p[0]).toFixed(1)},${y(p[1]).toFixed(1)}`).join("")}" fill="none" stroke="${col}" stroke-width="${se.width || 2.5}"${se.dashed ? ' stroke-dasharray="5 5"' : ""}/>`;
    }
    if (marker && Number.isFinite(marker[0])) {
      s += `<line x1="${x(marker[0])}" y1="${T}" x2="${x(marker[0])}" y2="${H - B}" stroke="var(--cool)" stroke-dasharray="4 4"/>`;
      if (Number.isFinite(marker[1])) s += `<circle cx="${x(marker[0])}" cy="${y(marker[1])}" r="7" fill="none" stroke="var(--cool)" stroke-width="2"/>`;
    }
    chartPanel.querySelector(".chart-wrap").innerHTML = `<svg viewBox="0 0 ${W} ${H}" width="100%" role="img" aria-label="${esc(c.yLabel)} against ${esc(c.xLabel)}">${s}</svg>`;
    chartPanel.querySelector(".legend").innerHTML = series.filter((se) => se.name).map((se) =>
      `<span><i style="background:${colors[se.color] || colors.brass}${se.dots ? ";height:8px;width:8px;border-radius:50%" : ""}"></i>${esc(se.name)}</span>`).join("") +
      (marker ? `<span><i style="background:var(--cool)"></i>what the floor shows now</span>` : "");
  }

  // --- Tests ---
  const tabs = testsPanel.querySelector(".tabs"), body = testsPanel.querySelector(".test-body");
  const saved = store(`foundry-${cfg.id}-calls`) || {};
  const calls = cfg.tests.map((_, i) => saved[i] || { pick: null, size: null, locked: false });
  let active = 0;

  function evaluate(test) {
    const base = { ...defaults, ...test.baseline };
    const baseVal = cfg.model(base).values[test.rankBy];
    const rows = test.options.map((o) => {
      const p = { ...base, ...o.params };
      const r = cfg.model(p);
      const v = r.values[test.rankBy];
      const ratio = test.better === "higher" ? v / baseVal : baseVal / v;
      return { ...o, p, r, v, ratio };
    });
    const bestId = test.best ? test.best(rows, baseVal) :
      rows.reduce((a, b) => ((test.better === "higher" ? b.v > a.v : b.v < a.v) ? b : a)).id;
    return { base, baseVal, rows, bestId };
  }

  function sizeOf(ratio) { return SIZES.find((s) => ratio >= s.lo && ratio < s.hi)?.id || "small"; }

  function renderTabs() {
    tabs.innerHTML = cfg.tests.map((t, i) => {
      const c = calls[i];
      let mark = "";
      if (c.locked) mark = c.pick === evaluate(t).bestId ? `<span class="mark right">✓</span>` : `<span class="mark wrong">✗</span>`;
      return `<button type="button" class="tab" role="tab" aria-selected="${i === active}" data-i="${i}">Test ${i + 1}${mark}</button>`;
    }).join("");
    tabs.querySelectorAll(".tab").forEach((b) => b.addEventListener("click", () => { active = Number(b.dataset.i); renderTest(); }));
  }

  function renderTest() {
    renderTabs();
    const t = cfg.tests[active], c = calls[active];
    const ev = evaluate(t);
    const m = metricByKey[t.rankBy];
    const mf = (v) => (m?.format ? m.format(v, {}) : fmt(v)) + (m?.unit ? ` ${m.unit}` : "");
    show(ev.base, "today");
    body.innerHTML = `<div class="test">
      <h3>${esc(t.title)}</h3>
      <div class="situation">${t.situation}</div>
      <div class="today">Today: <b>${esc(m?.label || t.rankBy)} ${esc(mf(ev.baseVal))}</b></div>
      <div class="q">${esc(t.question || "Your call: which option helps most?")}</div>
      <div class="choices">${t.options.map((o) => `<button type="button" class="choice" data-id="${esc(o.id)}" aria-pressed="${c.pick === o.id}"><span class="id">${esc(o.id)}</span><span>${esc(o.label)}${o.detail ? `<small>${esc(o.detail)}</small>` : ""}</span></button>`).join("")}</div>
      ${t.size === false ? "" : `<div class="q">How big is the effect of your pick, compared with today?</div>
      <div class="sizes">${SIZES.map((s) => `<button type="button" class="size" data-id="${s.id}" aria-pressed="${c.size === s.id}">${s.label}</button>`).join("")}</div>`}
      <button type="button" class="lock">Lock my call</button>
      <div class="reveal"></div></div>`;
    const lock = body.querySelector(".lock");
    const ready = () => c.pick && (t.size === false || c.size);
    const sync = () => {
      body.querySelectorAll(".choice").forEach((b) => { b.setAttribute("aria-pressed", String(b.dataset.id === c.pick)); b.disabled = c.locked; });
      body.querySelectorAll(".size").forEach((b) => { b.setAttribute("aria-pressed", String(b.dataset.id === c.size)); b.disabled = c.locked; });
      lock.disabled = !ready() || c.locked;
      lock.hidden = c.locked;
    };
    body.querySelectorAll(".choice").forEach((b) => b.addEventListener("click", () => { if (!c.locked) { c.pick = b.dataset.id; sync(); } }));
    body.querySelectorAll(".size").forEach((b) => b.addEventListener("click", () => { if (!c.locked) { c.size = b.dataset.id; sync(); } }));
    lock.addEventListener("click", () => { c.locked = true; store(`foundry-${cfg.id}-calls`, calls); sync(); reveal(); renderTabs(); score(); });
    sync();
    if (c.locked) reveal();

    function reveal() {
      const best = ev.rows.find((r) => r.id === ev.bestId);
      const mine = ev.rows.find((r) => r.id === c.pick);
      const pickRight = c.pick === ev.bestId;
      const sizeRight = t.size === false ? null : sizeOf(mine.ratio) === c.size;
      const sizeText = t.size === false ? "" :
        ` Your size call: <b class="${sizeRight ? "right" : "wrong"}">${SIZES.find((s) => s.id === c.size).label.split(" (")[0]}</b>; the real effect of ${esc(mine.id)} is <b>${fmt(mine.ratio, 1)}×</b>.`;
      const head = pickRight ? `<b class="right">Right call.</b> ${esc(best.id)} helps most.` :
        `<b class="wrong">Not the best call.</b> You picked ${esc(mine.id)}; ${esc(best.id)} helps most.`;
      body.querySelector(".reveal").innerHTML = `
        <div class="verdict ${pickRight ? "right" : "wrong"}">${head}${sizeText}</div>
        <table class="results"><thead><tr><th>Option</th><th class="r">${esc(m?.label || t.rankBy)}</th><th class="r">vs today</th><th></th></tr></thead>
        <tbody>${ev.rows.map((r) => `<tr class="${r.id === ev.bestId ? "best" : ""}"><td>${esc(r.id)} · ${esc(r.label)}</td><td class="r num">${esc(mf(r.v))}</td>
          <td class="r num">${Number.isFinite(r.ratio) ? fmt(r.ratio, 1) + "×" : "–"}</td><td><button type="button" data-id="${esc(r.id)}">Show</button></td></tr>`).join("")}</tbody></table>
        <div class="learning"><span class="label">What this teaches</span>${t.learning}</div>`;
      body.querySelectorAll(".results button").forEach((b) => b.addEventListener("click", () => {
        const r = ev.rows.find((x) => x.id === b.dataset.id);
        show(r.p, `${r.id} · ${r.label}`);
      }));
    }
  }

  function score() {
    const done = cfg.tests.map((t, i) => [t, calls[i]]).filter(([, c]) => c.locked);
    const right = done.filter(([t, c]) => c.pick === evaluate(t).bestId).length;
    const sized = done.filter(([t]) => t.size !== false);
    const sizeRight = sized.filter(([t, c]) => {
      const ev = evaluate(t);
      return sizeOf(ev.rows.find((r) => r.id === c.pick).ratio) === c.size;
    }).length;
    testsPanel.querySelector(".score").innerHTML = `Calls right: <b class="num">${right}/${done.length}</b> · sizes right: <b class="num">${sizeRight}/${sized.length}</b> · ${cfg.tests.length - done.length} test${cfg.tests.length - done.length === 1 ? "" : "s"} left`;
    return { right, done: done.length, sizeRight, sized: sized.length };
  }
  testsPanel.querySelector(".copy").addEventListener("click", async (e) => {
    const s = score();
    const lines = cfg.tests.map((t, i) => {
      const c = calls[i];
      if (!c.locked) return `Test ${i + 1}: not done`;
      const ev = evaluate(t);
      const mine = ev.rows.find((r) => r.id === c.pick);
      return `Test ${i + 1}: picked ${c.pick} (best ${ev.bestId})${t.size === false ? "" : `, size ${c.size} (actual ${fmt(mine.ratio, 1)}x)`}`;
    });
    const text = `${cfg.id} results: calls ${s.right}/${s.done}, sizes ${s.sizeRight}/${s.sized}\n${lines.join("\n")}`;
    try { await navigator.clipboard.writeText(text); e.target.textContent = "Copied"; }
    catch { e.target.textContent = "Select and copy:"; testsPanel.querySelector(".score").textContent = text; }
  });

  // Reset all calls (for a second attempt).
  const resetBtn = el("button", "", "Start the tests again");
  resetBtn.type = "button";
  resetBtn.addEventListener("click", () => { calls.forEach((c) => Object.assign(c, { pick: null, size: null, locked: false })); store(`foundry-${cfg.id}-calls`, calls); renderTest(); score(); });
  testsPanel.querySelector(".summary").append(resetBtn);

  renderTest();
  score();

  return {
    show,
    refresh: () => { drawChart(); if (sceneApi?.update) sceneApi.update(current, result); },
    get current() { return current; },
    get result() { return result; },
  };
}

/* ---------- The isometric stage ---------- */
function makeStage(host, opts) {
  const reduceMotion = matchMedia("(prefers-reduced-motion: reduce)").matches;
  const renderer = new THREE.WebGLRenderer({ antialias: true });
  renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
  renderer.shadowMap.enabled = true;
  renderer.toneMapping = THREE.ACESFilmicToneMapping;
  renderer.toneMappingExposure = 0.85;
  host.prepend(renderer.domElement);
  const scene = new THREE.Scene();
  // Metals need something to reflect; a neutral room keeps brass and steel readable.
  scene.environment = new THREE.PMREMGenerator(renderer).fromScene(new RoomEnvironment(), 0.04).texture;
  const camera = new THREE.OrthographicCamera(-1, 1, 1, -1, 0.1, 400);
  const target = new THREE.Vector3(...(opts.target || [0, 0, 0]));
  camera.position.set(target.x + 40, 40, target.z + 40);
  camera.lookAt(target);
  scene.add(new THREE.HemisphereLight(0x6f8aa6, 0x0b0d10, 0.6));
  const key = new THREE.DirectionalLight(0xffe2b0, 1.5);
  key.position.set(-20, 40, 15); key.castShadow = true; key.shadow.mapSize.set(2048, 2048);
  Object.assign(key.shadow.camera, { left: -25, right: 25, top: 25, bottom: -25 });
  scene.add(key);

  const mats = {
    floor: new THREE.MeshStandardMaterial({ color: 0x12161c, roughness: 0.95 }),
    dark: new THREE.MeshStandardMaterial({ color: 0x2c333d, metalness: 0.6, roughness: 0.45 }),
    steel: new THREE.MeshStandardMaterial({ color: 0x5b6774, metalness: 0.8, roughness: 0.35 }),
    brass: new THREE.MeshStandardMaterial({ color: 0xb8893f, metalness: 0.9, roughness: 0.32 }),
    belt: new THREE.MeshStandardMaterial({ color: 0x1d232b, metalness: 0.3, roughness: 0.8 }),
    jam: new THREE.MeshStandardMaterial({ color: 0x300000, emissive: 0xe5573f, emissiveIntensity: 2.5 }),
    cool: new THREE.MeshStandardMaterial({ color: 0x0b1620, emissive: 0x7fb3d6, emissiveIntensity: 1.6 }),
  };
  const glow = (intensity = 2.2) => new THREE.MeshStandardMaterial({ color: 0x2a1a05, emissive: 0xffb547, emissiveIntensity: intensity });

  const [fw, fd] = opts.floor || [34, 22];
  const floor = new THREE.Mesh(new THREE.BoxGeometry(fw, 0.4, fd), mats.floor);
  floor.position.set(target.x, -0.2, target.z); floor.receiveShadow = true; scene.add(floor);
  const grid = new THREE.GridHelper(Math.max(fw, fd), Math.max(fw, fd), 0x1e252e, 0x171c23);
  grid.position.set(target.x, 0.01, target.z); scene.add(grid);

  const add = (m, parent) => { m.castShadow = m.receiveShadow = true; (parent || scene).add(m); return m; };
  const box = (w, h, d, mat, x = 0, y = 0, z = 0, parent) => { const m = new THREE.Mesh(new THREE.BoxGeometry(w, h, d), mat); m.position.set(x, y + h / 2, z); return add(m, parent); };
  const cyl = (r, h, mat, x = 0, y = 0, z = 0, parent, seg = 24) => { const m = new THREE.Mesh(new THREE.CylinderGeometry(r, r, h, seg), mat); m.position.set(x, y + h / 2, z); return add(m, parent); };
  const sphere = (r, mat, x = 0, y = 0, z = 0, parent) => { const m = new THREE.Mesh(new THREE.SphereGeometry(r, 16, 10), mat); m.position.set(x, y, z); return add(m, parent); };
  const remove = (obj) => { obj.parent?.remove(obj); obj.traverse?.((o) => { o.geometry?.dispose?.(); }); };

  const composer = new EffectComposer(renderer);
  composer.addPass(new RenderPass(scene, camera));
  composer.addPass(new UnrealBloomPass(new THREE.Vector2(1, 1), 0.9, 0.5, 0.8));
  composer.addPass(new OutputPass());
  let view = opts.view || 22;
  function resize() {
    const w = host.clientWidth, h = host.clientHeight, a = w / h;
    renderer.setSize(w, h, false); composer.setSize(w, h);
    const v = a < 1.2 ? (view * 1.3) / a : view;
    Object.assign(camera, { left: (-v * a) / 2, right: (v * a) / 2, top: v / 2, bottom: -v / 2 });
    camera.updateProjectionMatrix();
  }
  new ResizeObserver(resize).observe(host);
  resize();

  const tickers = [];
  let last = performance.now(), t = 0;
  function frame(now) {
    const dt = Math.min(0.1, (now - last) / 1000); last = now; t += dt;
    for (const f of tickers) { try { f(dt, t); } catch (e) { console.error(e); } }
    composer.render();
    if (!reduceMotion) requestAnimationFrame(frame);
  }
  requestAnimationFrame(frame);

  return {
    THREE, scene, camera, mats, glow, box, cyl, sphere, remove, reduceMotion,
    hud: host.querySelector(".hud"),
    onTick: (f) => tickers.push(f),
    setView: (v) => { view = v; resize(); },
  };
}

function niceTicks(min, max, count = 6) {
  const span = max - min || 1;
  const raw = span / count;
  const mag = 10 ** Math.floor(Math.log10(raw));
  const step = [1, 2, 2.5, 5, 10].map((m) => m * mag).find((s) => span / s <= count) || 10 * mag;
  const out = [];
  for (let v = Math.ceil(min / step) * step; v <= max + step * 0.999; v += step) out.push(Number(v.toFixed(10)));
  return out;
}
