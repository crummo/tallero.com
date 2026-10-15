// Shared behaviour for the /rules/ pages: footer year, mobile nav toggle,
// and the printable score sheet.
//
// The sheet is configured from data-* attributes on <section id="sheet">, so
// each game page only declares its shape:
//   data-title    heading printed above the table
//   data-cols     comma-separated sub-columns per player ("+,Total")
//   data-rows     how many numbered rows (hands / turns)
//   data-min / data-max / data-default   player-count range for the picker
//   data-unit     what the picker counts ("players" or "teams")
//   data-labels   optional "|"-separated row labels instead of numbered rows
//                 (a Yahtzee card); a label starting with "*" is a total row
//
// Printing adds body.print-sheet for the duration of the dialog; the print
// CSS in tally.css hides everything but #sheet while that class is on. A plain
// Cmd-P still prints the whole page, which is what someone printing the rules
// themselves wants.
(function () {
  var yr = document.getElementById("yr");
  if (yr) yr.textContent = new Date().getFullYear();

  var t = document.getElementById("navToggle"), n = document.getElementById("siteNav");
  if (t && n) {
    var set = function (o) {
      n.classList.toggle("open", o);
      t.setAttribute("aria-expanded", o ? "true" : "false");
      t.setAttribute("aria-label", o ? "Close menu" : "Open menu");
    };
    t.addEventListener("click", function () { set(!n.classList.contains("open")); });
    n.addEventListener("click", function (e) { if (e.target.closest("a")) set(false); });
  }

  var sheet = document.getElementById("sheet");
  if (!sheet) return;
  var cols = (sheet.dataset.cols || "Score").split(",");
  var rows = +sheet.dataset.rows || 20;
  var min = +sheet.dataset.min || 2, max = +sheet.dataset.max || 8;
  var def = +sheet.dataset.default || 4;
  var unit = sheet.dataset.unit || "players";
  var labels = sheet.dataset.labels ? sheet.dataset.labels.split("|") : null;
  var subhead = cols.length > 1;
  var select = sheet.querySelector("select");
  var holder = sheet.querySelector(".sheet__scroll");
  var title = sheet.querySelector(".sheet__title");
  if (title) title.textContent = sheet.dataset.title || "";

  for (var i = min; i <= max; i++) {
    var o = document.createElement("option");
    o.value = i; o.textContent = i + " " + (i === 1 ? unit.replace(/s$/, "") : unit);
    if (i === def) o.selected = true;
    select.appendChild(o);
  }

  function build(players) {
    var last = cols.length - 1;
    var who = unit === "teams" ? "Team " : "Player ";
    var h = '<table' + (labels ? ' class="labeled"' : "") + '><thead><tr class="names"><th class="gap"' +
      (subhead ? ' rowspan="2"' : "") + ">" + (labels ? "" : "#") + "</th>";
    for (var p = 0; p < players; p++) {
      h += '<th colspan="' + cols.length + '" class="gap" aria-label="' + who + (p + 1) + ' name"></th>';
    }
    h += "</tr>";
    if (subhead) {
      h += "<tr>";
      for (p = 0; p < players; p++) {
        cols.forEach(function (c, ci) { h += "<th" + (ci === last ? ' class="gap"' : "") + ">" + c + "</th>"; });
      }
      h += "</tr>";
    }
    h += "</thead><tbody>";
    var rowNames = labels || Array.apply(null, Array(rows)).map(function (_, i) { return String(i + 1); });
    rowNames.forEach(function (name) {
      var total = name.charAt(0) === "*";
      h += "<tr" + (total ? ' class="total"' : "") + '><td class="n gap">' + (total ? name.slice(1) : name) + "</td>";
      for (p = 0; p < players; p++) {
        cols.forEach(function (c, ci) { h += "<td" + (ci === last ? ' class="gap"' : "") + "></td>"; });
      }
      h += "</tr>";
    });
    holder.innerHTML = h + "</tbody></table>";
  }

  build(+select.value);
  select.addEventListener("change", function () { build(+select.value); });

  sheet.querySelector("[data-print]").addEventListener("click", function () {
    document.body.classList.add("print-sheet");
    window.print();
  });
  window.addEventListener("afterprint", function () { document.body.classList.remove("print-sheet"); });
})();
