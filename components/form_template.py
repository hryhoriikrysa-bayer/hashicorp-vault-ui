
from components.custom_styles.custom_form import *
from components.scripts import validate_form_script


def get_submit_form(include_owner_input=False, submit_action=None):
    html = f"""
        <div class="px-5  {container0_bg_color} p-7 rounded-lg shadow-sm0">
            <form id="form" class="space-y-6" onsubmit="{validate_form_script}">
                <div class="space-y-4 p-4 px-6 {container1_bg_color} cursor-pointer border rounded-lg {container1_border_color}">
                    <label for="app" class="block text-base {label_text_color} mb-2">Application</label>
                    <input id="app" type="text" class="form-input w-full px-4 py-2 rounded bg-white text-black" />
                </div>
            
                <div class="space-y-4 p-4 px-6 {container1_bg_color} cursor-pointer border rounded-lg {container1_border_color}">
                    <label for="env" class="block text-base {label_text_color} mb-2">Environment</label>
                    <input id="env" type="text" class="form-input w-full px-4 py-2 rounded bg-white text-black" />
                </div>
            
                <div class="space-y-4 p-4 px-6 {container1_bg_color} cursor-pointer border rounded-lg {container1_border_color}">
                    <label for="sub" class="block text-base {label_text_color} mb-2">Subcomponent</label>
                    <input id="sub" type="text" class="form-input  w-full px-4 py-2 rounded bg-white text-black" />
                </div>
        """

    if include_owner_input:
        html += f"""
                <div class="space-y-4 p-4 px-6 {container1_bg_color} cursor-pointer border rounded-lg {container1_border_color}">
                    <label for="owner" class="block text-base {label_text_color} mb-2">Owner CWID</label>
                    <input id="owner" type="text" class="form-input w-full px-4 py-2 rounded bg-white text-black" />
                </div>
        """

    html += f"""
                <div class="pl-1">
                    <p id="input-error-info" class="{error_message_text_color} text-base"></p>
                </div>
                <div class="">
                    <button type="submit" class="w-full {submit_button_bg_color} {submit_button_text_color} border {submit_button_border_color} hover:{submit_button_hover_bg_color} font-semibold py-2 rounded">
                      Submit
                    </button>
                </div>
            </form>
        </div>
    """

    return html