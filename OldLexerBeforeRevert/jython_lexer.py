"""
Custom Pygments Lexer for Jython (Jumperless Python)
Extends the standard Python lexer with Jumperless-specific keywords and functions.
"""

from pygments.lexer import RegexLexer, words
from pygments.lexers.python import PythonLexer
from pygments.token import Token, Keyword, Name, Comment, String, Number

# Define custom token types for Jumperless-specific elements
class JythonTokens:
    # Jumperless-specific token types
    JumperlessFunction = Token.Name.Function.Jumperless
    JumperlessConstant = Token.Name.Constant.Jumperless
    JumperlessType = Token.Name.Type.Jumperless
    JFSFunction = Token.Name.Function.JFS
    HardwareConstant = Token.Name.Constant.Hardware

class JythonLexer(PythonLexer):
    """
    Custom lexer for Jython (Jumperless Python) that extends Python 
    with Jumperless-specific keywords and functions.
    """
    
    name = 'Jython'
    aliases = ['jython', 'jumperless-python', 'jumperless']
    filenames = ['*.py', '*.python', '*.jumperless.py']
    mimetypes = ['text/x-jython', 'application/x-jython']

    # Define Jumperless-specific keywords and functions
    JUMPERLESS_FUNCTIONS = {
        # DAC Functions
        'dac_set', 'dac_get', 'set_dac', 'get_dac',
        
        # ADC Functions  
        'adc_get', 'get_adc',
        
        # INA (Current/Voltage Sensor) Functions
        'ina_get_current', 'ina_get_voltage', 'ina_get_bus_voltage', 'ina_get_power',
        'get_current', 'get_voltage', 'get_bus_voltage', 'get_power',
        
        # GPIO Functions
        'gpio_set', 'gpio_get', 'gpio_set_dir', 'gpio_get_dir', 'gpio_set_pull', 'gpio_get_pull',
        'set_gpio', 'get_gpio', 'set_gpio_dir', 'get_gpio_dir', 'set_gpio_pull', 'get_gpio_pull',
        
        # Connection Functions
        'connect', 'disconnect', 'is_connected', 'nodes_clear', 'node',
        
        # OLED Functions
        'oled_print', 'oled_clear', 'oled_connect', 'oled_disconnect',
        
        # Clickwheel Functions
        'clickwheel_up', 'clickwheel_down', 'clickwheel_press',
        
        # Debug/Info Functions
        'print_bridges', 'print_paths', 'print_crossbars', 'print_nets', 'print_chip_status',
        
        # Probe Functions
        'probe_read', 'read_probe', 'probe_read_blocking', 'probe_read_nonblocking',
        'get_button', 'probe_button', 'probe_button_blocking', 'probe_button_nonblocking',
        'probe_wait', 'wait_probe', 'probe_touch', 'wait_touch', 'button_read', 'read_button',
        'check_button', 'button_check', 'arduino_reset', 'probe_tap', 'run_app', 'format_output',
        'help_nodes',
    }

    JUMPERLESS_CONSTANTS = {
        # Rails and Power
        'TOP_RAIL', 'BOTTOM_RAIL', 'GND',
        
        # DAC/ADC
        'DAC0', 'DAC1', 'ADC0', 'ADC1', 'ADC2', 'ADC3', 'ADC4',
        
        # Special Functions
        'PROBE', 'ISENSE_PLUS', 'ISENSE_MINUS', 'UART_TX', 'UART_RX', 'BUFFER_IN', 'BUFFER_OUT',
        
        # GPIO
        'GPIO_1', 'GPIO_2', 'GPIO_3', 'GPIO_4', 'GPIO_5', 'GPIO_6', 'GPIO_7', 'GPIO_8',
        
        # Arduino Digital Pins
        'D0', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'D11', 'D12', 'D13',
        
        # Arduino Analog Pins
        'A0', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7',
        
        # Pads
        'D13_PAD', 'TOP_RAIL_PAD', 'BOTTOM_RAIL_PAD', 'LOGO_PAD_TOP', 'LOGO_PAD_BOTTOM',
        
        # Button States
        'CONNECT_BUTTON', 'REMOVE_BUTTON', 'BUTTON_NONE', 'CONNECT', 'REMOVE', 'NONE',
    }

    JFS_FUNCTIONS = {
        # File operations
        'open', 'read', 'write', 'close', 'seek', 'tell', 'size', 'available',
        
        # Directory operations
        'exists', 'listdir', 'mkdir', 'rmdir', 'remove', 'rename', 'stat', 'info',
        
        # Filesystem functions
        'fs_exists', 'fs_listdir', 'fs_read', 'fs_write', 'fs_cwd',
    }

    JFS_CONSTANTS = {
        'SEEK_SET', 'SEEK_CUR', 'SEEK_END',
    }

    def get_tokens_unprocessed(self, text):
        """
        Override the parent's token processing to add Jumperless-specific highlighting.
        """
        for index, token, value in PythonLexer.get_tokens_unprocessed(self, text):
            # Check if this is a name token that might be a Jumperless keyword
            if token is Name:
                if value in self.JUMPERLESS_FUNCTIONS:
                    token = JythonTokens.JumperlessFunction
                elif value in self.JUMPERLESS_CONSTANTS:
                    token = JythonTokens.JumperlessConstant
                elif value in self.JFS_FUNCTIONS:
                    token = JythonTokens.JFSFunction
                elif value in self.JFS_CONSTANTS:
                    token = JythonTokens.JFSFunction
            
            yield index, token, value

    @staticmethod
    def analyse_text(text):
        """
        Analyze text to determine if it's likely Jython code.
        Returns a float between 0.0 and 1.0 indicating confidence.
        """
        score = 0.0
        
        # Check for Jumperless-specific imports
        if 'import jumperless' in text or 'from jumperless' in text:
            score += 0.3
            
        # Check for Jumperless function calls
        jumperless_functions = ['connect(', 'disconnect(', 'gpio_set(', 'dac_set(', 'adc_get(']
        for func in jumperless_functions:
            if func in text:
                score += 0.1
                
        # Check for Jumperless constants
        jumperless_constants = ['TOP_RAIL', 'BOTTOM_RAIL', 'GPIO_', 'DAC0', 'ADC0']
        for const in jumperless_constants:
            if const in text:
                score += 0.05
                
        # Cap the score at 1.0
        return min(score, 1.0)


# Register the lexer (this would typically be done via entry points in a package)
def get_jython_lexer(**options):
    """Factory function to create a Jython lexer instance."""
    return JythonLexer(**options)


# Export for use
__all__ = ['JythonLexer', 'JythonTokens', 'get_jython_lexer'] 