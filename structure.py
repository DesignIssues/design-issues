# -*- coding: utf-8 -*-
"""Volume and chapter structure for the Design Issues book.

Every essay on https://www.w3.org/DesignIssues/ is assigned to exactly one
chapter. VOLUMES is the single source of truth for reading order.
"""

VOLUMES = [
 dict(num="I", title="Axioms",
      epistemic="Design commitments, stated as principles and argued from first needs.",
      blurb="The irreducible choices. What the Web had to be for it to work at all.",
      chapters=["Principles.html","Axioms.html","NameMyth.html","Model.html",
                "Architecture.html","Abstractions.html"]),
 dict(num="II", title="Naming",
      epistemic="Architectural fact, checkable against the URI and HTTP specifications.",
      blurb="What a URI is, what it identifies, and why that question took fifteen years.",
      chapters=["HTTP-URI.html","HTTP-URI2.html","TermResource.html","Generic.html",
                "Fragment.html","Relative.html","PersistentDomains.html",
                "HTTPFilenameMapping.html","PhilosophicalEngineering.html"]),
 dict(num="III", title="Evolution",
      epistemic="Architectural fact and specification practice.",
      blurb="How a deployed system changes without breaking. Extensibility, modularity, ambiguity.",
      chapters=["Evolution.html","Extensible.html","Mandatory.html","Modularity.html",
                "Stack.html","Specification.html","Ambiguity.html","HTML-XML.html",
                "XML.html","Open.html","Webize.html"]),
 dict(num="IV", title="Meaning",
      epistemic="Proposal and specification; the parts that shipped are marked.",
      blurb="From metadata to semantics. What it takes for a document to mean something.",
      chapters=["Metadata.html","Meaning.html","NamespacesAreResources.html",
                "Semantic.html","RDFnot.html","RDF-XML.html","RDB-RDF.html",
                "Identity.html","QuotingURIs.html","TagLabel.html",
                "Interpretation.html","InterpretationProperties.html","CG.html"]),
 dict(num="V", title="Logic and Notation",
      epistemic="Proposal and specification. Notation3 and its alternatives.",
      blurb="Rules, inference, and a notation designed to be read by people.",
      chapters=["Logic.html","Rules.html","Notation3.html","N3Alternatives.html",
                "Reify.html","Diff.html","Inconsistent.html","RDF-Future.html",
                "TopTen.html"]),
 dict(num="VI", title="Linked Data and Solid",
      epistemic="Proposal, deployment record, and the contested present.",
      blurb="Four rules, a decade of data, and an attempt to give the Web back its write half.",
      chapters=["LinkedData.html","ReadWriteLinkedData.html","BagOfChips.html",
                "ConnectingScience.html","GovData.html","CloudStorage.html",
                "PodStuff.html","TabulatorGoals.html","Footprints.html","Live.html",
                "IcingOnTheCake.html","SemanticClipboard.html","Conversations.html",
                "PaperTrail.html","LookAtiCalendar.html","Feeds.html","WebServices.html"]),
 dict(num="VII", title="Trust",
      epistemic="The contested present. Positions attributed and dated.",
      blurb="Origins, certificates, CORS and snooping. Who the browser protects, and from whom.",
      chapters=["Security-ModelTrust.html","Security-NotTheS.html","Security-Origin.html",
                "Security-ClientCerts.html","WebAppDistrustCORS.html","NoSnooping.html",
                "PrivateData.html","PersonalPublic.html","Gradient.html"]),
 dict(num="VIII", title="Law",
      epistemic="Normative argument, dated. Legal facts have moved since writing.",
      blurb="Links, filtering, neutrality and names. Where Web architecture meets the courts.",
      chapters=["LinkLaw.html","LinkMyths.html","Filtering.html","NetNeutrality.html",
                "TLD.html","DRM.html","Blockchain.html"]),
 dict(num="IX", title="Interface and Society",
      epistemic="Design argument and social observation.",
      blurb="What the Web does to the people using it, and what the editor should have been.",
      chapters=["UI.html","Editor.html","UserAgent.html","UserInterface.html","Pretty.html",
                "Fractal.html","Culture.html","StretchFriend.html","Dysfunction.html",
                "Good.html"]),
 dict(num="X", title="Futures",
      epistemic="Disciplined speculation, labeled as such by its author.",
      blurb="Agents that work for you, and a world where they do.",
      chapters=["Beneficent.html","Charlie.html","Works.html","Singularity13.html",
                "Vision.html"]),
]

FRONT_MATTER = ["Preface.html"]


# ---------------------------------------------------------------------------
# The reading path: fifteen chapters that carry the whole argument, in order.
# A reader who follows only these has met every idea the book depends on.
PATH = [1, 2, 3, 16, 23, 25, 32, 49, 51, 54, 67, 71, 87, 90, 96]

# Chapters marked in the contents as worth singling out. The path, plus a few
# that are landmarks in their own right.
LANDMARKS = set(PATH) | {4, 30, 31, 40, 93, 95}

# One line per path chapter, saying what the reader gets from it. Written for
# somebody who has never heard of any of this.
PATH_BLURB = {
 1:  "Six rules for building something other people will build on. Everything else follows from these.",
 2:  "Why every single thing on the Web has an address, and what that one decision made possible.",
 3:  "Why web addresses rot, why the fix everyone proposes will not work, and what would.",
 16: "How a standard actually gets made: a cycle driven by companies competing, and its limits.",
 23: "Why the Web is full of broken pages, explained by what a page author is rewarded for.",
 25: "Ten different things people mean by \u201copen\u201d, and why arguments about it go nowhere.",
 32: "One fact written five ways. The clearest explanation in the book of why structure is not meaning.",
 49: "Four rules for publishing data anyone can use. The most quoted thing its author ever wrote.",
 51: "Five stars for open data, and a bag of crisps that explains how vocabularies mix.",
 54: "The proposal to separate your data from the apps that use it, and why that changes everything.",
 67: "An argument that the way the Web was secured broke something more important.",
 71: "What the list of pages you visited says about you, and why reading should be unobserved.",
 87: "Why a healthy society needs groups of every size, and what happens when it does not get them.",
 90: "How social networks came to work the way they do, mechanism by mechanism.",
 96: "The last chapter: its author admits he could not imagine what would be built on his own work.",
}
