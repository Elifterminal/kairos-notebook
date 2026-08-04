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
    "An open record of a proposed weak-signal detection system — one that looks for "
    "opportunities before they go viral. The premise, the objections that nearly killed it, "
    "and the narrower thing that survived."
)
UPDATED = "2026-08-04"

# Tabs are jobs, not chapters. Each one answers a question a reader actually arrives with.
TABS = [
    ("premise", "The premise"),
    ("holds", "What holds up"),
    ("breaks", "Where it breaks"),
    ("design", "What to build"),
    ("open", "Open questions"),
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
