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
        'FakeGpioDisconnect',
        'FakeGpioPin',
        'adc_get',
        'arduino_reset',
        'button_check',
        'button_read',
        'change_terminal_color',
        'check_button',
        'check_switch_position',
        'clickwheel_down',
        'clickwheel_get_button',
        'clickwheel_get_direction',
        'clickwheel_get_position',
        'clickwheel_is_initialized',
        'clickwheel_press',
        'clickwheel_reset_position',
        'clickwheel_up',
        'connect',
        'context_get',
        'context_toggle',
        'cycle_term_color',
        'dac_get',
        'dac_set',
        'disconnect',
        'fast_connect',
        'fast_disconnect',
        'force_service',
        'force_service_by_index',
        'fs_cwd',
        'fs_exists',
        'fs_listdir',
        'fs_read',
        'fs_write',
        'get_adc',
        'get_all_nets',
        'get_all_paths',
        'get_bridge',
        'get_bus_voltage',
        'get_button',
        'get_current',
        'get_dac',
        'get_gpio',
        'get_gpio_dir',
        'get_gpio_pull',
        'get_gpio_read_floating',
        'get_ina_bus_voltage',
        'get_ina_current',
        'get_ina_power',
        'get_ina_voltage',
        'get_net_color',
        'get_net_color_name',
        'get_net_info',
        'get_net_name',
        'get_net_nodes',
        'get_num_bridges',
        'get_num_nets',
        'get_num_paths',
        'get_path_between',
        'get_path_info',
        'get_power',
        'get_service_index',
        'get_state',
        'get_switch_position',
        'get_voltage',
        'get_wavegen_amplitude',
        'get_wavegen_freq',
        'get_wavegen_offset',
        'get_wavegen_output',
        'get_wavegen_wave',
        'gpio_claim_pin',
        'gpio_get',
        'gpio_get_dir',
        'gpio_get_pull',
        'gpio_get_read_floating',
        'gpio_release_all_pins',
        'gpio_release_pin',
        'gpio_set',
        'gpio_set_dir',
        'gpio_set_pull',
        'gpio_set_read_floating',
        'help',
        'ina_get_bus_voltage',
        'ina_get_current',
        'ina_get_power',
        'ina_get_voltage',
        'io',
        'is_connected',
        'jfs',
        'la_capture_single_sample',
        'la_enable_channel',
        'la_get_control_analog',
        'la_get_control_digital',
        'la_is_capturing',
        'la_set_control_analog',
        'la_set_control_digital',
        'la_set_num_samples',
        'la_set_sample_rate',
        'la_set_trigger',
        'la_start_continuous_capture',
        'la_stop_capture',
        'net_color',
        'net_info',
        'net_name',
        'node',
        'nodes_clear',
        'nodes_discard',
        'nodes_has_changes',
        'nodes_help',
        'nodes_save',
        'oled_clear',
        'oled_connect',
        'oled_copy_print',
        'oled_disconnect',
        'oled_display_bitmap',
        'oled_get_current_font',
        'oled_get_fonts',
        'oled_get_framebuffer',
        'oled_get_framebuffer_size',
        'oled_get_pixel',
        'oled_get_text_size',
        'oled_load_bitmap',
        'oled_print',
        'oled_set_font',
        'oled_set_framebuffer',
        'oled_set_pixel',
        'oled_set_text_size',
        'oled_show',
        'oled_show_bitmap_file',
        'os',
        'overlay_clear',
        'overlay_clear_all',
        'overlay_count',
        'overlay_place',
        'overlay_serialize',
        'overlay_set',
        'overlay_set_pixel',
        'overlay_shift',
        'pause_core2',
        'print_bridges',
        'print_chip_status',
        'print_crossbars',
        'print_nets',
        'print_paths',
        'probe_button',
        'probe_button_blocking',
        'probe_button_nonblocking',
        'probe_read',
        'probe_read_blocking',
        'probe_read_nonblocking',
        'probe_tap',
        'probe_touch',
        'probe_wait',
        'pwm',
        'pwm_set_duty_cycle',
        'pwm_set_frequency',
        'pwm_stop',
        'read_button',
        'read_probe',
        'run_app',
        'send_raw',
        'set_dac',
        'set_gpio',
        'set_gpio_dir',
        'set_gpio_pull',
        'set_gpio_read_floating',
        'set_net_color',
        'set_net_color_hsv',
        'set_net_name',
        'set_pwm',
        'set_pwm_duty_cycle',
        'set_pwm_frequency',
        'set_state',
        'set_switch_position',
        'set_wavegen_amplitude',
        'set_wavegen_freq',
        'set_wavegen_offset',
        'set_wavegen_output',
        'set_wavegen_sweep',
        'set_wavegen_wave',
        'start_wavegen',
        'stop_pwm',
        'stop_wavegen',
        'switch_slot',
        'wait_probe',
        'wait_touch',
        'wavegen_get_amplitude',
        'wavegen_get_freq',
        'wavegen_get_offset',
        'wavegen_get_output',
        'wavegen_get_wave',
        'wavegen_is_running',
        'wavegen_set_amplitude',
        'wavegen_set_freq',
        'wavegen_set_offset',
        'wavegen_set_output',
        'wavegen_set_sweep',
        'wavegen_set_wave',
        'wavegen_start',
        'wavegen_stop',
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
        
        # FakeGPIO Modes
        'FAKE_GPIO_INPUT', 'FAKE_GPIO_OUTPUT',
        
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