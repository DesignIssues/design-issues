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

 ("HTML", "Hypertext Markup Language", None,
  "The format web pages are written in. Text, with tags around parts of "
  "it saying this is a heading, this is a link, this is a picture."),

 ("XML", None, 17,
  "A general way of putting tags around things, from which many formats "
  "were built. Related to HTML, and more strict: a document is either "
  "well formed or it is rejected."),

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

 ("schema", None, 17,
  "A description of what a document or a set of data is allowed to "
  "contain. Used to check that something is well formed before relying on "
  "it."),

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

 ("SPARQL", None, 30,
  "A language for asking questions of data written as statements, the way "
  "a database query language asks questions of tables."),

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

 ("TLS", "and the https prefix", 67,
  "The encryption that protects a connection, so that nobody in between "
  "can read or alter what passes."),

 ("PKI", "public key infrastructure", 66,
  "The arrangement by which a handful of companies vouch for who owns a "
  "web address, which is how a browser decides a site is what it claims."),

 ("pod", "a personal online data store", 54,
  "A place on the Web that holds one person’s data under that person’s "
  "control, which any application may read or write with permission."),

 ("Solid", None, 54,
  "The project to build that: a person’s data in one place they own, with "
  "applications kept separate from it."),

 ("content negotiation", None, 10,
  "The exchange in which a browser says what forms it can handle and the "
  "server picks one. It is how a single address can serve a page in the "
  "reader’s language, or a picture in a format the device supports."),

 ("idempotent", None, 2,
  "An operation that can be repeated without further effect. Asking for a "
  "page is idempotent; buying a book is not."),

 ("specification", "often shortened to spec", 21,
  "The document that defines a format or a protocol precisely enough that "
  "two people can build things that work together without meeting."),

 ("W3C", "the World Wide Web Consortium", None,
  "The body that publishes many of the Web’s specifications. Founded in "
  "1994 and directed for most of its history by the author of these "
  "notes."),

 ("RFC", "Request for Comments", None,
  "The numbered documents in which the Internet’s protocols are "
  "published. The name is a relic of when they really were requests for "
  "comment."),

 ("TAG", "the Technical Architecture Group", None,
  "A small group at the Consortium that rules on questions about how the "
  "Web fits together. Several chapters here record arguments it settled."),

]
