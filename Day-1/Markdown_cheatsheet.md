# Markdown Cheatsheet

Markdown is a simple markup language used to format text in README files, wikis, and documentation. This cheatsheet will help you quickly apply formatting in your Markdown files.

## Headings

Use the `#` symbol to create headings. Add more `#` for smaller heading levels.

# H1 Heading  
## H2 Heading  
### H3 Heading  
#### H4 Heading  
##### H5 Heading  
###### H6 Heading

---

## Lists

### Bulleted Lists

You can use `*`, `+`, or `-` followed by a space for bullet points.

- Item one  
- Item two  
    - Nested item  
* Another item  
+ One more item

### Numbered Lists

Use numbers with periods.

1. First point  
2. Second point  
3. Third point  
    1. Sub-point A  
    2. Sub-point B

---

## Emphasis

Apply basic text styles:

- **Bold:** `**bold**` or `__bold__` → **bold**  
- *Italic:* `*italic*` or `_italic_` → *italic*  
- ~~Strikethrough:~~ `~~strikethrough~~` → ~~strikethrough~~

Example:


**Bold text**  
*Italic text*  
~~Strikethrough~~



## Links

You can create inline links or use reference-style links.

### Inline Links

The link text is enclosed in square brackets `[]`, and the URL is enclosed in parentheses `()`. You can optionally add a title attribute in double quotes after the URL.
[GitHub](https://github.com)


### Reference-style Links

Reference-style links make your Markdown more readable, especially for long URLs. You define the link in the text using a label in square brackets, and then you define the link itself elsewhere in the document.
[GitHub][github-link]

[github-link]: https://github.com

## Images

Add images by placing an exclamation mark ! before the link.


![Sample image](https://placekitten.com/200/300 "Cute kitten")

Result:

## Code Blocks

Use triple backticks for larger code sections. Add a language for highlighting.

``` python
def greet(name):
    print(f"Hello, {name}!")
```

### Inline Code

Use backticks \` around the code.
The `print()` function in Python displays output.



## Tables

Create tables using pipes | and hyphens -.

| Name  | Role    |
| ----- | ------- |
| Alice | Engineer |
| Bob   | Designer |



### Column Alignment


  * `:--`: Left-align
  * `--:`: Right-align
  * `:-:`: Center-align

| Left   | Center | Right  |
| :----- | :----: | ------:|
| A      | B      | C      |
| D      | E      | F      |


## Horizontal Rules

Create a horizontal line using three or more:

* Hyphens: ---
* Asterisks: ***
* Underscores: ___


***
---
___

---

---