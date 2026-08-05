"""Single source of truth for the Kairos design notebook.

Everything the page says lives here as data. gen_page.py renders it and check_page.py
enforces the rules that a human would otherwise forget — most importantly that the page
names its own project in the h1, which is the mistake we already made once on ATexamples.

The prose is deliberately written for someone with no context. This page exists to be
pasted to people who weren't in the conversation.
"""
from __future__ import annotations

PROJECT = "Kairos"
DOC_TYPE = "Design notebook"
SUBTITLE = (
    "An open record of a weak-signal detection system — one that looks for opportunities before "
    "they go viral. The premise, the objections that nearly killed it, the narrower thing that "
    "survived, and what happened when it was actually built."
)
UPDATED = "2026-08-05"

# Tabs are jobs, not chapters. Each one answers a question a reader actually arrives with.
TABS = [
    ("premise", "The premise"),
    ("holds", "What holds up"),
    ("breaks", "Where it breaks"),
    ("design", "What to build"),
    ("open", "Open questions"),
    ("built", "What the build found"),
    ("reply", "For ChatGPT"),
]

# --- The seven stages. Also drives the ladder figure. ---
STAGES = [
    ("1", "Enabling condition changes",
     "A law changes, a component gets cheap, a platform appears, something hard becomes easy."),
    ("2", "Specialists experiment",
     "Researchers, developers, hobbyists and obsessives start building before anyone can say why it matters."),
    ("3", "Repeated problems appear",
     "The same questions, the same obstacles, the same awkward improvised workarounds, from unrelated people."),
    ("4", "Money begins moving",
     "Hiring, procurement requests, small vendors selling out, capital spending showing up in filings."),
    ("5", "Entrepreneurs flood in",
     "The category fills. Margins start compressing before most people have heard the name."),
    ("6", "The media names it",
     "It gets a label. The label is the thing that makes it legible — and copyable."),
    ("7", "Everyone hears about it",
     "Search volume goes vertical. By now the opportunity is a job, not an opening."),
]
DETECT_FROM, DETECT_TO = 2, 4

PREMISE_READS = [
    ("Popularity is a lagging indicator.",
     "The usual instinct is to watch for things getting popular. But popularity is the "
     "*result* of an opportunity being taken, not the signal that one exists. By the time a "
     "thing trends, the people who profited from it are already positioned. What you want "
     "instead is the state that precedes it: demand, capability or behaviour changing faster "
     "than supply can respond. Imbalance is the early signal. Popularity is the receipt."),
    ("Most trend tools measure stage six.",
     "Search-volume tools, social listening, and news monitoring nearly all sit at stages five "
     "through seven of the ladder below. They're not wrong, they're just late by construction — "
     "they measure attention, and attention is what arrives after the fact. That isn't a "
     "criticism of the tools. It's a statement about which question they answer."),
]

FADS_CARD = {
    "title": "The uncomfortable part: fads are not predictable",
    "body": (
        "The examples people reach for — Beanie Babies, cupcake shops, homebrew — are mostly "
        "<em>fads</em>, and fads are close to a coin flip even with perfect data. At time zero, "
        "Beanie Babies was not distinguishable from the five hundred collectibles that went "
        "nowhere with identical early signals. No amount of data fixes this, because the outcome "
        "was determined by mimetic dynamics that hadn't happened yet. Looking backward makes "
        "every precursor seem meaningful; that's hindsight, not signal."
    ),
    "tail": (
        "Homebrew is the exception in that list, and it's instructive: it wasn't really a fad. It "
        "was a regulatory unlock — states finishing legalisation through the eighties and "
        "nineties — plus a taste shift driven by the microbrewery boom. Both were visible years "
        "ahead. That's the class worth chasing."
    ),
}

HOLDS = [
    ("The reframe is correct",
     "Imbalance over popularity. It's the whole game, and it reorganises everything downstream."),
    ("The stage ladder is a real contribution",
     "Naming seven stages, and locating the detector at two through four, is the most useful "
     "structural idea in the design. It converts a vague instinct into a placement decision."),
    ("Trend strength and business usefulness must be separate",
     "A topic can score brilliantly as a trend and terribly as an opportunity. Millions of people "
     "discussing a film is a trend. A growing group of cinema owners asking where to get one "
     "specific piece of equipment, when two suppliers exist, is an opportunity. Most tools "
     "collapse these and become useless."),
    ("Point-in-time replay is non-negotiable",
     "You must be able to replay what the system knew on 1 March without letting it glimpse "
     "15 March. That's look-ahead leakage, and it's the single most common way a backtest ends "
     "up lying to you."),
    ("Convergence beats volume",
     "Several unrelated papers, plus new repositories, plus deployment questions, plus a hiring "
     "signal — while ordinary consumer search stays flat — is a fundamentally different object "
     "from ten thousand posts descended from one viral video. Independence of origin is the "
     "thing being measured, not count."),
    ("The output should be a card with kill conditions",
     "Who might pay, the cheapest test that could kill it, the evidence against, and the "
     "conditions under which you walk away. That turns “something interesting is happening” into "
     "something you can be wrong about on a schedule."),
    ("Alert, don't trade",
     "Any securities branch should produce research alerts, never automatic positions. Stock "
     "chatter is the easiest signal class in the world to manufacture, and “early” there often "
     "means being someone else's exit liquidity."),
]

# --- The objections. `weight` drives the visual emphasis. ---
BREAKS = [
    {
        "id": "weights",
        "weight": "fatal",
        "title": "You cannot learn the weights",
        "claim": "The design ends with “the weights should be learned through historical replay.” "
                 "That sentence is load-bearing for the whole system, and it will not work.",
        "why": "The score has nine free parameters, eleven counting the dampeners. Learning eleven "
               "weights needs labelled outcomes: real opportunities, and things that looked "
               "identical and died. Realistically you can assemble thirty to fifty by hand, every "
               "one arguable. Eleven parameters against fifty noisy subjective labels isn't "
               "learning — it's overfitting with a scientific vocabulary.",
        "worse": "The label set is contaminated at source. You'll draw positives from memory, so "
                 "you'll draw famous ones, so you're selecting on outcome — the exact survivorship "
                 "bias the design warns about elsewhere. And fair negatives barely exist: something "
                 "that looked promising at the time and died quietly leaves almost no record. Your "
                 "negative class will be systematically easier than reality.",
        "fix": "Set the weights by hand, keep them few and crude, and use replay only to <em>reject</em> "
               "the system — never to tune it. Replay answers one question: would this have fired on "
               "what mattered, before it mattered, without firing on everything? If no, you don't "
               "adjust and retry. That's fitting the test set by hand. You change the sources, or you stop.",
    },
    {
        "id": "product",
        "weight": "high",
        "title": "Multiplying nine estimates compounds nine errors",
        "claim": "A score built as a product of nine sparse estimates is fragile in a way the formula hides.",
        "why": "Each factor is a guess from thin evidence — often literally ten mentions. One factor "
               "off by 2× moves the result by 2×. One near zero annihilates everything, including "
               "things that should have surfaced.",
        "worse": "And a cardinal score isn't even the output you need. The decision this supports is "
                 "“which ten do I read on Sunday.” Three decimal places imply a precision the inputs "
                 "cannot support.",
        "fix": "Hard gates plus a shallow rank. Gates are boolean and disqualifying — no identifiable "
               "payer, saturation already high, all evidence traceable to one origin, window shorter "
               "than your action latency. What survives gets ranked on three things: convergence "
               "breadth, acceleration, evidence quality. Three hand-set weights you can reason about "
               "beat eleven learned ones you can't.",
    },
    {
        "id": "archive",
        "weight": "high",
        "title": "Half the sources have no replayable history — and it's the wrong half",
        "claim": "Backtesting is named as indispensable, but roughly half the proposed sources cannot be replayed at all.",
        "why": "The unavailable half is exactly where the design puts its <em>demand</em> evidence: "
               "repeated questions, complaints, improvised workarounds, hiring language. So the parts "
               "you most want to validate are the parts you cannot validate.",
        "worse": "There's a quieter version of the same trap. Business-formation and labour series get "
                 "revised after publication. Backtest against today's revised numbers and you've leaked "
                 "the future into the past without noticing. You need vintage data — the numbers as "
                 "printed on the day.",
        "fix": "Build v1 preferentially on archive-replayable sources, even where they're weaker signals, "
               "because otherwise the backtest tells you nothing and you're flying on vibes. Add the "
               "unarchivable sources later as live-only enrichment, and be honest that their "
               "contribution is untested.",
    },
    {
        "id": "clusters",
        "weight": "med",
        "title": "Semantic clustering is harder than the example makes it look",
        "claim": "The worked example — local AI agents, private inference, on-device models, sovereign "
                 "AI, edge deployment — is chosen to be easy. Those phrases already sit near each other.",
        "why": "Genuinely early signals are <em>descriptive rather than named</em>, because nobody had a "
               "word yet. “I got the model running on my own box so client files never leave the "
               "building” will not reliably embed next to “sovereign AI.” By the time the noun exists, "
               "you're at stage four.",
        "worse": "Cluster identity also drifts. What meant one thing in March may have absorbed something "
                 "else by June — your time series is now measuring a different object and nothing tells "
                 "you. Tracking cluster identity over time is a genuinely open problem, not a pipeline box.",
        "fix": "Anchor on stable identifiers: repositories, companies, filing numbers, industry codes, "
               "bill numbers, patent classes. Entities don't drift. Treat text clustering as a secondary "
               "corroborating layer over an entity spine, never as the spine.",
    },
    {
        "id": "burst",
        "weight": "med",
        "title": "The burst maths has no power at the volumes that matter",
        "claim": "A log-ratio against a moving-average baseline breaks at exactly the counts you care about.",
        "why": "At three mentions, then eight, the baseline is mostly zeros — so any single event produces "
               "an enormous deviation. The system fires constantly on everything obscure, which is "
               "everything. Classical burst detection is the right family but was designed for document "
               "streams with real volume.",
        "worse": "The design half-catches this and treats it as a normalisation problem. It's a "
                 "distributional one.",
        "fix": "A minimum-evidence gate that simply refuses to score below a floor does about ninety "
               "percent of the work. The sophisticated count model buys very little on top. Take the "
               "simple one.",
    },
    {
        "id": "precision",
        "weight": "high",
        "title": "Nobody asked what precision makes this worth reading",
        "claim": "This is the omission that should decide whether the thing gets built at all.",
        "why": "Say it surfaces twenty candidates a week and — generously — one in forty is real. That's "
               "one genuine lead a fortnight, arriving inside thirty-nine duds, each costing reading time "
               "and a little self-credibility.",
        "worse": "So the real question was never “can we detect weak signals.” It's triage economics: is "
                 "one real lead per fortnight worth twenty cards a week plus the build plus the "
                 "maintenance?",
        "fix": "Estimate that number before writing a collector, and re-estimate it from the prediction "
               "log after eight weeks. Agree the shutdown threshold in advance, while it's still cheap "
               "to be objective about.",
    },
    {
        "id": "manipulation",
        "weight": "med",
        "title": "The manipulation checks target yesterday's manipulation",
        "claim": "Penalising repost chains and affiliate campaigns is right, but that's the naive attack.",
        "why": "Star-farming on code repositories is a service you can buy today. Companies post roles "
               "they have no intention of filling, to signal direction. And filing language is the worst "
               "offender — mentions of “AI” in annual reports went vertical with no matching change in "
               "capital spending.",
        "worse": "Keyword presence in filings is close to worthless. Dollars in filings are not.",
        "fix": "Prefer signals that <em>cost the sender something</em>. A business registration costs a fee "
               "and an intention. Capital expenditure costs money. A filled job costs salary. A repo star "
               "costs nothing, a press release less. Weight by cost-to-fake and most of the manipulation "
               "problem dissolves without any adversarial detection at all.",
    },
    {
        "id": "adversary",
        "weight": "med",
        "title": "Two hallucinations arguing don't produce a truth",
        "claim": "The prospector / sceptic pair is a good idea that doesn't fix what it appears to fix.",
        "why": "Both agents are the same model with the same blind spots, reading the same sparse "
               "evidence. A small local model asked to argue against a thesis will produce a fluent, "
               "confident, plausible counter-argument whether or not the thesis is wrong.",
        "worse": "Adversarial framing feels like verification. It isn't, when both sides share a prior.",
        "fix": "The fix isn't more agents, it's binding generation to evidence. Every claim either cites a "
               "specific ledger row by ID or gets stripped before the card renders. The model connects and "
               "interprets retrieved rows. It never supplies facts of its own.",
    },
    {
        "id": "stack",
        "weight": "low",
        "title": "The stack is over-specified for a v1 that doesn't exist",
        "claim": "Two languages, two databases, columnar snapshots, embeddings and a local model — before "
                 "the first card exists.",
        "why": "That's a three-month build that front-loads every infrastructure decision to the moment "
               "you know the least.",
        "worse": "",
        "fix": "One process, one database file, one scheduled job. Add the rest when a collector is "
               "provably too slow — which it won't be, because the whole corpus is a few hundred thousand "
               "rows a month.",
    },
]

# --- The pipeline reorder: the one structural change worth making. ---
REORDER = {
    "title": "Put the fit filter first, not last",
    "lede": (
        "In the proposed pipeline, fit — with your abilities, capital, location and access — is a "
        "multiplier at the very end, after collection, clustering, burst detection, convergence "
        "analysis and agent evaluation. Everything gets fully processed, and then most of it gets "
        "multiplied by something near zero."
    ),
    "body": (
        "For any individual operator the fit filter is brutally tight. Solo, no capital at risk, no "
        "licence, no premises, no staff. That combination eliminates the overwhelming majority of "
        "anything the world would call an opportunity. Applied at the front, the system stops "
        "scanning the world and starts scanning the small slice of it you could actually act on — "
        "twenty to thirty times less to collect, cluster, score and read."
    ),
    "kicker": (
        "It also raises precision, because most false positives in a general system are things that "
        "are genuinely happening but that you could never touch. The same logic applies to timing: "
        "being early only pays if you can act before the window shuts. If your realistic action "
        "latency is weeks, anything with a sub-two-month window is worthless to detect no matter how "
        "cleanly you detect it. That single gate prunes almost the entire consumer-fad branch."
    ),
}

PIPELINE = [
    ("Fit gate", "Solo-executable, no capital at risk, no licence, window over two months."),
    ("Evidence floor", "Minimum row count from minimum distinct sources before anything is scored at all."),
    ("Convergence", "At least two independent origins, weighted by cost-to-fake."),
    ("Saturation check", "If mainstream search or ad load is already moving, flag as late and demote."),
    ("Card", "Rendered with every claim bound to a ledger row ID. Uncited claims are stripped."),
]

FEASIBILITY = [
    ("ok", "Solved and easy",
     "Detecting statistically unusual activity in a stream. Well understood; off-the-shelf methods work."),
    ("warn", "Hard but tractable",
     "Detecting unusual activity with a <em>legible cause</em> — a rule changed, a price crossed a "
     "threshold, a capability arrived. Long lead times, traceable mechanism, and no machine learning "
     "required. Good collectors and a filter. This is where the value is."),
    ("bad", "Not solvable — stop promising it",
     "Predicting which consumer fads take off. Cut the branch, or demote it to something honest: detect "
     "fads at stage four or five — too late to <em>be</em> the fad — and route them to the "
     "picks-and-shovels question instead. Cupcake bakeries were saturated by 2005; commercial pan "
     "suppliers and franchise consultants had room for years."),
]

BINDING_CONSTRAINT = (
    "The binding constraint on this whole project is not the algorithm. It's labelled outcome data. "
    "You cannot learn this function, because you cannot assemble a training set that isn't "
    "contaminated. What you can do is encode your priors explicitly, log every prediction with a date, "
    "and find out in six months whether the priors were any good. That's a slower, less impressive, and "
    "far more honest machine."
)

# --- Sources, scored on the two axes that actually decide inclusion. ---
SOURCES = [
    ("Federal Register + state bill trackers", "yes", "high", "Regulatory unlock. Longest lead time, cleanest causality."),
    ("Business formation statistics (weekly, by industry code)", "yes", "high", "People committing money before the press notices."),
    ("Securities filings — capital spending, not keywords", "yes", "high", "Dollars are expensive to fake. Nouns are free."),
    ("Public code-hosting event archives", "yes", "low", "Deep history available. But stars are purchasable — weight accordingly."),
    ("Preprint metadata", "yes", "med", "Complete and dated. Stage-two signal for technical domains."),
    ("Technical news aggregators", "yes", "low", "Full history via search API. Corroboration only, never primary."),
    ("Consumer search volume", "yes", "n/a", "Included deliberately as a <em>saturation gauge</em>. If it moves, we're late."),
    ("Forums and chat communities", "no", "low", "Archives largely closed. Live-only enrichment; contribution untested."),
    ("Job postings", "no", "med", "No affordable historical corpus. Nobody sells you 2019's listings."),
]

OPEN_QUESTIONS = [
    ("Which domain does v1 point at?",
     "The obvious answer is the one where the operator's technical understanding is deepest, because "
     "they can judge a card in thirty seconds rather than thirty minutes. But that's also the most "
     "crowded category. The regulatory and business-formation channels are far less watched, and the "
     "edge may be larger there precisely because judging them is slower. Undecided, and it's the "
     "decision that should be made before a line of collector code is written."),
    ("What is the honest precision target?",
     "Unknown until it runs. The commitment worth making now is the shutdown rule, not the target: "
     "after eight weeks, if the digest hasn't produced one candidate that led to a real action, and "
     "the ninety-day review shows no call that landed, it gets turned off. Not tuned. Turned off."),
    ("Does entity-spine anchoring actually beat text clustering?",
     "Asserted here, not demonstrated. It's a testable claim — build both over the same window and "
     "compare how often each produces a coherent time series. Nobody has run that."),
    ("How much does cost-to-fake weighting really buy?",
     "The principle is sound but the weights are guesses. This is exactly the kind of parameter that "
     "cannot be learned from fifty labels, so it stays a hand-set prior with a note attached."),
]

REPLY_TO_CHATGPT = {
    "lede": (
        "This page exists partly so the design's original author can respond to the critique directly. "
        "The design being examined here is a good one — better than most systems design I've seen from "
        "a model — and the objections below are meant as engineering, not as a takedown. Four points "
        "where a response would genuinely change what gets built:"
    ),
    "points": [
        ("On learned weights",
         "Is there a formulation that survives the labelling problem? Specifically: a way to get "
         "supervision that isn't selected on outcome. Semi-supervised approaches, or learning a ranking "
         "from pairwise human judgements rather than from outcomes, might work — but pairwise judgements "
         "of <em>early</em> signals are themselves contaminated by hindsight. If there's a way through "
         "this, it changes the whole design."),
        ("On the archive asymmetry",
         "Is there a demand-side source with genuine replayable history that's been overlooked? This is "
         "the biggest practical gap. Everything on the supply and capability side is archived; almost "
         "nothing on the demand side is. A single good archived demand source would be worth more than "
         "any modelling improvement."),
        ("On fit-first ordering",
         "Any objection to moving fit from a terminal multiplier to a front gate? The efficiency argument "
         "seems clear, but there may be a cost: a hard front gate can't surface adjacent opportunities "
         "that a soft terminal multiplier would have merely demoted. How much does that matter in practice?"),
        ("On the consumer-fad branch",
         "Is the claim that fads are unpredictable too strong? The position taken here is that at time "
         "zero the eventual winners are statistically indistinguishable from the failures, and that "
         "hindsight manufactures the apparent precursors. If there's a counter-case — a fad class with "
         "genuine ex-ante structure — it deserves to be made, because it would restore a whole branch of "
         "the design."),
    ],
}


# --- Added 2026-08-05, after the thing was built. -----------------------------
#
# The rest of this file is the argument as it stood before any code existed. It has NOT been
# edited to match what happened — that's the point of an open notebook. Corrections attach; they
# don't replace. What follows is the record of contact with real data.

BUILT_LEDE = (
    "The design above was written before a line of code existed. Then it was built: nine "
    "collectors, five candidate builders, an append-only ledger, around three hundred tests, and "
    "a digest that mails itself once a week. This section records what survived contact with real "
    "data, what was strengthened, and what broke — including the places where the author of the "
    "critique above committed the exact error the critique warns about."
)

BUILT_CONFIRMED = [
    ("The archive asymmetry was worse than the objection claimed",
     "The original objection was that demand-side sources mostly lack replayable history, so the "
     "part you most want to validate is the part you cannot. Reality went further. The dominant "
     "secondary-market platform has closed sold-price data to new developers entirely — not "
     "merely unarchived but unavailable live, at any price, with the old endpoint decommissioned "
     "and no paid tier that restores it. A free remote-jobs feed returns a salary field that is "
     "zero on every single posting. So parts of the demand side aren't just unbacktestable; "
     "they're unobservable. The objection understated the problem."),
    ("The convergence requirement worked, by producing nothing",
     "One class was deliberately gated on evidence from two unrelated origins, on the grounds "
     "that a single source naming something is indistinguishable from one party manufacturing "
     "its own trend. It sat silent through the entire build — candidates were being constructed "
     "and every one was rejected. That silence was the gate doing its job, and it was the single "
     "most tempting thing to weaken. It only started producing when a genuinely independent "
     "second origin arrived: research preprints, which share no incentive and no timescale with "
     "corporate disclosure."),
    ("Costly-to-fake signals really are better",
     "The best free signal turned out to be regulatory filings, because companies are legally "
     "obliged to disclose material risks and a statement in a filing carries legal exposure. And "
     "the useful number there is not mentions but *distinct filers* — ten filings from one "
     "company is one company with a house style. Volume can be manufactured by a single verbose "
     "party; independent identities cannot."),
]

BUILT_BUGS = {
    "title": "Three real defects, all of the same kind",
    "lede": (
        "None of these announced themselves. Nothing crashed, no test failed at the time, and "
        "every one produced confident output that was quietly wrong. That is the failure mode "
        "worth designing against, because it is the one you ship."
    ),
    "items": [
        ("A ranking sorted by a hand-typed constant",
         "A ranker led with a number a human had typed into a configuration file — an estimate of "
         "how long a problem had been open. Because the strongest candidates all tied on the "
         "measured criterion, that guess became the effective sort key. The system was ranking by "
         "its author's priors while appearing to rank by evidence. Found by a reader who couldn't "
         "see the code, noticed a candidate that looked strong sitting below the cut, and said so."),
        ("A threshold in the wrong units",
         "An evidence floor required five observations. In most classes an observation is one "
         "mention, so that means five mentions. In one class an observation was already an "
         "aggregate summarising eighty-eight papers or twelve distinct companies — so the floor "
         "silently meant 'require five separate sources', a bar nothing could ever clear. The "
         "number was defensible; the unit was not."),
        ("Two call sites drifting apart",
         "The same list of builders existed in two commands. One got updated and the other "
         "didn't, so two entire classes were present in one view of the system and silently "
         "absent from the other. Neither errored."),
    ],
}

BUILT_DISCIPLINE = {
    "title": "The author committing the error the notebook warns about",
    "body": (
        "The central objection on this page is that you cannot learn the weights — that tuning "
        "parameters until they produce the answer you wanted is overfitting with a scientific "
        "vocabulary. During the build, a reader pointed at a candidate ranked just below the cut "
        "and said it looked close."
    ),
    "tail": (
        "What followed was a new weighting parameter, justified by a genuinely plausible argument "
        "about one signal arriving earlier in the sequence than another. The argument may even be "
        "correct. But it was only sought after someone pointed at a specific candidate, which "
        "makes it motivated reasoning regardless of whether it is true — and it did not change "
        "that candidate's rank anyway. It was reverted, and the reasoning left in place as a "
        "comment marking where the temptation was. A parameter invented to reach a conclusion, "
        "which then fails to reach it, has nothing at all going for it."
    ),
}

# The design's original author reviewed the published page and answered the four questions.
# Two of the answers were good enough to change the system the same day; one refuted a claim
# made on this page. Recorded here because an open notebook that only logs its own wins isn't one.
REVIEW = {
    "lede": (
        "The page was sent back to the author of the design it critiques. The reply engaged with "
        "the argument rather than defending the original, and three of its points were acted on "
        "within hours. One of them refuted a claim made above."
    ),
    "refuted": {
        "title": "Refuted: 'there is no replayable demand-side source'",
        "body": (
            "The objection above said demand-side data mostly lacks replayable history, so the "
            "part you most want to validate is the part you cannot. That was too strong. The "
            "archive is not absent — it is <em>fragmented by market</em>, and each fragment is "
            "real: developer demand in question-and-answer site data dumps published since 2009; "
            "governmental demand in federal solicitations and awards, where a solicitation is "
            "expressed intent and an award is proof somebody paid; labour demand in archived "
            "job-openings releases, whose *archived* form preserves what was published at the "
            "time rather than today's revisions; and enterprise demand in purchase commitments "
            "and capital spending inside filings."
        ),
        "tail": (
            "The consequence is a design change, not just a correction: what's needed is "
            "domain-specific demand adapters rather than one general demand collector. One "
            "caveat the reply didn't carry — the question-and-answer dumps were moved behind "
            "authentication by their publisher in 2024 and community reuploads were discouraged, "
            "so that source survives on volunteer effort and should be treated as fragile."
        ),
    },
    "adopted": [
        ("An exploration lane",
         "Ten to twenty percent of each digest should be sampled from candidates just below the "
         "cut. Without it the output only ever contains what the ranking already liked, so any "
         "signal drawn from which cards get acted on is conditioned on the ranking's own "
         "preferences — learning from that could only ever confirm it. Implemented the same day, "
         "and deterministically rather than randomly, because randomness would silently destroy "
         "the replay guarantee the ledger is built around."),
        ("Log every surfaced candidate, not only the ones acted on",
         "This was stated as a principle in the original evaluation and turned out never to have "
         "been built: cards were rendered, emailed, and gone. There was nothing for a ninety-day "
         "review to read. Now written to an append-only table before the email is attempted, so a "
         "failed send cannot lose the week's record."),
        ("Say when a human's guess decided a rank",
         "The suggestion was a percentage split between measured evidence and configured priors. "
         "Implemented differently: a tuple sort is lexicographic, so the first term decides unless "
         "it ties and a percentage would be fiction. What is answerable exactly is <em>which term "
         "broke the tie against the next candidate</em>. Each card now names it, and shouts when "
         "that term was a human estimate. It fired on the first real slate."),
    ],
    "pushback": {
        "title": "Accepted pushback: the shutdown rule was too blunt",
        "body": (
            "The original rule was a single test at eight weeks. The objection: eight weeks is "
            "enough to judge whether the <em>machine</em> works — whether collectors run, cards "
            "are readable, evidence is bound, garbage is controlled — and nowhere near enough to "
            "judge whether a detector built for rare events has found one. A system producing one "
            "excellent opportunity every six months would have been killed at week eight."
        ),
        "tail": (
            "Now staged: at eight weeks, shut down if the output is noisy, untrustworthy or "
            "unreadable. At ninety days, shut down or narrow the domain if no prediction has "
            "survived review. At a hundred and eighty days, shut down if no card has produced an "
            "economically meaningful action — and <em>avoided mistakes count</em>. Demonstrating "
            "that a seductive trend is already saturated is output the original rule couldn't "
            "credit."
        ),
    },
}

# Two design findings from building the near-miss lane, both general enough to be worth writing
# down: they're about what an opportunity system can honestly offer an operator, not about any
# particular operator.
ADJACENCY = {
    "title": "The near-miss lane, and why \u201cfind a partner\u201d is not an answer",
    "lede": (
        "Filtering hard on operator fit buys enormous precision and costs the ability to notice "
        "anything one step outside the operator's current shape. A separate, capped section for "
        "near-misses recovers some of that \u2014 things blocked on exactly one missing thing. "
        "Building it produced two corrections worth generalising."
    ),
    "items": [
        ("\u201cFind a partner\u201d is a category, not an action",
         "It has no defined first step, no deadline anyone else imposes, rejection built into the "
         "process, and an unbounded timeline. For an operator whose binding constraint is "
         "starting things, that is the worst possible shape of instruction \u2014 worse than "
         "relocating, which at least comes with lease dates and booked trucks. And a partner who "
         "shares the operator's existing constraints removes nothing. So these cards never say "
         "\u201cfind a partner\u201d. They name the specific missing capability and its "
         "magnitude, because the real question is whether this is someone you could plausibly "
         "ask, and fourteen thousand and four hundred thousand are the same category of blocker "
         "and completely different conversations."),
        ("Some constraints are non-delegable, and the system had to be told",
         "The first build cheerfully offered a physician post as \u201cone partner away\u201d. "
         "It isn't. A partner can fund a venture or hold a licence <em>for a business</em>; they "
         "cannot be qualified on your behalf so you can take a job. Employment is excluded from "
         "the lane entirely. The general form: before offering to route around a constraint, "
         "check whether that constraint is attached to the opportunity or to the person."),
        ("An unsized blocker is not a near-miss",
         "The first build filled the section with \u201cneeds capital, amount unknown\u201d. "
         "That isn't an opportunity blocked on a funder; it's one nobody has costed. It conveys "
         "nothing at a glance, which was the section's only purpose. Unknown magnitude is now a "
         "reason to exclude rather than a value to display."),
    ],
}

CONTAMINATION = {
    "title": "Six fake rows in the evidence ledger",
    "body": (
        "An early test run wrote six synthetic records into the production ledger, because a "
        "monkeypatch redirecting the database path silently didn't take effect. They sat there "
        "generating plausible cards \u2014 with titles like \u201cOpens A Market\u201d \u2014 "
        "for hours, indistinguishable in the output from real ones."
    ),
    "tail": (
        "The cleanup was trivial. The lesson isn't: an evidence store whose whole value is that "
        "its contents are real has no defence against test data except one that is enforced "
        "rather than remembered. The suite is now pointed at a throwaway directory before any "
        "module loads, and opening the real ledger during a test raises. Prevention, because "
        "cleanup requires noticing, and nobody noticed."
    ),
}

BUILT_STILL_UNPROVEN = [
    ("No backtest has run",
     "The ledger was built so that replay is possible and safe — every read requires a cutoff, and "
     "revised figures append rather than overwrite, so replaying to a past date shows what was "
     "known then rather than today's corrections. None of that machinery has been exercised. "
     "Until it is, no claim about whether the system works is supportable."),
    ("Nothing has been acted on",
     "It produces cards. No card has been acted on, and no prediction has been scored. The "
     "prediction log exists as a field on every card and is empty."),
    ("The central claim remains untested",
     "The objection that the weights cannot be learned still stands, because nothing has been "
     "learned. All thresholds are hand-set and crude, exactly as recommended. Whether that is "
     "sufficient is the open question the next six months answer."),
]
