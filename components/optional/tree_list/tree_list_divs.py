from components.optional.custom_styles.custom_mysecrets import *


def get_level0_container(element, row_id, parent_path=None):
    html = f"""
            <div class="{container0_bg_color} p-7 rounded-lg shadow-sm0">
                <div class="flex justify-between items-center p-4 mb-3 {container1_bg_color} cursor-pointer border rounded-lg {container1_border_color}" onclick="toggleRow('{row_id}')">
                    <div class="">
                        <p class="font-bold {text1_color}">{element}</p>
                    </div>
                    <div class="grid grid-cols-3 grid-rows-1 gap-2 divide-x divide-gray-500">
                        <div class="hidden flex items-center px-2 py-1 rounded"></div>
                        <button onclick="event.stopPropagation(); openModal('grant-modal', '{element}', '{parent_path}')" class="flex items-center px-2 py-1 rounded">
                          <svg xmlns="http://www.w3.org/2000/svg" class="ml-2 w-5 {ownership_button_stroke_color} cursor-pointer" fill="currentColor" viewBox="0 0 24 24" stroke="currentColor">
                              <path d="M5.25 6.375a4.125 4.125 0 1 1 8.25 0 4.125 4.125 0 0 1-8.25 0ZM2.25 19.125a7.125 7.125 0 0 1 14.25 0v.003l-.001.119a.75.75 0 0 1-.363.63 13.067 13.067 0 0 1-6.761 1.873c-2.472 0-4.786-.684-6.76-1.873a.75.75 0 0 1-.364-.63l-.001-.122ZM18.75 7.5a.75.75 0 0 0-1.5 0v2.25H15a.75.75 0 0 0 0 1.5h2.25v2.25a.75.75 0 0 0 1.5 0v-2.25H21a.75.75 0 0 0 0-1.5h-2.25V7.5Z" />
                          </svg>
                        </button>
                        
                        <button onclick="event.stopPropagation(); openModal('revoke-modal', '{element}', '{parent_path}')" class="flex items-center  px-2 py-1 rounded">
                          <svg xmlns="http://www.w3.org/2000/svg" class="ml-2 w-5 {ownership_button_stroke_color} cursor-pointer" viewBox="0 0 24 24" fill="currentColor" stroke="currentColor">
                              <path d="M10.375 2.25a4.125 4.125 0 1 0 0 8.25 4.125 4.125 0 0 0 0-8.25ZM10.375 12a7.125 7.125 0 0 0-7.124 7.247.75.75 0 0 0 .363.63 13.067 13.067 0 0 0 6.761 1.873c2.472 0 4.786-.684 6.76-1.873a.75.75 0 0 0 .364-.63l.001-.12v-.002A7.125 7.125 0 0 0 10.375 12ZM16 9.75a.75.75 0 0 0 0 1.5h6a.75.75 0 0 0 0-1.5h-6Z" />
                          </svg>
                        </button>
                        
                        <button onclick="event.stopPropagation(); openModal('delete-modal', '{element}', '{parent_path}')" class="flex items-center  px-2 py-1 rounded">
                           <svg xmlns="http://www.w3.org/2000/svg" class="ml-2 w-5 {delete_button_stroke_color} cursor-pointer" viewBox="0 0 24 24" fill="currentColor" stroke="currentColor">
                              <path fill-rule="evenodd" d="M16.5 4.478v.227a48.816 48.816 0 0 1 3.878.512.75.75 0 1 1-.256 1.478l-.209-.035-1.005 13.07a3 3 0 0 1-2.991 2.77H8.084a3 3 0 0 1-2.991-2.77L4.087 6.66l-.209.035a.75.75 0 0 1-.256-1.478A48.567 48.567 0 0 1 7.5 4.705v-.227c0-1.564 1.213-2.9 2.816-2.951a52.662 52.662 0 0 1 3.369 0c1.603.051 2.815 1.387 2.815 2.951Zm-6.136-1.452a51.196 51.196 0 0 1 3.273 0C14.39 3.05 15 3.684 15 4.478v.113a49.488 49.488 0 0 0-6 0v-.113c0-.794.609-1.428 1.364-1.452Zm-.355 5.945a.75.75 0 1 0-1.5.058l.347 9a.75.75 0 1 0 1.499-.058l-.346-9Zm5.48.058a.75.75 0 1 0-1.498-.058l-.347 9a.75.75 0 0 0 1.5.058l.345-9Z" clip-rule="evenodd" />
                            </svg>
                        </button>
                    </div>
                </div>
            """
    return html

def get_level1_container(element, row_id, parent_path=None):
    html = f"""
            <div class="{container0_bg_color} p-4 rounded-lg shadow-sm0">
                <div class="flex justify-between items-center p-4 {container2_bg_color} cursor-pointer border {container2_border_color} rounded-lg" onclick="toggleRow('{row_id}')">
                    <div class="">
                        <p class="font-medium {text1_color}">{element}</p>
                    </div>
                    <div class="grid grid-cols-3 grid-rows-1 gap-2 divide-x divide-gray-500">
                        <div class="hidden flex items-center px-2 py-1 rounded"></div>
                        <button onclick="event.stopPropagation(); openModal('grant-modal', '{element}', '{parent_path}')" class="flex items-center px-2 py-1 rounded">
                          <svg xmlns="http://www.w3.org/2000/svg" class="ml-2 w-5 {ownership_button_stroke_color} cursor-pointer" fill="currentColor" viewBox="0 0 24 24" stroke="currentColor">
                              <path d="M5.25 6.375a4.125 4.125 0 1 1 8.25 0 4.125 4.125 0 0 1-8.25 0ZM2.25 19.125a7.125 7.125 0 0 1 14.25 0v.003l-.001.119a.75.75 0 0 1-.363.63 13.067 13.067 0 0 1-6.761 1.873c-2.472 0-4.786-.684-6.76-1.873a.75.75 0 0 1-.364-.63l-.001-.122ZM18.75 7.5a.75.75 0 0 0-1.5 0v2.25H15a.75.75 0 0 0 0 1.5h2.25v2.25a.75.75 0 0 0 1.5 0v-2.25H21a.75.75 0 0 0 0-1.5h-2.25V7.5Z" />
                          </svg>
                        </button>
                        
                        <button onclick="event.stopPropagation(); openModal('revoke-modal', '{element}', '{parent_path}')" class="flex items-center  px-2 py-1 rounded">
                          <svg xmlns="http://www.w3.org/2000/svg" class="ml-2 w-5 {ownership_button_stroke_color} cursor-pointer" viewBox="0 0 24 24" fill="currentColor" stroke="currentColor">
                              <path d="M10.375 2.25a4.125 4.125 0 1 0 0 8.25 4.125 4.125 0 0 0 0-8.25ZM10.375 12a7.125 7.125 0 0 0-7.124 7.247.75.75 0 0 0 .363.63 13.067 13.067 0 0 0 6.761 1.873c2.472 0 4.786-.684 6.76-1.873a.75.75 0 0 0 .364-.63l.001-.12v-.002A7.125 7.125 0 0 0 10.375 12ZM16 9.75a.75.75 0 0 0 0 1.5h6a.75.75 0 0 0 0-1.5h-6Z" />
                          </svg>
                        </button>
                        
                        <button onclick="event.stopPropagation(); openModal('delete-modal', '{element}', '{parent_path}')" class="flex items-center  px-2 py-1 rounded">
                           <svg xmlns="http://www.w3.org/2000/svg" class="ml-2 w-5 {delete_button_stroke_color} cursor-pointer" viewBox="0 0 24 24" fill="currentColor" stroke="currentColor">
                              <path fill-rule="evenodd" d="M16.5 4.478v.227a48.816 48.816 0 0 1 3.878.512.75.75 0 1 1-.256 1.478l-.209-.035-1.005 13.07a3 3 0 0 1-2.991 2.77H8.084a3 3 0 0 1-2.991-2.77L4.087 6.66l-.209.035a.75.75 0 0 1-.256-1.478A48.567 48.567 0 0 1 7.5 4.705v-.227c0-1.564 1.213-2.9 2.816-2.951a52.662 52.662 0 0 1 3.369 0c1.603.051 2.815 1.387 2.815 2.951Zm-6.136-1.452a51.196 51.196 0 0 1 3.273 0C14.39 3.05 15 3.684 15 4.478v.113a49.488 49.488 0 0 0-6 0v-.113c0-.794.609-1.428 1.364-1.452Zm-.355 5.945a.75.75 0 1 0-1.5.058l.347 9a.75.75 0 1 0 1.499-.058l-.346-9Zm5.48.058a.75.75 0 1 0-1.498-.058l-.347 9a.75.75 0 0 0 1.5.058l.345-9Z" clip-rule="evenodd" />
                            </svg>
                        </button>
                    </div>
                </div>
            """

    return html

def get_subcomponents_container(element, parent_path=None):
    html = f"""
           <div class="flex justify-between items-center m-3">
               <span class="{text1_color} m-2"> {element}</span>
               <div class="grid grid-cols-3 grid-rows-1 gap-2 divide-x divide-gray-500">
                  <div class="hidden flex items-center px-2 py-1 rounded"></div>
                        <button onclick="event.stopPropagation(); openModal('grant-modal', '{element}', '{parent_path}')" class="flex items-center px-2 py-1 rounded">
                          <svg xmlns="http://www.w3.org/2000/svg" class="ml-2 w-5 {ownership_button_stroke_color} cursor-pointer" fill="currentColor" viewBox="0 0 24 24" stroke="currentColor">
                              <path d="M5.25 6.375a4.125 4.125 0 1 1 8.25 0 4.125 4.125 0 0 1-8.25 0ZM2.25 19.125a7.125 7.125 0 0 1 14.25 0v.003l-.001.119a.75.75 0 0 1-.363.63 13.067 13.067 0 0 1-6.761 1.873c-2.472 0-4.786-.684-6.76-1.873a.75.75 0 0 1-.364-.63l-.001-.122ZM18.75 7.5a.75.75 0 0 0-1.5 0v2.25H15a.75.75 0 0 0 0 1.5h2.25v2.25a.75.75 0 0 0 1.5 0v-2.25H21a.75.75 0 0 0 0-1.5h-2.25V7.5Z" />
                          </svg>
                        </button>
                        
                        <button onclick="event.stopPropagation(); openModal('revoke-modal', '{element}', '{parent_path}')" class="flex items-center  px-2 py-1 rounded">
                          <svg xmlns="http://www.w3.org/2000/svg" class="ml-2 w-5 {ownership_button_stroke_color} cursor-pointer" viewBox="0 0 24 24" fill="currentColor" stroke="currentColor">
                              <path d="M10.375 2.25a4.125 4.125 0 1 0 0 8.25 4.125 4.125 0 0 0 0-8.25ZM10.375 12a7.125 7.125 0 0 0-7.124 7.247.75.75 0 0 0 .363.63 13.067 13.067 0 0 0 6.761 1.873c2.472 0 4.786-.684 6.76-1.873a.75.75 0 0 0 .364-.63l.001-.12v-.002A7.125 7.125 0 0 0 10.375 12ZM16 9.75a.75.75 0 0 0 0 1.5h6a.75.75 0 0 0 0-1.5h-6Z" />
                          </svg>
                        </button>
                        
                        <button onclick="event.stopPropagation(); openModal('delete-modal', '{element}', '{parent_path}')" class="flex items-center  px-2 py-1 rounded">
                           <svg xmlns="http://www.w3.org/2000/svg" class="ml-2 w-5 {delete_button_stroke_color} cursor-pointer" viewBox="0 0 24 24" fill="currentColor" stroke="currentColor">
                              <path fill-rule="evenodd" d="M16.5 4.478v.227a48.816 48.816 0 0 1 3.878.512.75.75 0 1 1-.256 1.478l-.209-.035-1.005 13.07a3 3 0 0 1-2.991 2.77H8.084a3 3 0 0 1-2.991-2.77L4.087 6.66l-.209.035a.75.75 0 0 1-.256-1.478A48.567 48.567 0 0 1 7.5 4.705v-.227c0-1.564 1.213-2.9 2.816-2.951a52.662 52.662 0 0 1 3.369 0c1.603.051 2.815 1.387 2.815 2.951Zm-6.136-1.452a51.196 51.196 0 0 1 3.273 0C14.39 3.05 15 3.684 15 4.478v.113a49.488 49.488 0 0 0-6 0v-.113c0-.794.609-1.428 1.364-1.452Zm-.355 5.945a.75.75 0 1 0-1.5.058l.347 9a.75.75 0 1 0 1.499-.058l-.346-9Zm5.48.058a.75.75 0 1 0-1.498-.058l-.347 9a.75.75 0 0 0 1.5.058l.345-9Z" clip-rule="evenodd" />
                            </svg>
                        </button>
                    </div>
           </div>
           <hr class='{container3_border_color}'>
        """

    return html
