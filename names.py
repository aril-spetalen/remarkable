from objectmaphelper import *

application_window = {"type": "QQuickWindowQmlImpl", "title": "remarkable_mobile"}

# Top menu bar
topMenu_new_folder = {"container": application_window, "id": "newFolder", "type": "RMIconButton"}
topMenu_search = {"container": application_window, "id": "searchButton", "type": "RMIconButton"}
back_button = {"container": application_window, "id": "backButton", "type": "RMIconButton"}

# Drawer objects (when long-pressing items)
drawer_select_multiple = {"container": application_window, "text": "Select multiple", "type": "SidebarItem"}
drawer_copy = {"container": application_window, "text": "Copy", "type": "SidebarItem"}
drawer_move = {"container": application_window, "text": "Move", "type": "SidebarItem"}
drawer_rename = {"container": application_window, "text": "Rename", "type": "SidebarItem"}
drawer_favorite = {"container": application_window, "text": "Favorite", "type": "SidebarItem"}
drawer_move_to_trash = {"container": application_window, "text": "Move to trash", "type": "SidebarItem"}
drawer_share = {"container": application_window, "text": "Share", "type": "SidebarItem"}
drawer_delete = {"container": application_window, "text": "Delete", "type": "SidebarItem"}
drawer_restore = {"container": application_window, "text": "Restore", "type": "SidebarItem"}

# Header objects (when completing or cancelling multiple items selection)
header_cancel = {"container": application_window, "id": "cancelButton","type": "RMIconButton"}
header_done = {"container": application_window, "id": "doneButton", "type": "RMIconButton"}

# Move action buttons
movepanel_move_here = {"container": application_window, "id": "moveButton", "type": "NavigatorToolButton"}
movepanel_cancel_move = {"container": application_window, "id": "cancelMoveButton", "type": "NavigatorToolButton"}
movepanel_label = {"container": application_window, "id": "moveLabel", "type": "StyledText", "text": "Select a destination for your item"}

# Sidebar menu items
sidebar_my_files = {"container": application_window, "id": "filterMyFiles", "type": "SidebarFilterItem"}
sidebar_notebooks = {"container": application_window, "id": "filterNotebooks", "type": "SidebarFilterItem"}
sidebar_pdfs = {"container": application_window, "id": "filterDocuments", "type": "SidebarFilterItem"}
sidebar_ebooks = {"container": application_window, "id": "filterEbooks", "type": "SidebarFilterItem"}
sidebar_favorites = {"container": application_window, "id": "filterPinned", "type": "SidebarFilterItem"}
sidebar_trash = {"container": application_window, "id": "filterTrashed", "type": "SidebarFilterItem"}
sidebar_settings = {"container": application_window, "id": "settingsButton", "type": "SidebarFilterItem"}

# Layout styles
layout_GridView = {"container": application_window, "id": "gridView", "type": "GridView"}
layout_ListView = {"container": application_window, "id": "listView", "type": "ListView"}

# Search view
search_input_field = {"container": application_window, "id": "searchField", "type": "TextInput"}
search_results = {"container": application_window, "id": "searchGridView", "type": "EntryGridView"} 
