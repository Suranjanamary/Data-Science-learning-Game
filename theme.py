import random

import streamlit as st
import streamlit.components.v1 as components
import matplotlib.pyplot as plt
from cycler import cycler

TEAL = "#0e8aa8"
CORAL = "#ff6f61"
GOLD = "#e8b923"
PINK = "#f48fb1"
NAVY = "#0a2a4a"
AQUA = "#e9fbff"

plt.rcParams.update({
    "figure.facecolor": AQUA,
    "axes.facecolor": "#ffffff",
    "axes.edgecolor": NAVY,
    "axes.labelcolor": NAVY,
    "xtick.color": NAVY,
    "ytick.color": NAVY,
    "text.color": NAVY,
    "axes.grid": True,
    "grid.color": "#cfeef5",
    "axes.prop_cycle": cycler(color=[TEAL, CORAL, GOLD, PINK, NAVY]),
})

HINTS = {
    "home": [
        "Every level hides some data until you submit. Make your best guess first!",
        "Levels 2 and 3 unlock when you win the level before them.",
        "Every round uses brand new random data, so replaying is never the same.",
    ],
    "l1": [
        "Training error keeps shrinking as the curve gets wigglier. Do not trust it alone!",
        "A curve that touches every dot is memorising noise, not learning the pattern.",
        "Too stiff = underfitting. Too wiggly = overfitting. Aim for the middle.",
    ],
    "l2": [
        "The margin of error only measures random luck, not bias.",
        "A bigger sample cannot fix a sample that was picked in a biased way.",
        "In a random sample, every posting has an equal chance of being picked.",
    ],
    "l3": [
        "When two things move together, ask: could a third thing be pushing both?",
        "Controlling for a variable compares cases where that variable is about the same.",
        "Experiments break hidden links by deciding the treatment at random.",
    ],
}

SWIMMERS = [
    # emoji, top %, seconds, delay, swims right-to-left?, size in rem
    ("🧜‍♀️", 16, 46, -6, False, 3.0),
    ("🧜‍♀️", 58, 58, -30, True, 2.6),
    ("🐠", 32, 30, -12, True, 2.0),
    ("🐟", 72, 36, -20, False, 1.8),
    ("🐡", 44, 50, -40, False, 2.0),
    ("🐙", 85, 70, -10, True, 2.2),
]
COINS = [(4, 24), (94, 38), (6, 62), (93, 70)]
SEABED = ["🌿", "🪸", "🐚", "🌿", "⭐", "🪸", "🐚", "🌿", "🪸", "🐚", "🌿", "🪸"]

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');
:root { --pixel: 'Press Start 2P', 'Courier New', monospace; }
.stApp { background: linear-gradient(180deg, #d9f8ff 0%, #7fd6ec 40%, #2a86b8 80%, #124a78 100%); background-attachment: fixed; }
header[data-testid="stHeader"] { background: transparent; }
.block-container { background: rgba(255,255,255,0.92); border-radius: 26px; padding: 2rem 2.4rem 5rem !important; margin-top: 1rem; box-shadow: 0 8px 30px rgba(10,42,74,0.35); border: 4px solid #0a2a4a; max-width: 980px !important; }
[data-testid="stSidebar"] { background: linear-gradient(180deg, #0a2a4a 0%, #135b8c 100%); }
[data-testid="stSidebar"] * { color: #e6fbff !important; }
[data-testid="stSidebar"] h1 { font-family: var(--pixel); font-size: 1rem; line-height: 1.7; color: #ffe066 !important; }
.stButton > button { font-family: var(--pixel); background: #ff6f61; color: #fff; border: 3px solid #0a2a4a; border-radius: 10px; padding: .7rem 1.2rem; box-shadow: 0 5px 0 #0a2a4a; transition: transform .08s, box-shadow .08s; }
.stButton > button p { font-family: var(--pixel) !important; font-size: .65rem !important; line-height: 1.6; }
.stButton > button:hover { background: #ff8a7e; color: #fff; border-color: #0a2a4a; transform: translateY(-2px); box-shadow: 0 7px 0 #0a2a4a; }
.stButton > button:active { transform: translateY(4px); box-shadow: 0 1px 0 #0a2a4a; }
.stButton > button:disabled { background: #b9c9d1; color: #fff; border-color: #7d8e96; box-shadow: 0 5px 0 #7d8e96; }
[data-testid="stChatMessage"] { background: #fff; border: 3px solid #0a2a4a; border-radius: 16px; box-shadow: 4px 4px 0 #0a2a4a; margin-bottom: .8rem; }
[data-testid="stAlert"] { border: 2px solid #0a2a4a; border-radius: 12px; }
[data-testid="stExpander"] { border: 2px solid #0a2a4a; border-radius: 12px; background: #fff; }
.banner { text-align: center; padding: 1.2rem; border-radius: 12px; background: linear-gradient(135deg, #0e8aa8, #1b6ca8 60%, #4b3b9a); margin-bottom: 1rem; border: 4px solid #0a2a4a; box-shadow: 0 6px 0 #0a2a4a; }
.banner h1 { font-family: var(--pixel); font-size: 1.2rem !important; line-height: 1.7; color: #ffe066 !important; text-shadow: 3px 3px 0 #0a2a4a; margin: 0; padding: 0; }
.banner p { font-family: var(--pixel); font-size: .55rem; line-height: 1.8; margin: .8rem 0 0; color: #e6fbff; }
.waves { text-align: center; font-size: 1.5rem; letter-spacing: .5rem; margin: .3rem 0 1rem; }
.hud { display: flex; justify-content: space-between; flex-wrap: wrap; gap: .5rem; background: #0a2a4a; border: 4px solid #ffe066; border-radius: 10px; padding: .7rem 1rem; margin-bottom: 1rem; font-family: var(--pixel); color: #fff; font-size: .55rem; box-shadow: 0 5px 0 rgba(0,0,0,.35); }
.hud div { text-align: center; line-height: 2; }
.hud b { display: block; color: #ffe066; font-size: .8rem; font-weight: normal; }
.qrow { display: flex; justify-content: center; gap: 1rem; margin: .5rem 0 1.2rem; }
.qblock { width: 54px; height: 54px; display: flex; align-items: center; justify-content: center; font-family: var(--pixel); font-size: 1.4rem; color: #fff; background: #f4b400; border: 4px solid #8a5a1e; border-radius: 8px; box-shadow: inset -4px -4px 0 #c98a00, inset 4px 4px 0 #ffd966; cursor: help; text-shadow: 2px 2px 0 #8a5a1e; }
.qblock:hover { animation: bump .35s ease-out; }
.map { display: flex; align-items: center; justify-content: center; flex-wrap: wrap; gap: .3rem; margin: 1rem 0 1.4rem; padding: 1.6rem .6rem 1rem; border-radius: 14px; background: linear-gradient(180deg, #bff3ff, #8be0f0); border: 4px solid #0a2a4a; }
.node { position: relative; width: 96px; text-align: center; font-family: var(--pixel); font-size: .5rem; line-height: 1.7; color: #0a2a4a; }
.node .dot { width: 62px; height: 62px; margin: 0 auto .4rem; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.8rem; border: 4px solid #0a2a4a; background: #ffe066; box-shadow: 0 5px 0 #0a2a4a; }
.node.locked .dot { background: #b9c9d1; }
.node.done .dot { background: #7ae582; }
.node.open .dot { animation: pulse 1.2s ease-in-out infinite; }
.node .here { position: absolute; top: -30px; left: 50%; font-size: 1.6rem; animation: hop 1s ease-in-out infinite; }
.link { font-size: 1.2rem; color: #0a2a4a; letter-spacing: -2px; }
.bubbles { position: fixed; inset: 0; pointer-events: none; z-index: 4; overflow: hidden; }
.bubbles span { position: absolute; bottom: -80px; border-radius: 50%; background: radial-gradient(circle at 30% 30%, rgba(255,255,255,.95), rgba(255,255,255,.25)); border: 1px solid rgba(255,255,255,.7); animation: rise linear infinite; }
.swimmers { position: fixed; inset: 0; pointer-events: none; z-index: 5; overflow: hidden; }
.swim { position: absolute; left: -12%; animation: swim linear infinite; }
.swim.rev { animation-name: swimrev; transform: scaleX(-1); }
.swim span { display: inline-block; animation: bob 3s ease-in-out infinite; }
.coin { position: absolute; font-size: 1.6rem; animation: spin 2.2s linear infinite; }
.seabed { position: fixed; left: 0; right: 0; bottom: 0; height: 38px; z-index: 6; pointer-events: none; background: repeating-linear-gradient(90deg, #d9a85b 0 38px, #b8863f 38px 40px); border-top: 4px solid #8a5a1e; }
.seabed .row { position: absolute; left: 0; right: 0; bottom: 34px; display: flex; justify-content: space-around; font-size: 2rem; }
.seabed .row span { display: inline-block; transform-origin: bottom center; animation: sway 3.2s ease-in-out infinite; }
.seabed .row span:nth-child(odd) { animation-delay: -1.4s; }
.walker { position: absolute; bottom: 34px; left: 2%; font-size: 1.7rem; animation: walk linear infinite alternate; }
.walker.b { animation-direction: alternate-reverse; }
#pop-layer { position: fixed; inset: 0; pointer-events: none; z-index: 9998; overflow: hidden; }
.pop-bubble { position: absolute; bottom: -80px; border-radius: 50%; cursor: pointer; pointer-events: auto; background: radial-gradient(circle at 30% 30%, rgba(255,255,255,.95), rgba(255,255,255,.2)); border: 2px solid rgba(255,255,255,.9); box-shadow: inset 0 0 8px rgba(255,255,255,.7); animation: rise linear forwards; }
.pop-bubble:hover { filter: brightness(1.2); }
.drop { position: absolute; width: 8px; height: 8px; margin: -4px; border-radius: 50%; background: #fff; border: 2px solid #7fd6ec; animation: droplet .6s ease-out forwards; }
.pop-text { position: absolute; transform: translate(-50%, -50%); font-family: var(--pixel); font-size: 14px; color: #fff; text-shadow: 2px 2px 0 #0a2a4a; white-space: nowrap; animation: floatup .8s ease-out forwards; }
@keyframes rise { from { transform: translateY(0) translateX(0); opacity: .9; } 50% { transform: translateY(-60vh) translateX(25px); } to { transform: translateY(-115vh) translateX(-15px); opacity: 0; } }
@keyframes swim { from { left: -12%; } to { left: 108%; } }
@keyframes swimrev { from { left: 108%; } to { left: -12%; } }
@keyframes bob { 0%, 100% { transform: translateY(0) rotate(-4deg); } 50% { transform: translateY(-14px) rotate(4deg); } }
@keyframes spin { to { transform: rotateY(360deg); } }
@keyframes sway { 0%, 100% { transform: rotate(-6deg); } 50% { transform: rotate(6deg); } }
@keyframes walk { from { left: 2%; } to { left: 92%; } }
@keyframes pulse { 50% { transform: scale(1.12); } }
@keyframes hop { 0%, 100% { transform: translate(-50%, 0); } 50% { transform: translate(-50%, -9px); } }
@keyframes bump { 40% { transform: translateY(-14px); } }
@keyframes droplet { to { transform: translate(var(--dx), var(--dy)) scale(.2); opacity: 0; } }
@keyframes floatup { to { transform: translate(-50%, -190%); opacity: 0; } }
@media (prefers-reduced-motion: reduce) { .swim, .walker, .coin, .bubbles span, .seabed .row span, .node.open .dot, .node .here { animation: none !important; } }
</style>
"""

# This script runs in a tiny iframe. It copies the function main() into the real page
# so the music and bubbles keep playing even when Streamlit refreshes the iframe.
ARCADE_JS = """
<script>
function main() {
  if (window.__arcade) { return; }
  var AC = window.AudioContext || window.webkitAudioContext;
  if (!AC) { return; }

  var ctx = new AC();
  var master = ctx.createGain();
  master.connect(ctx.destination);
  var sfxBus = ctx.createGain();
  sfxBus.connect(master);
  var musicBus = ctx.createGain();
  musicBus.gain.value = 0.55;
  musicBus.connect(master);
  var state = { sfx: true, music: true, unlocked: false };
  window.__arcade = state;

  function midi(n) { return 440 * Math.pow(2, (n - 69) / 12); }

  function tone(freq, when, dur, type, vol, freqEnd, bus) {
    var o = ctx.createOscillator();
    var g = ctx.createGain();
    o.type = type;
    o.frequency.setValueAtTime(freq, when);
    if (freqEnd) { o.frequency.exponentialRampToValueAtTime(freqEnd, when + dur); }
    g.gain.setValueAtTime(0.0001, when);
    g.gain.exponentialRampToValueAtTime(vol, when + 0.01);
    g.gain.exponentialRampToValueAtTime(0.0001, when + dur);
    o.connect(g);
    g.connect(bus || sfxBus);
    o.start(when);
    o.stop(when + dur + 0.05);
  }

  // ---------- Sound effects ----------
  window.__sfx = function (name) {
    if (!state.sfx) { return; }
    if (ctx.state === "suspended") { ctx.resume(); }
    var t = ctx.currentTime;
    if (name === "pop") {
      tone(450 + Math.random() * 250, t, 0.14, "sine", 0.3, 1500);
    } else if (name === "coin") {
      tone(988, t, 0.08, "square", 0.07);
      tone(1319, t + 0.08, 0.22, "square", 0.07);
    } else if (name === "win") {
      [523, 659, 784, 1047, 784, 1047, 1319].forEach(function (f, i) {
        tone(f, t + i * 0.13, 0.22, "square", 0.08);
      });
    } else if (name === "wrong") {
      tone(300, t, 0.18, "sawtooth", 0.08, 150);
      tone(200, t + 0.18, 0.3, "sawtooth", 0.08, 100);
    } else if (name === "splash") {
      tone(300, t, 0.25, "triangle", 0.15, 900);
    }
  };

  // ---------- Background music (a looping chiptune melody) ----------
  var STEP = 0.3;
  var CHORDS = [
    { bass: 45, arp: [57, 60, 64, 69] },
    { bass: 41, arp: [53, 57, 60, 65] },
    { bass: 48, arp: [60, 64, 67, 72] },
    { bass: 43, arp: [55, 59, 62, 67] }
  ];
  var SHAPE = [0, 1, 2, 3, 2, 1, 2, 3];
  var BLIPS = [81, 84, 86, 88, 91];
  var nextT = 0;
  var stepNo = 0;
  var timer = null;

  function playStep(i, t) {
    var chord = CHORDS[Math.floor(i / 8) % CHORDS.length];
    var k = i % 8;
    tone(midi(chord.arp[SHAPE[k]]), t, 0.32, "sine", 0.09, null, musicBus);
    if (k === 0 || k === 4) {
      tone(midi(chord.bass), t, 0.9, "triangle", 0.14, null, musicBus);
    }
    if (k === 0) {
      chord.arp.slice(0, 3).forEach(function (n) {
        tone(midi(n), t, 2.3, "sine", 0.025, null, musicBus);
      });
    }
    if (Math.random() < 0.12) {
      var n = BLIPS[Math.floor(Math.random() * BLIPS.length)];
      tone(midi(n), t + 0.15, 0.2, "sine", 0.035, midi(n + 7), musicBus);
    }
  }

  function schedule() {
    if (!state.music) { return; }
    if (nextT < ctx.currentTime) { nextT = ctx.currentTime + 0.05; }
    while (nextT < ctx.currentTime + 0.6) {
      playStep(stepNo, nextT);
      nextT += STEP;
      stepNo += 1;
    }
  }

  function startMusic() {
    if (!timer) { timer = setInterval(schedule, 150); }
  }
  function stopMusic() {
    if (timer) { clearInterval(timer); timer = null; }
    nextT = 0;
  }

  // ---------- Unlock audio on the first click ----------
  function unlock() {
    if (state.unlocked) { return; }
    state.unlocked = true;
    ctx.resume();
    if (state.music) { startMusic(); }
    var h = document.getElementById("arcade-hint");
    if (h) { h.remove(); }
  }
  document.addEventListener("pointerdown", unlock, true);
  document.addEventListener("keydown", unlock, true);

  // Coin ding on every Streamlit button
  document.addEventListener("click", function (e) {
    var b = e.target.closest ? e.target.closest("button") : null;
    if (b && !b.classList.contains("arcade-btn")) { window.__sfx("coin"); }
  });

  // ---------- Toggle buttons and hint ----------
  function makeBtn(id, text, title, right) {
    var b = document.createElement("button");
    b.id = id;
    b.className = "arcade-btn";
    b.textContent = text;
    b.title = title;
    b.style.cssText = "position:fixed;right:" + right + "px;bottom:56px;z-index:10000;width:46px;" +
      "height:46px;border-radius:50%;border:3px solid #0a2a4a;background:#ffe066;font-size:20px;" +
      "cursor:pointer;box-shadow:0 4px 0 #0a2a4a;";
    document.body.appendChild(b);
    return b;
  }

  var musicBtn = makeBtn("music-btn", "🎵", "Music on/off", 14);
  var sfxBtn = makeBtn("sfx-btn", "🔊", "Sound effects on/off", 68);

  musicBtn.addEventListener("click", function () {
    state.music = !state.music;
    musicBtn.textContent = state.music ? "🎵" : "🔕";
    musicBus.gain.value = state.music ? 0.55 : 0;
    if (state.music) { if (state.unlocked) { ctx.resume(); startMusic(); } } else { stopMusic(); }
  });
  sfxBtn.addEventListener("click", function () {
    state.sfx = !state.sfx;
    sfxBtn.textContent = state.sfx ? "🔊" : "🔇";
  });

  var hint = document.createElement("div");
  hint.id = "arcade-hint";
  hint.textContent = "🎵 Click anywhere to start the music!";
  hint.style.cssText = "position:fixed;right:14px;bottom:110px;z-index:10000;padding:8px 12px;" +
    "background:#0a2a4a;color:#ffe066;border:3px solid #ffe066;border-radius:10px;" +
    "font:10px 'Press Start 2P','Courier New',monospace;line-height:1.6;max-width:210px;";
  document.body.appendChild(hint);

  // ---------- Poppable bubbles ----------
  var layer = document.createElement("div");
  layer.id = "pop-layer";
  document.body.appendChild(layer);
  var WORDS = ["POP!", "+1 🪙", "💥", "✨", "SPLASH!"];

  function spawn() {
    var b = document.createElement("div");
    b.className = "pop-bubble";
    var s = 22 + Math.random() * 30;
    b.style.width = s + "px";
    b.style.height = s + "px";
    b.style.left = (3 + Math.random() * 92) + "%";
    b.style.animationDuration = (10 + Math.random() * 12) + "s";
    b.addEventListener("click", function () { burst(b); });
    b.addEventListener("animationend", function () { b.remove(); spawn(); });
    layer.appendChild(b);
  }

  function burst(b) {
    window.__sfx("pop");
    var r = b.getBoundingClientRect();
    var x = r.left + r.width / 2;
    var y = r.top + r.height / 2;
    b.remove();
    for (var i = 0; i < 8; i++) {
      var d = document.createElement("div");
      d.className = "drop";
      d.style.left = x + "px";
      d.style.top = y + "px";
      var a = (i / 8) * 2 * Math.PI;
      d.style.setProperty("--dx", Math.cos(a) * 42 + "px");
      d.style.setProperty("--dy", Math.sin(a) * 42 + "px");
      layer.appendChild(d);
      (function (el) { setTimeout(function () { el.remove(); }, 650); })(d);
    }
    var t = document.createElement("div");
    t.className = "pop-text";
    t.textContent = WORDS[Math.floor(Math.random() * WORDS.length)];
    t.style.left = x + "px";
    t.style.top = y + "px";
    layer.appendChild(t);
    setTimeout(function () { t.remove(); }, 850);
    setTimeout(spawn, 1500);
  }

  for (var j = 0; j < 9; j++) { setTimeout(spawn, j * 800); }
}

var parentDoc = window.parent.document;
if (!parentDoc.getElementById("arcade-script")) {
  var s = parentDoc.createElement("script");
  s.id = "arcade-script";
  s.textContent = "(" + main.toString() + ")();";
  parentDoc.head.appendChild(s);
}
</script>
"""


def _decor():
    """Background bubbles, swimming mermaids and fish, coins and the sandy seabed."""
    rnd = random.Random(7)
    bubbles = "".join(
        f'<span style="left:{rnd.randint(2, 96)}%;width:{(s := rnd.randint(10, 30))}px;height:{s}px;'
        f'animation-duration:{rnd.randint(9, 22)}s;animation-delay:-{rnd.randint(0, 20)}s"></span>'
        for _ in range(12)
    )
    swimmers = "".join(
        f'<div class="swim{" rev" if rev else ""}" style="top:{top}%;animation-duration:{dur}s;'
        f'animation-delay:{delay}s;font-size:{size}rem"><span>{emo}</span></div>'
        for emo, top, dur, delay, rev, size in SWIMMERS
    )
    coins = "".join(
        f'<div class="coin" style="left:{x}%;top:{y}%">🪙</div>' for x, y in COINS
    )
    row = "".join(f"<span>{e}</span>" for e in SEABED)
    st.markdown(
        f'<div class="bubbles">{bubbles}</div>'
        f'<div class="swimmers">{swimmers}{coins}</div>'
        f'<div class="seabed"><div class="row">{row}</div>'
        f'<div class="walker" style="animation-duration:26s">🦀</div>'
        f'<div class="walker b" style="animation-duration:38s">🐢</div></div>',
        unsafe_allow_html=True,
    )


def inject():
    """Call once at the top of app.py: adds the ocean-arcade look, sound and music."""
    st.markdown(CSS, unsafe_allow_html=True)
    _decor()
    components.html(ARCADE_JS, height=0)


def play(name):
    """Play a sound effect: 'pop', 'coin', 'win', 'wrong' or 'splash'."""
    components.html(
        f"<script>if (window.parent.__sfx) {{ window.parent.__sfx('{name}'); }}</script>",
        height=0,
    )


def banner(title, subtitle=""):
    st.markdown(f'<div class="banner"><h1>{title}</h1><p>{subtitle}</p></div>',
                unsafe_allow_html=True)


def waves():
    st.markdown('<div class="waves">🌊 🐚 🫧 🐟 🫧 🐚 🌊</div>', unsafe_allow_html=True)


def hud(world="MAP"):
    """Mario-style score bar."""
    scores = st.session_state.get("scores", {})
    coins = sum(scores.values())
    shells = sum(1 for k in ("l1", "l2", "l3") if st.session_state.get(f"{k}_won"))
    st.markdown(
        f'<div class="hud"><div>PEARLS<b>🪙 {coins:03d}</b></div>'
        f'<div>WORLD<b>{world}</b></div>'
        f'<div>SHELLS<b>🐚 {shells}/3</b></div>'
        f'<div>GOAL<b>300</b></div></div>',
        unsafe_allow_html=True,
    )


def block_row():
    """Hoverable ? blocks with little data science tips."""
    tips = [
        "Overfitting means memorising the noise",
        "A bigger sample does not fix a biased sample",
        "Correlation does not mean causation",
        "Randomising breaks hidden links",
    ]
    blocks = "".join(f'<div class="qblock" title="{t}">?</div>' for t in tips)
    st.markdown(f'<div class="qrow">{blocks}</div>', unsafe_allow_html=True)
    st.caption("Hover over the ? blocks for tips. Click the bubbles to pop them!")


def world_map():
    """Mario-style level map: Fizzy hops to the next open level."""
    ss = st.session_state
    all_won = all(ss.get(f"l{i}_won") for i in (1, 2, 3))
    steps = [
        ("💼", "1 Salary Curve", "l1", True),
        ("🪼", "2 Fake Jobs", "l2", bool(ss.get("l1_won"))),
        ("🔎", "3 Posting Mystery", "l3", bool(ss.get("l2_won"))),
        ("🏰", "Poseidon’s Palace", None, all_won),
    ]
    cells, placed = [], False
    for icon, label, key, unlocked in steps:
        if key is None:
            state = "done" if all_won else "locked"
        elif ss.get(f"{key}_won"):
            state = "done"
        elif unlocked:
            state = "open"
        else:
            state = "locked"
        marker = ""
        if state == "open" and not placed:
            marker, placed = '<div class="here">🐟</div>', True
        shown = "🔒" if (state == "locked" and key) else icon
        cells.append(f'<div class="node {state}">{marker}<div class="dot">{shown}</div>{label}</div>')
    st.markdown(f'<div class="map">{"<div class=link>•••</div>".join(cells)}</div>',
                unsafe_allow_html=True)


def mystery_block(key):
    """Show a random hint for the current page."""
    st.toast(random.choice(HINTS.get(key, HINTS["home"])), icon="🪙")


def say(who, avatar, text):
    """A character 'speaks' in a chat bubble."""
    with st.chat_message(who, avatar=avatar):
        st.markdown(text)


def celebrate_if_needed():
    if st.session_state.pop("celebrate", False):
        st.balloons()
        st.toast("🏁 LEVEL CLEAR!", icon="🪙")
        play("win")


def record(key, score):
    """Save the best score for a level and mark it as won (unlocks the next one)."""
    scores = st.session_state.setdefault("scores", {})
    scores[key] = max(score, scores.get(key, 0))
    st.session_state[f"{key}_won"] = True