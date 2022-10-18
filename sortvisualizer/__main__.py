import pygame
from data_class import Data
from sortalgorithms.base import BaseSort
from sortvisualizer.sortalgorithms.selectionsort import SelectedSort

def cycle_generator(x):
    while True:
        for i in x:
            yield i

class MainWindow:
    def __init__(self, data_size = 100) -> None:
        pygame.init()
        pygame.mixer.init()
        self._width = 800
        self._height = 600
        _window_size = (self._width, self._height)
        self._screen = pygame.display.set_mode(_window_size)
        self._background_color = (0, 0, 0)
        self._sorting = False
        self._animated = False
        pygame.display.set_caption("Sort Visualizer")
        self._is_running = True
        self._sort_algorithms = cycle_generator(
            [
                BaseSort(Data(size=data_size)),
                SelectedSort(Data(size=data_size)),
            ]
            )
        self._sort_algorithm :BaseSort = next(self._sort_algorithms)

    def stop(self):
        self._is_running = False
        print("Closing the sort visualizer ...")
    def check_event(self):
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    self.stop()
                    break
                case pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_ESCAPE:
                            self.stop()
                            break
                        case pygame.K_s:
                            print("sort data")
                            self._sorting = True
                            break
                        case pygame.K_a:
                            print("change animated ...")
                            self._animated = not self._animated 
                            break
                        case pygame.K_q:
                            print("change algorithm ...")
                            self.change_algorithm()
                            break
                        case pygame.K_d:
                            print("update data ...")
                            self._sort_algorithm.reset()
                            self._sorting = False
                            break
                        
    def draw_data(self, data:Data):
        width = int(self._width / len(data))
        for i, value in enumerate(data.data):
            x = i * width

            height = value * (self._height / (self._height/4))
            y = self._height - (value  * (self._height / (self._height/4))) 

            color = (100, 200, 100)

            if i == data.unsorted_index:
                color = (0, 200, 150)
            if i == data.selected_index:
                color = (0, 100, 200)
            if i == data.current_index:
                color = (200, 100, 100)
            pygame.draw.rect(self._screen, color, (x, y , width, height ))

    def change_algorithm(self):
        self._sort_algorithm = next(self._sort_algorithms)
        self.draw_information()

    def text(self, surface: pygame.Surface, text, position=(0, 0) ,text_color=(0, 255, 0), bg_color=(255,255,255), size=24):
        font = pygame.font.Font('freesansbold.ttf', size)
        text = font.render(text, True, text_color, bg_color)
        textRect = text.get_rect()
        textRect.center = (position[0] + textRect.width/2, position[1] + textRect.height/2)
        surface.blit(text, textRect)

    def draw_information(self):
        texts = []
        texts.append(f"q: {self._sort_algorithm.name}")
        texts.append(f"a: {self._animated}")
        texts.append("s: start")
        texts.append("d: shuffle")
        size = 24
        for index, text in enumerate(texts):
            self.text(self._screen, text, position=(10, 5 + index*size), size=size, bg_color=self._background_color)

    def draw(self):
        self._screen.fill(self._background_color)
        self.draw_data(self._sort_algorithm._data)
        self.draw_information()

    def start(self):
        clock = pygame.time.Clock()
        while self._is_running:
            clock.tick(120)
            self.check_event()
            if self._sorting:
                self._sort_algorithm.update(check_animation=self._animated)
            self.draw()
            pygame.display.update()
                
main_window = MainWindow()
main_window.start()

pygame.quit()