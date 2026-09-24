# ═══════════════════════════════════════════════════════════════
#  VARIABLES.RPY — Persistent game state
# ═══════════════════════════════════════════════════════════════
#  PURPOSE
#    • Central home for every variable that the story READS or
#      WRITES while the player progresses.
#    • Keeping them here (instead of scattered across chapters)
#      makes save/load safe and debugging easy.
#
#  RULES
#    • Use `default` — NOT `define` — for anything mutable.
#        default = value is set once at game start, then may change.
#        define  = constant; Ren'Py forbids reassigning it.
#    • Every variable must be declared here so it exists before
#      any chapter tries to read it.
#    • Group related variables with a section banner comment.
#    • Prefer descriptive snake_case names:
#        ch1_met_nahid        (a flag)
#        affection_nahid      (a counter)
#        route_locked         (a state)
#
#  REN'PY CHEAT SHEET
#    default flag = False               # boolean flag
#    default points = 0                 # integer counter
#    default name = ""                  # string
#    default choices = []               # list (mutable!)
#    default seen = set()               # set of visited labels
#
#    To change during play:
#        $ flag = True
#        $ points += 1
#        $ choices.append("airport")
#
#    To branch dialogue:
#        if flag:
#            "..."
#        else:
#            "..."
# ═══════════════════════════════════════════════════════════════

