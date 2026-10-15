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

# ------------------------------------------------------------------ CORNHOLE
ch = hero("Cornhole", "cornhole", "oklch(0.928 0.045 150)", "Cornhole rules and scoring",
  "How cancellation scoring works, what counts as a dead bag, board setup and distances, and how a game is won — plus a printable score sheet.") + f'''
<section class="section section--tight">
  <div class="wrap">
    <div class="prose">
      <ul class="toc">
        <li><a href="#scoring">Scoring</a></li>
        <li><a href="#example">Example frame</a></li>
        <li><a href="#setup">Setup</a></li>
        <li><a href="#play">Playing a frame</a></li>
        <li><a href="#winning">Winning</a></li>
        <li><a href="#score-sheet">Score sheet</a></li>
      </ul>

      <p class="gist">Two sides take turns pitching bags at a board 27 feet away — four bags each, eight to a <strong>frame</strong>. A bag through the hole is 3, a bag on the board is 1, and only the side with more points in a frame scores: they get the <strong>difference</strong>. First to 21 wins.</p>

      <h2 id="scoring">How scoring works</h2>
      <table class="score-table">
        <thead><tr><th>Bag</th><th>Points</th></tr></thead>
        <tbody>
          <tr><td>In the hole<span class="note">Goes through at any point in the frame — including being knocked in by another bag.</span></td><td class="v">3</td></tr>
          <tr><td>On the board<span class="note">Still resting on the board when the frame ends.</span></td><td class="v">1</td></tr>
          <tr><td>Dead bag<span class="note">Touched the ground before landing on the board, is touching both board and ground, or hit an overhead object.</span></td><td class="v">0</td></tr>
        </tbody>
      </table>
      <p><strong>Cancellation scoring:</strong> add up each side's points for the frame, then subtract the smaller from the larger. Only the side that came out ahead scores, and it scores the difference. A tied frame scores nothing for anyone.</p>

      <div class="example" id="example">
        <h3>Example frame</h3>
        <p>You: one bag in the hole and two on the board — <strong>5</strong>. Them: three bags on the board — <strong>3</strong>.</p>
        <p>You score 5 − 3 = <strong>2</strong>. They score nothing, even though they had more bags on the board.</p>
      </div>

      <h2 id="setup">Setting up</h2>
      <ul>
        <li>Place the boards facing each other <strong>27 feet apart</strong>, front edge to front edge.</li>
        <li>A regulation board is 2 ft × 4 ft, with a 6-inch hole centered 9 inches from the top.</li>
        <li>The front edge of each board is the foul line. Pitch from beside the board, with your feet behind it.</li>
      </ul>

      <h2 id="play">Playing a frame</h2>
      <ul>
        <li>Toss a coin for first pitch. Players alternate until all eight bags are thrown, then the frame is scored.</li>
        <li>Bags can be knocked in, knocked off or blocked right up to the last pitch — nothing counts until the frame is over.</li>
        <li><strong>Singles:</strong> both players pitch from the same end, then walk to the other board, score, and pitch back.</li>
        <li><strong>Doubles:</strong> partners stand at opposite boards. One player from each team pitches at one end, then their partners pitch back from the other.</li>
        <li>The side that scored pitches first in the next frame. If nobody scored, the side that went first keeps it.</li>
      </ul>

      <h2 id="winning">Winning</h2>
      <p>In the American Cornhole League's rules, the first side to <strong>reach or pass 21</strong> at the end of a frame wins. There's no need to land on it exactly.</p>
      <h3>Backyard house rules</h3>
      <ul>
        <li><strong>Exactly 21 (bust):</strong> you have to land on 21 exactly, and going over knocks you back to a lower score — Tallero's default drops you to 11.</li>
        <li><strong>Skunk:</strong> end the game early if one side leads 11–0.</li>
        <li><strong>Win by two:</strong> keep playing until someone is at least 21 and two ahead.</li>
      </ul>

      <h2>Quick answers</h2>
      <h3>Does a bag that bounces off the ground onto the board count?</h3>
      <p>No. Any bag that touches the ground before coming to rest on the board is dead and comes off.</p>
      <h3>Do both teams score in a frame?</h3>
      <p>Not with cancellation scoring — only the side with more points scores the difference. Some casual games let both sides keep everything, which makes for a much faster game.</p>
''' + callout("Every frame, every format.",
  "Enter the difference for the side that won the frame. Tallero keeps the totals to 21 and handles busts, skunks and win-by-two if your yard plays them.") + '''
    </div>
  </div>
</section>
''' + sheet("Cornhole score sheet", "Points each frame and the running total for each side. First to 21.", "+,Total", 20, 2, 2, 2, unit="teams")

page("/rules/cornhole/", "Cornhole Rules & Scoring — Cancellation Scoring Explained — Tallero",
     "How to play cornhole: cancellation scoring, 3 for the hole and 1 on the board, dead bags, board distance and setup, singles and doubles, winning at 21, backyard house rules, and a printable score sheet.",
     [("Game rules", "/rules/"), ("Cornhole", "/rules/cornhole/")], ch)

# ------------------------------------------------------------------ GOLF (CARDS)
def down(): return '<span class="card down" role="img" aria-label="face-down card"></span>'
golf = hero("Golf (Cards)", "golf_cards", "oklch(0.928 0.045 150)", "Golf card game rules and scoring",
  "Six-card Golf: the deal, a turn, what every card costs, how column pairs cancel, and the four-, eight- and nine-card versions — plus a printable scorecard.") + f'''
<section class="section section--tight">
  <div class="wrap">
    <div class="prose">
      <ul class="toc">
        <li><a href="#values">Card values</a></li>
        <li><a href="#deal">The deal</a></li>
        <li><a href="#turn">A turn</a></li>
        <li><a href="#end">Ending a hole</a></li>
        <li><a href="#variants">Other versions</a></li>
        <li><a href="#score-sheet">Scorecard</a></li>
      </ul>

      <p class="gist">Golf is a card game where the low score wins. Each player has six cards laid out face down in two rows of three, and swaps cards in and out over the hand, trying to end with as few points as possible — a matching pair in the same column cancels to nothing. Each hand is a <strong>hole</strong>; play nine and the lowest total wins.</p>

      <h2 id="values">What the cards cost</h2>
      <table class="score-table">
        <thead><tr><th>Card</th><th>Points</th></tr></thead>
        <tbody>
          <tr><td>2</td><td class="v">−2</td></tr>
          <tr><td>Ace</td><td class="v">1</td></tr>
          <tr><td>3 – 10</td><td class="v">face value</td></tr>
          <tr><td>Jack, Queen</td><td class="v">10</td></tr>
          <tr><td>King</td><td class="v">0</td></tr>
          <tr><td>A pair in the same column<span class="note">Two cards of the same rank, one above the other, score 0 — even a pair of 2s.</span></td><td class="v">0</td></tr>
        </tbody>
      </table>
      <div class="example">
        <h3>Example layout</h3>
        <div class="card-grid">
          <div>{B("8♣")}{down()}{R("K♥")}</div>
          <div>{R("8♦")}{B("4♠")}{down()}</div>
        </div>
        <p>The two 8s share a column, so they cancel — side by side in a row they'd cost 16. The King is free, the 4 costs 4, and the two face-down cards are still unknown.</p>
      </div>

      <h2 id="deal">The deal</h2>
      <ul>
        <li>Deal six cards to each player, face down, in two rows of three. Use one deck for up to four players, two for five to eight, and three beyond that.</li>
        <li>Put the rest face down as the stock, and turn its top card face up to start the discard pile.</li>
        <li>Each player turns any two of their own cards face up. The others stay hidden — from everyone, the owner included.</li>
      </ul>

      <h2 id="turn">Taking a turn</h2>
      <ul>
        <li>Draw one card: the top of the stock, or the top of the discard pile.</li>
        <li>Swap it for any card in your layout, face up or face down. The card you replace goes face up on the discard pile.</li>
        <li>If you drew from the stock and don't want the card, you can discard it instead. Some tables then make you turn one of your face-down cards up.</li>
        <li>A card taken from the discard pile has to go into your layout — you can't just put it back.</li>
      </ul>

      <h2 id="end">Ending a hole</h2>
      <ul>
        <li>The hole ends as soon as one player's sixth card is face up. Many groups give everyone else one more turn first.</li>
        <li>Everyone turns over any face-down cards and adds up their layout.</li>
        <li>A standard game is nine holes, lowest total wins. Eighteen holes is a common longer game.</li>
      </ul>

      <h2>Common variants</h2>
      <ul>
        <li><strong>Jokers:</strong> add two jokers to the deck, worth −2 each.</li>
        <li><strong>Going-out penalty:</strong> some tables penalise the player who ended the hole if anyone ties or beats their score.</li>
      </ul>

      <h2 id="variants">Four-, eight- and nine-card Golf</h2>
      <ul>
        <li><strong>Four-card:</strong> a 2 × 2 layout. Players may <strong>knock</strong> to end the hand.</li>
        <li><strong>Eight-card:</strong> four columns of two, played with a double deck and jokers.</li>
        <li><strong>Nine-card:</strong> a 3 × 3 layout with three cards turned up to start. A full column of three matching cards scores 0.</li>
        <li><strong>Ten-card:</strong> five columns of two, with at least two decks.</li>
      </ul>
''' + callout("Nine holes, no adding up.",
  "Enter each player's hand total per hole — negative scores welcome — and Tallero keeps the running totals for 9 holes, 18, or out at 100.") + '''
    </div>
  </div>
</section>
''' + sheet("Golf scorecard", "Each player's score for every hole, and the total. Lowest wins.", "Score", 0, 2, 8, 4,
            labels=["Hole 1", "Hole 2", "Hole 3", "Hole 4", "Hole 5", "Hole 6", "Hole 7", "Hole 8", "Hole 9", "*Total"])

page("/rules/golf/", "Golf Card Game Rules & Scoring — Six-Card Golf — Tallero",
     "How to play the Golf card game: dealing six-card Golf, taking a turn, card values (2s are −2, Kings 0), cancelling column pairs, ending a hole, four-, eight- and nine-card versions, and a printable scorecard.",
     [("Game rules", "/rules/"), ("Golf (Cards)", "/rules/golf/")], golf)

# ------------------------------------------------------------------ QWIRKLE
QC = ["#D43838", "#E8821E", "#F2C12E", "#2E7D43", "#1E5BBF", "#7B3AA8"]
QS = {"circle": "●", "diamond": "◆", "square": "■", "clover": "✤", "starburst": "✸", "star": "✦"}
def qt(shape, color, placed=False):
    return f'<span class="qt{" placed" if placed else ""}" style="color:{QC[color]}" role="img" aria-label="{shape}">{QS[shape]}</span>'
def qrow(cells):
    return '<div>' + "".join(qt(*c) if c else '<span class="qt empty"></span>' for c in cells) + '</div>'

qw = hero("Qwirkle", "qwirkle", "oklch(0.928 0.045 255)", "Qwirkle rules and scoring",
  "How lines are built, how every turn is scored, the 12-point Qwirkle, trading tiles and the end-game bonus — plus a printable score sheet.") + f'''
<section class="section section--tight">
  <div class="wrap">
    <div class="prose">
      <ul class="toc">
        <li><a href="#lines">Building lines</a></li>
        <li><a href="#turn">A turn</a></li>
        <li><a href="#scoring">Scoring</a></li>
        <li><a href="#end">Ending</a></li>
        <li><a href="#score-sheet">Score sheet</a></li>
      </ul>

      <p class="gist">108 tiles: six colors, six shapes, three of every combination. Take turns adding tiles to a shared grid, building lines where every tile shares a color <em>or</em> a shape. You score every line you build or extend, and completing a line of six — a <strong>Qwirkle</strong> — is worth 12. When the bag is empty and someone plays their last tile, highest score wins.</p>

      <h2 id="lines">Building lines</h2>
      <ul>
        <li>A line is all one color in different shapes, or all one shape in different colors.</li>
        <li>No tile can appear twice in the same line, so a line can never be longer than six.</li>
        <li>Every tile you place must fit every line it touches — across and down.</li>
      </ul>

      <h2 id="turn">Taking a turn</h2>
      <ul>
        <li><strong>Setup:</strong> everyone draws six tiles from the bag and keeps them hidden.</li>
        <li><strong>First turn:</strong> the player who can play the most tiles sharing one color or one shape (no duplicates) goes first, and scores them.</li>
        <li><strong>Play:</strong> place one or more tiles, all in a single line. They must connect to the tiles already on the table, but needn't touch each other — as long as the finished line has no gaps.</li>
        <li><strong>Or trade:</strong> instead of playing, put any number of tiles back in the bag and draw replacements. That's your whole turn, and you score nothing.</li>
        <li>After playing, draw back up to six.</li>
      </ul>

      <h2 id="scoring">How scoring works</h2>
      <table class="score-table">
        <thead><tr><th>Scores</th><th>Points</th></tr></thead>
        <tbody>
          <tr><td>Each line you create or add to<span class="note">Count every tile in the line, including the ones already there.</span></td><td class="v">1 per tile</td></tr>
          <tr><td>A tile in two lines<span class="note">A tile that extends a line across and a line down scores both.</span></td><td class="v">both lines</td></tr>
          <tr><td>Qwirkle<span class="note">Completing a line of all six: 6 for the tiles plus a 6-point bonus.</span></td><td class="v">12</td></tr>
          <tr><td>Going out<span class="note">Playing your last tile once the bag is empty.</span></td><td class="v">+6</td></tr>
        </tbody>
      </table>
      <div class="example">
        <h3>Example: 17 points in one turn</h3>
        <div class="qgrid">
          {qrow([None, None, ("clover", 0), None, None, ("diamond", 0)])}
          {qrow([("circle", 4), ("square", 4), ("clover", 4, True), ("starburst", 4), ("star", 4), ("diamond", 4, True)])}
          {qrow([None, None, None, None, None, ("diamond", 3)])}
        </div>
        <p>The two outlined blue tiles were just played into the blue row. That completes all six blue shapes: a Qwirkle, <strong>12</strong>. The blue clover also makes a two-tile clover column (<strong>2</strong>), and the blue diamond completes a three-tile diamond column (<strong>3</strong>). Total: <strong>17</strong>.</p>
      </div>

      <h2 id="end">How it ends</h2>
      <p>Once the bag is empty, players carry on without drawing. The first player to play their last tile ends the game and scores 6 bonus points on top of that turn. Highest total wins.</p>

      <h2>Quick answers</h2>
      <h3>Is a Qwirkle 6 or 12 points?</h3>
      <p>12 — six for the tiles in the line plus a six-point bonus.</p>
      <h3>Can you play tiles in two directions in one turn?</h3>
      <p>No. Everything you place in a turn goes in one line, though each tile also scores any line it crosses.</p>
''' + callout("Quick-add for the big turns.",
  "Tap +12 for a Qwirkle, +5, +1 — most turns are a couple of taps — and Tallero adds the going-out bonus when the last tile is played.") + '''
      <p class="small" style="margin-top:18px;color:var(--txt-3)">Qwirkle® is a trademark of its owner. Tallero is independent and not affiliated with or endorsed by the maker of Qwirkle.</p>
    </div>
  </div>
</section>
''' + sheet("Qwirkle score sheet", "Points each turn and the running total. Highest wins.", "+,Total", 25, 2, 4, 2)

page("/rules/qwirkle/", "Qwirkle Rules & Scoring — How to Score a Qwirkle — Tallero",
     "How to play Qwirkle: building lines by color or shape, taking a turn, trading tiles, scoring every line, the 12-point Qwirkle, the going-out bonus, and a printable score sheet.",
     [("Game rules", "/rules/"), ("Qwirkle", "/rules/qwirkle/")], qw)

# ------------------------------------------------------------------ RUMMY
rm = hero("Rummy", "rummy", "oklch(0.928 0.045 78)", "Rummy rules and scoring",
  "Basic Rummy and Rummy 500: melds, a turn, laying off, going rummy, and how each version is scored — plus a printable score sheet.") + f'''
<section class="section section--tight">
  <div class="wrap">
    <div class="prose">
      <ul class="toc">
        <li><a href="#melds">Melds</a></li>
        <li><a href="#turn">A turn</a></li>
        <li><a href="#scoring">Scoring</a></li>
        <li><a href="#r500">Rummy 500</a></li>
        <li><a href="#score-sheet">Score sheet</a></li>
      </ul>

      <p class="gist">Draw and discard, building <strong>melds</strong> — runs and sets — and laying them on the table. The first player to get rid of every card goes out, and scores the cards everyone else is still holding. Basic Rummy is below; what changes for Rummy 500 is at the end.</p>

      <h2 id="melds">Melds</h2>
      <ul>
        <li>A <strong>run</strong> is three or more cards in sequence, all one suit: {R("5♥")} {R("6♥")} {R("7♥")}</li>
        <li>A <strong>set</strong> is three or four cards of the same rank: {B("8♠")} {R("8♦")} {B("8♣")}</li>
        <li>Aces are low in standard play: A-2-3 is a run, Q-K-A isn't. Some tables play aces high instead.</li>
      </ul>

      <h2 id="turn">Dealing and taking a turn</h2>
      <ul>
        <li>Deal 10 cards each with two players, 7 each with three or four, 6 each with five or six. Turn the next card up to start the discard pile; the rest is the stock.</li>
        <li><strong>Draw</strong> one card — from the stock or the top of the discard pile.</li>
        <li><strong>Meld</strong> if you like. Standard rules allow one meld per turn; many tables allow as many as you want.</li>
        <li><strong>Lay off</strong> any number of cards onto melds already on the table, yours or anyone else's.</li>
        <li><strong>Discard</strong> one card to end your turn. You can't discard the card you just took from the discard pile.</li>
        <li>If the stock runs out, turn the discard pile over without shuffling to make a new stock.</li>
      </ul>

      <h2 id="scoring">Scoring a hand</h2>
      <table class="score-table">
        <thead><tr><th>Card left in a loser's hand</th><th>Points</th></tr></thead>
        <tbody>
          <tr><td>Face cards</td><td class="v">10</td></tr>
          <tr><td>Number cards</td><td class="v">face value</td></tr>
          <tr><td>Aces<span class="note">15 at tables that play aces high.</span></td><td class="v">1</td></tr>
        </tbody>
      </table>
      <p>The player who goes out scores the total of every card left in the other players' hands — melded or not. Play to an agreed target, or a set number of deals.</p>
      <ul>
        <li><strong>Going rummy:</strong> going out in a single turn, having melded or laid off nothing before, doubles the hand's score (or earns a 10-point bonus at some tables).</li>
        <li><strong>Penalty scoring:</strong> some tables flip it — each loser scores their own leftovers as penalty points, and the lowest total wins when someone reaches 100.</li>
        <li><strong>Block Rummy:</strong> the discard pile is never reused. If the stock runs out, the hand ends and everyone counts their cards.</li>
      </ul>

      <h2 id="r500">Rummy 500 — what changes</h2>
      <ul>
        <li>Use 52 cards plus two jokers; five or more players shuffle two decks together. Deal 13 each with two players, 7 each otherwise.</li>
        <li>You may take a card from deeper in the discard pile — but you must meld it immediately and take every card above it too.</li>
        <li><strong>Everyone scores their own melds.</strong> A card you lay off on someone else's meld goes in front of you and counts for you.</li>
        <li>Card values: 2–10 face value, face cards 10, aces and jokers 15 — except an ace used low in A-2-3, which is 1. Jokers are wild; say which card a joker stands for when you meld it.</li>
        <li>If a discard could have been melded, any other player may call <strong>“Rummy!”</strong>, take the pile down to that card, and meld it.</li>
        <li>At the end of a hand, score your melded cards minus the cards still in your hand — a bad hand can go negative. First to 500 wins.</li>
      </ul>
''' + callout("Whichever Rummy you play.",
  "Basic, Rummy 500, winner-scores or penalty points — enter each hand and Tallero keeps the totals to your target.") + '''
    </div>
  </div>
</section>
''' + sheet("Rummy score sheet", "Each hand's points and the running total.", "+,Total", 20, 2, 6, 4)

page("/rules/rummy/", "Rummy Rules & Scoring — Basic Rummy and Rummy 500 — Tallero",
     "How to play Rummy: runs and sets, how many cards to deal, a turn, laying off, going rummy, scoring a hand, Block Rummy, Rummy 500 rules and scoring, and a printable score sheet.",
     [("Game rules", "/rules/"), ("Rummy", "/rules/rummy/")], rm)

# ------------------------------------------------------------------ DOMINOES
dm = hero("Dominoes", "dominoes", "oklch(0.928 0.045 194)", "Dominoes rules and scoring",
  "All Fives (Muggins-style) dominoes: the spinner, scoring multiples of five, going out and blocked hands — plus Block and Draw dominoes, and a printable score sheet.") + '''
<section class="section section--tight">
  <div class="wrap">
    <div class="prose">
      <ul class="toc">
        <li><a href="#deal">The deal</a></li>
        <li><a href="#play">Playing a hand</a></li>
        <li><a href="#fives">Scoring fives</a></li>
        <li><a href="#end">Ending a hand</a></li>
        <li><a href="#block">Block &amp; Draw</a></li>
        <li><a href="#score-sheet">Score sheet</a></li>
      </ul>

      <p class="gist">This is <strong>All Fives</strong>, the dominoes game where you score as you play. Match tiles end to end, and whenever the open ends of the layout add up to a multiple of five, you score that total. Going out scores the pips left in everyone else's hands. First to 250 wins with two players, 200 with three or four.</p>

      <h2 id="deal">The deal</h2>
      <ul>
        <li>Use a double-six set: 28 tiles, every pairing from blank to six.</li>
        <li>Deal 9 tiles each with two players, 7 with three, 5 with four (often as partnerships). The rest stay face down as the <strong>boneyard</strong>.</li>
        <li>Draw lots for the first lead. After that, whoever went out last hand leads. Any tile may be led.</li>
      </ul>

      <h2 id="play">Playing a hand</h2>
      <ul>
        <li>Play a tile against an open end of the layout so the touching numbers match.</li>
        <li>Doubles are laid crosswise, so both halves show.</li>
        <li>The first double played is the <strong>spinner</strong>: it can be played on from all four sides — first its two long sides, then its two ends.</li>
        <li>Can't play? Draw from the boneyard until you can. Only pass once the boneyard is empty.</li>
      </ul>

      <h2 id="fives">Scoring multiples of five</h2>
      <p>After you play, add up the pips on every open end of the layout. If the total is a multiple of five, you score it right away.</p>
      <table class="score-table">
        <thead><tr><th>Open end</th><th>Counts</th></tr></thead>
        <tbody>
          <tr><td>An ordinary tile<span class="note">The number showing at that end.</span></td><td class="v">its end</td></tr>
          <tr><td>A double at an end<span class="note">A 5-5 at the end of a line counts 10.</span></td><td class="v">both halves</td></tr>
          <tr><td>The spinner<span class="note">Counts both its ends until both long sides have tiles; after that only the arm ends count.</span></td><td class="v">see note</td></tr>
        </tbody>
      </table>
      <div class="example">
        <h3>Example</h3>
        <p>A 6-6 spinner has three arms: one ending in a 5, one in a 3, and one in a 1-1 double. The spinner itself no longer counts, so the ends are 5 + 3 + 2 = <strong>10</strong> — a multiple of five, so the player who made it scores 10.</p>
      </div>

      <h2 id="end">Ending a hand</h2>
      <ul>
        <li><strong>Going out:</strong> play your last tile and you score the pips still in everyone else's hands, rounded to the nearest five.</li>
        <li><strong>Blocked:</strong> if nobody can play and the boneyard is empty, whoever holds the fewest pips scores the others' pips, rounded the same way. A tie for fewest scores nothing.</li>
        <li>Some players divide every score by five and keep count on a cribbage board, playing to 61.</li>
      </ul>

      <h2 id="block">Block and Draw dominoes</h2>
      <p>Two simpler games on the same tiles, with no spinner — the layout is a single line, and nothing scores during the hand.</p>
      <ul>
        <li><strong>Block:</strong> you never draw. If you can't play, you pass.</li>
        <li><strong>Draw:</strong> draw from the boneyard until you can play, and pass only when it's empty.</li>
        <li>The hand ends when someone plays their last tile or nobody can move. The player with the fewest pips wins the hand and scores the other players' pips minus their own. A tie for fewest scores nothing.</li>
        <li>Play to 100 with two players or partnerships, or 61 with three or four playing individually — so a cribbage board can keep score.</li>
      </ul>
''' + callout("Fives, tallied.",
  "Quick-add buttons for every multiple of five during the hand, then enter the leftover pips — Tallero rounds them and adds them up.") + '''
    </div>
  </div>
</section>
''' + sheet("Dominoes score sheet", "Points as they're scored and the running total.", "+,Total", 25, 2, 4, 2)

page("/rules/dominoes/", "Dominoes Rules & Scoring — All Fives, Block & Draw — Tallero",
     "How to play dominoes: All Fives scoring with the spinner and multiples of five, going out and blocked hands, how many tiles to deal, plus Block and Draw dominoes, and a printable score sheet.",
     [("Game rules", "/rules/"), ("Dominoes", "/rules/dominoes/")], dm)

# ------------------------------------------------------------------ DUTCH BLITZ
db = hero("Dutch Blitz", "dutchblitz", "oklch(0.928 0.045 78)", "Dutch Blitz rules and scoring",
  "Setting up your piles, playing to the Dutch piles, Post piles, calling Blitz, and scoring each round — plus a printable score sheet.") + '''
<section class="section section--tight">
  <div class="wrap">
    <div class="prose">
      <ul class="toc">
        <li><a href="#setup">Setup</a></li>
        <li><a href="#play">How to play</a></li>
        <li><a href="#post">Post piles</a></li>
        <li><a href="#scoring">Scoring</a></li>
        <li><a href="#score-sheet">Score sheet</a></li>
      </ul>

      <p class="gist">A speed card game with no turns — everyone plays at once, racing to lay cards in shared piles in the middle. You score for every card you get down, and the round ends the instant someone empties their Blitz pile and shouts <strong>“Blitz!”</strong> Cards left in your Blitz pile cost you. First to 75 wins.</p>

      <h2 id="setup">Setup</h2>
      <ul>
        <li>Each player has their own 40-card deck — red, blue, green and yellow, numbered 1 to 10. The backs (pump, carriage, plow, pail) tell the decks apart.</li>
        <li>Deal yourself a <strong>Blitz pile</strong> of 10 cards, top card face up, and three face-up <strong>Post piles</strong> of one card each. With two players, four or five Post piles are often used to keep the game from stalling.</li>
        <li>The rest is your <strong>hand</strong>, held face down.</li>
      </ul>

      <h2 id="play">How to play</h2>
      <ul>
        <li>Count cards off your hand three at a time onto a face-up <strong>Wood pile</strong>; only its top card is playable. When your hand runs out, turn the Wood pile over — without shuffling — and keep going.</li>
        <li>Play from the top of your Blitz pile, your Wood pile, or a Post pile — onto the shared <strong>Dutch piles</strong> in the middle, or onto your own Post piles.</li>
        <li>Dutch piles start with a 1 and build up to 10, one color per pile. Anyone can play on any Dutch pile.</li>
        <li>Play with one hand only, one card at a time.</li>
        <li>If everyone is stuck, each player moves the top card of their Wood pile to the bottom and play resumes.</li>
      </ul>

      <h2 id="post">Post piles</h2>
      <ul>
        <li>Post piles build <strong>down</strong>, and each card must alternate between a boy and a girl. In the standard deck, red and blue cards show a boy and green and yellow cards a girl; expansion packs use other colors, so go by the picture.</li>
        <li>Only the exposed lowest card of a Post pile is playable.</li>
        <li>When you empty a Post pile, fill it with the top card of your Blitz pile — another way to drain it.</li>
      </ul>

      <h2 id="scoring">Calling Blitz and scoring</h2>
      <p>Empty your Blitz pile, shout “Blitz!”, and everyone stops. Sort the Dutch piles by the pictures on the card backs so everyone gets their own cards back, then score:</p>
      <table class="score-table">
        <thead><tr><th>Card</th><th>Points</th></tr></thead>
        <tbody>
          <tr><td>Each card you played to the Dutch piles</td><td class="v">+1</td></tr>
          <tr><td>Each card left in your Blitz pile</td><td class="v">−2</td></tr>
          <tr><td>Cards in your Post piles, Wood pile or hand</td><td class="v">0</td></tr>
        </tbody>
      </table>
      <div class="example">
        <h3>Example</h3>
        <p>You got 14 cards into the middle but still had 3 in your Blitz pile: 14 − 6 = <strong>8</strong> for the round. Negative rounds happen.</p>
      </div>
      <p>Keep playing rounds until someone reaches 75. Highest score wins.</p>
''' + callout("Negative rounds welcome.",
  "Enter each player's net for the round — minus signs and all — and Tallero keeps the race to 75 sorted with the leader on top.") + '''
      <p class="small" style="margin-top:18px;color:var(--txt-3)">Dutch Blitz® is a trademark of its owner. Tallero is independent and not affiliated with or endorsed by the maker of Dutch Blitz.</p>
    </div>
  </div>
</section>
''' + sheet("Dutch Blitz score sheet", "Each round's net score and the running total. First to 75.", "+,Total", 20, 2, 8, 4)

page("/rules/dutch-blitz/", "Dutch Blitz Rules & Scoring — Tallero",
     "How to play Dutch Blitz: the Blitz, Post and Wood piles, building Dutch piles 1 to 10, the boy-girl rule, calling Blitz, scoring +1 and −2, playing to 75, and a printable score sheet.",
     [("Game rules", "/rules/"), ("Dutch Blitz", "/rules/dutch-blitz/")], db)

# ------------------------------------------------------------------ FLIP 7
f7 = hero("Flip 7", "flip7", "oklch(0.928 0.045 78)", "Flip 7 rules and scoring",
  "Hit or stay, busting, the Flip 7 bonus, modifier and action cards, and the order to add up a round — plus a printable score sheet.") + '''
<section class="section section--tight">
  <div class="wrap">
    <div class="prose">
      <ul class="toc">
        <li><a href="#deck">The deck</a></li>
        <li><a href="#round">A round</a></li>
        <li><a href="#actions">Action cards</a></li>
        <li><a href="#scoring">Scoring</a></li>
        <li><a href="#score-sheet">Score sheet</a></li>
      </ul>

      <p class="gist">A push-your-luck card game. Take cards one at a time and add up their numbers — but draw a number you already have and you <strong>bust</strong>, scoring nothing for the round. Stay to bank your points, or flip seven different numbers for a 15-point bonus. Rounds continue until someone reaches 200.</p>

      <h2 id="deck">The deck</h2>
      <ul>
        <li>94 cards. Number cards run from twelve 12s, eleven 11s, ten 10s… down to a single 1, plus one 0 — the bigger the number, the more copies.</li>
        <li>Six <strong>modifier</strong> cards: +2, +4, +6, +8, +10 and ×2.</li>
        <li>Nine <strong>action</strong> cards: three each of Freeze, Flip Three and Second Chance.</li>
      </ul>

      <h2 id="round">Playing a round</h2>
      <ul>
        <li>The dealer deals one card face up to each player, themselves included. If an action card comes up, resolve it before carrying on.</li>
        <li>Then, in turn, each player chooses to <strong>hit</strong> (take one more card) or <strong>stay</strong> (bank their points and leave the round). Keep number cards in one row so duplicates are easy to spot.</li>
        <li>Draw a second card of a number you already have and you <strong>bust</strong>: you're out of the round with nothing.</li>
        <li>The round ends when every player has stayed or busted, or when someone gets seven different number cards — a <strong>Flip 7</strong> — which ends it for everyone immediately.</li>
        <li>Used cards go aside, not back into the deck. Pass the deck left; that player deals next. Reshuffle the discards when the deck runs out.</li>
      </ul>

      <h2 id="actions">Action cards</h2>
      <p>Action cards can be played on any <strong>active</strong> player — anyone who hasn't stayed or busted — including yourself. If you're the only active player left, you must take it yourself.</p>
      <table class="score-table">
        <tbody>
          <tr><td><strong>Freeze</strong><span class="note">The player banks what they have and is out of the round.</span></td><td class="v"></td></tr>
          <tr><td><strong>Flip Three</strong><span class="note">The player must take the next three cards, one at a time, stopping early on a bust or a Flip 7. A Freeze or Flip Three turned up along the way is resolved after all three (if they haven't busted).</span></td><td class="v"></td></tr>
          <tr><td><strong>Second Chance</strong><span class="note">Keep it. The next time you'd bust, discard it and the duplicate instead. You can hold only one; a second goes to another active player. Unused Second Chances are discarded at the end of the round.</span></td><td class="v"></td></tr>
        </tbody>
      </table>

      <h2 id="scoring">Scoring a round</h2>
      <p>Add it up in this order:</p>
      <ol>
        <li>Add your number cards.</li>
        <li>If you have the ×2, double that sum.</li>
        <li>Add any +2 to +10 modifiers.</li>
        <li>If you flipped 7 numbers, add 15.</li>
      </ol>
      <div class="example">
        <h3>Example</h3>
        <p>Numbers 3, 11, 5, 7 and 10 make 36. With the ×2 that's 72. With a +10 instead, it would be 46.</p>
      </div>
      <ul>
        <li>Modifiers aren't number cards: you can't bust on them, and they don't count toward the seven.</li>
        <li>You still score modifiers with no number cards in front of you — except the ×2, which has nothing to double.</li>
        <li>The 0 scores nothing, but it counts as one of your seven different numbers.</li>
      </ul>

      <h2>Ending the game</h2>
      <p>At the end of a round in which at least one player reaches 200, the player with the most points wins — not necessarily the first to 200.</p>
''' + callout("Busts and Flip 7s, logged.",
  "Enter each player's round total — leave a bust blank — and tag a Flip 7 with one tap. Tallero settles the race to 200 at the end of the round.") + '''
      <p class="small" style="margin-top:18px;color:var(--txt-3)">Flip&nbsp;7™ is a trademark of its owner. Tallero is independent and not affiliated with or endorsed by the maker of Flip&nbsp;7.</p>
    </div>
  </div>
</section>
''' + sheet("Flip 7 score sheet", "Each round's score and the running total. Race to 200.", "+,Total", 15, 3, 8, 4)

page("/rules/flip-7/", "Flip 7 Rules & Scoring — Tallero",
     "How to play Flip 7: the deck, hit or stay, busting, the Flip 7 bonus, Freeze, Flip Three and Second Chance, modifier cards, how to score a round, and a printable score sheet.",
     [("Game rules", "/rules/"), ("Flip 7", "/rules/flip-7/")], f7)

# ------------------------------------------------------------------ MINI GOLF
mg = hero("Mini Golf", "minigolf", "oklch(0.928 0.045 150)", "Mini golf scoring",
  "How to keep score in mini golf: strokes, par, birdies and bogeys, stroke limits, and a printable 18-hole scorecard.") + '''
<section class="section section--tight">
  <div class="wrap">
    <div class="prose">
      <ul class="toc">
        <li><a href="#basics">The basics</a></li>
        <li><a href="#par">Par and the names</a></li>
        <li><a href="#house">Common course rules</a></li>
        <li><a href="#score-sheet">Scorecard</a></li>
      </ul>

      <p class="gist">Every stroke counts against you. Write down how many strokes each player takes on each hole, add them up at the end, and the <strong>lowest total wins</strong>. Most courses are 9 or 18 holes.</p>

      <h2 id="basics">The basics</h2>
      <ul>
        <li>Every swing at the ball is a stroke, whether it moves an inch or the length of the hole.</li>
        <li>The hole is finished when the ball drops in. Write down that player's strokes and move on.</li>
      </ul>

      <h2 id="par">Par, birdies and bogeys</h2>
      <p><strong>Par</strong> is the number of strokes a hole should take — the course usually prints it on the scorecard or at each tee. Scores are named by how they compare:</p>
      <table class="score-table">
        <thead><tr><th>Result</th><th>Strokes</th></tr></thead>
        <tbody>
          <tr><td>Hole in one</td><td class="v">1</td></tr>
          <tr><td>Eagle</td><td class="v">2 under par</td></tr>
          <tr><td>Birdie</td><td class="v">1 under par</td></tr>
          <tr><td>Par</td><td class="v">even</td></tr>
          <tr><td>Bogey</td><td class="v">1 over par</td></tr>
          <tr><td>Double bogey</td><td class="v">2 over par</td></tr>
        </tbody>
      </table>
      <p>Par only changes how a score is described, not the score itself — the winner is still whoever took the fewest strokes.</p>

      <h2 id="house">Course rules</h2>
      <p>Mini golf has no single official rulebook. Most courses post their own on the scorecard — commonly a maximum number of strokes per hole, what to do when a ball leaves the course, and whether you can move a ball away from a wall. Agree on them before the first tee.</p>
''' + callout("Leave the pencil at the counter.",
  "Tap + for each stroke and Next Hole — Tallero tracks par, birdies and bogeys for 9 or 18 holes, and fills skipped holes at the end.") + '''
    </div>
  </div>
</section>
''' + sheet("Mini golf scorecard", "Strokes for every hole, front nine, back nine and total.", "Strokes", 0, 1, 8, 4,
            labels=["Par"] + [f"Hole {i}" for i in range(1, 10)] + ["*Out"] + [f"Hole {i}" for i in range(10, 19)] + ["*In", "*Total"])

page("/rules/mini-golf/", "Mini Golf Scoring — How to Keep Score & Printable Scorecard — Tallero",
     "How to keep score in mini golf: strokes, par, birdies, bogeys and holes in one, common course rules like stroke limits, and a printable 18-hole mini golf scorecard.",
     [("Game rules", "/rules/"), ("Mini Golf", "/rules/mini-golf/")], mg)

# ------------------------------------------------------------------ QUICK SCORE
qs = hero("Quick Score", "score", "oklch(0.928 0.045 78)", "Quick Score: a score counter for any game",
  "Tap to count, hold to subtract, set a target if you're racing to one. For the games Tallero doesn't have built in — or the ones you're making up as you go.") + '''
<section class="section section--tight">
  <div class="wrap">
    <div class="prose">
      <p class="gist">Quick Score is the fastest way to keep score in Tallero: one tap from the home screen, no setup, no rules. Each player gets a tile, and every tap adds a point.</p>

      <h2>How it works</h2>
      <table class="score-table">
        <thead><tr><th>Do this</th><th>Result</th></tr></thead>
        <tbody>
          <tr><td>Tap a player's tile</td><td class="v">+1</td></tr>
          <tr><td>Tap +5 or +10</td><td class="v">+5 / +10</td></tr>
          <tr><td>Press and hold the tile, +5 or +10</td><td class="v">subtract</td></tr>
          <tr><td>Swipe a tile down</td><td class="v">−1</td></tr>
        </tbody>
      </table>
      <ul>
        <li><strong>+ Player</strong> adds as many players as you need, and tapping a name renames it.</li>
        <li><strong>Racing to a number?</strong> Set a target and the first player past it wins automatically.</li>
        <li>Tapped the wrong player? Hold their tile to take the point back off.</li>
      </ul>

      <h2>When to use it</h2>
      <ul>
        <li>A game Tallero doesn't have a built-in scorer for.</li>
        <li>A game you're inventing as you go.</li>
        <li>Anything where you just need a tally: points in a backyard game, rounds won, who's buying the next round.</li>
      </ul>
      <p>Want the same setup every week, with a target and high- or low-wins? Use <a href="/rules/custom/">Custom</a> instead and save it as its own tile.</p>
''' + callout("One tap from the home screen.",
  "Quick Score sits at the top of Tallero's home screen — open it and start counting.") + '''
    </div>
  </div>
</section>
''' + sheet("Score sheet", "A blank tally sheet for any game: points each round and the running total.", "+,Total", 20, 2, 8, 4)

page("/rules/quick-score/", "Quick Score — A Simple Score Counter for Any Game — Tallero",
     "Tallero's Quick Score is a tap-to-count score counter for any game: tap to add, hold to subtract, add players, and set a target. Plus a printable blank score sheet.",
     [("Game rules", "/rules/"), ("Quick Score", "/rules/quick-score/")], qs)

# ------------------------------------------------------------------ QUICK TIMER
qtm = hero("Quick Timer", "timer", "oklch(0.928 0.045 293)", "Quick Timer: a countdown timer for game night",
  "Turn limits, drawing rounds, sand-timer games — a big, simple countdown that's one tap from the home screen.") + '''
<section class="section section--tight">
  <div class="wrap">
    <div class="prose">
      <p class="gist">Quick Timer is a countdown timer built for the table: big ring, big buttons, and a chime when time's up.</p>

      <h2>How it works</h2>
      <ul>
        <li><strong>Pick a time:</strong> tap a preset — 30, 60, 90 or 120 seconds — or type any number of seconds.</li>
        <li><strong>Or drag the ring</strong> to set the time directly.</li>
        <li><strong>Start</strong> it with the button, or tap the ring to start and pause.</li>
        <li><strong>Need more time?</strong> Add 30 seconds or a minute while it's running.</li>
        <li>When it runs out you'll hear a chime and see <strong>Time's up!</strong> — then Reset to go again.</li>
        <li>It keeps accurate time even if your phone locks mid-countdown.</li>
      </ul>

      <h2>Good for</h2>
      <ul>
        <li>Turn limits for players who take too long.</li>
        <li>Drawing and guessing games like Pictionary or charades.</li>
        <li>Any game that came with a sand timer you can't find.</li>
      </ul>
''' + callout("Always one tap away.",
  "Quick Timer sits next to Quick Score on Tallero's home screen.") + '''
    </div>
  </div>
</section>
'''

page("/rules/quick-timer/", "Quick Timer — A Countdown Timer for Game Night — Tallero",
     "Tallero's Quick Timer is a countdown timer for board and party games: 30 to 120 second presets or any time you like, drag-to-set, add time mid-turn, and a chime when time's up.",
     [("Game rules", "/rules/"), ("Quick Timer", "/rules/quick-timer/")], qtm)

# ------------------------------------------------------------------ CUSTOM
cu = hero("Custom", "custom", "oklch(0.928 0.045 255)", "Custom: score any game your way",
  "Set up players, a target and how the game is won — then save it as its own tile for next time.") + '''
<section class="section section--tight">
  <div class="wrap">
    <div class="prose">
      <p class="gist">Custom is for any game Tallero doesn't have built in. You choose how it's scored and how it's won, and Tallero keeps the totals, crowns the winner and keeps the stats — just like a built-in game.</p>

      <h2>Setting it up</h2>
      <table class="score-table">
        <thead><tr><th>Option</th><th>Choices</th></tr></thead>
        <tbody>
          <tr><td>Scoring mode<span class="note">Enter everyone's score each round, or one player at a time as turns come round.</span></td><td class="v">Round / Turn</td></tr>
          <tr><td>Target score<span class="note">0 means no target — just play rounds.</span></td><td class="v">any number</td></tr>
          <tr><td>Max rounds<span class="note">0 means play freely.</span></td><td class="v">any number</td></tr>
          <tr><td>Negative entries<span class="note">Allow penalties that subtract points.</span></td><td class="v">on / off</td></tr>
        </tbody>
      </table>

      <h2>How the game is won</h2>
      <table class="score-table">
        <tbody>
          <tr><td><strong>Race</strong><span class="note">First to the target wins.</span></td><td class="v"></td></tr>
          <tr><td><strong>Exact</strong><span class="note">Hit the target exactly; go over and you bust back — to half, to zero, or the throw simply doesn't count.</span></td><td class="v"></td></tr>
          <tr><td><strong>Avoid</strong><span class="note">First to the target is out, and the lowest score wins.</span></td><td class="v"></td></tr>
        </tbody>
      </table>
      <p>With no target, the game runs for your set number of rounds, and you choose whether the highest or lowest total wins.</p>

      <h2>Save it for next time</h2>
      <p>Save a Custom setup and it becomes its own tile on the home screen, so your house-rules game is one tap away next week.</p>

      <h2>Custom or Quick Score?</h2>
      <p><a href="/rules/quick-score/">Quick Score</a> is a blank tap counter for when you just need a tally. Custom is for when the game has a target, a way to win, or rounds you want tracked — and when you want it in your stats.</p>
''' + callout("Any game, your rules.",
  "Set it up once, save it as a tile, and Tallero scores it like it was built in.") + '''
    </div>
  </div>
</section>
''' + sheet("Score sheet", "A blank score sheet for any game: points each round and the running total.", "+,Total", 20, 2, 8, 4)

page("/rules/custom/", "Custom Score — Keep Score for Any Game — Tallero",
     "Tallero's Custom mode scores any game: choose round or turn scoring, a target, race, exact-hit or avoid-the-target endings, then save it as its own tile. Plus a printable blank score sheet.",
     [("Game rules", "/rules/"), ("Custom", "/rules/custom/")], cu)

# ------------------------------------------------------------------ HUB
def card(key, tile, name, blurb, path, cta="Read the rules →"):
    return f'''      <a class="rules-card" href="{path}">
        <div class="tile" style="background:{tile}"><img src="/assets/games/{key}.svg" alt=""/></div>
        <h2>{name}</h2>
        <p>{blurb}</p>
        <span class="link">{cta}</span>
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
    card("cornhole", "oklch(0.928 0.045 150)", "Cornhole", "Cancellation scoring, dead bags, board setup, and winning at 21.", "/rules/cornhole/"),
    card("golf_cards", "oklch(0.928 0.045 150)", "Golf (Cards)", "Six-card Golf: card values, cancelling pairs, and the other layouts.", "/rules/golf/"),
    card("qwirkle", "oklch(0.928 0.045 255)", "Qwirkle", "Building lines, scoring every turn, and the 12-point Qwirkle.", "/rules/qwirkle/"),
    card("rummy", "oklch(0.928 0.045 78)", "Rummy", "Basic Rummy and Rummy 500: melds, laying off, and scoring a hand.", "/rules/rummy/"),
    card("dominoes", "oklch(0.928 0.045 194)", "Dominoes", "All Fives scoring with the spinner, plus Block and Draw.", "/rules/dominoes/"),
    card("dutchblitz", "oklch(0.928 0.045 78)", "Dutch Blitz", "Your piles, the boy-girl rule, calling Blitz, and +1 / −2 scoring.", "/rules/dutch-blitz/"),
    card("flip7", "oklch(0.928 0.045 78)", "Flip 7", "Hit or stay, action cards, and the order to add up a round.", "/rules/flip-7/"),
    card("minigolf", "oklch(0.928 0.045 150)", "Mini Golf", "Strokes, par, birdies and bogeys, and an 18-hole scorecard.", "/rules/mini-golf/"),
]) + '''
    </div>
    <h2 class="faq-group" style="margin:48px 0 16px">Also in Tallero</h2>
    <div class="rules-grid">
''' + "\n".join([
    card("score", "oklch(0.928 0.045 78)", "Quick Score", "A tap-to-count score counter for any game, plus a blank score sheet.", "/rules/quick-score/", "How it works →"),
    card("timer", "oklch(0.928 0.045 293)", "Quick Timer", "A countdown timer for turn limits and party games.", "/rules/quick-timer/", "How it works →"),
    card("custom", "oklch(0.928 0.045 255)", "Custom", "Score any game your way, then save it as its own tile.", "/rules/custom/", "How it works →"),
]) + '''
    </div>
  </div>
</section>
'''
page("/rules/", "Game Rules & Scoring — Tallero",
     "Rules and scoring guides for 17 games — Cribbage, Euchre, Spades, Yahtzee, Flip 7, Mölkky and more — with printable score sheets, from Tallero, the score-keeper for game night.",
     [("Game rules", "/rules/")], hub)
