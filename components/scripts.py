config_head = """
    <script src="https://cdn.tailwindcss.com"></script>
"""


validate_form_script = """
    document.addEventListener('DOMContentLoaded', function () {
        const form = document.getElementById('form');
    
        form.addEventListener('submit', function (event) {
            event.preventDefault();
    
            const inputs = form.querySelectorAll('input.form-input');
            const regex = /^[a-zA-Z0-9]+$/;
            let allValid = true;
    
            inputs.forEach((input) => {
                const value = input.value.trim();
                input.classList.remove('border-rose-800', 'ring-2', 'ring-rose-600');
    
                if (!regex.test(value)) {
                    input.classList.add('border-rose-800', 'ring-2', 'ring-rose-600');
                    allValid = false;
                }
            });
    
            if (!allValid) {
                document.getElementById('input-error-info').textContent = "Invalid input";
            }
        });
    });
"""