# Markdown

## Basic Syntax

This part of Markdown is supported by nearly all Markdown apps, though various variations may occur.

### Headings

To create a heading, add a number sign (#) in front of a word or phrase. The number of signs 
corresponds to the heading level (one for \<h1>, two for \<h2>, etc.).

```markdown
# Heading level 1

## Heading level 2
```

For \<h1> and \<h2>, the following alternative syntax is also possible:

```Markdown
Heading level 1
===============

Heading level 2
---------------
```

It's best practice to always include a space between the number sign and the heading, and to put
blank lines before and after a heading.

### Paragraphs

Paragraphs are simply lines of text, separated from others by blank lines. They should never be
indented, unless they are part of a list.

#### Line Breaks

To insert a line break, you can end a line with two spaces then hit Return. This will usually work,
but this choice has been controversial, since it's hard to see trailing whitespace, and it can 
easily be added by accident. Another option is to use the **\<br>** HTLM tag, since many Markdown
apps support HTML (but not all). Some other apps may have custom ways to insert line breaks, but 
none are widely support everywhere, so stick to either trailing whitespace or the **\<br>** tag.

#### Emphasis

You can bold text by surrounding it with either two asterisks (**) or two underscores (__) on each
side. Asterisks have the advantage that they can also be used inside a word, so they should be
preferred.

You can italicize text by surrounding it with either one asterisk (*) or one underscore (_) on each
side. Likewise, asterisks have the advantage that they can be used inside a word, so they should be
prefered here too.

You can both italicize AND bold text by surrounding it with either three asteriks (***), three
underscores (___), or a mix of them (two asteris + one underscore, or vice versa) on each side. 
Again, only asterisks can be used inside a word.

Overall, favor asterisks. One on each side to italize, two on each side to bold, and three on each
side to both bold and italicize.

### Blockquotes

You can create a block quote by starting a line with **>**. A blockquote can have multiple lines and
paragraphs, but even blank lines should start with **>**. They can also be nested, in which case the
nested blockquote starts with multiple **>** (**>>** for the second level for example).

Blockquotes can even contain other Markdown elements such as headings, lists, emphasis markers. 

Blockquotes, like many other Markdown elements (paragraphs, headings) should be surrounded by two
blank lines, before and after.

### Lists

#### Ordered Lists

Simply start each line of the list with a number followed by a period (1. then 2.). Technically, the
numbers don't have to be in numerical order, in fact you could even start every line with (1.)

#### Unordered Lists

Start each line of the list with a list delimiter (most commonly a dash **-**, but you can also use
an asterisk (*), or a plus sign (+). The most important things is not to mix different ones).

In case an element of your unordered list needs to start with a number followed by a period, you can
escape the period with a backslash.

### Code

You can denote a word or phrase as code by surrounding it with backticks (\`). For example, \`nano\`
will look like `nano`. In case your code itself includes backticks, you can use double backticks,
for example \`\` \`code\` \`\` will look like `` `code` ``.

#### Codeblocks

For longer exceprts, you can creade code blocks by indenting every line of your code exceprt
four spaces or one tab (you can have code excerpts without indentation with fenced code blocks,
but this is part of the extended syntax which may have less support).

### Links

To create a link, enclose the text link in brackets ([text for the link]) and then follow it 
immediately with the URL in parenthesis ( (url.com) ). 

### Horizontal Rules

Simply write either three asterisks (*), dashes (-) or underscores (_) on a line by themselves to 
create a horizontal rule.

### Escaping

If you need to display a character that is already a symbol in Markdown, simply escape it with a
backslash (as in many programming languages).

### HTML

Many Markdown apps will allow you to use HTML tags in Markdown formatted texts. It can be helpful
if you prefer HTML for things like images, if you want to edit the styling attribute of an element,
the width of an image, etc.

When using block-level HTML elements (div, table, pre, etc.), insert a blank line before and after
them. Also note that you will not be able to use Markdown syntax inside these blocks.