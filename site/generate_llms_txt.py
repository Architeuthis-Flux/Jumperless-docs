"""
MkDocs hook to generate llms.txt and llms-full.txt during build.

llms.txt  - An index file following the llms.txt spec (https://llmstxt.org/)
llms-full.txt - All documentation concatenated into a single LLM-friendly text file

These files are written into the site output directory so they're served
alongside the built docs, or can be uploaded to a Cloudflare R2 bucket.
"""

import os
import re


def _strip_html(text):
    """Remove HTML tags (iframes, divs, img tags, anchor wrappers, etc.) but keep markdown."""
    # Remove full iframe lines
    text = re.sub(r'<iframe[^>]*>.*?</iframe>', '', text, flags=re.DOTALL)
    # Remove HTML image tags
    text = re.sub(r'<img[^>]*/?>', '', text)
    # Remove div blocks (opening and closing)
    text = re.sub(r'</?div[^>]*>', '', text)
    # Remove anchor tags but keep inner text
    text = re.sub(r'<a[^>]*>(.*?)</a>', r'\1', text, flags=re.DOTALL)
    # Remove any remaining HTML tags
    text = re.sub(r'<[^>]+>', '', text)
    # Remove HTML comments
    text = re.sub(r'<!--.*?-->', '', text, flags=re.DOTALL)
    # Also handle unclosed HTML comments like <!---
    text = re.sub(r'<!---.*?-->', '', text, flags=re.DOTALL)
    return text


def _strip_markdown_images(text):
    """Convert markdown images to just their alt text."""
    # ![alt](url) -> [Image: alt] (keep alt text for context)
    text = re.sub(r'!\[([^\]]*)\]\([^)]+\)', lambda m: f'[Image: {m.group(1)}]' if m.group(1) else '', text)
    return text


def _clean_for_llm(text):
    """Clean markdown content to be LLM-friendly."""
    text = _strip_html(text)
    text = _strip_markdown_images(text)
    # Remove lines that contain only whitespace
    cleaned_lines = []
    for line in text.split('\n'):
        if line.strip() == '':
            cleaned_lines.append('')
        else:
            cleaned_lines.append(line)
    text = '\n'.join(cleaned_lines)
    # Collapse runs of 3+ blank lines down to 2
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()


def _get_nav_pages(config):
    """Extract ordered (title, file_path) pairs from the mkdocs nav config."""
    nav = config.get('nav', [])
    pages = []
    for entry in nav:
        if isinstance(entry, dict):
            for title, path in entry.items():
                if isinstance(path, str) and path.endswith('.md'):
                    pages.append((title, path))
        elif isinstance(entry, str):
            pages.append((entry, entry))
    return pages


def _build_llms_txt(pages, site_url):
    """Build the llms.txt index file following the llms.txt spec."""
    # Normalize site_url
    site_url = site_url.rstrip('/')

    # Short descriptions for each page (keyed by filename without extension)
    descriptions = {
        'index': 'Overview of Jumperless V5 features and getting started links',
        '01-basic-controls': 'Probe, click wheel, slot system, and connecting/disconnecting nodes',
        '03-app': 'Companion desktop app for serial control, Wokwi import, and Arduino flashing',
        '04-oled': 'Adding and using an external OLED display',
        '05-arduino': 'UART passthrough, automatic flashing, and Arduino integration',
        '06-config': 'Persistent settings stored on the device',
        '07-debugging': 'Crossbar view, bridge list, net list, and diagnostic tools',
        '08-file-manager': 'Filesystem access, YAML slot editing, and built-in text editor',
        '08-micropython': 'Using the onboard MicroPython interpreter to script circuits',
        '09.5-micropythonAPIreference': 'Complete API reference for all Jumperless MicroPython hardware calls',
        '09.6-jfs': 'Jumperless FileSystem module for reading/writing files from MicroPython',
        '09.8-odds-and-ends': 'Miscellaneous features, tips, and edge cases',
        '10-3d-stand': '3D printable stand models and printing tips',
        '11-WritingApps': 'Guide to writing custom apps for the Jumperless firmware',
        '12-llm-tools-specification': 'Specification for LLM tool-use with Jumperless serial commands',
        '99-glossary': 'Key terms: slots, nodes, bridges, nets, W command, and more',
    }

    lines = []
    lines.append("# Jumperless V5 Documentation")
    lines.append("")
    lines.append("> Jumperless V5 is a software-defined breadboard and integrated hardware IDE "
                 "with an RP2350B, programmable power supplies, multimeter, oscilloscope, "
                 "function generator, logic analyzer, and RGB LEDs under every hole. "
                 "Connect any point to any other using software-defined jumpers. "
                 "Circuits are scriptable via MicroPython or controllable from the companion app.")
    lines.append("")
    lines.append("- The full documentation text is available in a single file: "
                 "[llms-full.txt](llms-full.txt)")
    lines.append("- Source and hardware: https://github.com/Architeuthis-Flux/JumperlessV5")
    lines.append("- Firmware: https://github.com/Architeuthis-Flux/JumperlOS")
    lines.append("- App: https://github.com/Architeuthis-Flux/Jumperless-App")
    lines.append("- Community Discord: https://discord.gg/bvacV7r3FP")
    lines.append("- Buy the new Jumperless V5 rev 7: https://shop.jumperless.org")
    lines.append("- Buy a refurbished one: https://shop.jumperless.org/products/jumperless-v5-offcuts")
    lines.append("- Buy a Jumperless V5 on Crowd Supply: https://www.crowdsupply.com/architeuthis-flux/jumperless-v5")
    lines.append("")

    # Group pages into sections
    core_pages = []
    programming_pages = []
    reference_pages = []

    for title, path in pages:
        name = os.path.splitext(path)[0]
        # Build the URL path the way readthedocs / mkdocs generates it
        if path == 'index.md':
            url_path = ''
        else:
            url_path = name + '/'

        desc = descriptions.get(name, title)
        entry = (title, f"{site_url}/{url_path}", desc)

        if name in ('index', '01-basic-controls', '03-app', '04-oled', '06-config', '07-debugging'):
            core_pages.append(entry)
        elif name in ('05-arduino', '08-micropython', '09.5-micropythonAPIreference',
                       '09.6-jfs', '08-file-manager', '11-WritingApps',
                       '12-llm-tools-specification'):
            programming_pages.append(entry)
        else:
            reference_pages.append(entry)

    if core_pages:
        lines.append("## Core Documentation")
        lines.append("")
        for title, url, desc in core_pages:
            lines.append(f"- [{title}]({url}): {desc}")
        lines.append("")

    if programming_pages:
        lines.append("## Programming & APIs")
        lines.append("")
        for title, url, desc in programming_pages:
            lines.append(f"- [{title}]({url}): {desc}")
        lines.append("")

    if reference_pages:
        lines.append("## Optional")
        lines.append("")
        for title, url, desc in reference_pages:
            lines.append(f"- [{title}]({url}): {desc}")
        lines.append("")

    return '\n'.join(lines)


def _build_llms_full_txt(pages, docs_dir, site_url):
    """Build llms-full.txt with all doc content concatenated."""
    site_url = site_url.rstrip('/')

    sections = []
    sections.append("# Jumperless V5 - Complete Documentation")
    sections.append("")
    sections.append("> This file contains the full text of all Jumperless V5 documentation,")
    sections.append("> intended for use by LLMs and AI assistants.")
    sections.append(">")
    sections.append(f"> Source: {site_url}")
    sections.append(f"> Generated from MkDocs source files.")
    sections.append("")
    sections.append("---")
    sections.append("")

    for title, path in pages:
        filepath = os.path.join(docs_dir, path)
        if not os.path.exists(filepath):
            continue

        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        cleaned = _clean_for_llm(content)
        if not cleaned:
            continue

        sections.append(f"# {title}")
        sections.append("")
        # If the content already starts with a heading, skip adding a duplicate
        if cleaned.startswith('# '):
            # The first line is already a heading, use the content as-is
            # but skip the first heading to avoid duplication
            first_newline = cleaned.find('\n')
            if first_newline > 0:
                sections.append(cleaned[first_newline + 1:])
            else:
                sections.append(cleaned)
        else:
            sections.append(cleaned)

        sections.append("")
        sections.append("---")
        sections.append("")

    return '\n'.join(sections)


def on_post_build(config):
    """
    MkDocs hook: runs after the site is built.
    Generates llms.txt and llms-full.txt in the site output directory.
    """
    site_dir = config['site_dir']
    docs_dir = config['docs_dir']
    site_url = config.get('site_url', 'https://docs.jumperless.org')

    pages = _get_nav_pages(config)
    if not pages:
        print("⚠ No nav pages found, skipping llms.txt generation")
        return

    # Generate llms.txt (index)
    llms_txt = _build_llms_txt(pages, site_url)
    llms_txt_path = os.path.join(site_dir, 'llms.txt')
    with open(llms_txt_path, 'w', encoding='utf-8') as f:
        f.write(llms_txt)
    print(f"✓ Generated {llms_txt_path}")

    # Generate llms-full.txt (all content)
    llms_full_txt = _build_llms_full_txt(pages, docs_dir, site_url)
    llms_full_path = os.path.join(site_dir, 'llms-full.txt')
    with open(llms_full_path, 'w', encoding='utf-8') as f:
        f.write(llms_full_txt)
    print(f"✓ Generated {llms_full_path} ({len(llms_full_txt):,} chars)")
