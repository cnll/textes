// This function gets your whole document as its `body` and formats
// it as a simple report.
#let pressrelease(
  title: "TITLE",
  author: "CNLL",
  date: "DRAFT",
  paper: "a4",
  version: "draft",
  body,
) = {
  // Set the document's metadata.
  set document(title: title, author: author)

  // Configure the page properties.
  set page(
    paper: paper,
    margin: (bottom: 1.75cm, top: 2.25cm),
  )

  set text(12pt, font: "Rosario")

  // Configure paragraph properties.
  set par(
    leading: 0.78em,
    first-line-indent: 2em,
    justify: true,
  )
  // show par: set block(spacing: 0.78em)

  // Configure page properties.
  set page(
    numbering: "1",

    // The header always contains the book title on odd pages and
    // the chapter title on even pages, unless the page is one
    // the starts a chapter (the chapter title is obvious then).
    header: locate(loc => {
      // Are we on an odd page?
      let i = counter(page).at(loc).first()
      // if calc.odd(i) {
      //   return text(0.95em, smallcaps(title))
      // }

      // Are we on a page that starts a chapter? (We also check
      // the previous page because some headings contain pagebreaks.)
      let all = query(heading, loc)
      if all.any(it => it.location().page() in (i - 1, i)) {
        return
      }

      // Find the heading of the section we are currently in.
      let before = query(selector(heading).before(loc), loc)
      if before != () {
        align(right, text(0.95em, smallcaps(before.last().body)))
      }
    }),
  )

  // Configure headings.
  show heading: it => {
    if it.level == 2 [
      #set text(weight: "bold")
      #set par(leading: 0.6em)
      #set block(above: 2.5em, below: 1.5em)
      #it
    ]
    if it.level == 3 [
      #set text(1.1em, weight: "semibold", style: "italic")
      #set par(leading: 0.6em)
      #set block(above: 2em, below: 1.5em)
      #it
    ]
  }

  // Underline links
  show link: it => [
    // #set text(color: blue)
    #text(blue)[
      #underline(stroke: 1pt + blue, offset: 3pt)[#it]
    ]
  ]

  // Display the title
  v(3pt, weak: true)
  align(center, text(20pt, title))
  v(3em, weak: true)

  // Display the version
  align(center, text(version))
  v(1em)

  body
}
