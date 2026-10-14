# -*- coding: utf-8 -*-
"""The glossary. Every entry is written for somebody who has never met the term.

Keep the definitions short, concrete, and free of other jargon. If an entry
needs another term to make sense, that term must have its own entry.
`ch` is the chapter where the idea is treated properly, if there is one.
"""

GLOSSARY = [
 ("URI", "Uniform Resource Identifier", 2,
  "A name for something, written so that it works anywhere in the world. "
  "Web addresses are the familiar kind. The point of a URI is that it "
  "means the same thing to everybody it is given to."),

 ("URL", "Uniform Resource Locator", 3,
  "An older word for the same thing as a URI, still in common use. This "
  "book follows its source in mostly saying URI, and treats the "
  "distinction between a name and an address as a mistake: see Chapter 3."),

 ("HTTP", "Hypertext Transfer Protocol", 20,
  "The rules a browser and a server follow when one asks the other for a "
  "page. It says how to ask, how to answer, and what the answer means."),

 ("server", None, None,
  "A computer, or a program running on one, that holds pages or data and "
  "hands them out when asked. The program doing the asking, usually a "
  "browser, is called the client."),

 ("header", None, None,
  "A labelled line at the top of a message, saying something about what "
  "follows: what kind of file it is, when it was made, how long it may be "
  "kept. Every request and reply on the Web carries several."),

 ("status code", None, 7,
  "The three-digit number at the start of a server’s reply. 200 means "
  "“here it is”, 404 “not found”, 303 “look over there instead”."),

 ("redirect", None, 8,
  "A reply from a server that, instead of the thing asked for, gives "
  "another address to try. The browser follows it, usually without the "
  "reader noticing."),

 ("httpRange-14", None, 7,
  "The name of a long argument, settled by the TAG in 2005, over whether "
  "a plain web address can name a person or an idea as well as a page. "
  "The answer was a convention: the server replies with the status code "
  "303 and points to a page about the thing."),

 ("GET", None, 2,
  "The kind of request that only asks for something. Following a link "
  "sends one. It must never change anything, so it is always safe to "
  "repeat."),

 ("POST", None, 84,
  "The kind of request that asks a server to act: place an order, send a "
  "message, add a comment. Unlike fetching, it may commit the person who "
  "sends it to something."),

 ("PUT", None, 50,
  "The kind of request that stores a document at a chosen address, "
  "replacing whatever was there."),

 ("cache", None, None,
  "A store of copies kept near the reader, so that a page fetched once "
  "need not be fetched again. Its hard part is knowing when a copy has "
  "gone out of date."),

 ("HTML", "Hypertext Markup Language", None,
  "The format web pages are written in. Text, with tags around parts of "
  "it saying this is a heading, this is a link, this is a picture."),

 ("XML", None, 17,
  "A general way of putting tags around things, from which many formats "
  "were built. Related to HTML, and more strict: a document is either "
  "well formed or it is rejected."),

 ("markup", None, None,
  "Tags written into a text to say what its parts are: this is a "
  "heading, this is a link. HTML and XML are both markup languages."),

 ("XHTML", None, 23,
  "HTML rewritten to obey the strict rules of XML, so that a page with a "
  "mistake in it is rejected rather than guessed at."),

 ("parser", None, None,
  "The part of a program that reads text written in some format and "
  "works out its structure, so that the rest of the program can use it."),

 ("JSON", "JavaScript Object Notation", None,
  "A plain, compact text format for data: lists and labelled values, "
  "nested inside each other. Most programs on the Web now exchange data "
  "in it."),

 ("media type", "also called a MIME type", 11,
  "A short label saying what kind of thing a file is: a web page, a "
  "photograph, a sound recording. It travels with the file and tells the "
  "receiving program how to read it."),

 ("fragment identifier", "the part after a #", 11,
  "The piece of a web address after the hash. It names a part of, or a "
  "view of, whatever the rest of the address names. It is never sent to "
  "the server: the browser that already has the page works it out."),

 ("scheme", "the part before the colon", 4,
  "The first word of a web address, such as https. It says which set of "
  "rules applies to the rest of the address."),

 ("DNS", "the Domain Name System", 6,
  "The system that turns a name like example.org into the machine that "
  "answers for it. It is also how the Web decides who is responsible for "
  "what: owning the name means answering for what is served under it."),

 ("domain name", None, 13,
  "A name such as example.org, rented from a registry, under which a "
  "person or organisation publishes. Whoever holds the name decides what "
  "its addresses mean, for as long as they keep paying for it."),

 ("top-level domain", None, 79,
  "The last part of a domain name, such as .org or .uk. Each is run by "
  "one organisation, which rents out the names beneath it."),

 ("ICANN", "Internet Corporation for Assigned Names and Numbers", 79,
  "The non-profit body that oversees domain names at the top, deciding "
  "which top-level domains exist and who runs each."),

 ("IP", "Internet Protocol", 6,
  "The lowest common layer of the Internet. It gives every connected "
  "machine a number, its IP address, and carries small packets of data "
  "from one number to another, without promising they arrive."),

 ("TCP", "Transmission Control Protocol", 6,
  "The layer on top of IP that makes delivery reliable: it numbers the "
  "packets, resends any that are lost and puts them back in order, so "
  "two programs can talk as if along a wire."),

 ("ISP", "internet service provider", 78,
  "The company that connects a home or office to the Internet and "
  "carries its traffic."),

 ("net neutrality", None, 78,
  "The principle that an ISP must treat all traffic alike: not block "
  "sites, not slow some down, and not charge to speed others up."),

 ("dereference", None, 49,
  "To look something up. Given a name, go and fetch what it names."),

 ("opaque", None, 2,
  "Something that may be used but not looked inside. A path in a web "
  "address is opaque to a browser, which passes it on without trying to "
  "work out what it means."),

 ("namespace", None, 17,
  "A set of terms owned by one group, so that two groups can each use the "
  "word “title” for different things without colliding."),

 ("vocabulary", "also called an ontology", 51,
  "An agreed set of terms for talking about some subject, published so "
  "that anyone can use them and mean the same thing."),

 ("Dublin Core", None, None,
  "One of the oldest vocabularies for describing documents: title, "
  "creator, date, subject and a few more. Libraries and archives use it "
  "widely."),

 ("FOAF", "Friend of a Friend", None,
  "A vocabulary for describing people and who they know: a name, a "
  "photograph, a home page, a list of friends."),

 ("schema", None, 17,
  "A description of what a document or a set of data is allowed to "
  "contain. Used to check that something is well formed before relying on "
  "it."),

 ("metadata", None, 27,
  "Data about data: who wrote a document, when, in what language, under "
  "what licence. Written so that a program, not only a person, can use it."),

 ("RDF", "the Resource Description Framework", 32,
  "A way of writing data as a pile of simple statements, each of the form "
  "“this thing has that property with this value”. Because every "
  "statement stands alone, data from different places can simply be put "
  "together."),

 ("triple", None, 32,
  "One statement in that form: a subject, a property and a value. “This "
  "page · was written by · Ora”."),

 ("graph", None, 32,
  "What a pile of such statements makes when drawn: things as dots, "
  "relationships as arrows between them."),

 ("Linked Data", None, 49,
  "Data published so that the things it mentions have addresses that can "
  "be looked up, and so that it points at other people’s data. Four "
  "rules, set out in Chapter 49."),

 ("Semantic Web", None, 30,
  "The name for the whole project of putting data, rather than only "
  "documents, on the Web. Not artificial intelligence: see Chapter 31."),

 ("ontology", None, 88,
  "A vocabulary, usually one with some structure saying how its terms "
  "relate to each other."),

 ("inference", None, 40,
  "Working out something that follows from what is already known. If "
  "every cat is an animal and this is a cat, then this is an animal."),

 ("Turtle", "and N3, its larger relative", 42,
  "A way of writing those statements down that a person can read. N3 adds "
  "rules and logic to it."),

 ("N3", "Notation3", 42,
  "Turtle with rules and logic added. Curly brackets let a group of "
  "statements be treated as one thing, so that a rule can say “if these "
  "are true, then so are those”."),

 ("SPARQL", None, 30,
  "A language for asking questions of data written as statements, the way "
  "a database query language asks questions of tables."),

 ("relational database", None, 33,
  "The ordinary kind of database, which keeps data in tables of rows and "
  "columns, with tables linked by shared values."),

 ("SQL", None, 33,
  "The standard language for asking questions of a relational database "
  "and changing what it holds."),

 ("OWL", "the Web Ontology Language", 34,
  "A language for saying how the terms in a vocabulary relate: this kind "
  "of thing is a kind of that, no two things share this value, and so on."),

 ("reification", None, 44,
  "Describing a statement as a thing, so that something can be said about "
  "it. “Jane said that”, where “that” is itself a statement."),

 ("monotonic", None, 42,
  "A system is monotonic when adding new information never withdraws an "
  "old conclusion. It matters because on the Web anyone may add "
  "information at any time, without asking."),

 ("same-origin policy", None, 68,
  "The rule that code on a page from one site may not read data from "
  "another. It is what stops a malicious page raiding somebody’s bank, "
  "and what makes combining data from several places difficult."),

 ("CORS", "Cross-Origin Resource Sharing", 70,
  "The permission a server gives so that pages from other sites may read "
  "its data, relaxing the rule above."),

 ("encryption", None, 67,
  "Scrambling a message so that only someone holding the right key can "
  "read it. A key here is a long secret number."),

 ("public key", "and private key", 37,
  "A pair of keys made together. The private one is kept secret; the "
  "public one is given to anybody. What one of the pair locks, only the "
  "other can open, which makes both encryption and digital signatures "
  "possible."),

 ("digital signature", None, 37,
  "A seal made with a private key and attached to a document. Anyone with "
  "the matching public key can check that the document came from the key’s "
  "holder and has not been altered since."),

 ("hash", None, None,
  "Two things in this book. The # sign in a web address, after which "
  "comes a fragment identifier. And a short fingerprint worked out from a "
  "piece of data, which changes completely if a single character of the "
  "data changes: used to check that a copy is exact."),

 ("TLS", "and the https prefix", 67,
  "The encryption that protects a connection, so that nobody in between "
  "can read or alter what passes."),

 ("access control", None, None,
  "The rules saying who may read or change what, and the machinery that "
  "enforces them."),

 ("OAuth", None, None,
  "A widely used scheme by which a person lets one site reach some of "
  "their data held by another, without handing over a password."),

 ("PKI", "public key infrastructure", 66,
  "The arrangement by which a handful of companies vouch for who owns a "
  "web address, which is how a browser decides a site is what it claims."),

 ("certificate", None, 69,
  "A small signed document saying that a public key belongs to a "
  "particular site or person. Browsers check one before showing a "
  "padlock."),

 ("certificate authority", None, 66,
  "A company that issues certificates and is trusted, by browsers, to "
  "have checked who it issued them to."),

 ("pod", "a personal online data store", 54,
  "A place on the Web that holds one person’s data under that person’s "
  "control, which any application may read or write with permission."),

 ("Solid", None, 54,
  "The project to build that: a person’s data in one place they own, with "
  "applications kept separate from it."),

 ("WebID", None, 54,
  "A web address that stands for a person. Looking it up gives a profile "
  "the person controls, so that one name can be used to sign in anywhere."),

 ("content negotiation", None, 10,
  "The exchange in which a browser says what forms it can handle and the "
  "server picks one. It is how a single address can serve a page in the "
  "reader’s language, or a picture in a format the device supports."),

 ("idempotent", None, 2,
  "An operation that can be repeated without further effect. Asking for a "
  "page is idempotent; buying a book is not."),

 ("API", "Application Programming Interface", 65,
  "The set of commands one program offers to others: what can be asked "
  "for, how to ask, and what comes back."),

 ("SMTP", "Simple Mail Transfer Protocol", None,
  "The rules by which email is passed from one mail server to another."),

 ("RSS", None, 64,
  "A standard format for a site’s list of latest posts. A feed reader "
  "checks the list regularly and shows what is new."),

 ("DRM", "digital rights management", 80,
  "Software that lets a film or a book be played on a person’s own "
  "machine while stopping them from copying it."),

 ("blockchain", None, 81,
  "A shared ledger, copied to every participant, to which entries can be "
  "added but not changed. No single party keeps it, so none can quietly "
  "rewrite it."),

 ("specification", "often shortened to spec", 21,
  "The document that defines a format or a protocol precisely enough that "
  "two people can build things that work together without meeting."),

 ("W3C", "the World Wide Web Consortium", None,
  "The body that publishes many of the Web’s specifications. Founded in "
  "1994 and directed for most of its history by the author of these "
  "notes."),

 ("Recommendation", None, 21,
  "The Consortium’s word for a finished specification, approved by its "
  "members after a period of testing. A W3C standard, in all but name."),

 ("RFC", "Request for Comments", None,
  "The numbered documents in which the Internet’s protocols are "
  "published. The name is a relic of when they really were requests for "
  "comment."),

 ("IETF", "the Internet Engineering Task Force", None,
  "The open body of engineers that develops the Internet’s protocols and "
  "publishes them as RFCs."),

 ("IANA", "the Internet Assigned Numbers Authority", None,
  "The office that keeps the Internet’s official lists: which media types "
  "and schemes exist, and which top-level domains, and who runs each."),

 ("TAG", "the Technical Architecture Group", None,
  "A small group at the Consortium that rules on questions about how the "
  "Web fits together. Several chapters here record arguments it settled."),

]
