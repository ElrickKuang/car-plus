import flet as ft


def main(page: ft.Page):
    page.bgcolor=ft.colors.BLACK87
    greeding=ft.SafeArea(ft.Text("Hello, Welcome to C+ CAR SPA"))
    operating_hour=ft.Text("Operating Hour 8:30am-6:00pm > DailyLunchBreak")
    img = ft.Image(
        src=f"/icons/logo.jpg",
        width=100,
        height=100,
        border_radius=10,
        fit=ft.ImageFit.CONTAIN,
    )
    # Create WhatsApp button with icon
    whatsapp_button = ft.ElevatedButton(
        text="Contact on WhatsApp",
        icon=ft.icons.MESSAGE,
        on_click=lambda e: page.launch_url("https://wa.me/60168687563")
    )
    
    # Create Facebook button with icon
    facebook_button = ft.ElevatedButton(
        text="Visit Facebook Profile",
        icon=ft.icons.FACEBOOK,
        on_click=lambda e: page.launch_url("https://www.facebook.com/CPLUSCARSPA")
    )
    
    page.add( 
        ft.Container(
            ft.Column(
                [
                    img,
                    greeding,
                    operating_hour,
                    ft.Container(height=10),
                    whatsapp_button,
                    ft.Container(height=10),
                    facebook_button
                 ],
                 alignment=ft.alignment.center,
                 horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            alignment=ft.alignment.center,
            padding=20,
        
            
        ),
        
    )
    
ft.app(main)




# import flet as ft

# def main(page: ft.Page):
#     page.title = "Images Example"
#     page.theme_mode = ft.ThemeMode.DARK
#     page.padding = 50
#     page.update()

#     img = ft.Image(
#         src=f"/icons/icon-192.png",
#         width=100,
#         height=100,
#         fit=ft.ImageFit.CONTAIN,
#     )
#     images = ft.Row(expand=1, wrap=False, scroll="always")

#     page.add(img, images)

#     for i in range(0, 30):
#         images.controls.append(
#             ft.Image(
#                 src=f"https://picsum.photos/200/200?{i}",
#                 width=200,
#                 height=200,
#                 fit=ft.ImageFit.NONE,
#                 repeat=ft.ImageRepeat.NO_REPEAT,
#                 border_radius=ft.border_radius.all(10),
#             )
#         )
#     page.update()

# ft.app(target=main)