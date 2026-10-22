# Lab kit contract

Every lab page is `web/labs/<slug>.html`, a full HTML document that loads `../kit/lab.css`, the three.js import map, and one module script calling `createLab(config)`. Copy `web/labs/kingman.html` and replace the config and the scene. Never edit `kit/` from a lab.

## Teaching rules (why the kit looks like this)
- **Judgement, not arithmetic.** Viktor never calculates. He makes a call between concrete business options, guesses how big the effect is, locks it, and only then sees the result.
- **Business language.** Parameters, options and metrics use the story's units: engineers, days, euros, units sold, months of runway. No Greek letters or bare model variables in labels; put those in `hint` text if needed.
- **Every option is one click.** An option sets the parameters itself (`params`), so Viktor never translates a decision into slider positions.
- **The ideal is explicit.** Each test's `learning` states the answer, the size of each option's effect, and the rule of thumb (the "ideal" and when it changes).

## Config
```js
createLab({
  id: "L07", area: "Growth strategy", title: "Bass diffusion",
  goal: "html: what Viktor will be able to decide after this lab (one sentence)",
  story: "html: the concrete setting, in numbers, ideally his own company",
  params: [ // free-play levers; tests override them
    { key, label, min, max, step, value, format?: v => string, hint? },          // slider
    { key, label, options: [{ value, label }], value, hint? },                   // segmented choice
  ],
  metrics: [{ key, label, unit?, format?: (v, values) => string }],              // shown live
  model: (p) => ({ values: { [metricKey]: number }, caption: "one plain sentence" }), // pure and fast (< 5 ms)
  chart?: { title, xLabel, yLabel, xMin?, xMax?, yMin?, yMax?, xFormat?, yFormat?,
            series: (p, result) => [{ name, color: "brass"|"glow"|"cool"|"ok"|"jam"|"dim", points: [[x, y]], dots?, dashed? }],
            marker?: (p, result) => [x, y], note? },
  stage?: { floor: [w, d], view: 21, target: [x, 0, z] },
  scene?: (k) => ({ update(params, result) {} }),   // k: THREE, scene, mats, glow(), box(), cyl(), sphere(), remove(), hud, onTick(fn(dt, t))
  tests: [{                                          // 3 or 4 tests
    title: "Test 1. ...", situation: "html", question?: "Your call: ...",
    baseline: { ...params },                         // merged over param defaults; this is "today"
    options: [{ id: "A", label, detail?, params: { ... } }],   // 3-4 options
    rankBy: "metricKey", better: "lower" | "higher",
    size?: false,                                    // set false when "how big" makes no sense
    best?: (rows, baseValue) => "id",                // custom rule, e.g. "busiest plan that keeps the promise"
    learning: "html: the answer, each option's effect size, the rule of thumb",
  }],
  takeaways: ["html", ...],                          // 3-4 lines Viktor keeps; they become cards
});
```

## Checks before you hand back
1. `node tools/check_lab.mjs web/labs/<slug>.html`: syntax check of the module script.
2. Compute every test by hand from your model and make sure each `learning` text states the numbers the page will show. The page computes the reveal; your text must agree with it.
3. The best option must not always be the first one, and the obvious instinct should be wrong in at least one test.
