from components.optional.tree_list.tree_list_divs import get_level0_container, get_level1_container, get_subcomponents_container

def generate_tree_list(data, level=0, parent_path=""):
    html = ""
    parent_path = parent_path + "/"

    if isinstance(data, dict):
        for i, (element, val) in enumerate(data.items()):
            row_id = f"{element.replace(' ', '_')}_{level}_{i}"

            if level == 0:
                html += get_level0_container(element=element, row_id=row_id, parent_path=parent_path)
                html += f"""
                    <div id="{row_id}"">
                        {generate_tree_list(val, level + 1, parent_path+element)}
                    </div>
                    """
            elif level == 1:
                html += get_level1_container(element=element, row_id=row_id, parent_path=parent_path)
                html += f"""
                    <div id="{row_id}" class="hidden ml-4 p-2 space-y-3">
                        {generate_tree_list(val, level + 1, parent_path+element)}
                    </div>
                    """

            html += "</div>"

    elif isinstance(data, list):
        for element in data:
            html += get_subcomponents_container(element, parent_path=parent_path)

    return html
