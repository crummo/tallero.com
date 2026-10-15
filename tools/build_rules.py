import json, os, sys

SITE = sys.argv[1]
APP = "https://apps.apple.com/app/id6781403658"
CHEV = ""

def head(title, desc, path, crumbs):
    url = "https://gettallero.com" + path
    ld = {"@context": "https://schema.org", "@type": "BreadcrumbList",
          "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": "https://gettallero.com" + p}
                              for i, (n, p) in enumerate(crumbs)]}
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>{title}</title>
<meta name="description" content="{desc}"/>
<link rel="canonical" href="{url}"/>
<link rel="icon" href="/assets/icon-app.svg"/>
<meta name="apple-itunes-app" content="app-id=6781403658"/>
<meta property="og:type" content="article"/>
<meta property="og:url" content="{url}"/>
<meta property="og:title" content="{title}"/>
<meta property="og:description" content="{desc}"/>
<meta property="og:image" content="https://gettallero.com/assets/og-image.png"/>
<meta name="twitter:card" content="summary_large_image"/>
<meta name="twitter:image" content="https://gettallero.com/assets/og-image.png"/>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400..800&display=swap" rel="stylesheet"/>
<link rel="stylesheet" href="/tally.css"/>
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</head>
<body>

<!-- ============ HEADER ============ -->
<header class="site-header">
  <div class="wrap site-header__inner">
    <a class="lockup" href="/" aria-label="Tallero home">
      <svg class="mark" viewBox="0 0 100 100" fill="none" style="color:var(--ink)" aria-hidden="true">
        <rect x="13.64" y="13.64" width="11.36" height="72.73" rx="3" fill="#9b7af0"/>
        <rect x="34.09" y="13.64" width="11.36" height="72.73" rx="3" fill="#e0457b"/>
        <rect x="54.55" y="13.64" width="11.36" height="72.73" rx="3" fill="#2baa6b"/>
        <rect x="75" y="13.64" width="11.36" height="72.73" rx="3" fill="#2bafa6"/>
        <rect x="1.5" y="44" width="97" height="12" rx="3" transform="rotate(-18 50 50)" fill="currentColor"/>
      </svg>
      <span class="wordmark">Tallero</span>
    </a>
    <nav class="site-nav" id="siteNav">
      <a href="/#features">Features</a>
      <a href="/#games">Games</a>
      <a href="/rules/" style="color:var(--blue)">Rules</a>
      <a href="/support.html">Support</a>
    </nav>
    <button class="nav-toggle" id="navToggle" aria-label="Open menu" aria-expanded="false" aria-controls="siteNav">
      <svg viewBox="0 0 24 24" width="24" height="24" fill="none" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
    </button>
    <div class="site-header__cta">
      <a class="btn btn--ghost" href="/">Back to home</a>
    </div>
  </div>
</header>
'''

FOOT = f'''
<!-- ============ FOOTER ============ -->
<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div>
        <a class="lockup" href="/" aria-label="Tallero home">
          <svg class="mark" viewBox="0 0 100 100" fill="none" style="color:#fff" aria-hidden="true">
            <rect x="13.64" y="13.64" width="11.36" height="72.73" rx="3" fill="#9b7af0"/>
            <rect x="34.09" y="13.64" width="11.36" height="72.73" rx="3" fill="#e0457b"/>
            <rect x="54.55" y="13.64" width="11.36" height="72.73" rx="3" fill="#2baa6b"/>
            <rect x="75" y="13.64" width="11.36" height="72.73" rx="3" fill="#2bafa6"/>
            <rect x="1.5" y="44" width="97" height="12" rx="3" transform="rotate(-18 50 50)" fill="currentColor"/>
          </svg>
          <span class="wordmark">Tallero</span>
        </a>
        <p class="blurb">The friendly score-keeper for card games and game nights. Settle the score.</p>
        <div class="social-row">
          <a href="https://www.instagram.com/talleroapp" target="_blank" rel="noopener" aria-label="Tallero on Instagram">
            <svg viewBox="0 0 24 24" width="22" height="22" fill="none" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5" stroke="currentColor" stroke-width="1.8"/><circle cx="12" cy="12" r="4" stroke="currentColor" stroke-width="1.8"/><circle cx="17.4" cy="6.6" r="1.2" fill="currentColor"/></svg>
          </a>
        </div>
      </div>
      <div class="fcol">
        <h4>Product</h4>
        <ul>
          <li><a href="/#features">Features</a></li>
          <li><a href="/#games">Games</a></li>
          <li><a href="/rules/">Game rules</a></li>
          <li><a href="{APP}" target="_blank" rel="noopener">App Store</a></li>
        </ul>
      </div>
      <div class="fcol">
        <h4>Company</h4>
        <ul>
          <li><a href="/support.html">Support</a></li>
          <li><a href="/privacy.html">Privacy Policy</a></li>
          <li><a href="mailto:support@gettallero.com">support@gettallero.com</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-legal">
      <span class="small">© <span id="yr">2026</span> Slow Dust Software. All rights reserved.</span>
      <span class="tm">Phase&nbsp;10® / Yahtzee® / Qwirkle® / Flip&nbsp;7™ / Dutch&nbsp;Blitz® / Mölkky® and other game names are trademarks of their respective owners. Tallero is independent and unaffiliated.</span>
    </div>
  </div>
</footer>

<script src="/rules/rules.js"></script>
</body>
</html>
'''

def hero(name, key, tile, h1, lede):
    return f'''
<!-- ============ PAGE HERO ============ -->
<section class="page-hero">
  <div class="wrap">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="/rules/">Game rules</a> / {name}</nav>
    <div class="rules-hero__row">
      <div class="tile" style="background:{tile}"><img src="/assets/games/{key}.svg" alt=""/></div>
      <h1>{h1}</h1>
    </div>
    <p>{lede}</p>
  </div>
</section>
'''

def callout(h, p):
    return f'''
      <div class="callout">
        <div>
          <h2>{h}</h2>
          <p>{p}</p>
        </div>
        <a class="appstore-badge" href="{APP}" target="_blank" rel="noopener" aria-label="Download Tallero on the App Store"><img src="/assets/appstore-badge.svg" alt="Download on the App Store"/></a>
      </div>'''

def sheet(title, sub, cols, rows, mn, mx, dflt, labels=None, unit="players"):
    extra = (f' data-labels="{"|".join(labels)}"' if labels else "") + f' data-unit="{unit}"'
    picker = unit.capitalize()
    return f'''
<!-- ============ SCORE SHEET ============
     A direct child of <body> on purpose: the print CSS hides every other
     body child while body.print-sheet is on (see rules/rules.js). -->
<section class="sheet" id="sheet" data-title="{title}" data-cols="{cols}" data-rows="{rows}" data-min="{mn}" data-max="{mx}" data-default="{dflt}"{extra}>
  <div class="wrap">
    <div class="sheet__head">
      <div>
        <h2 id="score-sheet">Printable score sheet</h2>
        <p>{sub}</p>
      </div>
      <div class="sheet__controls">
        <label for="sheetPlayers">{picker}</label>
        <select id="sheetPlayers"></select>
        <button class="btn btn--primary" type="button" data-print>Print</button>
      </div>
    </div>
    <div class="sheet__title"></div>
    <div class="sheet__scroll"></div>
    <p class="sheet__foot">gettallero.com — or skip the pencil and let Tallero keep score.</p>
  </div>
</section>
'''

def page(path, title, desc, crumbs, body):
    out = os.path.join(SITE, path.strip("/"), "index.html")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w") as f:
        f.write(head(title, desc, path, crumbs) + body + FOOT)
    print("wrote", out)

def _card(c, red):
    return f'<span class="card{" r" if red else ""}" role="img" aria-label="{c}"><b>{c[:-1]}</b><i>{c[-1]}</i></span>'
def R(c): return _card(c, True)
def B(c): return _card(c, False)

# ------------------------------------------------------------------ FARKLE
farkle = hero("Farkle", "farkle", "oklch(0.928 0.045 357)", "Farkle rules and scoring",
  "What every roll is worth, how a turn works, and the variants tables argue about — plus a printable score sheet.") + f'''
<section class="section section--tight">
  <div class="wrap">
    <div class="prose">
      <ul class="toc">
        <li><a href="#scoring">Scoring chart</a></li>
        <li><a href="#turn">Taking a turn</a></li>
        <li><a href="#winning">Winning</a></li>
        <li><a href="#variants">Variants</a></li>
        <li><a href="#score-sheet">Score sheet</a></li>
      </ul>

      <p class="gist">Roll six dice, set aside the ones that score, and choose: roll what's left to build the turn higher, or bank what you've got. Roll nothing that scores and you <strong>Farkle</strong> — the entire turn's points vanish. First past 10,000 doesn't end it: everyone else gets one last turn to catch you.</p>
      <p>You need six dice, two or more players, and something to keep score with.</p>

      <h2 id="scoring">Farkle scoring chart</h2>
      <p>These are the values printed in the retail game. Combinations only count when they come up in a single roll — you can't build a three of a kind out of dice from two different rolls.</p>
      <table class="score-table">
        <thead><tr><th>Dice</th><th>Points</th></tr></thead>
        <tbody>
          <tr><td>Each 1</td><td class="v">100</td></tr>
          <tr><td>Each 5</td><td class="v">50</td></tr>
          <tr><td>Three of a kind<span class="note">Three 2s = 200, three 3s = 300, and so on up to three 6s = 600.</span></td><td class="v">face × 100</td></tr>
          <tr><td>Three 1s<span class="note">Common variant: 300.</span></td><td class="v">1,000</td></tr>
          <tr><td>Four of a kind</td><td class="v">1,000</td></tr>
          <tr><td>Five of a kind</td><td class="v">2,000</td></tr>
          <tr><td>Six of a kind</td><td class="v">3,000</td></tr>
          <tr><td>Straight <span class="dice"><span class="pc">1</span><span class="pc">2</span><span class="pc">3</span><span class="pc">4</span><span class="pc">5</span><span class="pc">6</span></span></td><td class="v">1,500</td></tr>
          <tr><td>Three pairs <span class="dice"><span class="pc">2</span><span class="pc">2</span> &nbsp;<span class="pc">4</span><span class="pc">4</span> &nbsp;<span class="pc">6</span><span class="pc">6</span></span></td><td class="v">1,500</td></tr>
          <tr><td>Four of a kind + a pair <span class="dice"><span class="pc">4</span><span class="pc">4</span><span class="pc">4</span><span class="pc">4</span> &nbsp;<span class="pc">6</span><span class="pc">6</span></span></td><td class="v">1,500</td></tr>
          <tr><td>Two triplets <span class="dice"><span class="pc">1</span><span class="pc">1</span><span class="pc">1</span> &nbsp;<span class="pc">3</span><span class="pc">3</span><span class="pc">3</span></span></td><td class="v">2,500</td></tr>
          <tr><td>No scoring dice in a roll<span class="note">Everything built up this turn is lost.</span></td><td class="v">Farkle</td></tr>
        </tbody>
      </table>
      <p>On their own, 2s, 3s, 4s and 6s are worth nothing — they only score as part of a combination.</p>

      <h2 id="turn">Taking a turn</h2>
      <ul>
        <li>Roll all six dice. Every roll, you must set aside at least one scoring die. If you can't, you've Farkled and lose everything you'd built up this turn.</li>
        <li>Dice you've set aside are locked for the turn — you can't re-roll them to improve a combination.</li>
        <li>After setting dice aside, either roll the rest or <strong>bank</strong>: stop and add the turn's points to your score. Points are only yours once you bank them.</li>
        <li><strong>Hot dice:</strong> score with all six dice and you can pick them all back up and keep rolling the same turn. Everything you've built is still at risk — Farkle and it's all gone.</li>
      </ul>
      <div class="example">
        <h3>Example turn</h3>
        <p>You roll <span class="dice"><span class="pc">1</span><span class="pc">5</span><span class="pc">2</span><span class="pc">2</span><span class="pc">4</span><span class="pc">6</span></span>. Set aside the 1 and the 5 for 150, then roll the other four: <span class="dice"><span class="pc">3</span><span class="pc">3</span><span class="pc">3</span><span class="pc">6</span></span>. Three 3s is 300, so you're on 450 with one die left. Bank the 450, or roll that last die — a 1 or a 5 gives you hot dice, anything else is a Farkle and you score nothing.</p>
      </div>

      <h2 id="winning">Winning</h2>
      <p>The first player to pass 10,000 doesn't win on the spot. Everyone else gets one more turn to beat them, and the highest total when that lap finishes takes the game — so a big last turn can steal it.</p>

      <h2 id="variants">Common variants</h2>
      <p>Farkle is a folk game and printings genuinely disagree. Settle these before the first roll:</p>
      <ul>
        <li><strong>Three 1s = 300</strong> instead of 1,000 — the Pocket Farkel rule.</li>
        <li><strong>Straight = 2,500</strong> at some tables, rather than 1,500.</li>
        <li><strong>Four, five and six of a kind double up</strong> — each extra die doubles the three-of-a-kind value — instead of the flat 1,000 / 2,000 / 3,000.</li>
        <li><strong>Getting on the board:</strong> you must bank at least 500 in one turn before any of your points count.</li>
        <li><strong>Three Farkles in a row</strong> costs you 1,000 points.</li>
      </ul>

      <h2>Quick answers</h2>
      <h3>What does “Farkle” mean in the game?</h3>
      <p>A roll with no scoring dice in it. It ends your turn and wipes out every point you'd built up that turn, though your banked score is safe.</p>
      <h3>Can you re-roll dice you've already set aside?</h3>
      <p>No. Once a die is set aside it's locked until your turn ends — unless all six score, which gives you hot dice and a fresh roll of all six.</p>
      <h3>Do you have to keep every scoring die?</h3>
      <p>No — you only have to keep at least one. Leaving a lone 5 in the roll gives you more dice to throw next time.</p>
''' + callout("Let Tallero do the adding.",
  "Roll for real and enter each turn's total — Tallero keeps the running scores, handles the final lap, and has this chart a tap away.") + '''
    </div>
  </div>
</section>
''' + sheet("Farkle score sheet", "Write each turn's points, then the running total. Room for 20 turns.", "+,Total", 20, 2, 8, 4)

page("/rules/farkle/", "Farkle Rules & Scoring Chart — Tallero",
     "How to play Farkle: the full scoring chart (three pairs, straights, four of a kind), how a turn works, hot dice, winning, common variants, and a printable score sheet.",
     [("Game rules", "/rules/"), ("Farkle", "/rules/farkle/")], farkle)

# ------------------------------------------------------------------ CRIBBAGE
crib = hero("Cribbage", "cribbage", "oklch(0.928 0.045 78)", "Cribbage rules and scoring",
  "How the deal, the play and the show work, what every combination is worth, and worked examples of counting a hand.") + f'''
<section class="section section--tight">
  <div class="wrap">
    <div class="prose">
      <ul class="toc">
        <li><a href="#scoring">Scoring</a></li>
        <li><a href="#deal">The deal</a></li>
        <li><a href="#play">The play</a></li>
        <li><a href="#show">Counting a hand</a></li>
        <li><a href="#winning">Winning</a></li>
        <li><a href="#score-sheet">Score sheet</a></li>
      </ul>

      <p class="gist">Each hand, players are dealt six cards and put two face down into the <strong>crib</strong> — a bonus hand the dealer counts later — and one shared cut card is turned face up. First comes <strong>the play</strong> (pegging): you take turns laying cards against a running total, scoring for fifteens, runs, pairs and 31. Then comes <strong>the show</strong>: each hand is counted, with the cut card as a fifth card. First to 121 wins.</p>
      <p>The rules below are for two players, the classic game. Three- and four-player differences are noted in the deal.</p>

      <h2 id="scoring">What's worth what</h2>
      <p>Every combination counts, and cards are reused across them — score each fifteen, each pair and each run your five cards can make, then add them together.</p>
      <table class="score-table">
        <thead><tr><th>Combination</th><th>Points</th></tr></thead>
        <tbody>
          <tr><td>Fifteen<span class="note">Any cards totalling exactly 15. Face cards count 10, aces 1. Count every combination separately.</span></td><td class="v">2</td></tr>
          <tr><td>Pair</td><td class="v">2</td></tr>
          <tr><td>Three of a kind<span class="note">Three separate pairs.</span></td><td class="v">6</td></tr>
          <tr><td>Four of a kind<span class="note">Six separate pairs.</span></td><td class="v">12</td></tr>
          <tr><td>Run of three or more<span class="note">One point per card. Suits don't matter; aces are low, so K-A-2 isn't a run.</span></td><td class="v">1 per card</td></tr>
          <tr><td>Flush in the hand<span class="note">All four hand cards one suit; 5 if the cut matches too. In the crib, all five cards must match.</span></td><td class="v">4</td></tr>
          <tr><td>His Nobs<span class="note">In the show: the Jack in your hand matching the cut card's suit.</span></td><td class="v">1</td></tr>
          <tr><td>His Heels<span class="note">When the cut card is a Jack, the dealer scores immediately.</span></td><td class="v">2</td></tr>
          <tr><td>Hitting 31<span class="note">In the play, bringing the count to exactly 31.</span></td><td class="v">2</td></tr>
          <tr><td>Last card<span class="note">In the play, laying the final card of a sequence that stops short of 31.</span></td><td class="v">1</td></tr>
        </tbody>
      </table>
      <h3>Double and triple runs</h3>
      <p>These are the same rules applied to overlapping cards, but they're worth knowing by sight:</p>
      <table class="score-table">
        <tbody>
          <tr><td>Double run of three<span class="note">e.g. 3-4-5-5: two runs of three and a pair.</span></td><td class="v">8</td></tr>
          <tr><td>Double run of four<span class="note">e.g. 3-4-5-6-6: two runs of four and a pair.</span></td><td class="v">10</td></tr>
          <tr><td>Triple run<span class="note">e.g. 3-4-5-5-5: three runs of three and three of a kind.</span></td><td class="v">15</td></tr>
          <tr><td>Double double run<span class="note">e.g. 3-3-4-5-5: four runs of three and two pairs.</span></td><td class="v">16</td></tr>
        </tbody>
      </table>
      <p>Fifteens are counted on top of all of these.</p>

      <h2 id="deal">The deal</h2>
      <ul>
        <li>Deal six cards each. Both players look, then discard two face down to the dealer's crib, leaving four cards in each hand and four in the crib.</li>
        <li>The non-dealer cuts the deck and the dealer turns the top card face up — the <strong>cut card</strong>. If it's a Jack, the dealer pegs 2 for His Heels.</li>
        <li>The crib stays face down until the show. Nobody looks at it, the dealer included. The deal alternates every hand.</li>
      </ul>
      <p><strong>Three players:</strong> five cards each, plus one card dealt straight from the deck into the crib; everyone discards one. <strong>Four players:</strong> five cards each, everyone discards one, and partners sitting opposite peg a single shared score.</p>

      <h2 id="play">The play (pegging)</h2>
      <ul>
        <li>The non-dealer plays first, then you alternate, laying one card face up and calling the running total out loud. Nobody may take the total past 31.</li>
        <li>Combinations come from the cards on the table, not just your own: lay a 7 on their 8 for fifteen-two, or match the card just played for a pair.</li>
        <li>A run doesn't have to be played in order — 4, then 6, then 5 completes 4-5-6 — but it can't span a pair: play 2-3-3-4 and only the pair scores.</li>
        <li>If you can't play without going over 31, say <strong>“go.”</strong> The other player keeps playing if they can. When neither can, whoever laid the last card pegs 1 — or 2 for hitting exactly 31, never both.</li>
        <li>The count then resets to zero and play continues. Nothing played before a reset can pair or run with anything after it.</li>
      </ul>
      <div class="example">
        <h3>Example: pegging</h3>
        <ol>
          <li>You lead {B("5♠")} — count 5.</li>
          <li>They play {R("K♥")} — count 15, <strong>fifteen for 2</strong>.</li>
          <li>You play {R("8♦")} — count 23.</li>
          <li>They play {B("8♣")} — count 31, <strong>pair for 2 and 31 for 2</strong>.</li>
          <li>The count resets. You lead {R("8♥")} — no pair, because the other 8s came before the reset.</li>
        </ol>
      </div>

      <h2 id="show">The show: counting a hand</h2>
      <ul>
        <li>The non-dealer counts first, then the dealer, then the dealer's crib — turned face up for the first time. Order matters near the end: the non-dealer can win before the dealer counts.</li>
        <li>Every hand counts the cut card as a fifth card, and so does the crib.</li>
        <li>By convention, count fifteens first, then pairs, then runs, then flush and His Nobs — it makes a missed point easy to catch.</li>
      </ul>
      <div class="example">
        <h3>Example: 10 points</h3>
        <p>Hand {B("5♠")} {R("5♥")} {R("K♦")} {B("2♣")}, cut {B("Q♣")}.</p>
        <p>Each 5 makes fifteen with the King and again with the Queen: four fifteens for 8. The two 5s pair for 2. Total: <strong>10</strong>.</p>
      </div>
      <div class="example">
        <h3>Example: a double run for 8</h3>
        <p>Hand {B("3♠")} {R("4♥")} {R("5♦")} {B("9♣")}, cut {B("5♣")}.</p>
        <p>The cut makes a second run: 3-4-5 with either five is two runs of three (6), and the two fives pair (2). No fifteens. Total: <strong>8</strong>.</p>
      </div>
      <h3>The best possible hand: 29</h3>
      <p>Three 5s and a Jack in hand, with the fourth 5 cut in the Jack's suit. Eight fifteens (16), four of a kind (12), and His Nobs (1). No hand can score 19, 25, 26 or 27 — which is why players say “nineteen” for a hand worth nothing.</p>

      <h2 id="winning">Winning</h2>
      <p>First to 121 wins, the instant they get there — mid-play or mid-count, with no finishing the hand. There's no landing on it exactly and no going bust.</p>
      <h3>Common variants</h3>
      <ul>
        <li><strong>Muggins:</strong> if a player undercounts, an opponent can call it and take the missed points.</li>
        <li><strong>Skunk:</strong> beat someone who hasn't reached 91 and it counts as two games; under 61 is a double skunk.</li>
        <li><strong>Short game:</strong> play to 61, once around the board.</li>
      </ul>
''' + callout("No board? No problem.",
  "Tallero is the board: peg points as they land in the play, add your hand totals in the show, and it marks whose crib it is.") + '''
    </div>
  </div>
</section>
''' + sheet("Cribbage score sheet", "No board handy? Write each hand's points and the running total, first to 121.", "+,Total", 20, 2, 4, 2)

page("/rules/cribbage/", "Cribbage Rules & How to Count a Hand — Tallero",
     "How to play cribbage: the deal, pegging, counting fifteens, pairs, runs, flushes and His Nobs, worked hand examples, the 29 hand, and a printable score sheet.",
     [("Game rules", "/rules/"), ("Cribbage", "/rules/cribbage/")], crib)

# ------------------------------------------------------------------ PHASE 10
PH = ["2 sets of 3", "1 set of 3 + 1 run of 4", "1 set of 4 + 1 run of 4", "1 run of 7", "1 run of 8",
      "1 run of 9", "2 sets of 4", "7 cards of one color", "1 set of 5 + 1 set of 2", "1 set of 5 + 1 set of 3"]
rows = "\n".join(f'          <tr><td>Phase {i+1}</td><td class="v">{p}</td></tr>' for i, p in enumerate(PH))
p10 = hero("Phase 10", "phase10", "oklch(0.928 0.045 255)", "Phase 10 rules and phases",
  "All ten phases, how a turn works, Wilds and Skips, and how scoring breaks a tie — plus a printable score sheet.") + f'''
<section class="section section--tight">
  <div class="wrap">
    <div class="prose">
      <ul class="toc">
        <li><a href="#phases">The 10 phases</a></li>
        <li><a href="#turn">A turn</a></li>
        <li><a href="#cards">Wilds &amp; Skips</a></li>
        <li><a href="#scoring">Scoring</a></li>
        <li><a href="#score-sheet">Score sheet</a></li>
      </ul>

      <p class="gist">Work through ten phases in order, each a specific combination you have to collect and lay down. Complete your phase in a hand and you move on; fail and you're stuck repeating it while everyone else advances. First player to finish Phase 10 wins — points only break a tie.</p>

      <h2 id="phases">The 10 phases</h2>
      <table class="score-table">
        <thead><tr><th>Phase</th><th>You need</th></tr></thead>
        <tbody>
{rows}
        </tbody>
      </table>
      <p>A <strong>set</strong> is cards of the same number, any colors. A <strong>run</strong> is consecutive numbers, any colors — 4-5-6-7 in four different colors is a legal run of 4. Phase 8 is the only phase that cares about color: seven cards of one color, in any order.</p>

      <h2>The deck and the deal</h2>
      <ul>
        <li>The deck has 108 cards: 1 to 12 in four colors, twice over, plus eight Wilds and four Skips.</li>
        <li>Deal ten cards each. The rest is the draw pile, with its top card turned face up to start the discard pile.</li>
      </ul>

      <h2 id="turn">Taking a turn</h2>
      <ul>
        <li><strong>Draw</strong> one card, from the draw pile or the top of the discard pile.</li>
        <li><strong>Lay down</strong> your phase if you hold all of it. Where a phase wants a set and a run, holding the set alone lays nothing.</li>
        <li><strong>Hit</strong>: once your phase is down, add cards to any phase on the table — yours or anyone else's. That's the only thing spare cards can do; you can never start an extra set or run.</li>
        <li><strong>Discard</strong> one card to end your turn.</li>
      </ul>
      <p>The first player to get rid of every card ends the hand. Everyone who completed their phase that hand moves on to the next one, whether or not they went out.</p>

      <h2 id="cards">Wilds and Skips</h2>
      <ul>
        <li>A <strong>Wild</strong> stands in for any number or color. Use as many as you like in a phase, as long as there's at least one real numbered card in it. Once played, a Wild stays put for the rest of the hand.</li>
        <li>A <strong>Skip</strong> is played as your discard, in front of any player you choose: they lose their next turn. A Skip can't be used in a phase, can't be picked up from the discard pile, and can't be played on someone who already has one waiting.</li>
      </ul>

      <h2 id="scoring">Scoring</h2>
      <p>When a hand ends, everyone still holding cards adds up the penalty points below. The player who went out scores nothing.</p>
      <table class="score-table">
        <thead><tr><th>Card</th><th>Points</th></tr></thead>
        <tbody>
          <tr><td>1 – 9</td><td class="v">5</td></tr>
          <tr><td>10 – 12</td><td class="v">10</td></tr>
          <tr><td>Skip</td><td class="v">15</td></tr>
          <tr><td>Wild</td><td class="v">25</td></tr>
        </tbody>
      </table>
      <p>Points are penalties, not a prize, and they only matter at the very end: if two or more players complete Phase 10 in the same hand, the lowest total wins.</p>

      <h2>Quick answers</h2>
      <h3>Do runs have to be the same color?</h3>
      <p>No. Runs and sets ignore color entirely. Only Phase 8 asks for one color.</p>
      <h3>Can you hit before laying down your own phase?</h3>
      <p>No. You can only add to phases on the table once your own phase for that hand is down.</p>
      <h3>Can you complete more than one phase in a hand?</h3>
      <p>No. Lay down one phase per hand, then use leftover cards to hit. The next phase waits for the next hand.</p>
''' + callout("Keep track of who's on which phase.",
  "Tallero tracks every player's phase and penalty points, picks up the zero-point player automatically, and settles the tie-break for you.") + '''
      <p class="small" style="margin-top:18px;color:var(--txt-3)">Phase&nbsp;10® is a trademark of its owner. Tallero is independent and not affiliated with or endorsed by the maker of Phase&nbsp;10.</p>
    </div>
  </div>
</section>
''' + sheet("Phase 10 score sheet", "Track each player's phase and running penalty points, hand by hand.", "Phase,Points", 16, 2, 6, 4)

page("/rules/phase-10/", "Phase 10 Rules & List of Phases — Tallero",
     "How to play Phase 10: the list of all 10 phases, sets and runs, how a turn works, Wilds and Skips, card point values and scoring, and a printable score sheet.",
     [("Game rules", "/rules/"), ("Phase 10", "/rules/phase-10/")], p10)

# ------------------------------------------------------------------ YAHTZEE
def dice(s):
    return '<span class="dice">' + "".join(f'<span class="pc">{d}</span>' for d in s) + '</span>'

yz = hero("Yahtzee", "yahtzee", "oklch(0.928 0.045 293)", "Yahtzee rules and scoring",
  "Every box on the scorecard, the 63-point upper bonus, bonus Yahtzees and the Joker rules — plus a printable scorecard.") + f'''
<section class="section section--tight">
  <div class="wrap">
    <div class="prose">
      <ul class="toc">
        <li><a href="#turn">A turn</a></li>
        <li><a href="#upper">Upper section</a></li>
        <li><a href="#lower">Lower section</a></li>
        <li><a href="#bonus">Bonus Yahtzees</a></li>
        <li><a href="#score-sheet">Scorecard</a></li>
      </ul>

      <p class="gist">Roll five dice up to three times a turn, keeping the dice you want and re-rolling the rest. Every turn ends by writing a score into one of thirteen boxes — and once a box is used, it's gone. Thirteen turns each, and the highest total wins.</p>

      <h2 id="turn">Taking a turn</h2>
      <ul>
        <li>Roll all five dice. Set aside any you want to keep, then re-roll the others — up to two more times. You can stop after any roll.</li>
        <li>You can change your mind between rolls: a die you kept after the first roll can go back in for the third.</li>
        <li>After your last roll you <strong>must</strong> fill one open box on your scorecard. If nothing fits, you scratch a box by writing 0 in it.</li>
      </ul>
      <div class="example">
        <h3>Example turn</h3>
        <p>You roll {dice("23356")}. Keep the two 3s and re-roll three dice: {dice("33416")}. Keep the three 3s, re-roll the 4 and the 1: {dice("33365")}. Score it as 3 of a Kind for 20 (the sum of all five dice), or put 9 in Threes and work toward the upper bonus.</p>
      </div>

      <h2 id="upper">Upper section</h2>
      <table class="score-table">
        <thead><tr><th>Box</th><th>Score</th></tr></thead>
        <tbody>
          <tr><td>Aces</td><td class="v">Sum of 1s</td></tr>
          <tr><td>Twos</td><td class="v">Sum of 2s</td></tr>
          <tr><td>Threes</td><td class="v">Sum of 3s</td></tr>
          <tr><td>Fours</td><td class="v">Sum of 4s</td></tr>
          <tr><td>Fives</td><td class="v">Sum of 5s</td></tr>
          <tr><td>Sixes</td><td class="v">Sum of 6s</td></tr>
          <tr><td>Upper bonus<span class="note">If the six upper boxes total 63 or more.</span></td><td class="v">+35</td></tr>
        </tbody>
      </table>
      <p>63 is exactly three of each number (3 + 6 + 9 + 12 + 15 + 18), so the bonus is a steady target: get three of a face in every upper box, or bank a four of a kind in one to make up for a pair in another.</p>

      <h2 id="lower">Lower section</h2>
      <table class="score-table">
        <thead><tr><th>Box</th><th>Score</th></tr></thead>
        <tbody>
          <tr><td>3 of a Kind<span class="note">At least three dice the same.</span></td><td class="v">Sum of all dice</td></tr>
          <tr><td>4 of a Kind<span class="note">At least four dice the same.</span></td><td class="v">Sum of all dice</td></tr>
          <tr><td>Full House <span class="dice">{"".join(f'<span class="pc">{d}</span>' for d in "222")} &nbsp;{"".join(f'<span class="pc">{d}</span>' for d in "55")}</span><span class="note">Three of one number and two of another.</span></td><td class="v">25</td></tr>
          <tr><td>Small Straight <span class="dice">{"".join(f'<span class="pc">{d}</span>' for d in "2345")}</span><span class="note">Four in a row: 1-2-3-4, 2-3-4-5 or 3-4-5-6.</span></td><td class="v">30</td></tr>
          <tr><td>Large Straight <span class="dice">{"".join(f'<span class="pc">{d}</span>' for d in "12345")}</span><span class="note">Five in a row: 1-2-3-4-5 or 2-3-4-5-6.</span></td><td class="v">40</td></tr>
          <tr><td>Yahtzee <span class="dice">{"".join(f'<span class="pc">{d}</span>' for d in "66666")}</span><span class="note">Five of a kind.</span></td><td class="v">50</td></tr>
          <tr><td>Chance<span class="note">Anything at all — your safety net.</span></td><td class="v">Sum of all dice</td></tr>
        </tbody>
      </table>

      <h2 id="bonus">Bonus Yahtzees and the Joker rules</h2>
      <p>If you've already scored 50 in the Yahtzee box, every further Yahtzee earns a <strong>+100 bonus</strong> — and you still have to place the roll somewhere on your card:</p>
      <ul>
        <li>First choice is forced: if the upper box for that number is open, it goes there — five 4s score 20 in Fours.</li>
        <li>If that box is taken, the roll is a <strong>Joker</strong> for any open lower box, and the fixed boxes pay full value however the dice look: Full House 25, Small Straight 30, Large Straight 40. 3 of a Kind, 4 of a Kind and Chance score the five dice.</li>
        <li>If every lower box is gone too, you must write a 0 in an open upper box.</li>
        <li>Scratched your Yahtzee box for 0 earlier? A later Yahtzee earns no bonus, but the same placement rules still apply.</li>
      </ul>

      <h2>Winning</h2>
      <p>After thirteen turns every box is full. Add the upper section and its bonus, the lower section, and any Yahtzee bonuses — highest grand total wins.</p>

      <h2>Quick answers</h2>
      <h3>Can a Yahtzee count as a Full House?</h3>
      <p>Only as a Joker. If your Yahtzee box is filled and the matching upper box is taken, five of a kind can go in Full House for 25 — or either straight.</p>
      <h3>Does a Large Straight also count as a Small Straight?</h3>
      <p>Yes. 1-2-3-4-5 contains four in a row, so it can score 30 in Small Straight if that's the box you'd rather fill.</p>
      <h3>What's the highest possible score?</h3>
      <p>1,575 — thirteen Yahtzees in a row, with every bonus and the Joker rules working in your favour. You won't see it.</p>
''' + callout("Skip the pencil.",
  "Tallero's Yahtzee card fills in as you go, adds the 35-point bonus the moment you reach 63, and tracks every player's card side by side.") + '''
      <p class="small" style="margin-top:18px;color:var(--txt-3)">Yahtzee® is a trademark of its owner. Tallero is independent and not affiliated with or endorsed by the maker of Yahtzee.</p>
    </div>
  </div>
</section>
''' + sheet("Yahtzee scorecard", "One column per player, every box on the card.", "Score", 0, 1, 6, 4,
            labels=["Aces", "Twos", "Threes", "Fours", "Fives", "Sixes", "*Upper total", "*Bonus (63+ = 35)",
                    "3 of a Kind", "4 of a Kind", "Full House (25)", "Sm. Straight (30)", "Lg. Straight (40)",
                    "Yahtzee (50)", "Chance", "Yahtzee bonus (100 each)", "*Lower total", "*Grand total"])

page("/rules/yahtzee/", "Yahtzee Rules & Scoring — Bonus, Joker Rules & Scorecard — Tallero",
     "How to play Yahtzee: every scorecard box, the 63-point upper bonus, bonus Yahtzees and the Joker rules, and a printable Yahtzee scorecard.",
     [("Game rules", "/rules/"), ("Yahtzee", "/rules/yahtzee/")], yz)

# ------------------------------------------------------------------ SPADES
sp = hero("Spades", "spades", "oklch(0.928 0.045 194)", "Spades rules and scoring",
  "Bidding, how tricks are won, how bids, bags and nil are scored, and how to play with two, three or six — plus a printable score sheet.") + f'''
<section class="section section--tight">
  <div class="wrap">
    <div class="prose">
      <ul class="toc">
        <li><a href="#bidding">Bidding</a></li>
        <li><a href="#tricks">Playing tricks</a></li>
        <li><a href="#scoring">Scoring</a></li>
        <li><a href="#nil">Nil</a></li>
        <li><a href="#counts">Other player counts</a></li>
        <li><a href="#score-sheet">Score sheet</a></li>
      </ul>

      <p class="gist">Four players in two teams of two, partners sitting opposite. Each hand, everyone bids how many tricks they'll take, and each team tries to take at least its combined bid. Make it and you score the bid × 10, plus 1 for every extra trick. Spades are always trump. First team past 500 wins.</p>

      <h2 id="bidding">Dealing and bidding</h2>
      <ul>
        <li>Deal the whole deck one card at a time, clockwise: 13 cards each, so every hand is 13 tricks.</li>
        <li>Starting left of the dealer and going once round, each player looks at their cards and bids the number of tricks they expect to win. You don't have to bid higher than the player before you.</li>
        <li>Partners' bids are added together into the team's contract. <strong>You don't need to hit your own number — only the team's total.</strong></li>
        <li>Bids are called aloud in turn, so a partner who bids second knows the first bid. Partners can't discuss their hands.</li>
      </ul>
      <div class="example">
        <h3>Example: making the contract</h3>
        <p>Ann bids 4 and takes 2. Ben bids 3 and takes 6. Neither hit their own number, but together they bid 7 and took 8 — contract made. The team scores <strong>71</strong>: 70 for the bid, plus 1 for the extra trick.</p>
      </div>

      <h2 id="tricks">Playing the tricks</h2>
      <ul>
        <li>The player left of the dealer leads the first trick; after that, whoever won the last trick leads.</li>
        <li>You must follow the suit led if you can. If you can't, you may play anything — including a spade.</li>
        <li>The highest spade takes the trick. If no spade was played, the highest card of the suit led takes it.</li>
        <li>Spades can't be led until they're <strong>broken</strong> — until someone has played a spade on another suit because they couldn't follow. The exception: a player holding nothing but spades.</li>
        <li>You can't trump a suit you're able to follow, even if someone before you already has.</li>
      </ul>
      <div class="example">
        <h3>Example trick</h3>
        <p>Clubs led: {B("A♣")} {B("7♣")} {B("2♠")} {B("K♣")}. The <strong>2♠ wins</strong> — the lowest spade beats the highest club. It could only be played by someone with no clubs left.</p>
      </div>

      <h2 id="scoring">How scoring works</h2>
      <table class="score-table">
        <thead><tr><th>Result</th><th>Points</th></tr></thead>
        <tbody>
          <tr><td>Make your contract<span class="note">Take at least the team's combined bid.</span></td><td class="v">bid × 10</td></tr>
          <tr><td>Each extra trick (a “bag”)</td><td class="v">+1</td></tr>
          <tr><td>Miss your contract<span class="note">Bicycle's rules score 0; Pagat's deduct the bid, −bid × 10. Agree which before you start.</span></td><td class="v">0 or −bid × 10</td></tr>
          <tr><td>Nil made<span class="note">Bid nil and take no tricks at all.</span></td><td class="v">+100</td></tr>
          <tr><td>Nil broken<span class="note">Take even one trick.</span></td><td class="v">−100</td></tr>
          <tr><td>Blind nil<span class="note">Declared before looking at your cards.</span></td><td class="v">±200</td></tr>
        </tbody>
      </table>
      <p>The hand is scored against your bid, not against the other team: 9 tricks on a bid of 10 scores nothing (or costs you 100), while 3 on a bid of 3 scores 30.</p>
      <h3>Bags and sandbagging</h3>
      <p>Extra tricks are worth only 1 point each, but at many tables they also pile up (Pagat treats this as standard; Bicycle lists it as something “some games” do): every time a team's running total of bags reaches 10, it loses 100 points. That's what stops a team from bidding low and hoovering up tricks.</p>

      <h2 id="nil">Bidding nil</h2>
      <p>A nil bid says you'll take no tricks at all. It's scored on its own — even in a partnership — and isn't added to the team's contract: your partner has to make their own bid alone. Any trick the nil bidder does take still counts as a bag for the team, but can't help fill the partner's bid.</p>
      <div class="example">
        <h3>Example: a broken nil</h3>
        <p>Cass bids nil and takes a trick: <strong>−100</strong>. Dee bids 4 and takes 4: the contract is made for <strong>40</strong>, and Cass's trick adds a bag, <strong>+1</strong>. The team still finishes the hand on <strong>−59</strong>.</p>
      </div>
      <p>Blind nil is the same bid made before looking at your hand, for double. Usually it's only allowed to a team that's 100 or more behind, and the bidder then swaps two cards face down with their partner.</p>

      <h2>How it ends</h2>
      <p>The first team past 500 wins. If both get there in the same hand, the higher total takes it. 200 or 300 makes a shorter game.</p>

      <h2 id="counts">Playing with other counts</h2>
      <ul>
        <li><strong>Two players:</strong> don't deal. Take turns drawing: look at the top card and either keep it and discard the next face down, or discard it and keep the next. Carry on until you each hold 13.</li>
        <li><strong>Three players:</strong> deal 17 each and set the last card aside, so a hand is 17 tricks. Everyone plays for themselves.</li>
        <li><strong>Six players:</strong> shuffle two decks together with two low cards removed. Traditionally three teams of two.</li>
        <li><strong>Cutthroat:</strong> four players with no partners, each bidding and scoring alone.</li>
      </ul>
''' + callout("Bids, bags and nils, added up for you.",
  "Lock in bids, enter tricks, and Tallero scores the contract, the bags and any nil — and checks the tricks add up to 13.") + '''
    </div>
  </div>
</section>
''' + sheet("Spades score sheet", "Bid, tricks taken and running score for each team, hand by hand.", "Bid,Took,Score", 16, 2, 4, 2, unit="teams")

page("/rules/spades/", "Spades Rules & Scoring — Bids, Bags & Nil — Tallero",
     "How to play Spades: bidding, trump and breaking spades, how bids, bags, sandbagging and nil are scored, rules for 2, 3 and 6 players, and a printable score sheet.",
     [("Game rules", "/rules/"), ("Spades", "/rules/spades/")], sp)

# ------------------------------------------------------------------ HEARTS
ht = hero("Hearts", "hearts", "oklch(0.928 0.045 357)", "Hearts rules and scoring",
  "Passing, leading, breaking hearts, the Queen of Spades and shooting the moon — plus a printable score sheet.") + f'''
<section class="section section--tight">
  <div class="wrap">
    <div class="prose">
      <ul class="toc">
        <li><a href="#passing">Passing</a></li>
        <li><a href="#play">Playing a hand</a></li>
        <li><a href="#scoring">Scoring</a></li>
        <li><a href="#moon">Shooting the moon</a></li>
        <li><a href="#counts">Other player counts</a></li>
        <li><a href="#score-sheet">Score sheet</a></li>
      </ul>

      <p class="gist">Hearts is a trick-taking game where you want to <em>lose</em> tricks. Every heart you take is a point against you, and the Queen of Spades is 13. Fewest points wins, and the game ends the moment anyone reaches 100. Take every heart and the Queen yourself, though, and it flips — everyone else takes the points instead.</p>

      <h2 id="passing">Dealing and passing</h2>
      <ul>
        <li>With four players, deal the whole deck: 13 cards each.</li>
        <li>After looking at your cards, pass three of them face down to another player. The direction rotates each hand: <strong>left, right, across, then no pass</strong> — and repeat.</li>
      </ul>

      <h2 id="play">Playing a hand</h2>
      <ul>
        <li>Whoever holds the {B("2♣")} leads it to the first trick.</li>
        <li>You must follow the suit led if you can. If you can't, you may play any card.</li>
        <li>On the first trick, nobody may play a heart or the Queen of Spades — unless their hand is nothing but point cards.</li>
        <li>The highest card of the suit led takes the trick, and the winner leads the next one.</li>
        <li>Hearts can't be led until they're <strong>broken</strong> — until a heart has been discarded on another suit — unless hearts are all you have left. The Queen of Spades is just a spade for leading purposes: once the first trick is done, it can be led like any other spade.</li>
        <li>Tricks you take go face down in your own pile, and nobody can look back through them.</li>
      </ul>
      <div class="example">
        <h3>Example trick</h3>
        <p>Clubs led: {B("4♣")} {B("A♠")} {B("Q♣")} {R("9♦")}. The <strong>Q♣ wins</strong> — the A♠ is higher, but it's the wrong suit, and there's no trump in Hearts.</p>
      </div>

      <h2 id="scoring">How scoring works</h2>
      <p>Tricks are worth nothing in themselves — only the cards in them count. Each hand adds up to 26.</p>
      <table class="score-table">
        <thead><tr><th>Card</th><th>Points</th></tr></thead>
        <tbody>
          <tr><td>Each heart {R("♥")}</td><td class="v">1</td></tr>
          <tr><td>Queen of Spades {B("Q♠")}</td><td class="v">13</td></tr>
          <tr><td>Shoot the moon<span class="note">Take all 13 hearts and the Q♠ in one hand.</span></td><td class="v">+26 to others</td></tr>
        </tbody>
      </table>

      <h2 id="moon">Shooting the moon</h2>
      <p>If one player takes every heart and the Queen of Spades in a single hand, they score 0 and every other player takes 26. It's a gamble: miss a single heart and you're stuck with most of the 26 yourself.</p>
      <p>Some tables score it the other way — the shooter takes −26 and nobody else scores — or let the shooter choose, which matters when +26 would push someone else to 100.</p>

      <h2>How it ends</h2>
      <p>The game ends the moment anyone reaches 100 at the end of a hand. The lowest score wins, and the player who crossed 100 finishes last.</p>

      <h2>Common variants</h2>
      <ul>
        <li><strong>Omnibus:</strong> the Jack of Diamonds {R("J♦")} is worth −10 to whoever takes it, so a hand totals 16. It isn't part of shooting the moon.</li>
        <li><strong>Shorter game:</strong> some groups play to 50 instead of 100.</li>
      </ul>

      <h2 id="counts">Playing with other counts</h2>
      <p>The deck has to divide evenly, so with other player counts a few low cards come out before dealing:</p>
      <table class="score-table">
        <tbody>
          <tr><td>Three players</td><td class="v">17 cards each</td></tr>
          <tr><td>Four players</td><td class="v">13 cards each</td></tr>
          <tr><td>Five players</td><td class="v">10 cards each</td></tr>
          <tr><td>Six players</td><td class="v">8 cards each</td></tr>
        </tbody>
      </table>
      <p>With three players the 2♦ usually comes out, and with five the 2♣ (so the 3♣ leads). There's no standard six-player deal; dropping four low cards to deal 8 each is one way to do it. Agree which cards come out and how passing rotates before you start.</p>

      <h2>Quick answers</h2>
      <h3>Can you lead the Queen of Spades before hearts are broken?</h3>
      <p>Yes. Only hearts need breaking, and the Queen is a spade, so it can be led on any trick after the first. Rule sets differ on one point: Bicycle's printed rules also count the Queen, discarded on another suit, as breaking hearts; Pagat's standard rules count only a heart.</p>
      <h3>Can you play a heart on the first trick?</h3>
      <p>No — not even if you're out of clubs. The only exception is a hand of nothing but hearts and the Queen.</p>
      <h3>Do you have to pass every hand?</h3>
      <p>With four players, every fourth hand is a “hold” hand with no passing at all.</p>
''' + callout("Moon detection included.",
  "Enter each hand's points and Tallero keeps the totals, spots a moon automatically, and ends the game the moment someone hits 100.") + '''
    </div>
  </div>
</section>
''' + sheet("Hearts score sheet", "Points taken each hand, and the running total. First to 100 ends it.", "+,Total", 20, 3, 6, 4)

page("/rules/hearts/", "Hearts Rules & Scoring — Shooting the Moon — Tallero",
     "How to play Hearts: passing, leading the 2 of clubs, breaking hearts, scoring the Queen of Spades, shooting the moon, rules for 3 to 6 players, and a printable score sheet.",
     [("Game rules", "/rules/"), ("Hearts", "/rules/hearts/")], ht)

# ------------------------------------------------------------------ EUCHRE
eu = hero("Euchre", "euchre", "oklch(0.928 0.045 150)", "Euchre rules and scoring",
  "The bowers, ordering up, going alone, and how every hand is scored — plus a printable score sheet.") + f'''
<section class="section section--tight">
  <div class="wrap">
    <div class="prose">
      <ul class="toc">
        <li><a href="#trump">Trump &amp; the bowers</a></li>
        <li><a href="#bidding">Bidding</a></li>
        <li><a href="#play">Playing tricks</a></li>
        <li><a href="#scoring">Scoring</a></li>
        <li><a href="#score-sheet">Score sheet</a></li>
      </ul>

      <p class="gist">Euchre is a trick-taking game for two teams of two, partners sitting opposite, played with a 24-card deck of 9s through Aces. Each hand, one team calls trump and becomes the <strong>makers</strong>: they need at least three of the five tricks. Make it and they score; fall short and they're <strong>euchred</strong>, and the defenders score instead. First team to 10 wins.</p>

      <h2 id="trump">Trump and the bowers</h2>
      <p>Once trump is chosen, the two Jacks of that color become the top two trumps:</p>
      <table class="score-table">
        <thead><tr><th>Rank</th><th>Card</th></tr></thead>
        <tbody>
          <tr><td>Right bower<span class="note">The Jack of the trump suit — the highest card in the game.</span></td><td class="v">1st</td></tr>
          <tr><td>Left bower<span class="note">The other Jack of the same color. For this hand it <em>is</em> a trump, not a card of its printed suit.</span></td><td class="v">2nd</td></tr>
          <tr><td>Then the rest of trump<span class="note">Ace, King, Queen, 10, 9.</span></td><td class="v">3rd–7th</td></tr>
        </tbody>
      </table>
      <div class="example">
        <h3>Example: spades are trump</h3>
        <p>{B("J♠")} {B("J♣")} {B("A♠")} {B("K♠")} {B("Q♠")} {B("10♠")} {B("9♠")}</p>
        <p>Both Jacks outrank the Ace. The J♣ counts as a spade for the whole hand, so it can't be played to follow a club lead. The other suits rank normally: A, K, Q, J, 10, 9.</p>
      </div>

      <h2 id="bidding">Dealing and bidding</h2>
      <ul>
        <li>Deal five cards each, in packets of two and three. Turn the next card face up — the <strong>upcard</strong> — and set the last three aside.</li>
        <li><strong>Round one:</strong> starting left of the dealer, each player either passes or <strong>orders up</strong> the upcard's suit as trump. The first to accept ends the bidding, and their team are the makers. The dealer picks up the upcard — even if an opponent ordered it — and discards a card face down.</li>
        <li><strong>Round two:</strong> if everyone passes, turn the upcard down. Going round again, any player may name one of the other three suits as trump. If all four pass again, the hand is thrown in and the deal moves on.</li>
        <li><strong>Going alone:</strong> whoever calls trump may announce they're going alone. Their partner lays their cards face down and sits the hand out.</li>
      </ul>

      <h2 id="play">Playing the tricks</h2>
      <ul>
        <li>The player left of the dealer leads the first trick. After that, whoever won the last trick leads.</li>
        <li>You must follow the suit led if you can — remembering the left bower belongs to trump, not its printed suit. If you can't follow, play anything, including a trump.</li>
        <li>The highest trump takes the trick. If no trump was played, the highest card of the suit led wins.</li>
      </ul>

      <h2 id="scoring">How scoring works</h2>
      <table class="score-table">
        <thead><tr><th>Result</th><th>Points</th></tr></thead>
        <tbody>
          <tr><td>Makers take 3 or 4 tricks</td><td class="v">1</td></tr>
          <tr><td>Makers take all 5 (a march)</td><td class="v">2</td></tr>
          <tr><td>Lone hand takes all 5</td><td class="v">4</td></tr>
          <tr><td>Lone hand takes 3 or 4</td><td class="v">1</td></tr>
          <tr><td>Makers euchred<span class="note">Fewer than three tricks — the defenders score.</span></td><td class="v">2</td></tr>
        </tbody>
      </table>
      <p>Only one team scores each hand. The first team to reach 10 points wins — you don't need to land on it exactly.</p>

      <h2>Common variants</h2>
      <ul>
        <li><strong>Stick the dealer:</strong> no throw-ins. If the first three players pass in round two, the dealer must name a trump suit.</li>
        <li><strong>Defending alone:</strong> some tables let a defender go alone too, and pay 4 if they euchre the makers.</li>
        <li><strong>Cutthroat:</strong> three players, each playing for themselves against the maker.</li>
      </ul>

      <h2>Quick answers</h2>
      <h3>Is the left bower a trump?</h3>
      <p>Yes. For that hand it's the second-highest trump and belongs to the trump suit — it can't be used to follow its printed suit.</p>
      <h3>Does the dealer have to pick up the upcard if an opponent orders it?</h3>
      <p>Yes. Whoever orders it up, the dealer takes the upcard into their hand and discards one.</p>
      <h3>What does “euchred” mean?</h3>
      <p>The team that called trump took fewer than three tricks. The other team scores 2.</p>
''' + callout("One tap per hand.",
  "Tap what happened — a point, a march, a loner or a euchre — on the team that scored, and Tallero keeps the running total to 10.") + '''
    </div>
  </div>
</section>
''' + sheet("Euchre score sheet", "Points each hand and the running total for each team. First to 10.", "+,Total", 20, 2, 2, 2, unit="teams")

page("/rules/euchre/", "Euchre Rules & Scoring — Bowers, Going Alone — Tallero",
     "How to play Euchre: the right and left bowers, ordering up and calling trump, going alone, how every hand is scored, common variants, and a printable score sheet.",
     [("Game rules", "/rules/"), ("Euchre", "/rules/euchre/")], eu)

# ------------------------------------------------------------------ GIN RUMMY
gr = hero("Gin Rummy", "ginrummy", "oklch(0.928 0.045 194)", "Gin Rummy rules and scoring",
  "Sets, runs and deadwood, when you can knock, laying off, and how gin, big gin and undercuts are scored — plus a printable score sheet.") + f'''
<section class="section section--tight">
  <div class="wrap">
    <div class="prose">
      <ul class="toc">
        <li><a href="#melds">Sets &amp; runs</a></li>
        <li><a href="#turn">A turn</a></li>
        <li><a href="#knock">Knocking</a></li>
        <li><a href="#scoring">Scoring</a></li>
        <li><a href="#game">Winning the game</a></li>
        <li><a href="#score-sheet">Score sheet</a></li>
      </ul>

      <p class="gist">A two-player game. Draw and discard until your ten cards are organised into sets and runs, then end the hand by <strong>knocking</strong>. The cards that don't fit — your <strong>deadwood</strong> — must total 10 or less to knock, and the knocker scores the difference between the two hands' deadwood. First to 100 wins.</p>

      <h2 id="melds">Sets, runs and deadwood</h2>
      <ul>
        <li>A <strong>set</strong> is three or four cards of the same rank. A <strong>run</strong> is three or more in sequence, all one suit.</li>
        <li>Each card can be in only one set or run.</li>
        <li>Aces are low: A-2-3 is a run, but Q-K-A and K-A-2 are not.</li>
        <li>Deadwood counts face cards 10, aces 1, and everything else its number.</li>
      </ul>
      <div class="example">
        <h3>Example: a hand that can knock</h3>
        <ul>
          <li>Run: {B("7♣")} {B("8♣")} {B("9♣")}</li>
          <li>Set: {R("4♦")} {R("4♥")} {B("4♠")} {B("4♣")}</li>
          <li>Deadwood: {R("5♥")} {R("3♦")} {B("A♠")}</li>
        </ul>
        <p>Seven cards are in a run and a set. The leftover 5, 3 and ace total <strong>9</strong> — 10 or less, so this hand can knock.</p>
      </div>

      <h2 id="turn">Dealing and taking a turn</h2>
      <ul>
        <li>Deal ten cards each, one at a time. Turn the next card face up to start the discard pile; the rest is the stock.</li>
        <li>The non-dealer may take that first upcard; if they pass, the dealer may. If neither wants it, the non-dealer draws from the stock and play carries on normally.</li>
        <li>Each turn: draw one card — from the stock or the top of the discard pile — then discard one.</li>
        <li>If only two cards are left in the stock and the player who drew the third-from-last discards without knocking, the hand is void and nobody scores.</li>
      </ul>

      <h2 id="knock">Knocking and laying off</h2>
      <ul>
        <li>You may knock on your turn if your deadwood totals 10 or less: draw as usual, then discard <strong>face down</strong>. Spread your hand with sets and runs together and deadwood apart.</li>
        <li>You never have to knock — you can keep playing to cut your deadwood or go for gin.</li>
        <li>The other player then spreads their hand and may <strong>lay off</strong>: add their deadwood cards to the knocker's sets and runs, reducing their own count. They can't lay off onto the knocker's deadwood.</li>
        <li>After a gin, Pagat's rules allow no laying off; Bicycle's still let the opponent lay off.</li>
      </ul>

      <h2 id="scoring">How scoring works</h2>
      <table class="score-table">
        <thead><tr><th>Result</th><th>Score</th></tr></thead>
        <tbody>
          <tr><td>Knock<span class="note">The knocker has less deadwood than the opponent, after laying off.</span></td><td class="v">the difference</td></tr>
          <tr><td>Gin<span class="note">All ten cards in sets and runs. Scores the opponent's deadwood plus a bonus, and can't be undercut.</span></td><td class="v">+20 or +25</td></tr>
          <tr><td>Big Gin<span class="note">All eleven cards — including the one just drawn — in sets and runs, with no discard. A popular extra; not in every rulebook.</span></td><td class="v">+31</td></tr>
          <tr><td>Undercut<span class="note">The opponent's deadwood is equal to or lower than the knocker's. The <em>opponent</em> scores the difference plus a bonus; the knocker scores nothing.</span></td><td class="v">+10 to +25</td></tr>
        </tbody>
      </table>
      <p>Bonus values genuinely differ: Pagat's and Bicycle's rules give 20 for gin and 10 for an undercut, while 25 for both is widely played. Settle it before the first deal.</p>
      <div class="example">
        <h3>Example: an undercut</h3>
        <p>You knock with 8 in deadwood. Your opponent lays off two cards on your run and is left with 6. They've undercut you: they score 8 − 6 = 2, plus the undercut bonus. You score nothing for the hand.</p>
      </div>

      <h2 id="game">Winning the game</h2>
      <p>Hands continue until someone reaches 100. Traditional scoring then adds end-of-game bonuses before totting up:</p>
      <ul>
        <li><strong>Game bonus:</strong> 100 to the winner.</li>
        <li><strong>Line or box bonus:</strong> a bonus for every hand each player won — 20 a hand in Pagat's rules.</li>
        <li><strong>Shutout:</strong> if the loser never scored, Pagat doubles the game bonus to 200; Bicycle adds an extra 100.</li>
      </ul>
      <p>Plenty of tables skip these and simply play first to 100.</p>

      <h2>Quick answers</h2>
      <h3>Can you knock with exactly 10?</h3>
      <p>Yes — 10 or less.</p>
      <h3>What if both hands have the same deadwood?</h3>
      <p>That counts as an undercut: the knocker's opponent wins the hand.</p>
''' + callout("The arithmetic, done.",
  "Pick Knock, Gin, Big Gin or Undercut, enter both players' deadwood, and Tallero adds the difference and the bonus — you'll see the sum before you commit.") + '''
    </div>
  </div>
</section>
''' + sheet("Gin Rummy score sheet", "Each hand's score and the running total. First to 100.", "+,Total", 20, 2, 2, 2)

page("/rules/gin-rummy/", "Gin Rummy Rules & Scoring — Knock, Gin & Undercut — Tallero",
     "How to play Gin Rummy: sets, runs and deadwood, when you can knock, laying off, scoring knocks, gin, big gin and undercuts, end-of-game bonuses, and a printable score sheet.",
     [("Game rules", "/rules/"), ("Gin Rummy", "/rules/gin-rummy/")], gr)

# ------------------------------------------------------------------ MÖLKKY
def pins(rows):
    return '<div class="pins" role="img" aria-label="Starting formation: back row 7, 9, 8; then 5, 11, 12, 6; then 3, 10, 4; front row 1, 2.">' + "".join(
        '<div class="pins__row">' + "".join(f'<span class="pin">{n}</span>' for n in r) + '</div>' for r in rows) + '<div class="pins__line">throwing line, 3.5 m (11.5 ft) away</div></div>'

mk = hero("Mölkky", "molkky", "oklch(0.928 0.045 293)", "Mölkky rules and scoring",
  "How to set up the pins, how a throw scores, the exactly-50 finish and the three-miss rule — plus a printable score sheet.") + f'''
<section class="section section--tight">
  <div class="wrap">
    <div class="prose">
      <ul class="toc">
        <li><a href="#setup">Setting up</a></li>
        <li><a href="#scoring">Scoring</a></li>
        <li><a href="#fifty">Exactly 50</a></li>
        <li><a href="#misses">Three misses</a></li>
        <li><a href="#score-sheet">Score sheet</a></li>
      </ul>

      <p class="gist">A Finnish throwing game. Toss a wooden throwing pin at twelve numbered pins: knock one down and you score its number; knock several down and you score how many fell. Fallen pins are stood up where they land, so the field spreads out all game. First to <strong>exactly 50</strong> wins — go over and you drop back to 25.</p>

      <h2 id="setup">Setting up</h2>
      <p>Stand the twelve pins in a tight block, 1 and 2 nearest the thrower, 3.5 metres (11.5 ft) from the throwing line:</p>
      {pins([[7, 9, 8], [5, 11, 12, 6], [3, 10, 4], [1, 2]])}
      <ul>
        <li>Players take turns throwing from behind the line. Any throwing style is allowed.</li>
        <li>After each throw, fallen pins are stood back up exactly where they landed, number facing the thrower.</li>
      </ul>

      <h2 id="scoring">How scoring works</h2>
      <table class="score-table">
        <thead><tr><th>Throw</th><th>Score</th></tr></thead>
        <tbody>
          <tr><td>One pin knocked down<span class="note">Knock down the 12 alone for the biggest single throw.</span></td><td class="v">pin's number</td></tr>
          <tr><td>Two or more pins down<span class="note">Five pins down scores 5, whatever their numbers.</span></td><td class="v">number of pins</td></tr>
          <tr><td>Miss<span class="note">Three misses in a row and you're out.</span></td><td class="v">0</td></tr>
        </tbody>
      </table>
      <p>A pin only counts if it's fully on the ground. One leaning on another pin, on the throwing pin, or on a natural feature like a root doesn't count; one resting against something artificial, like a curb, does.</p>

      <h2 id="fifty">Finishing on exactly 50</h2>
      <p>To win you need <strong>exactly 50</strong>. Overshoot and your score drops back to 25. Near the end, that makes the right single pin worth far more than a big scatter.</p>
      <div class="example">
        <h3>Example</h3>
        <p>You're on 44 and need 6. Knocking down the 6 alone wins. Knocking down six pins at once also scores 6 and wins. Knocking down the 9 takes you to 53 — back to 25.</p>
      </div>

      <h2 id="misses">Three misses and you're out</h2>
      <p>Miss every pin on three of your turns in a row and you're eliminated. Scoring anything resets the count. If everyone else is eliminated, the last player standing wins.</p>

''' + callout("Busts and eliminations, handled.",
  "Enter each throw and Tallero drops an overshoot back to 25, counts consecutive misses, and knocks out anyone who misses three in a row.") + '''
      <p class="small" style="margin-top:18px;color:var(--txt-3)">Mölkky® is a trademark of its owner. Tallero is independent and not affiliated with or endorsed by the maker of Mölkky.</p>
    </div>
  </div>
</section>
''' + sheet("Mölkky score sheet", "Each throw's points and the running total. Mark a miss with an X — three in a row and you're out.", "+,Total", 25, 2, 8, 4)

page("/rules/molkky/", "Mölkky Rules & Scoring — Exactly 50 — Tallero",
     "How to play Mölkky: the starting pin formation, how one pin and several pins score, finishing on exactly 50, falling back to 25, the three-miss rule, and a printable score sheet.",
     [("Game rules", "/rules/"), ("Mölkky", "/rules/molkky/")], mk)

# ------------------------------------------------------------------ HUB
def card(key, tile, name, blurb, path):
    return f'''      <a class="rules-card" href="{path}">
        <div class="tile" style="background:{tile}"><img src="/assets/games/{key}.svg" alt=""/></div>
        <h2>{name}</h2>
        <p>{blurb}</p>
        <span class="link">Read the rules →</span>
      </a>'''

hub = '''
<!-- ============ PAGE HERO ============ -->
<section class="page-hero">
  <div class="wrap">
    <span class="eyebrow">Game rules</span>
    <h1>How to play, and how to score.</h1>
    <p>Rules and scoring for the games Tallero keeps score for, with printable score sheets. More games on the way.</p>
  </div>
</section>

<section class="section section--tight">
  <div class="wrap">
    <div class="rules-grid">
''' + "\n".join([
    card("farkle", "oklch(0.928 0.045 357)", "Farkle", "The full scoring chart, hot dice, the final lap, and the variants tables argue about.", "/rules/farkle/"),
    card("cribbage", "oklch(0.928 0.045 78)", "Cribbage", "The deal, pegging, and how to count a hand — with worked examples and the 29 hand.", "/rules/cribbage/"),
    card("phase10", "oklch(0.928 0.045 255)", "Phase 10", "All ten phases, Wilds and Skips, and how penalty points break a tie.", "/rules/phase-10/"),
    card("yahtzee", "oklch(0.928 0.045 293)", "Yahtzee", "Every box on the card, the 63-point bonus, bonus Yahtzees and the Joker rules.", "/rules/yahtzee/"),
    card("spades", "oklch(0.928 0.045 194)", "Spades", "Bidding, breaking spades, and how bids, bags and nil are scored.", "/rules/spades/"),
    card("hearts", "oklch(0.928 0.045 357)", "Hearts", "Passing, the Queen of Spades, and how shooting the moon works.", "/rules/hearts/"),
    card("euchre", "oklch(0.928 0.045 150)", "Euchre", "The bowers, ordering up, going alone, and how every hand scores.", "/rules/euchre/"),
    card("ginrummy", "oklch(0.928 0.045 194)", "Gin Rummy", "Deadwood, knocking, laying off, and scoring gin, big gin and undercuts.", "/rules/gin-rummy/"),
    card("molkky", "oklch(0.928 0.045 293)", "Mölkky", "The pin setup, how throws score, exactly 50, and the three-miss rule.", "/rules/molkky/"),
]) + '''
    </div>
  </div>
</section>
'''
page("/rules/", "Game Rules & Scoring — Tallero",
     "Rules and scoring guides for Farkle, Cribbage, Phase 10, Yahtzee, Spades, Hearts, Euchre, Gin Rummy and Mölkky, with printable score sheets — from Tallero, the score-keeper for game night.",
     [("Game rules", "/rules/")], hub)
