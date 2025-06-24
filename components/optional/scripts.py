toggle_hidden_script = """
    function toggleRow(id) {{
        const el = document.getElementById(id);
        el.classList.toggle("hidden");
    }}
    function customAction(value) {{
        alert("Action for: " + value);
    }}
"""


toggle_modal_script = """
    function openModal(modalId, selectedElement = null, elementParentPath = null) {
        const modal = document.getElementById(modalId);
        if (!modal) return;
        console.log(selectedElement);
        console.log(elementParentPath);
        
        modal.classList.remove("hidden");
        boxes = document.querySelectorAll('.selectedPathName');
        
        boxes.forEach(el => {
            el.textContent = elementParentPath + selectedElement
        });

    }
        
    function closeModal(modalId) {
        const modal = document.getElementById(modalId);
        if (modal) modal.classList.add("hidden");
    }
"""

go_to_details_script = """
    function goToDetails(selectedElement, elementParentPath) {
        console.log(elementParentPath + selectedElement);
    }
"""