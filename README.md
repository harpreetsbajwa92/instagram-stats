# Instagram Stats
Live: https://harpreetsbajwa92.github.io/instagram-stats/ (repo harpreetsbajwa92/instagram-stats, GitHub Pages from main).
Dark, mobile-first. Page fetches data.json live (cache-busted, refreshes every 60s). All dates are Toronto dates.

## Tabs
- **Today** – Regular / Professionals toggle, stat cards (follows, accepted, texts, active chats), daily follow-goal bar (8 regular, 2 professionals), good prospects.
- **Trends** – Regular / Professionals / Combined filter; Weekly / Monthly / Yearly; bar charts for follows, accepted, texts, active chats; period totals, acceptance rate, days hit goal, current + best streak, all-time totals.
- **History** – day-by-day table, newest first, with filter (Combined shows Reg+Pro split); tap a day for handles followed/accepted/texted/chatted/flagged.

## data.json
`tracks.<regular|professionals>` has `people`, `prospects`, and `days`: `{ "YYYY-MM-DD": {follows, accepted, texts, chats, flagged} }`.

## Update (all commands accept `--date YYYY-MM-DD` for backfill; default today, Toronto)
    python3 update.py add-follow regular somehandle "Some Name"
    python3 update.py add-follow professionals agenthandle "Name" --date 2026-10-08
    python3 update.py accepted somehandle      # followed back
    python3 update.py text somehandle          # text sent (call per text)
    python3 update.py chat somehandle          # active chat
    python3 update.py flag somehandle "short note" ["Name"]   # good prospect
    python3 update.py set-day regular --date 2026-10-07 --follows 8 --accepted 2 --texts 5 --chats 1 --flagged 0   # set/override a day
    python3 update.py show [--date D]
    ./publish.sh                               # git add/commit/push (uses gh credential helper)
Auth: gh CLI logged in as harpreetsbajwa92 (same as linkedin-stats). No phone numbers in data.json.
