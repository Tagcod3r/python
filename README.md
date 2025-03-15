# Python Programs Collection

This repository contains four standalone Python programs, each demonstrating distinct programming concepts ranging from GUI applications to recursive fractals and web scraping. 


## Overview

| Program Name               | Key Concepts                  | Description                                                                 |
|----------------------------|-------------------------------|-----------------------------------------------------------------------------|
| **BMI Calculator**          | Tkinter (GUI)                 | Interactive GUI application that calculates Body Mass Index from user input |
| **Koch Snowflake Generator**| Turtle Graphics, Recursion    | Generates a recursive fractal pattern using Python's Turtle module          |
| **Sierpinski Triangle**     | Turtle Graphics, Recursion    | Creates a multi-colored recursive fractal triangle with depth visualization |
| **Wikipedia Image Scraper** | Web Scraping, BeautifulSoup   | Extracts and displays image URLs from Wikipedia pages                       |

## Features

- **Modular Design**: Each program operates independently
- **Educational Focus**: Demonstrates core Python concepts
- **Visual Output**: Includes both GUI and graphical renderings
- **Web Interaction**: Practical example of web scraping techniques

## Prerequisites

- Python 3.8+
- PIP package manager
- Required Python packages:
  ```bash
  tkinter       # Typically included with Python standard library
  turtle        # Included in standard library
  beautifulsoup4==4.12.3
  requests==2.31.0
  ```

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/python-programs.git
   cd python-programs
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run any program independently using these commands:

```bash
# BMI Calculator (GUI)
python bmi_calculator.py

# Koch Snowflake Generator
python koch_snowflake.py

# Sierpinski Triangle
python sierpinski_triangle.py

# Wikipedia Image Scraper
python wikipedia_scraper.py
```

**Note**: The Wikipedia Scraper defaults to Sachin Tendulkar's page. Modify the `URL` variable in the script to target different pages.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

**Maintainer**: Your Name | **Contact**: your.email@domain.com  
**Documentation Last Updated**: October 2023
