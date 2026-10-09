# Instagram Stats
Live: https://harpreetsbajwa92.github.io/instagram-stats/ (repo harpreetsbajwa92/instagram-stats, GitHub Pages from main).
Two tabs: Regular (goal 8 follows/day) and Professionals (goal 2/day). Page fetches data.json live (cache-busted).

## Update
    python3 update.py add-follow regular somehandle "Some Name"
    python3 update.py add-follow professionals agenthandle "Name"
    python3 update.py accepted somehandle      # followed back
    python3 update.py text somehandle          # text sent (call per text)
    python3 update.py chat somehandle          # active chat
    python3 update.py flag somehandle "short note" ["Name"]   # good prospect
    python3 update.py show
    ./publish.sh                               # git add/commit/push (uses gh credential helper)
Auth: gh CLI logged in as harpreetsbajwa92 (same as linkedin-stats). No phone numbers in data.json.
