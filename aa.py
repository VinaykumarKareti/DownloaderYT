# from kivy.app import App
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.button import Button
# from kivy.uix.textinput import TextInput
# from kivy.core.window import Window
# from pytube import YouTube
# from threading import Thread

# class YoutubeDownloaderApp(App):
#     def build(self):
#         Window.clearcolor = (0.2, 0.2, 0.2, 1)  # Set background color to dark gray
#         self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

#         self.url_input = TextInput(hint_text='Enter YouTube URL', multiline=False, background_color=(1, 1, 1, 1))
#         self.download_button = Button(text='Download', on_press=self.download_video, background_color=(0, 0.7, 0.7, 1))
        
#         self.layout.add_widget(self.url_input)
#         self.layout.add_widget(self.download_button)

#         return self.layout

#     def download_video(self, instance):
#         video_url = self.url_input.text
#         if video_url:
#             download_thread = Thread(target=self.download_video_thread, args=(video_url,))
#             download_thread.start()

#     def download_video_thread(self, video_url):
#         try:
#             yt = YouTube(video_url)
#             stream = yt.streams.filter(res="720p").first()
#             stream.download()
#             print(f'Download complete: {yt.title}')
#         except Exception as e:
#             print(f'Error: {e}')

# if __name__ == '__main__':
#     YoutubeDownloaderApp().run()

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.lang import Builder
from pytube import YouTube
from threading import Thread

Builder.load_string('''
<CustomLabel@Label>:
    color: 0, 0.7, 0.7, 1
    font_size: '18sp'
    font_name: 'data/fonts/LucidaSansRegular.ttf'  # Specify the path to the Lucida font
    size_hint_y: None
    height: self.texture_size[1]
    
<CustomBoxLayout@BoxLayout>:
    orientation: 'vertical'
    size_hint_y: None
    height: self.minimum_height
    background_color: 0.53, 0.81, 0.98, 1
''')

class YoutubeDownloaderApp(App):
    def build(self):
        Window.clearcolor = (0.2, 0.2, 0.2, 1)  # Set background color to dark gray
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.url_input = TextInput(hint_text='Enter YouTube URL', multiline=False, background_color=(1, 1, 1, 1))
        self.download_button = Button(text='Download', on_press=self.download_video, background_color=(0, 0.7, 0.7, 1))

        self.status_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.status_label = Label(text='', color=(1, 0, 0, 1), font_size='18sp', bold=True)

        self.status_layout.add_widget(self.status_label)

        self.layout.add_widget(self.url_input)
        self.layout.add_widget(self.download_button)
        self.layout.add_widget(self.status_layout)

        return self.layout

    def download_video(self, instance):
        video_url = self.url_input.text
        if video_url:
            self.status_label.text = 'Downloading...'
            download_thread = Thread(target=self.download_video_thread, args=(video_url,))
            download_thread.start()

    def download_video_thread(self, video_url):
        try:
            yt = YouTube(video_url)
            stream = yt.streams.filter(res="720p").first()
            stream.download()
            self.status_label.text = f'Download complete: {yt.title}'
            self.status_label.color = (0, 1, 0, 1)  # Green color for success
        except Exception as e:
            self.status_label.text = f'Error: {e}'
            self.status_label.color = (1, 0, 0, 1)  # Red color for failure

if __name__ == '__main__':
    YoutubeDownloaderApp().run()
