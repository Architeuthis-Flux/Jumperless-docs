// Custom Syntax Highlighter for Jumperless Documentation
// This script adds custom keyword highlighting to code blocks

(function() {
    // Define your custom keywords and their categories
    const customKeywords = {
        micropython: [
            'machine', 'Pin', 'ADC', 'PWM', 'Timer', 'UART', 'SPI', 'I2C',
            'micropython', 'utime', 'ujson', 'urequests', 'ure', 'uos',
            'const', 'mem32', 'mem16', 'mem8', 'sleep_ms', 'sleep_us',
            'ticks_ms', 'ticks_us', 'ticks_diff'
        ],
        hardware: [
            'GPIO', 'LED', 'button', 'sensor', 'servo', 'motor', 'relay',
            'resistor', 'capacitor', 'transistor', 'diode', 'voltage',
            'current', 'analog', 'digital', 'HIGH', 'LOW', 'INPUT', 'OUTPUT',
            'PULLUP', 'PULLDOWN'
        ],
        jumperless: [
            'bridge', 'path', 'slot', 'chip', 'menu', 'node', 'row', 'rail', 
            'net', 'positive', 'negative', 'power', 'ground', 'gnd', 'top_rail', 'bottom_rail',
            'connect', 'disconnect', 'is_connected', 'nodes_clear', 'node',
            'oled_print', 'oled_clear', 'oled_connect', 'oled_disconnect',
            'clickwheel_up', 'clickwheel_down', 'clickwheel_press',
            'print_bridges', 'print_paths', 'print_crossbars', 'print_nets', 'print_chip_status',
            'probe_read', 'read_probe', 'probe_read_blocking', 'probe_read_nonblocking',
            'get_button', 'probe_button', 'probe_button_blocking', 'probe_button_nonblocking',
            'probe_wait', 'wait_probe', 'probe_touch', 'wait_touch', 'button_read', 'read_button',
            'check_button', 'button_check', 'arduino_reset', 'probe_tap', 'run_app', 'format_output',
            'help_nodes', 'Probe', 'PROBE', 'ISENSE_PLUS', 'ISENSE_MINUS', 'UART_TX', 'UART_RX', 'BUFFER_IN', 'BUFFER_OUT',
            'ROUTABLE_BUFFER_IN', 'ROUTABLE_BUFFER_OUT', 
            'GPIO_1', 'GPIO_2', 'GPIO_3', 'GPIO_4', 'GPIO_5', 'GPIO_6', 'GPIO_7', 'GPIO_8',

            'D13_PAD', 'TOP_RAIL_PAD', 'BOTTOM_RAIL_PAD', 'LOGO_PAD_TOP', 'LOGO_PAD_BOTTOM',
            'CONNECT_BUTTON', 'REMOVE_BUTTON', 'BUTTON_NONE', 'CONNECT', 'REMOVE', 'NONE',
            'TOP_RAIL', 'BOTTOM_RAIL', 'GND', 'DAC0', 'DAC1', 'ADC0', 'ADC1', 'ADC2', 'ADC3', 'ADC4', 'ADC5', 'ADC6', 'ADC7',

        ],
        gpio: [
            'pinMode', 'digitalRead', 'digitalWrite', 'analogRead', 'analogWrite',
            'attachInterrupt', 'detachInterrupt', 'tone', 'noTone', 'pulseIn',
            'shiftOut', 'shiftIn'
        ],
        i2c: [
            'Wire', 'begin', 'beginTransmission', 'endTransmission', 'write',
            'available', 'read', 'requestFrom', 'onReceive', 'onRequest',
            'setClock', 'setWireTimeout', 'getWireTimeoutFlag', 'clearWireTimeoutFlag'
        ],
        breadboard: [
            'row', 'column', 'rail', 'bus', 'node', 'net',
            'positive', 'negative', 'power', 'ground', 'VCC', 'GND', '3V3', '5V',
            'D0', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'D11', 'D12', 'D13',
            'A0', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7',
        ]
    };

    // Function to highlight custom keywords
    function highlightCustomKeywords() {
        // Find all code blocks
        const codeBlocks = document.querySelectorAll('.highlight pre code, .highlight pre, pre code');
        
        codeBlocks.forEach(block => {
            let html = block.innerHTML;
            
            // Process each keyword category
            Object.keys(customKeywords).forEach(category => {
                customKeywords[category].forEach(keyword => {
                    // Create a regex that matches the keyword as a whole word
                    // but not if it's already inside HTML tags
                    const regex = new RegExp(
                        `(?<!<[^>]*)(\\b${keyword}\\b)(?![^<]*>)`,
                        'gi'
                    );
                    
                    html = html.replace(regex, `<span class="custom-keyword-${category}">$1</span>`);
                });
            });
            
            block.innerHTML = html;
        });
    }

    // Function to add custom styling for specific function names
    function highlightCustomFunctions() {
        const customFunctions = [
            'setGPIOState', 'readGPIO', 'setPin', 'clearPin', 'togglePin',
            'connectPath', 'disconnectPath', 'showConnections', 'listConnections',
            'setLEDColor', 'fadeInLED', 'fadeOutLED', 'blinkLED'
        ];

        const codeBlocks = document.querySelectorAll('.highlight pre code, .highlight pre, pre code');
        
        codeBlocks.forEach(block => {
            let html = block.innerHTML;
            
            customFunctions.forEach(func => {
                const regex = new RegExp(`\\b(${func})(?=\\s*\\()`, 'gi');
                html = html.replace(regex, '<span class="custom-keyword-jumperless">$1</span>');
            });
            
            block.innerHTML = html;
        });
    }

    // Function to highlight pin numbers and special values
    function highlightSpecialValues() {
        const codeBlocks = document.querySelectorAll('.highlight pre code, .highlight pre, pre code');
        
        codeBlocks.forEach(block => {
            let html = block.innerHTML;
            
            // Highlight pin numbers (like D0, A1, GPIO2, etc.)
            html = html.replace(/\b([DA]\d+|GPIO\d+)\b/gi, '<span class="custom-keyword-gpio">$1</span>');
            
            // Highlight special constants
            html = html.replace(/\b(True|False|None|NULL|true|false|null)\b/g, '<span class="custom-keyword-micropython">$1</span>');
            
            block.innerHTML = html;
        });
    }

    // Run highlighting when DOM is loaded
    function runCustomHighlighting() {
        highlightCustomKeywords();
        highlightCustomFunctions();
        highlightSpecialValues();
    }

    // Initialize when page loads
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', runCustomHighlighting);
    } else {
        runCustomHighlighting();
    }

    // Also run when new content might be loaded (for SPAs)
    const observer = new MutationObserver((mutations) => {
        mutations.forEach((mutation) => {
            if (mutation.addedNodes.length > 0) {
                mutation.addedNodes.forEach((node) => {
                    if (node.nodeType === 1 && // Element node
                        (node.querySelector('.highlight') || node.classList.contains('highlight'))) {
                        setTimeout(runCustomHighlighting, 100);
                    }
                });
            }
        });
    });

    observer.observe(document.body, {
        childList: true,
        subtree: true
    });

    // =====================================================================
    // GLOSSARY TERM HIGHLIGHTING SYSTEM
    // =====================================================================

    // Glossary terms and definitions (extracted programmatically)
    let glossaryTerms = {};
    let glossaryLoaded = false;

    // Function to parse glossary markdown content
    function parseGlossaryContent(content) {
        const terms = {};
        const lines = content.split('\n');
        
        for (let i = 0; i < lines.length; i++) {
            const line = lines[i].trim();
            
            // Look for definition lines starting with `term` = definition
            const match = line.match(/^`([^`]+)`\s*=\s*(.+)$/);
            if (match) {
                const term = match[1].toLowerCase();
                let definition = match[2];
                
                // Check if the definition continues on next lines (for multi-line definitions)
                let j = i + 1;
                while (j < lines.length && !lines[j].trim().match(/^`[^`]+`\s*=/) && lines[j].trim() !== '') {
                    if (lines[j].trim() && !lines[j].startsWith('#')) {
                        definition += ' ' + lines[j].trim();
                    }
                    j++;
                }
                
                terms[term] = definition.replace(/`([^`]+)`/g, '<em>$1</em>'); // Convert backticks to emphasis
                terms[term] = terms[term].replace(/\*([^*]+)\*/g, '<strong>$1</strong>'); // Convert asterisks to strong
            }
        }
        
        return terms;
    }

    // Function to load and parse the glossary
    async function loadGlossary() {
        if (glossaryLoaded) return;
        
        try {
            // Try to load the glossary file
            const response = await fetch('99-glossary.md');
            if (response.ok) {
                const content = await response.text();
                glossaryTerms = parseGlossaryContent(content);
                glossaryLoaded = true;
                console.log('Glossary loaded:', Object.keys(glossaryTerms).length, 'terms');
                
                // Highlight glossary terms after loading
                highlightGlossaryTerms();
            }
        } catch (error) {
            console.warn('Could not load glossary file:', error);
            
            // Fallback: Define some key terms manually
            glossaryTerms = {
                'net': 'a group of all the nodes that are connected together',
                'node': 'anything the crossbar array can connect to, which includes everything on the breadboard and Nano header',
                'row': 'kinda the same thing as node but generally used to mean stuff on the breadboard',
                'rail': 'refers to the 4 horizontal power rails on the top and bottom (top_rail, bottom_rail, gnd)',
                'bridge': 'a pair of exactly two nodes (what you\'re making when you connect stuff with the probe)',
                'path': 'the set of crossbar connections needed to make a single bridge',
                'slot': 'one of the 8 node files stored that you can switch between',
                'chip': 'shorthand for the CH446Qs specifically, lettered A-L',
                'menu': 'the onboard clickwheel menu'
            };
            glossaryLoaded = true;
            highlightGlossaryTerms();
        }
    }

    // Function to create tooltip element
    function createTooltip() {
        const tooltip = document.createElement('div');
        tooltip.className = 'glossary-tooltip';
        tooltip.style.cssText = `
            position: absolute;
            background: #2d2d2d;
            color: #f8f8f2;
            padding: 8px 12px;
            border-radius: 6px;
            border: 1px solid #44475a;
            font-size: 14px;
            line-height: 1.4;
            max-width: 300px;
            z-index: 10000;
            pointer-events: none;
            opacity: 0;
            transition: opacity 0.2s ease;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        `;
        document.body.appendChild(tooltip);
        return tooltip;
    }

    // Function to show tooltip
    function showTooltip(element, definition, event) {
        let tooltip = document.querySelector('.glossary-tooltip');
        if (!tooltip) {
            tooltip = createTooltip();
        }
        
        tooltip.innerHTML = definition;
        tooltip.style.opacity = '1';
        
        // Position tooltip
        const rect = element.getBoundingClientRect();
        const tooltipRect = tooltip.getBoundingClientRect();
        
        let left = rect.left + (rect.width / 2) - (tooltipRect.width / 2);
        let top = rect.top - tooltipRect.height - 8;
        
        // Adjust if tooltip goes off screen
        if (left < 10) left = 10;
        if (left + tooltipRect.width > window.innerWidth - 10) {
            left = window.innerWidth - tooltipRect.width - 10;
        }
        if (top < 10) {
            top = rect.bottom + 8;
        }
        
        tooltip.style.left = left + 'px';
        tooltip.style.top = top + 'px';
    }

    // Function to hide tooltip
    function hideTooltip() {
        const tooltip = document.querySelector('.glossary-tooltip');
        if (tooltip) {
            tooltip.style.opacity = '0';
        }
    }

    // Function to highlight glossary terms in body text
    function highlightGlossaryTerms() {
        if (!glossaryLoaded || Object.keys(glossaryTerms).length === 0) return;

        // Get all text nodes in the document (excluding code blocks and already processed elements)
        const walker = document.createTreeWalker(
            document.body,
            NodeFilter.SHOW_TEXT,
            {
                acceptNode: function(node) {
                    // Skip if parent is a code element, script, style, or already highlighted
                    const parent = node.parentElement;
                    if (!parent) return NodeFilter.FILTER_REJECT;
                    
                    const tagName = parent.tagName.toLowerCase();
                    if (['code', 'pre', 'script', 'style', 'textarea'].includes(tagName)) {
                        return NodeFilter.FILTER_REJECT;
                    }
                    
                    if (parent.classList.contains('glossary-term') || 
                        parent.classList.contains('glossary-tooltip') ||
                        parent.closest('.highlight')) {
                        return NodeFilter.FILTER_REJECT;
                    }
                    
                    return NodeFilter.FILTER_ACCEPT;
                }
            }
        );

        const textNodes = [];
        let node;
        while (node = walker.nextNode()) {
            textNodes.push(node);
        }

        // Process each text node
        textNodes.forEach(textNode => {
            let content = textNode.textContent;
            let hasChanges = false;
            let newHTML = content;

            // Sort terms by length (longest first) to handle overlapping terms correctly
            const sortedTerms = Object.keys(glossaryTerms).sort((a, b) => b.length - a.length);

            sortedTerms.forEach(term => {
                // Create regex to match whole words only
                const regex = new RegExp(`\\b(${term.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')})\\b`, 'gi');
                
                if (regex.test(content)) {
                    const definition = glossaryTerms[term.toLowerCase()];
                    newHTML = newHTML.replace(regex, `<span class="glossary-term" data-definition="${definition.replace(/"/g, '&quot;')}">$1</span>`);
                    hasChanges = true;
                }
            });

            // Replace the text node with HTML if changes were made
            if (hasChanges) {
                const wrapper = document.createElement('span');
                wrapper.innerHTML = newHTML;
                
                // Replace text node with the new elements
                const parent = textNode.parentNode;
                while (wrapper.firstChild) {
                    parent.insertBefore(wrapper.firstChild, textNode);
                }
                parent.removeChild(textNode);
            }
        });

        // Add event listeners to glossary terms
        document.querySelectorAll('.glossary-term').forEach(element => {
            element.style.cssText = `
                color: #8be9fd;
                text-decoration: underline;
                text-decoration-style: dotted;
                cursor: help;
                transition: color 0.2s ease;
            `;
            
            element.addEventListener('mouseenter', function(event) {
                this.style.color = '#50fa7b';
                showTooltip(this, this.dataset.definition, event);
            });
            
            element.addEventListener('mouseleave', function() {
                this.style.color = '#8be9fd';
                hideTooltip();
            });
        });
    }

    // Initialize glossary system
    loadGlossary();

    // Also run glossary highlighting when new content is added
    const glossaryObserver = new MutationObserver((mutations) => {
        let shouldHighlight = false;
        mutations.forEach((mutation) => {
            if (mutation.addedNodes.length > 0) {
                mutation.addedNodes.forEach((node) => {
                    if (node.nodeType === 1 && // Element node
                        !node.classList.contains('glossary-tooltip') &&
                        !node.closest('.highlight')) {
                        shouldHighlight = true;
                    }
                });
            }
        });
        
        if (shouldHighlight && glossaryLoaded) {
            setTimeout(highlightGlossaryTerms, 100);
        }
    });

    glossaryObserver.observe(document.body, {
        childList: true,
        subtree: true
    });

})(); 