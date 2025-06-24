from components.optional.custom_styles.custom_modals import *


def revoke_ownership_modal(owners=None):
    owners = [
        {"name": "John Doe", "cwid": "xyz"},
        {"name": "Jane Smith", "cwid": "abc"},
        {"name": "Mike Brown", "cwid": "def"},
        {"name": "Mike Brown", "cwid": "def"},
        # {"name": "John Doe", "cwid": "xyz"},
        # # {"name": "Jane Smith", "cwid": "abc"},
        # # {"name": "Mike Brown", "cwid": "def"},
        # # {"name": "Mike Brown", "cwid": "def"}
    ]

    checkboxes = ""
    button = ""
    height = 60

    if owners:
        button = f"""<button onclick="saveChanges()" class="px-4 py-2 {modal_h2_text_color} {modal_save_button_bg_color} rounded hover:{modal_save_button_hover_color}">Revoke</button>"""
        for owner in owners:
            checkboxes += f"""
                    <label class="flex items-center space-x-2">
                        <input type="checkbox" class="form-checkbox h-5 w-5 text-blue-600" value="{owner['cwid']}" />
                        <span class="text-sm {modal_h2_text_color}">{owner['name']} ({owner['cwid']})</span>
                    </label>
                """
            height += 5
    else:
        checkboxes += f"""
            <p class="{modal_notice_text_color} mt-2 text-m ">
                No owners to revoke.
            </p>
        """
        height += 4

    html = f"""
        <div id="revoke-modal" class="fixed inset-0 {modal_bg_color} flex justify-center hidden z-30">
          <div class="{modal_form_bg_color} border {modal_form_border_color} rounded-lg shadow-lg p-6 relative h-[80%] w-1/2 px-6 py-8">
            <div>
                <span class="inline-flex items-center justify-center rounded-md {ownership_icon_bg_color} p-4 shadow-lg mr-8">         
                    <svg xmlns="http://www.w3.org/2000/svg" class=" w-5 {ownership_icon_stroke_color}" viewBox="0 0 24 24" fill="currentColor" stroke="currentColor">
                        <path d="M10.375 2.25a4.125 4.125 0 1 0 0 8.25 4.125 4.125 0 0 0 0-8.25ZM10.375 12a7.125 7.125 0 0 0-7.124 7.247.75.75 0 0 0 .363.63 13.067 13.067 0 0 0 6.761 1.873c2.472 0 4.786-.684 6.76-1.873a.75.75 0 0 0 .364-.63l.001-.12v-.002A7.125 7.125 0 0 0 10.375 12ZM16 9.75a.75.75 0 0 0 0 1.5h6a.75.75 0 0 0 0-1.5h-6Z" />
                    </svg>
                </span>
            </div>

            <h2 class="{modal_h2_text_color} mt-5 text-base font-medium tracking-tight ">Revoke ownership</h3>
            <p class="{modal_p_text_color} mt-2 text-m ">
                Revoke ownership to other users. Select users to be revoked from path
                <span class='selectedPathName {modal_notice_text_color}'></span>.
            </p>

            <div class="mt-8 space-y-3 overflow-y-auto h-[25%]">
              {checkboxes}
            </div>

            <div class="flex justify-end gap-2 mt-7">
              <button onclick="closeModal('revoke-modal')" class="px-4 py-2 rounded {modal_cancel_button_bg_color} hover:{modal_cancel_button_hover_color}">Cancel</button>
                {button}            
            </div>

          </div>
        </div>
        """

    return html


grant_ownership_modal = f"""
<div id="grant-modal" class="fixed inset-0 {modal_bg_color} flex justify-center hidden z-30">
  <div class="{modal_form_bg_color} border {modal_form_border_color} rounded-lg shadow-lg p-3 relative h-[70%] w-1/2 px-6 py-8">
    <div>
        <span class="inline-flex items-center justify-center rounded-md {ownership_icon_bg_color} p-4 shadow-lg">         
            <svg xmlns="http://www.w3.org/2000/svg" class="w-6 {ownership_icon_stroke_color}" fill="currentColor" viewBox="0 0 24 24" stroke="currentColor">
                <path d="M5.25 6.375a4.125 4.125 0 1 1 8.25 0 4.125 4.125 0 0 1-8.25 0ZM2.25 19.125a7.125 7.125 0 0 1 14.25 0v.003l-.001.119a.75.75 0 0 1-.363.63 13.067 13.067 0 0 1-6.761 1.873c-2.472 0-4.786-.684-6.76-1.873a.75.75 0 0 1-.364-.63l-.001-.122ZM18.75 7.5a.75.75 0 0 0-1.5 0v2.25H15a.75.75 0 0 0 0 1.5h2.25v2.25a.75.75 0 0 0 1.5 0v-2.25H21a.75.75 0 0 0 0-1.5h-2.25V7.5Z" />
            </svg>
        </span>
    </div>
    
    <h2 class="{modal_h2_text_color} mt-5 text-base font-medium tracking-tight ">Edit ownership</h3>
    <p class="{modal_p_text_color} mt-2 text-m ">
        Grant ownership of path <span class='selectedPathName {modal_notice_text_color}'></span> to other users. Provide user's CWID below.
    </p>
    
    <input type="text" id="editInput" class="w-full border rounded p-2 mb-4 mt-8" />

    <div class="flex justify-end gap-2">
      <button onclick="closeModal('grant-modal')" class="px-4 py-2 rounded {modal_cancel_button_bg_color} hover:{modal_cancel_button_hover_color}">Cancel</button>
      <button onclick="saveChanges()" class="px-4 py-2 {modal_h2_text_color} {modal_save_button_bg_color} rounded hover:{modal_save_button_hover_color}">Grant</button>
    </div>
  </div>
</div>
"""

delete_item_modal = f"""
<div id="delete-modal" class="fixed inset-0 {modal_bg_color} flex justify-center pt-12 hidden z-30">
  <div class="{modal_form_bg_color} border {modal_delete_border_color} rounded-lg shadow-lg p-6 relative h-[68%] w-1/2">
      <div>
        <span class="inline-flex items-center justify-center rounded-md {delete_icon_bg_color} p-4 shadow-lg">         
            <svg xmlns="http://www.w3.org/2000/svg" class="w-5 {delete_icon_stroke_color} cursor-pointer" viewBox="0 0 24 24" fill="currentColor" stroke="currentColor">
               <path fill-rule="evenodd" d="M16.5 4.478v.227a48.816 48.816 0 0 1 3.878.512.75.75 0 1 1-.256 1.478l-.209-.035-1.005 13.07a3 3 0 0 1-2.991 2.77H8.084a3 3 0 0 1-2.991-2.77L4.087 6.66l-.209.035a.75.75 0 0 1-.256-1.478A48.567 48.567 0 0 1 7.5 4.705v-.227c0-1.564 1.213-2.9 2.816-2.951a52.662 52.662 0 0 1 3.369 0c1.603.051 2.815 1.387 2.815 2.951Zm-6.136-1.452a51.196 51.196 0 0 1 3.273 0C14.39 3.05 15 3.684 15 4.478v.113a49.488 49.488 0 0 0-6 0v-.113c0-.794.609-1.428 1.364-1.452Zm-.355 5.945a.75.75 0 1 0-1.5.058l.347 9a.75.75 0 1 0 1.499-.058l-.346-9Zm5.48.058a.75.75 0 1 0-1.498-.058l-.347 9a.75.75 0 0 0 1.5.058l.345-9Z" clip-rule="evenodd" />
            </svg>
        </span>
    </div>
    
    <h2 class="{modal_h2_text_color} mt-5 text-base font-medium tracking-tight ">Delete secret path</h3>
    <p class="{modal_p_text_color} mt-2 text-m mb-4">
        Are you sure you want to delete path for </br>
            <span class='selectedPathName {modal_delete_item_text_color}'>f</span>? <br>
        Every underlying secret will be removed. 
    </p>    
    
    <div class="flex justify-end gap-2 p-2 mb-4 mt-8">
      <button onclick="closeModal('delete-modal')" class="px-4 py-2 rounded {modal_cancel_button_bg_color} hover:{modal_cancel_button_hover_color}">Cancel</button>
      <button onclick="saveChanges()" class="px-4 py-2 {modal_h2_text_color} {modal_delete_button_bg_color} rounded hover:{modal_delete_button_hover_color}">Delete</button>
    </div>
    
  </div>
</div>
"""