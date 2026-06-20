import os

# Faz o Pygame rodar sem abrir janela nem usar som (necessario para os testes
# que criam Arqueiro, Morcego e Flecha rodarem em qualquer computador).
os.environ.setdefault("SDL_VIDEODRIVER", "dummy")
os.environ.setdefault("SDL_AUDIODRIVER", "dummy")

import pygame
import pytest


@pytest.fixture(scope="session", autouse=True)
def iniciar_pygame():
    """Liga o Pygame uma vez antes de todos os testes e desliga no fim."""
    pygame.init()
    pygame.display.set_mode((100, 100))
    yield
    pygame.quit()
