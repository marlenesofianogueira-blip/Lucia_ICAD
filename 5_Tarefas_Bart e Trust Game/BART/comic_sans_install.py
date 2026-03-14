from psychopy import visual, core

win = visual.Window(size=[800, 600], color="black")
text = visual.TextStim(win, text="Hello, Comic Sans!", font="Comic Sans MS", color="white")

text.draw()
win.flip()
core.wait(2)
win.close()

try:
    import pyglet
    print("Pyglet instalado com sucesso!")
except ImportError:
    print("Erro: O módulo pyglet não está instalado.")


python --version