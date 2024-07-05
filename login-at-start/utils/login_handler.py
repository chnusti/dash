import dash
restricted_page = {}

def require_login(page):
    for pg in dash.page_registry:
        if page == "page-1":
            restricted_page[dash.page_registry[pg]['path']] = True