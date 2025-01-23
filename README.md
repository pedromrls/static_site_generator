# Static Site Generator

A Python-based static site generator that converts markdown files to HTML pages using customizable templates.

## Features
* Markdown to HTML conversion
* Template-based page generation
* Static file handling
* Built-in development server
* Comprehensive test suite

## Project Structure
.
├── README.md
├── content
│   ├── index.md
│   └── majesty
│       └── index.md
├── main.sh
├── src
│   ├── __init__.py
│   ├── copy_static.py
│   ├── gen_content.py
│   ├── htmlnode.py
│   ├── inline_markdown.py
│   ├── main.py
│   ├── markdown_blocks.py
│   ├── tests
│   │   ├── __init__.py
│   │   ├── test_extract_title.py
│   │   ├── test_htmlnode.py
│   │   ├── test_inline_markdown.py
│   │   ├── test_leafnode.py
│   │   ├── test_markdown_blocks.py
│   │   ├── test_parentnode.py
│   │   └── test_textnode.py
│   └── textnode.py
├── static
│   ├── images
│   │   └── rivendell.png
│   └── index.css
├── template.html
└── test.sh

## Installation
1. Clone the repository
2. Ensure Python 3.x is installed
3. No additional dependencies required

## Quick Start
```bash
git clone <repo-url>
./main.sh
```

The site will be available at http://localhost:8888

## Testing
```bash
./test.sh
```

The test suite includes:

* Unit tests for markdown parsing
* Text node manipulation tests
* Title extraction validation
* Integration tests for page generation

## Example

Input markdown:

```
# Hello World
This is **markdown**
```

Generates:

```
<h1>Hello World</h1>
<p>This is <b>markdown</b></p>
```

## How It Works

* Reads markdown from content/ directory
* Converts markdown to HTML using custom parser
* Applies template from template.html
* Copies static assets to public/ directory
