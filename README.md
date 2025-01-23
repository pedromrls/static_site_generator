# Static Site Generator

A Python-based static site generator that converts markdown files to HTML pages using customizable templates.

## Features
* Markdown to HTML conversion
* Template-based page generation
* Static file handling
* Built-in development server
* Comprehensive test suite

## Installation
1. Clone the repository
2. Ensure Python 3.x is installed
3. No additional dependencies required

## Quick Start
```bash
git clone <your-repo-url>
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
