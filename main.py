#!/usr/bin/env python

import asyncio
import socket
import time

import pygame


FPS = 100
WIDTH, HEIGHT = 800, 400


class Ball:  # using a Sprite would be better
    def __init__(self):
        # self.ball = pygame.image.load("intro_ball.gif")
        self.ball = pygame.image.load("./img/ball.png")
        self.rect = self.ball.get_rect()
        self.speed = [3, 2]

    def move(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0 or self.rect.bottom > HEIGHT:
            self.speed[1] = -self.speed[1]

    def draw(self, screen):
        screen.blit(self.ball, self.rect)


def pygame_event_loop(event_loop, gui_queue):
    print('pygame_event_loop start')
    while True:
        event = pygame.event.wait()
        asyncio.run_coroutine_threadsafe(
                gui_queue.put(event),
                loop=event_loop,
        )

    pass # эта строка не выполнится никогда, втч при закрытии приложения


async def animation_loop(screen, player_command_queue, ball):
    black = 0, 0, 0

    current_time = 0
    while True:
        last_time, current_time = current_time, time.time()
        await asyncio.sleep(1 / FPS - (current_time - last_time))  # tick

        if not player_command_queue.empty():
            command = await player_command_queue.get()
            speed = int(command['input_char'])
            ball.speed = [speed,speed]

        ball.move()
        screen.fill(black)
        ball.draw(screen)
        pygame.display.flip()



async def gui_loop(gui_queue, ball):
    while True:
        event = await gui_queue.get()

        if event.type == pygame.QUIT:
            break
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if ball.speed == [0, 0]:
                    ball.speed = [2, 2]
                else:
                    ball.speed = [0, 0]
        else:
            pass
            # print("event", event)
    asyncio.get_event_loop().stop()



#
#
#
async def client_task(loop, client, clients_command_queue):
    peer = client.getpeername()
    print('open connection with {}'.format(peer))

    # вызывается при подключении клиента


    request = None
    while True:
        try:
            request = (await loop.sock_recv(client, 255)).decode('utf8')
        except UnicodeDecodeError:
            request = 'UnicodeDecodeError\r\n'
        response_str = str(request)

        response =  response_str + '\n'
        await loop.sock_sendall(client, response.encode('utf8'))
        if len(response_str) >=4 and response_str[:4] == 'exit':
            break
        elif response_str[0] == '1' or response_str[0] == '2' or response_str[0] == '3' or response_str[0] == '0':
            clients_command = {
                'player_name': peer[0],        # ip
                'input_char': response_str[0],
            }
            await clients_command_queue.put(clients_command)

    client.close()
    print('closed connection with {}'.format(peer))



#
#
#
async def server_loop(loop, server, clients_command_queue):
    print('server_loop start ')

    while True:
        client, _ = await loop.sock_accept(server)
        loop.create_task(client_task(loop, client, clients_command_queue))

    #pass # недосягаемый код, втч при закрытии приложения



#
#
#
def main():
    # запустим главный цикл событий asyncio
    # он запускает все остальные таски
    main_event_loop = asyncio.get_event_loop()


    # очередь команд от гуя
    gui_queue = asyncio.Queue()

    # очередь команд клиентов
    clients_command_queue = asyncio.Queue()

    pygame.init()

    pygame.display.set_caption("My game")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    ball = Ball()

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('', 9300))
    server.listen(8)
    server.setblocking(False)


    # run_in_executor позволяет запускать блокирующий код
    # returned : Future object
    #
    # в данном случае pygame_event_loop будет крутится до закрытия приложения
    # pygame_task нужна только для того чтобы закрыть потом ее , при закрытии приложения
    #
    pygame_task = main_event_loop.run_in_executor(
            None,  # executor.      if None  - Run in the default loop's executor
            pygame_event_loop,  # функцию которую запускаем
            main_event_loop,    # 1й параметр pygame_event_loop
            gui_queue         # 2й параметр pygame_event_loop
    )

    # создадим задачу на аниммацию,
    animation_task = asyncio.ensure_future(animation_loop(screen, clients_command_queue, ball))

    # создадим задачу на аниммацию,
    event_task = asyncio.ensure_future(gui_loop(gui_queue, ball))

    # создадим задачу на аниммацию,
    server_task = asyncio.ensure_future(server_loop(main_event_loop, server, clients_command_queue))


    try:
        main_event_loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        pygame_task.cancel()
        animation_task.cancel()
        event_task.cancel()
        server_task.cancel()
        print('Server closed')

    pygame.quit()


if __name__ == "__main__":
    main()
