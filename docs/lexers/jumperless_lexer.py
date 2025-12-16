"""
Custom Pygments Lexer for Jython (Jumperless Python)
Extends the standard Python lexer with Jumperless-specific keywords and functions.
"""

from pygments.lexer import RegexLexer, words
from pygments.lexers.python import PythonLexer
from pygments.token import Token, Keyword, Name, Comment, String, Number

# Define custom token types for Jumperless-specific elements
class JumperlessTokens:
    # Jumperless-specific token types
    JumperlessFunction = Token.Name.Function.Jumperless
    JumperlessConstant = Token.Name.Constant.Jumperless
    JumperlessType = Token.Name.Type.Jumperless
    JFSFunction = Token.Name.Function.JFS
    JFSConstant = Token.Name.Constant.JFS
    HardwareConstant = Token.Name.Constant.Hardware

class JumperlessPythonLexer(PythonLexer):
    """
    Custom lexer for Jython (Jumperless Python) that extends Python 
    with Jumperless-specific keywords and functions.
    """
    
    name = 'Jython'
    aliases = ['jython', 'jumperless-python', 'jumperless', 'j']
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
        'get_ina_current', 'get_ina_voltage', 'get_ina_bus_voltage', 'get_ina_power',
        'get_current', 'get_voltage', 'get_bus_voltage', 'get_power',
        
        # GPIO Functions
        'gpio_set', 'gpio_get', 'gpio_set_dir', 'gpio_get_dir', 'gpio_set_pull', 'gpio_get_pull',
        'set_gpio', 'get_gpio', 'set_gpio_dir', 'get_gpio_dir', 'set_gpio_pull', 'get_gpio_pull',
        
        # Connection Functions
        'connect', 'disconnect', 'fast_connect', 'fast_disconnect', 'is_connected', 'nodes_clear', 'node',
        'nodes_save', 'nodes_discard', 'nodes_has_changes', 'switch_slot',
        
        # Net Information API
        'get_net_name', 'set_net_name', 'get_net_color', 'get_net_color_name', 'set_net_color', 'set_net_color_hsv',
        'get_num_nets', 'get_num_bridges', 'get_net_nodes', 'get_bridge', 'get_net_info',
        'net_name', 'net_color', 'net_info',
        
        # Path Query Functions
        'get_num_paths', 'get_path_info', 'get_all_paths', 'get_path_between',
        
        # OLED Functions
        'oled_print', 'oled_clear', 'oled_connect', 'oled_disconnect', 'oled_show',
        
        # Clickwheel Functions
        'clickwheel_up', 'clickwheel_down', 'clickwheel_press',
        'clickwheel_get_position', 'clickwheel_reset_position', 'clickwheel_get_direction',
        'clickwheel_get_button', 'clickwheel_is_initialized',
        
        # Debug/Info Functions
        'print_bridges', 'print_paths', 'print_crossbars', 'print_nets', 'print_chip_status',
        
        # Probe Functions
        'probe_read', 'read_probe', 'probe_read_blocking', 'probe_read_nonblocking',
        'get_button', 'probe_button', 'probe_button_blocking', 'probe_button_nonblocking',
        'probe_wait', 'wait_probe', 'probe_touch', 'wait_touch', 'button_read', 'read_button',
        'check_button', 'button_check',
        
        # Probe Switch Functions
        'get_switch_position', 'set_switch_position', 'check_switch_position', 'probe_tap',
        
        # System/Misc Functions
        'arduino_reset', 'run_app', 'pause_core2', 'send_raw',
        'context_toggle', 'context_get',
        'change_terminal_color', 'cycle_term_color',
        
        # Service Management Functions
        'force_service', 'force_service_by_index', 'get_service_index',
        
        # Help Functions
        'nodes_help', 'help',
        
        # PWM Functions
        'pwm', 'pwm_set_duty_cycle', 'pwm_set_frequency', 'pwm_stop',
        'set_pwm', 'set_pwm_duty_cycle', 'set_pwm_frequency', 'stop_pwm',

        # Wavegen Functions
        'wavegen_set_output', 'set_wavegen_output',
        'wavegen_set_freq', 'set_wavegen_freq',
        'wavegen_set_wave', 'set_wavegen_wave',
        'wavegen_set_sweep', 'set_wavegen_sweep',
        'wavegen_set_amplitude', 'set_wavegen_amplitude',
        'wavegen_set_offset', 'set_wavegen_offset',
        'wavegen_start', 'start_wavegen',
        'wavegen_stop', 'stop_wavegen',
        'wavegen_get_output', 'get_wavegen_output',
        'wavegen_get_freq', 'get_wavegen_freq',
        'wavegen_get_wave', 'get_wavegen_wave',
        'wavegen_get_amplitude', 'get_wavegen_amplitude',
        'wavegen_get_offset', 'get_wavegen_offset',
        'wavegen_is_running',
        
        # Logic Analyzer Functions
        'la_set_trigger', 'la_capture_single_sample', 'la_start_continuous_capture',
        'la_stop_capture', 'la_is_capturing', 'la_set_sample_rate', 'la_set_num_samples',
        'la_enable_channel', 'la_set_control_analog', 'la_set_control_digital',
        'la_get_control_analog', 'la_get_control_digital',
        
        # Legacy Filesystem Functions
        'fs_exists', 'fs_listdir', 'fs_read', 'fs_write', 'fs_cwd',
    }

    JUMPERLESS_CONSTANTS = {
        # Rails and Power (with aliases)
        'TOP_RAIL', 'T_RAIL', 'BOTTOM_RAIL', 'BOT_RAIL', 'B_RAIL', 'GND',
        
        # DAC/ADC (with aliases)
        'DAC0', 'DAC_0', 'DAC1', 'DAC_1',
        'ADC0', 'ADC1', 'ADC2', 'ADC3', 'ADC4', 'ADC7',
        
        # Special Functions (with aliases)
        'PROBE', 'UART_TX', 'TX', 'UART_RX', 'RX',
        'ISENSE_PLUS', 'ISENSE_P', 'I_P', 'CURRENT_SENSE_PLUS', 'CURRENT_SENSE_P',
        'ISENSE_MINUS', 'ISENSE_N', 'I_N', 'CURRENT_SENSE_MINUS', 'CURRENT_SENSE_N',
        'BUFFER_IN', 'BUF_IN', 'BUFFER_OUT', 'BUF_OUT',
        
        # GPIO (with aliases)
        'GPIO_1', 'GPIO_2', 'GPIO_3', 'GPIO_4', 'GPIO_5', 'GPIO_6', 'GPIO_7', 'GPIO_8',
        'GP1', 'GP2', 'GP3', 'GP4', 'GP5', 'GP6', 'GP7', 'GP8',
        'GPIO_20', 'GPIO_21', 'GPIO_22', 'GPIO_23', 'GPIO_24', 'GPIO_25', 'GPIO_26', 'GPIO_27',
        
        # GPIO States
        'HIGH', 'LOW', 'FLOATING',
        
        # GPIO Directions
        'INPUT', 'OUTPUT',
        
        # Arduino Digital Pins (with NANO_ aliases)
        'D0', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'D11', 'D12', 'D13',
        'NANO_D0', 'NANO_D1', 'NANO_D2', 'NANO_D3', 'NANO_D4', 'NANO_D5', 'NANO_D6', 'NANO_D7',
        'NANO_D8', 'NANO_D9', 'NANO_D10', 'NANO_D11', 'NANO_D12', 'NANO_D13',
        
        # Arduino Analog Pins (with NANO_ aliases)
        'A0', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7',
        'NANO_A0', 'NANO_A1', 'NANO_A2', 'NANO_A3', 'NANO_A4', 'NANO_A5', 'NANO_A6', 'NANO_A7',
        
        # Probe Pad Constants
        'NO_PAD', 'LOGO_PAD_TOP', 'LOGO_PAD_BOTTOM',
        'GPIO_PAD', 'DAC_PAD', 'ADC_PAD',
        'BUILDING_PAD_TOP', 'BUILDING_PAD_BOTTOM',
        
        # Arduino Digital Pin Pads
        'D0_PAD', 'D1_PAD', 'D2_PAD', 'D3_PAD', 'D4_PAD', 'D5_PAD', 'D6_PAD', 'D7_PAD',
        'D8_PAD', 'D9_PAD', 'D10_PAD', 'D11_PAD', 'D12_PAD', 'D13_PAD',
        'RESET_PAD', 'AREF_PAD',
        
        # Arduino Analog Pin Pads
        'A0_PAD', 'A1_PAD', 'A2_PAD', 'A3_PAD', 'A4_PAD', 'A5_PAD', 'A6_PAD', 'A7_PAD',
        
        # Rail Pads
        'TOP_RAIL_PAD', 'BOTTOM_RAIL_PAD', 'BOT_RAIL_PAD',
        'TOP_RAIL_GND', 'TOP_GND_PAD', 'BOTTOM_RAIL_GND', 'BOT_RAIL_GND', 'BOTTOM_GND_PAD', 'BOT_GND_PAD',
        
        # Nano Power/Control Pads
        'NANO_VIN', 'VIN_PAD', 'NANO_RESET_0', 'RESET_0_PAD', 'NANO_RESET_1', 'RESET_1_PAD',
        'NANO_GND_0', 'GND_0_PAD', 'NANO_GND_1', 'GND_1_PAD',
        'NANO_3V3', '3V3_PAD', 'NANO_5V', '5V_PAD',
        
        # Button States
        'BUTTON_NONE', 'BUTTON_CONNECT', 'BUTTON_REMOVE',
        'CONNECT_BUTTON', 'REMOVE_BUTTON',
        
        # Probe Switch States
        'SWITCH_MEASURE', 'SWITCH_SELECT', 'SWITCH_UNKNOWN',
        
        # Clickwheel States
        'CLICKWHEEL_NONE', 'CLICKWHEEL_UP', 'CLICKWHEEL_DOWN',
        'CLICKWHEEL_IDLE', 'CLICKWHEEL_PRESSED', 'CLICKWHEEL_HELD',
        'CLICKWHEEL_RELEASED', 'CLICKWHEEL_DOUBLECLICKED',

        # Wavegen constants
        'SINE', 'TRIANGLE', 'SAWTOOTH', 'SQUARE', 'RAMP', 'ARBITRARY',
        
        # Slot Management
        'CURRENT_SLOT',
    }

    JFS_FUNCTIONS = {
        # Module-level file operations
        'open', 'read', 'write', 'close', 'seek', 'tell', 'size', 'available',
        
        # File object methods (used as f.method())
        'print', 'flush', 'position', 'name',
        
        # Directory operations
        'exists', 'listdir', 'mkdir', 'rmdir', 'remove', 'rename', 'stat', 'info',
        
        # Legacy filesystem functions (jumperless.fs_*)
        'fs_exists', 'fs_listdir', 'fs_read', 'fs_write', 'fs_cwd',
    }
#keep jfs in here, we'll use it for random stuff too
    JFS_CONSTANTS = {
        'SEEK_SET', 'SEEK_CUR', 'SEEK_END', 'jfs', 'FatFS', 'vfs', 'LittleFS', 'SDFS', 
    }
    
    HARDWARE_CONSTANTS = {
        'Select', 'Measure', 'select', 'measure', 'Connect', 'Remove', 
    }

    def get_tokens_unprocessed(self, text):
        """
        Override the parent's token processing to add Jumperless-specific highlighting.
        """
        for index, token, value in PythonLexer.get_tokens_unprocessed(self, text):
            # Check if this is a name token that might be a Jumperless keyword
            if token is Name:
                if value in self.JUMPERLESS_FUNCTIONS:
                    token = JumperlessTokens.JumperlessFunction
                elif value in self.JUMPERLESS_CONSTANTS:
                    token = JumperlessTokens.JumperlessConstant
                elif value in self.JFS_FUNCTIONS:
                    token = JumperlessTokens.JFSFunction
                elif value in self.JFS_CONSTANTS:
                    token = JumperlessTokens.JFSConstant
                elif value in self.HARDWARE_CONSTANTS:
                    token = JumperlessTokens.HardwareConstant
            elif token is Name.Attribute:
                # Handle jfs.function() calls specifically
                if value in self.JFS_FUNCTIONS:
                    token = JumperlessTokens.JFSFunction
                elif value in self.JFS_CONSTANTS:
                    token = JumperlessTokens.JFSConstant
                elif value in self.HARDWARE_CONSTANTS:
                    token = JumperlessTokens.HardwareConstant
            yield index, token, value

    def analyse_text(self, text):
        """
        Analyze text to determine if it's likely Jython code.
        Returns a float between 0.0 and 1.0 indicating confidence.
        """
        import re
        score = 0.0
        
        # Check for Jumperless-specific imports
        if 'import jumperless' in text or 'from jumperless' in text:
            score += 0.8
            
        # Check for Jumperless functions using defined function set
        # Match function names with or without parentheses, using word boundaries
        for func in self.JUMPERLESS_FUNCTIONS:
            # Look for the function name as a whole word, optionally followed by parentheses
            pattern = r'\b' + re.escape(func) + r'(\s*\()?'
            if re.search(pattern, text):
                score = 0.99  # Almost maximum confidence
                break  # Only count once per text
                
        # Check for JFS function calls using defined function set
        # Match both jfs.function and standalone function names
        for func in self.JFS_FUNCTIONS:
            # Look for jfs.function or just the function name as a word
            if f'jfs.{func}' in text or re.search(r'\b' + re.escape(func) + r'\b', text):
                score = 0.99  # Almost maximum confidence
                break  # Only count once per text
                
        # Check for Jumperless constants using defined constant set
        for const in self.JUMPERLESS_CONSTANTS:
            # Use word boundaries to match constants exactly
            if re.search(r'\b' + re.escape(const) + r'\b', text):
                score = 0.99  # Almost maximum confidence
                break  # Only count once per text
                
        # Check for JFS constants using defined constant set
        for const in self.JFS_CONSTANTS:
            if re.search(r'\b' + re.escape(const) + r'\b', text):
                score = 0.99  # High confidence
                break  # Only count once per text
            
        # Check for hardware constants using defined constant set
        for const in self.HARDWARE_CONSTANTS:
            if re.search(r'\b' + re.escape(const) + r'\b', text):
                score = 0.99  # High confidence
                break  # Only count once per text
            
        # Return the score (no need to cap since we're using reasonable values)
        return min(score, 1.0)


# Register the lexer (this would typically be done via entry points in a package)
def get_jumperless_lexer(**options):
    """Factory function to create a Jumperless lexer instance."""
    return JumperlessPythonLexer(**options)


# Export for use
__all__ = ['JumperlessPythonLexer', 'JumperlessTokens', 'get_jumperless_lexer'] 