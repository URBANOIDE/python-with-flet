import flet as ft
def main(page: ft.Page):
    page.add(ft.Text("hola mundo"))
ft.app(target=main, view=ft.WEB_BROWSER) #for web browser
#ft.app(main) #for app desktop